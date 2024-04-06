# pylint: disable=missing-module-docstring
from datetime import datetime
from inspect import get_annotations
from pathlib import Path
import sqlite3
from typing import Any
from bookkeeper.repository.abstract_repository import AbstractRepository, T


class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий с базой sqlite
    """
    def __init__(self, db_file: Path, cls: type) -> None:
        self._db_filename = db_file
        self._data_type = cls
        self._table = self._data_type.__name__.lower()
        self._fields = get_annotations(self._data_type, eval_str=True)

        with sqlite3.connect(self._db_filename) as connect:
            cursor = connect.cursor()
            cursor.execute('PRAGMA foreign_keys = ON')
            cursor.execute(
                f'CREATE TABLE IF NOT EXISTS {self._table}'
                + '(pk INTEGER PRIMARY KEY NOT NULL'
                + " ".join(
                    f", {name} {self._convert_pytype_to_sql(tpy)}"
                    for name, tpy in self._fields.items() if name != 'pk'
                )
                + ")"
            )

    @staticmethod
    def _convert_pytype_to_sql(tpy: type) -> str:
        if tpy == int:
            return "INTEGER"
        if tpy == str:
            return "TEXT"
        if tpy == datetime:
            return "TIMESTAMP"
        raise ValueError(f"Type {tpy} is not supported")

    def add(self, obj: T) -> int:
        """
        Добавление одной записи в базу
        """
        if getattr(obj, "pk", None) != 0:
            raise ValueError("Trying to add object with filled 'pk' attribute")

        names = ", ".join([name for name in self._fields if name != 'pk'])
        placeholders = ", ".join("?" * (len(self._fields) - 1))

        values = [getattr(obj, name) for name in self._fields if name != 'pk']

        with sqlite3.connect(self._db_filename) as connect:
            cursor = connect.cursor()
            cursor.execute(
                f"INSERT INTO {self._table} ({names}) VALUES ({placeholders});",
                values,
            )
            obj.pk = cursor.lastrowid

        return obj.pk

    def get(self, pk: int) -> T | None:
        """
        Получить объект по ид
        """
        names = ', '.join(self._fields.keys())
        with sqlite3.connect(
                self._db_filename,
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        ) as connect:
            cur = connect.cursor()
            cur.execute(f"SELECT {names} FROM {self._table} WHERE pk = {pk}")
            res = cur.fetchone()
        if res is None:
            return None
        obj = self._data_type()
        for i, name in enumerate(self._fields, 0):
            setattr(obj, name, res[i])
        return obj

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        """
        Получить все записи по некоторому условию
        where - условие в виде словаря {'название_поля': значение}
        если условие не задано (по умолчанию), вернуть все записи
        """
        names = ', '.join(self._fields.keys())
        with sqlite3.connect(
                self._db_filename,
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        ) as connect:
            cursor = connect.cursor()
            if where is None:
                cursor.execute(f"SELECT {names} FROM {self._table}")
            else:
                where_keys = list(where.keys())
                where_values = list(where.values())
                text = f"SELECT {names} FROM {self._table} WHERE {where_keys[0]} = ?"
                for i in range(1, len(where)):
                    text += f" AND {where_keys[i]} = ?"
                cursor.execute(text, where_values)
            res = cursor.fetchall()
        out = []
        for element in res:
            obj = self._data_type()
            for j, name in enumerate(self._fields, 0):
                setattr(obj, name, element[j])
            out.append(obj)
        return out

    def update(self, obj: T) -> None:
        """
        Обновить данные об объекте. Объект должен содержать поле pk.
        """
        if getattr(obj, "pk", None) is None:
            raise ValueError("Object does not exist")

        names = ", ".join(self._fields)
        holders = ", ".join("?" * len(self._fields))

        values = [getattr(obj, key) for key in self._fields]

        with sqlite3.connect(self._db_filename) as connect:
            cursor = connect.cursor()
            cursor.execute(
                f"UPDATE {self._table} SET ({names}) = ({holders}) WHERE pk={obj.pk}",
                values,
            )
            if connect.total_changes == 0:
                raise ValueError(f"Object with pk = {obj.pk} does not exist")

    def delete(self, pk: int) -> None:
        """
        Удалить запись по ее ид
        """
        with sqlite3.connect(self._db_filename) as connect:
            cur = connect.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute(f"DELETE FROM {self._table} WHERE pk = {pk}")
            if connect.total_changes == 0:
                raise KeyError(f"Object with pk = {pk} does not exist")

    def del_all(self) -> None:
        """
        Удалить все записи
        """
        with sqlite3.connect(self._db_filename) as connect:
            cursor = connect.cursor()
            cursor.execute(f"DELETE FROM {self._table}")
            connect.commit()
            cursor.close()

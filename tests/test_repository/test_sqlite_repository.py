import pytest

from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

from bookkeeper.repository.sqlite_repository import SQLiteRepository


@pytest.fixture
def custom_class():
    @dataclass
    class Custom:
        pk: int = 0
        string: str = ''
        integer: int = 0
        date: datetime = datetime.now()

    return Custom


@pytest.fixture
def repo(tmp_path: Path, custom_class):
    return SQLiteRepository(tmp_path / 'test_data.db', custom_class)


def test_crud(repo, custom_class):
    obj = custom_class()
    pk = repo.add(obj)
    assert obj.pk == pk
    cur = repo.get(pk)
    assert cur == obj
    obj2 = custom_class()
    obj2.pk = pk
    repo.update(obj2)
    assert repo.get(pk) == obj2
    repo.delete(pk)
    assert repo.get(pk) is None


def test_cannot_add_with_pk(repo, custom_class):
    obj = custom_class()
    obj.pk = 1
    with pytest.raises(ValueError):
        repo.add(obj)


def test_cannot_add_without_pk(repo):
    with pytest.raises(ValueError):
        repo.add(0)


def test_cannot_delete_nonexistent(repo):
    with pytest.raises(KeyError):
        repo.delete(1)


def test_cannot_update_without_pk(repo, custom_class):
    obj = custom_class()
    with pytest.raises(ValueError):
        repo.update(obj)


def test_get_all(repo, custom_class):
    objects = [custom_class() for i in range(5)]
    for item in objects:
        repo.add(item)
    assert repo.get_all() == objects


def test_get_all_with_condition(repo, custom_class):
    objects = []
    date = datetime(2024, 4, 1, 12, 0, 0)
    for i in range(43):
        item = custom_class()
        item.integer = i
        item.string = 'test'
        item.date = date + timedelta(days=i)
        repo.add(item)
        objects.append(item)
    assert repo.get_all({'string': 'test'}) == objects
    assert repo.get_all({'integer': 42}) == [objects[-1]]
    assert repo.get_all({'date': date}) == [objects[0]]
    

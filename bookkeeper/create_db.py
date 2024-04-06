import sqlite3
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from inspect import get_annotations


con = sqlite3.connect('data/budget.db')
cur = con.cursor()
cur.execute('CREATE TABLE expense (amount, category, expense_date, date, comment)')
cur.execute('CREATE TABLE category (name, parent)')

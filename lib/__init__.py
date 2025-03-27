# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

# The __init__ method creates a new Python object, an instance of the Department class.
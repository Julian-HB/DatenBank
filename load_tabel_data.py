import sqlite3
from sqlite3 import Error
import os


class LoadFromTable:
    
    def load_data(self, table):
        database_path = os.path.join('../database_db_files', 'database.db')
        connection = sqlite3.connect(database_path)
        # Cusorobject wird erstellt. Der Cursor dient zur Tabellenmanipulation.
        cursor = connection.cursor()
        # Daten werden aus Tabelle entnommen.
        rows = cursor.executemany(f'SELECT * FROM {table} WHERE ID % (4*12) = 0')
        # Änderungen werden dauerhaft gespeichert.
        connection.commit()
        connection.close()
        return rows
    
    def load_data_partial(self, table, number):
        database_path = os.path.join('../database_db_files', 'database.db')
        connection = sqlite3.connect(database_path)
        # Cusorobject wird erstellt. Der Cursor dient zur Tabellenmanipulation.
        cursor = connection.cursor()
        # Daten werden aus Tabelle entnommen.
        rows = cursor.executemany(f'SELECT * FROM {table} WHERE ID % {number} = 0')
        # Änderungen werden dauerhaft gespeichert.
        connection.commit()
        connection.close()
        return rows
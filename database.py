import os
import sqlite3
from typing import Tuple

data_file = "macrofitas.db"


def create_tables():
    try:
        os.remove(data_file)
        print(f"Arquivo '{data_file}' removido com sucesso.")

    except FileNotFoundError:
        print(f"Criando novo arquivo '{data_file}'.")

    ocurrence_logs_create_statement = """

    CREATE TABLE IF NOT EXISTS OcurrenceLogs (
        RegistryDate CHAR(10),
        Sampling TEXT,
        Site TEXT,
        EnvironmentID INTEGER,
        EnvType CHAR(1),
        Subsystem TEXT,
        Specie TEXT
    );
    """

    conn = sqlite3.connect(data_file)
    cursor = conn.cursor()

    cursor.execute(ocurrence_logs_create_statement)
    conn.commit()
    conn.close()


def connect() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(data_file)
    return conn, conn.cursor()

import sqlite3
from typing import Tuple

data_file = "macrofitas.db"


def create_tables():
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

    ocurrence_logs_truncate_statement = "DELETE FROM OcurrenceLogs;"

    conn = sqlite3.connect(data_file)
    cursor = conn.cursor()

    cursor.execute(ocurrence_logs_create_statement)
    cursor.execute(ocurrence_logs_truncate_statement)
    conn.commit()
    conn.close()


def connect() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(data_file)
    return conn, conn.cursor()

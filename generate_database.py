import database
import data_source
from modos_vida import modos_vida
from datetime import datetime


def must_consider_ocurrence_row(ocurrence):
    ocurrence = ocurrence.strip()

    if len(ocurrence) <= 0:
        ocurrence = "0"

    return ocurrence != "0"


def append_ocurrence(cursor, row, specie):
    # Isso poderia ser feito via ORM - Model/Entity ? sim
    # Isso DEVERIA ser feito via ORM - Model/Entity ? NÃO

    current_day = datetime.strptime(
        row['RegistryDate'].replace('_', '-'), "%Y-%m-%d").date()

    insert_query = f"""
    INSERT INTO OcurrenceLogs (
        RegistryDate,
        Sampling,
        Site,
        EnvironmentID,
        EnvType,
        Subsystem,
        Specie
        )
        VALUES (
        '{current_day}',
        '{row['Sampling']}',
        '{row['Site']}',
        {row['EnvironmentID']},
        '{row['EnvType']}',
        '{row['Subsystem']}',
        '{specie}'
        );
    """

    cursor.execute(insert_query)


def main():

    dt_src = data_source.read_csv("data_source.csv")

    if len(dt_src) <= 0:
        print("O arquivo de origem 'data_source' está vazio.")
        return

    database.create_tables()

    conn, cursor = database.connect()

    print("Gerando registros de ocorrências")

    for row in dt_src:
        for _, plantas in modos_vida.items():
            for planta in plantas:
                if planta in row and must_consider_ocurrence_row(row[planta]):
                    append_ocurrence(cursor, row, planta)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()

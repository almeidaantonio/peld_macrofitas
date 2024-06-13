import csv
from typing import Dict, List


def read_csv(file_path: str) -> List[Dict[str, str]]:

    rows: List[Dict[str, str]] = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            rows.append(dict(row))

    return rows

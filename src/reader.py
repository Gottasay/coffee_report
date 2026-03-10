import csv
from pathlib import Path
from typing import List
import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from src.models import Record


def read_files(files: list[str]) -> List[Record]:
    records = []

    for file in files:
        path = Path(file)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file}")

        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = Record(
                    student=row["student"],
                    date=row["date"],
                    coffee_spent=int(row["coffee_spent"]),
                    sleep_hours=float(row["sleep_hours"]),
                    study_hours=int(row["study_hours"]),
                    mood=row["mood"],
                    exam=row["exam"],
                )

                records.append(record)

    return records


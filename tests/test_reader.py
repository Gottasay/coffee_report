import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.reader import read_files


def test_read_files(tmp_path):

    file = tmp_path / "test.csv"

    file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan,2024-06-01,100,5,10,ok,math\n",
        encoding="utf-8"
    )

    records = read_files([str(file)])

    assert len(records) == 1
    assert records[0].student == "Ivan"
    assert records[0].coffee_spent == 100

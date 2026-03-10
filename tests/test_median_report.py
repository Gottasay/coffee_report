import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.models import Record
from src.reports.median_coffee import MedianCoffeeReport


def test_median_report():

    records = [
        Record("Ivan", "", 100, 0, 0, "", ""),
        Record("Ivan", "", 200, 0, 0, "", ""),
        Record("Anna", "", 300, 0, 0, "", ""),
    ]

    report = MedianCoffeeReport()

    result = report.build(records)

    assert result[0][0] == "Anna"
    assert result[0][1] == 300
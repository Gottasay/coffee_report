from collections import defaultdict
from statistics import median

from .base import BaseReport


class MedianCoffeeReport(BaseReport):

    name = "median-coffee"

    def build(self, records):
        data = defaultdict(list)

        for r in records:
            data[r.student].append(r.coffee_spent)

        result = []

        for student, values in data.items():
            result.append((student, median(values)))

        result.sort(key=lambda x: x[1], reverse=True)

        return result
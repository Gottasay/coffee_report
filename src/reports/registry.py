from .median_coffee import MedianCoffeeReport

REPORTS = {
    MedianCoffeeReport.name: MedianCoffeeReport(),
}


def get_report(name: str):
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")

    return REPORTS[name]
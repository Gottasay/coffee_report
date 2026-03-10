from tabulate import tabulate

from cli import parse_args
from reader import read_files
from reports.registry import get_report


def main():
    args = parse_args()

    records = read_files(args.files)

    report = get_report(args.report)

    data = report.build(records)

    print(
        tabulate(
            data,
            headers=["Student", "Median coffee spent"],
            tablefmt="github"
        )
    )


if __name__ == "__main__":
    main()
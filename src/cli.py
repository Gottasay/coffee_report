import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV files"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name"
    )

    return parser.parse_args()
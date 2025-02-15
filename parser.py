import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")
    help_parser = subparsers.add_parser("ajuda")
    please_parser = subparsers.add_parser("porfavor")
    please_parser.add_argument("palavra")

    return parser

import argparse

from main import main

parser = argparse.ArgumentParser(description="Apply 'services.yaml'")
parser.add_argument("--deploy", action="store_true", help="Set dry-run to false")

args = parser.parse_args()
main(dry_run=not args.deploy)

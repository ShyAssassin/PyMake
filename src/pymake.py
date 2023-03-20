import toml
import argparse
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="pymake",
        description="A simple tool to add make-like functionality to Python projects.",
    )
    parser.add_argument("target", help="The target to run.")
    args = parser.parse_args()

    try:
        pyproject = toml.load("pyproject.toml")
        pymake = pyproject["tool"]["pymake"]
    except FileNotFoundError:
        print("pyproject.toml not found")
        return 1

    try:
        subprocess.run(pymake[args.target])
    except KeyError:
        print("Target not found")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

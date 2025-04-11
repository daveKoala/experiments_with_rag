import subprocess
import sys
from pathlib import Path
import os

ROOT = Path(__file__).parent

os.environ["PYTHONPATH"] = "src"


def run(command):
    print(f"\n🔧 Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print("❌ Failed")
        sys.exit(result.returncode)


def test():
    input_flag = "-s"
    print(f"PYTHONPATH=src pytest src/ {input_flag} ")
    run(f"PYTHONPATH=src pytest src/ {input_flag} ")


def watch():
    pytest_args = "-s -v"
    run(f"ptw src/ -- {pytest_args}")


def format():
    run("black src/")


def lint():
    run("ruff src/")


def check():
    format()
    lint()
    test()
    watch()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Project tooling runner")
    parser.add_argument(
        "task",
        choices=["test", "format", "lint", "check", "watch"],
        help="What task to run",
    )
    args = parser.parse_args()

    globals()[args.task]()

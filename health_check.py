import os
import sys


def check_path(path):
    if os.path.exists(path):
        print(f"SUCCESS: {path} found.")
        return True
    else:
        print(f"FAILURE: {path} not found.")
        return False


if __name__ == "__main__":
    target = os.getenv("CHECK_PATH", "/app")

    if check_path(target):
        sys.exit(0)
    else:
        sys.exit(1)

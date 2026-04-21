import os
import sys
import logging

LOG_DIR = "/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "health.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("HealthCheck")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_FILE)

formatter = logging.Formatter(
    fmt="%(asctime)s - [%(levelname)s] -> %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def check_path(path):
    if os.path.exists(path):
        logger.info(f"{path} found.")
        return True
    else:
        logger.error(f"{path} not found.")
        return False


if __name__ == "__main__":
    target = os.getenv("CHECK_PATH", "/app")

    if check_path(target):
        sys.exit(0)
    else:
        sys.exit(1)

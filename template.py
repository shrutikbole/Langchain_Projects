import os
from pathlib import Path
import logging



logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "langchain"

list_of_files = [
    ".github/workflow/.gitkeep",
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
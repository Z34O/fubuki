# fubuki-rewrite: not yet implemented

from datetime import datetime
import json
import os
import re

# Env variables
RED = "\033[31m"
BLUE = "\033[34m"
WHITE = "\033[37m"
ORANGE = "\033[33m"
DT_FORMAT = "%m/%d/%Y %H:%M"
DATA_DIRECTORY = ""
CONSOLE = f"{BLUE}[fubuki-rw] {ORANGE}"

# REPL
if __name__ == "__main__":
    os.system("bash banner.sh")

    while True:
        command = input(CONSOLE)

        if command in ["exit", "quit", "leave"]:
            exit()
        else:
            print(f"{RED}Oops: FUBUKI does not understand '{command}'{WHITE}")
else:
    print(f"{RED}Oops: FUBUKI cannot be imported to another code{WHITE}")

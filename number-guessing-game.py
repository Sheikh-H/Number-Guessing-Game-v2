import csv
import datetime
from rich import print
import time
import os
import sys


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen
    print(
        "[bold]Welcome to the[/bold] [bold green]Python CLI Number Guessing Game[/bold green]!"
    )


if __name__ == "__main__":
    main()
# I'll be honest, I still don't know the exact reason why i include this in all or most my code... Can someone explain in detail for me! :)

import csv
import datetime
from rich import print
import time
import os
import sys
import random


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def save_data(data):
    fieldnames = ["username", "attempts", "time", "won?"]
    if not os.path.exists("scores.csv"):
        with open("scores.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    else:
        with open("scores.csv", 'r') as f:
            scores = csv.DictReader(f, fieldnames=fieldnames)
            for score in scores:
                if score['username'] == data['username']: 
                    with open("scores.csv", "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writerow(data)
                else:
                    with open("scores.csv", "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writerow(data)


def main_game(mode):
    clear_screen()
    print("Let's take a username from you to store your results!")
    time.sleep(2)
    username = input("Enter username: ").upper().strip()
    clear_screen()
    print("Okay, let's begin in...")
    time.sleep(2)
    clear_screen()
    print("3...")
    time.sleep(1)
    clear_screen()
    print("2...")
    time.sleep(1)
    clear_screen()
    print("1...")
    time.sleep(1)
    clear_screen()
    print("Start!")
    time.sleep(1)
    clear_screen()
    start_time = time.time()
    attempts = 0
    if mode == "easy":
        attempts = 10
    elif mode == "medium":
        attempts = 5
    elif mode == "hard":
        attempts = 3
    number = random.randint(1, 10)
    answer = 0
    won = False
    attempts_made = 0
    while number != answer or attempts != 0:
        try:
            answer = int(input("Enter your guess: "))
        except ValueError:
            print("Please use numeric digits only!")
            continue
        attempts -= 1
        attempts_made += 1
        if answer == number:
            won = True
            break
        if attempts == 0:
            break
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 1)
    if won == True:
        clear_screen()
        print(
            f"[bold green]Congratulations![/bold green]\t\n{username} guessed the number '{number}' in {elapsed_time} seconds!"
        )
        time.sleep(3)
        print("Recording your score...")
        time.sleep(2)
        clear_screen()
        new_entry = {
            "username": username,
            "attempts": attempts_made,
            "time": elapsed_time,
            "won?": True,
        }
        save_data(new_entry)
        clear_screen()
        print("Done! Exiting game...")
        time.sleep(2)
        exit()
    if won == False and attempts == 0:
        clear_screen()
        print(
            f"😟 [bold orange]You've ran out of attempts![/bold orange] The number was {number}! Recording your score..."
        )
        time.sleep(3)
        print("Recording your score...")
        time.sleep(2)
        clear_screen()
        new_entry = {
            "username": username,
            "attempts": attempts_made,
            "time": elapsed_time,
            "won?": False,
        }
        save_data(new_entry)
        clear_screen()
        print("Done! Exiting game...")
        time.sleep(2)
        clear_screen()
        exit()


def easy_mode():
    main_game("easy")


def medium_mode():
    main_game("medium")


def hard_mode():
    main_game("hard")


def main():
    clear_screen()
    print(
        "[bold]Welcome to the[/bold] [bold green]Python CLI Number Guessing Game[/bold green]!"
    )
    time.sleep(2)
    clear_screen()
    print(
        "The aim of the game is to guess the number I'm thinking of [bold]between 1 and 100[/bold] as quickly as you can and with the least amount of attempt!"
    )
    time.sleep(2)
    clear_screen()
    print(
        "You would enter your guess in the terminal using the number keypad as each time the number of attempts you have is decremented."
    )
    time.sleep(2)
    clear_screen()
    print(
        "Once you have guessed the correct number or ran out of attempts the timer will stop and record your results in the leaderboard!"
    )
    time.sleep(2)
    clear_screen()
    print(
        "Difficulty Levels:\n\t1. [bold]Easy[/bold] - 10 guesses\n\t2. [bold]Medium[/bold] - 5 guesses\n\t3. [bold]Hard[/bold] - 3 guesses"
    )
    while True:
        option = int(input("Select which type of difficulty you would like: "))
        if option == 1:
            easy_mode()
        elif option == 2:
            medium_mode()
        elif option == 3:
            hard_mode()
        else:
            clear_screen()
            print("Invalid Entry! Try Again...")


if __name__ == "__main__":
    main()

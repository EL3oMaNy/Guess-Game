import random
import time
from playsound import playsound
from colorama import init, Fore

init(autoreset=True)

def print_colored(msg, color):
    print(getattr(Fore, color.upper(), Fore.WHITE) + msg)

def get_difficulty():
    playsound("start.mp3")
    print("🎮 Welcome to the Guessing Game!")
    print("Choose difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == "1":
            return 10, 5
        elif choice == "2":
            return 50, 7
        elif choice == "3":
            return 100, 10
        else:
            print_colored("❌ Invalid input. Please choose 1, 2, or 3.", "RED")
            playsound("wrong.mp3")

def play_game():
    max_num, max_attempts = get_difficulty()
    number = random.randint(1, max_num)
    attempts = 0

    print(f"\nGuess the number between 1 and {max_num}. You have {max_attempts} attempts!")
    start_time = time.time()

    while attempts < max_attempts:
        guess = input(f"\nAttempt {attempts + 1}/{max_attempts}: ")

        if not guess.isdigit():
            print_colored("❌ Please enter a valid number.", "YELLOW")
            playsound("wrong.mp3")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print_colored("⬆️ Too low!", "CYAN")
            playsound("wrong.mp3")
        elif guess > number:
            print_colored("⬇️ Too high!", "MAGENTA")
            playsound("wrong.mp3")
        else:
            duration = round(time.time() - start_time, 2)
            print_colored(f"✅ Correct! You guessed it in {attempts} tries and {duration} seconds.", "GREEN")
            playsound("correct.mp3")
            break
    else:
        print_colored(f"\n💀 Game over! The number was {number}", "RED")
        playsound("gameover.mp3")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print_colored("👋 Thanks for playing!", "BLUE")
            break

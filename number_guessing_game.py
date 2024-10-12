# Import the necessary module
from random import randint
from time import time


def play_game() -> bool:
    """Ask the player to either play the game or not"""
    while True:
        # Get the user responce 'Y' for yes and 'N' for no
        responce = input(f"Do you want to play [Y/N]: ")
        match responce.upper():
            case 'Y':
                return True
            case 'N':
                return False
            case _:
                print('Invalid Input: Try again.\n')
                continue



def welcoming(chance:int) -> None:
    """Display the welcoming Page"""
    print(f"\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {chance} chances to guess the correct number.")
    return None
    

def select_difficulty() -> int:
    """Select the difficulity level for the number of chances """
    
    difficulity = {"1": ["Easy",10], "2": ["Medium", 5], "3": ["Hard", 3]}

    print("\nPlease select the difficulty lever:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    while True:
        choice = input("Enter your choice: ")
        if choice in difficulity.keys():
            print(f"\nGreat! You have selected the {difficulity[choice][0]} difficulty level.")
            print(f"Let's start the game")
            return difficulity[choice][1]
        else:
            print("\nInvalid Input: try again.")
        

def valid_input(x:str) -> bool:
    """Check if the player input is an integer or not"""
    if not x.isdigit():
        print(f"Enter a valid input")
        return False
    return True


def guess(chance:int) -> int:
    """Get the player guessed number that fit in the interval [a,b]"""
    while True:
        try:
            player_num = input(f"\nEnter your guess: ").strip()
            if valid_input(player_num):
                player_num = int(player_num)
                if 1 <= player_num <= 100:
                    return player_num
                print("Incorrect! Your guess isn't in the interval [1,100]")
        except ValueError as e:
            print(f'{e}')


def get_hint(player_num:int, computer_num:int) -> None:
    """Get hints to help the player guess the number"""
    if player_num < computer_num:
        print(f"Incorrect! The number is greater than {player_num}.")
    else:
        print(f"Incorrect! The number is less than {player_num}.")
    return None


def is_guessed(player_num:int, computer_num:int, attempt:int, start_time: float) -> bool:
    if computer_num == player_num:
        end_time = time()
        delay = int(end_time - start_time)
        print(f"\nCongratulations! You guessed the correct number in {attempt} attempt and {delay}s")
        return True
    else:
        get_hint(player_num, computer_num)
        return False


def add_highscore(score:int , highscore:list[int]) -> None:
        highscore.append(score)


def display_highscore(highscore:list[int]):
    responce = input(f"\nDo you want to display the highscore [Y/N]").strip().lower()
    if responce == "Yes" and highscore:
        print(f"You highscore is {min(highscore)}")
    elif not highscore:
        print("No highscore available yet.")
    return None


def play() -> None:
    """Play the game"""
    # Initialise the highscore list
    highscore = []
    
    # Select the interval and generate the number to guess
    computer_num = randint(1, 101)
    print(computer_num)

    # Select the diffucilty and display a welcomin window
    chance = select_difficulty()
    welcoming(chance)

    start_time = time()

    
    # Try to guess the number
    for attempt in range(1, chance+1):
        player_num = guess(chance-attempt+1)
        if is_guessed(player_num, computer_num, attempt, start_time):
            add_highscore(attempt, highscore)
            display_highscore(highscore)
            return None

    # Displayt the message that the user lost
    print(f"You run out of chances, the number to guess was {computer_num}")
    return None
    

def main():
    while True:
        if play_game():
            play()
        else:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
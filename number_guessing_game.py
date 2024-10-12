# Import the necessary module
import pyautogui
from random import randint


def play_game() -> bool:
    """Ask the player to either play the game or not"""
    responce = pyautogui.confirm(f"Do you want to play?", "Main Menu",buttons=["Yes", "No"])
    return responce == "Yes"


def welcoming(a:int, b:int, chance:int) -> None:
    """Display the welcoming Page"""
    pyautogui.alert(f'''Welcome to the Number Guessing Game!\nI'm thinking of a number between {a} and {b}.\nYou have {chance} chances to guess the correct number.''')
    

def select_difficulity() -> int:
    """Select the difficulity level for the number of chances """
    responce = pyautogui.confirm(f"Select your diffucilty level:", "Configuration", buttons=["Easy","Medium","Hard"])
    match responce:
        case "Easy":
            return 10
        case "Medium":
            return 5
        case _:
            return 3
        

def valid_input(x:str) -> bool:
    """Check if the player input is an integer or not"""
    if not x.isdigit() or x is None:
        pyautogui.alert(f"Enter a valid input", f"Error")
        return False
    return True


def get_interval() -> list[int]:
    """Get the interval to generater an random number between it"""
    while True:
        try:
            a = pyautogui.prompt(f"Enter the lower bound: ", f"Input")
            if valid_input(a):
                a = int(a)
            else:
                continue
            
            b = pyautogui.prompt(f"Enter the upper bound: ", f"Input")
            if valid_input(b):
                b = int(b)
            else:
                continue

            if a >= b:
                pyautogui.alert(f"The lower bound is superior or equal to your upper bound", f"Error")
                continue
            else:
                return [a,b]

        except ValueError as e:
            pyautogui.alert(f"{e}", f"Error")


def guess(a:int, b:int, chance:int) -> int:
    """Get the player guessed number that fit in the interval [a,b]"""
    while True:
        try:
            player_num = pyautogui.prompt(f"The number is between {a} and {b}, {chance} chances left, guess it:", f"Input")
            if valid_input(player_num):
                player_num = int(player_num)
                if a <= player_num <= b:
                    return player_num
        except ValueError as e:
            pyautogui.alert(f'{e}')


def get_hint(player_num:int, computer_num:int) -> None:
    """Get hints to help the player guess the number"""
    if player_num < computer_num:
        pyautogui.alert(f"Wrong number. Your number is lower.", "Hint")
    else:
        pyautogui.alert(f"Wrong number. Your number is higher", "Hint")
    return None


def is_guessed(player_num:int, computer_num:int, chance:int) -> bool:
    if computer_num == player_num:
        pyautogui.alert(f"Congratulations, you guessed it. It took you {chance} chance", "Result")
        return True
    else:
        get_hint(player_num, computer_num)
        return False


def play() -> None:
    """Play the game"""
    # Select the interval and generate the number to guess
    a, b = get_interval()
    computer_num = randint(a, b+1)

    # Select the diffucilty and display a welcomin window
    chance = select_difficulity()
    welcoming(a, b, chance)
    
    # Try to guess the number
    for attempt in range(1, chance+1):
        player_num = guess(a, b, chance-attempt+1)
        if is_guessed(player_num, computer_num, attempt):
            return None
    
    # Displayt the message that the user lost
    pyautogui.alert(f"You run out of chances, the number to guess was {computer_num}")
    return None
    

def main():
    while True:
        if play_game():
            play()
        else:
            return None


if __name__ == "__main__":
    main()
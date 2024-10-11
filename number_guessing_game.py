# Import the necessary module
import pyautogui
from random import randint

def play_game() -> bool:
    """Ask the player to either play the game or not"""
    responce = pyautogui.confirm(f"Do you want to play?", buttons=["Yes", "No"])
    return responce == "Yes"


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
            a = pyautogui.promt(f"Enter the lower bound: ", f"Input")
            if valid_input(a):
                a = int(a)
            else:
                continue
            
            b = pyautogui.promt(f"Enter the upper bound: ", f"Input")
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


def guess(a:int,b:int) -> int:
    """Get the player guessed number that fit in the interval [a,b]"""
    while True:
        try:
            player_num = pyautogui.propmt(f"The number is between {a} and {b}, guess it:", f"Input")
            if valid_input(player_num) and a <= player_num <= b:
                player_num = int(player_num)
                return player_num
        except ValueError as e:
            pyautogui.alert(f'{e}')


def get_hint(player_num:int, computer_num:int) -> None:
    """Get hints to help the player guess the number"""
    if player_num < computer_num:
        pyautogui.alert(f"Your number is lower.", "Hint")
    else:
        pyautogui.alert(f"Your number is higher", "Hint")
    return

if __name__ == "__main__":
    pass
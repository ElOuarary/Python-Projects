# Import the necessary module
import pyautogui
from random import randint


def valid_input(x:str) -> bool:
    """Check if the user input is an integer or not"""
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
    """Get the user guesseed number that fit in the interval [a,b]"""
    while True:
        try:
            user_num = pyautogui.propmt(f"The number is between {a} and {b}, guess it:", f"Input")
            if valid_input(user_num):
                user_num = int(user_num)
                return user_num
        except ValueError as e:
            pyautogui.alert(f'{e}')


if __name__ == "__main__":
    pass
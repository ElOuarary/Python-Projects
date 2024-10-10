# Import the necessary module
import pyautogui
from random import randint

# Function to valid input

def valid_input(x:str) -> bool:
    if not x.isdigit():
        pyautogui.alert("Enter a valid input", "Error")
        return False
    return True

# Function to get the interval
def get_interval():

    while True:
        try:
            a = pyautogui.promt("Enter the lower bound: ", "")
            if valid_input(a):
                a = int(a)
            else:
                continue
            
            b = pyautogui.promt("Enter the upper bound: ", "")
            if valid_input(b):
                b = int(a)
            else:
                continue

            if a >= b:
                pyautogui.alert("The lower bound if superior to your upper bound", "Error")

        except:
            pass
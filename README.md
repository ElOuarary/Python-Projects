# Number Guessing Game
This is a Python console-based Number Guessing Game where the player tries to guess a number between 1 and 100 within a limited number of chances.  
The game offers three difficulty levels—Easy, Medium, and Hard—each with varying numbers of attempts.  
The game also tracks the player's high score based on the number of attempts used to guess the correct number.

## Features
Multiple difficulty levels: Easy (10 chances), Medium (5 chances), and Hard (3 chances).  
Random number generation between 1 and 100.  
Input validation for both game continuation and number guessing.  
Helpful hints for the player if the guessed number is too low or too high.  
High score tracking based on the number of attempts used in previous rounds.  
User can opt to display their high score at the end of each game session.  


## How to Play
1)Run the script.  
2)Select whether you'd like to play the game.  
3)Choose your difficulty level:  
-Easy: 10 chances to guess.  
-Medium: 5 chances to guess.  
-Hard: 3 chances to guess.  
4)Start guessing the number. If your guess is incorrect, you will receive a hint: the number is either greater or smaller than your guess.  
5)You win if you guess the correct number within the allowed chances. Your high score is updated based on the number of attempts taken.  
6)You lose if you run out of chances before guessing the number. The correct number will be revealed.  
7)After each game, choose whether to display the high score or exit.  


## Functions
-play_game() -> bool: Asks the player if they want to play and returns a boolean (True for yes, False for no).  
-welcoming(chance: int) -> None: Displays a welcome message and the number of available chances based on the selected difficulty level.  
-select_difficulty() -> int: Allows the player to select a difficulty level, returning the number of chances.  
-valid_input(x: str) -> bool: Validates if the player's input is a valid integer.  
-guess(chance: int) -> int: Prompts the player to guess the number and validates the input. Returns the player's guess.  
-get_hint(player_num: int, computer_num: int) -> None: Provides hints based on whether the guessed number is higher or lower than the correct number.  
-is_guessed(player_num: int, computer_num: int, attempt: int, start_time: float) -> bool: Checks if the player guessed the correct number, displays the result, and returns a boolean.  
-add_highscore(score: int, highscore: list[int]) -> None: Updates the high score list.  
-display_highscore(highscore: list[int]) -> None: Displays the high score if requested by the player.  
-play() -> None: Handles the game flow, including difficulty selection, number guessing, and high score tracking.  
-main(): The entry point of the program, looping through game sessions until the player decides to exit.  


## Requirements
Python 3.x  


## How to Run
1)Ensure Python is installed on your system.  
2)Run the script using:  
python number_guessing_game.py  
3)Follow the on-screen instructions to play.  
Example Output  
Do you want to play [Y/N]: Y  
Please select the difficulty level:  
1. Easy (10 chances)  
2. Medium (5 chances)  
3. Hard (3 chances)  

Enter your choice: 2  

Great! You have selected the Medium difficulty level.  
Let's start the game.  
Welcome to the Number Guessing Game!  
I'm thinking of a number between 1 and 100.  
You have 5 chances to guess the correct number.  

Enter your guess: 50  
Incorrect! The number is less than 50.  

Enter your guess: 25  
Incorrect! The number is greater than 25.  

Enter your guess: 35  
Congratulations! You guessed the correct number in 3 attempts and 22s.  
Do you want to display the high score [Y/N]: Y  
Your high score is 3.

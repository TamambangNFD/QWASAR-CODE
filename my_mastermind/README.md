# Welcome to My Mastermind
***

## Task
The task is to implement a simplified version of the classic Mastermind game in C.
The goal is to let the player guess a secret 4-digit code composed of distinct digits between 0 and 8.
After each guess, the program must display the number of well-placed and misplaced digits, continuing until the player wins or runs out of attempts.
## Description
This project reads the player's input directly from the standard input using the read() system call, character by character.
It validates the input to ensure it consists only of four digits between 0 and 8 and contains no repetitions.
The secret code can be either:

provided by the user using the -c flag, or

generated randomly by the program if no code is specified.

The program displays:

“Well placed pieces: X” — number of correct digits in the right position,

“Misplaced pieces: Y” — number of correct digits in the wrong position,
and stops when the player finds the correct code or when the maximum number of attempts (default 10) is reached.

## Installation
Clone or copy the project files into your working directory.

Make sure you have a C compiler installed (e.g., gcc).

In the project folder, compile the program by running:
make
This will create an executable file named my_mastermind.

## Usage
Run the program from your terminal:
./my_mastermind
You can also specify a custom secret code and number of attempts:
./my_mastermind -c "1234" -t 8
Example run:
Will you find the secret code?
Please enter a valid guess
Round 0
>1456
Well placed pieces: 0
Misplaced pieces: 2
-----
Round 1
>1234
Congratz! You did it!


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>

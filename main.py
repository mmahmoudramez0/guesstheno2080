import random

def user_guess(x):
    random_number = random.randint(1, x)
    max_attempts = 3  # You can adjust this as needed
    for attempt in range(max_attempts):
        guess = int(input(f'Attempt {attempt + 1}/{max_attempts}: Guess a number between 1 and {x}: '))
        if guess == random_number:
            print(f'Congratulations! You guessed the number {random_number} correctly!')
            break
        elif guess < random_number:
            print('Too low.')
        else:
            print('Too high.')
    else:
        print(f'Sorry, you did not guess the correct number. It was {random_number}.')

user_guess(10)
def computer_guess(x):
    low = 1
    high = x
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'c':
            print(f'Yay! The computer guessed your number, {guess}, correctly in {attempts} attempts!')
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print('Invalid input. Please enter H, L, or C.')

computer_guess(10)

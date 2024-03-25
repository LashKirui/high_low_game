from game_data import data
import random
import os

score = 0
game_should_continue = True
# Making the account at position B become the next position account at position A
account_b = random.choice(data)


# Make the game repeatable
while game_should_continue:
    def format_data(account):
        """take the account data and return the printable format the account data into a printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"


    def check_answer(guess, a_followers, b_followers):
        """Take the user guess and follower counts and return if they got it right."""
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"


    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    # generate random account from game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    # ask a user for a guess
    guess = input("Who has more followers? 'A' or 'B': ").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the Screen
    clear_screen()

    # give feedback to their Guess
    # Keeping Scoring
    if is_correct:
        score += 1
        print(f"You're right! current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong. The final score {score}")

    # Clear the Screen

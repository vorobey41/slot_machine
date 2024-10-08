import random

symbols = {1: "🍒", 2: "🍋", 3: "⭐️"}

def spin_slots():
    return [random.randint(1, 3) for _ in range(3)]

def display_symbols(spin_result):
    spin_symbols = [symbols[num] for num in spin_result]
    print(" | ".join(spin_symbols))

def calculate_payout(spin_result, user_bet):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return user_bet * 3, "Three symbols match! You win triple the rate!"
    elif spin_result[0] == spin_result[1] or spin_result[0] == spin_result[2] or spin_result[1] == spin_result[2]:
        return user_bet * 2, "Two symbols match! You win double the rate!"
    else:
        return -user_bet, "No match. You lose the bet."
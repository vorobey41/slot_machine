from slots import spin_slots, display_symbols, calculate_payout
from utils import get_user_bet, ask_to_continue, display_history
import json

def save_profile(balance, history, filename="profile.json"):
    data = {
        "balance": balance,
        "history": history
    }
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Game saved successfully.")

def load_profile(filename="profile.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("Game loaded successfully.")
            return data.get("balance", 100), data.get("history", [])
    except FileNotFoundError:
        print("No saved profile found. Starting with a balance of $100.")
        return 100, []
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("Game loaded successfully.")
            return data.get("balance", 100), data.get("history", [])
    except FileNotFoundError:
        print("No saved profile found. Starting new game.")
        return 100, []

def main():
    balance, history = load_profile()
    while balance > 0:
        print("\nWelcome to Python Slots!")
        print(f"Current balance: ${balance}")

        user_bet = get_user_bet(balance)

        spin_result = spin_slots()
        print("Spinning...")
        display_symbols(spin_result)

        payout, message = calculate_payout(spin_result, user_bet)
        balance += payout
        history.append({"bet": user_bet, "payout": payout, "balance": balance, "result": message})
        print(f"{message}\nNew balance: ${balance}")

        if balance > 0:
            if ask_to_continue() == 'Y':
                display_history(history)
                save_profile(balance, history)
                print("Thank you for playing!")
                break
        else:
            display_history(history)
            print("Your balance is zero. Game over!")
            break

if __name__ == "__main__":
    main()
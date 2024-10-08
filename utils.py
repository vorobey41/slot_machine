def get_user_bet(balance):
    while True:
        user_bet = input("Place your bet amount: ")
        if not user_bet.isdigit() or int(user_bet) <= 0 or int(user_bet) > balance:
            print("Invalid bet amount. Please enter a valid number within your balance.")
            continue
        return int(user_bet)

def ask_to_continue():
    while True:
        choice = input("Do you want to leave? Y/N: ").strip().upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            
def display_history(history):
    print("\nGame History:")
    for entry in history:
        result = f"Bet: ${entry['bet']} | Result: {entry['result']} | Payout: ${entry['payout']} | Balance: ${entry['balance']}"
        print(result)

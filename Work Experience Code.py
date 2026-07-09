
CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Income", "Other"]
KEYWORD_MAPPING = {
    "tesco": "Food",
    "sainsbury": "Food",
    "asda": "Food",
    "uber": "Transport",
    "train": "Transport",
    "bus": "Transport",
    "netflix": "Entertainment",
    "spotify": "Entertainment",
    "cinema": "Entertainment",
    "amazon": "Shopping",
    "ebay": "Shopping",
    "clothing": "Shopping",
    "electric": "Bills",
    "water": "Bills",
    "rent": "Bills",
    "salary": "Income",
    "dividend": "Income"
}

    
    # Loop
    for keyword, category in KEYWORD_MAPPING.items():
        if keyword in cleaned_desc:
            return category
            
    # Default fallback category 
    return "Other"

def handle_single_input():
    """Choice 1: Allows manual user entry via CLI."""
    print("\n--- Categorise a Transaction ---")
    description = input("Enter transaction description: ")
    if not description.strip():
        print("Error: Description cannot be empty.")
        return
        
    category = categorise_transaction(description)
    print(f"Predicted category: {category}")

def show_categories():
    """Choice 2: Prints the known categories."""
    print("Available Categories -")
    for cat in CATEGORIES:
        print(f"- {cat}")

def main_menu():
    """The main Command-Line Interface loop."""
    while True:
        print(" TRANSACTION CATEGORISER MENU ") 
        print("1. Categorise transactions")
        print("2. Show categories")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            handle_single_input()
        elif choice == "2":
            show_categories()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()

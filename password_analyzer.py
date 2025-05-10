import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def analyze_password(password):
    strength = 0
    weaknesses = []
    suggestions = []

    # Rule 1: Length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        weaknesses.append("Password is too short (less than 8 characters).")
        suggestions.append("Use at least 12 characters for better security.")

    # Rule 2: Uppercase Letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        weaknesses.append("Missing uppercase letters.")
        suggestions.append("Add some uppercase letters (A-Z).")

    # Rule 3: Lowercase Letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        weaknesses.append("Missing lowercase letters.")
        suggestions.append("Add some lowercase letters (a-z).")

    # Rule 4: Numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        weaknesses.append("Missing numbers.")
        suggestions.append("Add some numbers (0-9).")

    # Rule 5: Special Characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        weaknesses.append("Missing special characters.")
        suggestions.append("Add special characters like @, #, $, %, etc.")

    # Final Strength Rating
    if strength >= 7:
        rating = Fore.GREEN + "Strong 💪"
        bar_color = Fore.GREEN
    elif strength >= 4:
        rating = Fore.YELLOW + "Medium ⚡"
        bar_color = Fore.YELLOW
    else:
        rating = Fore.RED + "Weak ⚠️"
        bar_color = Fore.RED

    # Score Bar
    score_bar = bar_color + "[" + "■" * strength + " " * (7-strength) + "]"

    # Display Results
    print("\n🔍 Password Analysis 🔍")
    print(f"Strength: {rating}")
    print(f"Score: {score_bar} ({strength}/7)")

    if weaknesses:
        print(Fore.RED + "\n⚡ Weaknesses:")
        for w in weaknesses:
            print(f"- {w}")
    if suggestions:
        print(Fore.CYAN + "\n💡 Suggestions:")
        for s in suggestions:
            print(f"- {s}")

# Example usage:
password_input = input("Enter your password to analyze: ")
analyze_password(password_input)

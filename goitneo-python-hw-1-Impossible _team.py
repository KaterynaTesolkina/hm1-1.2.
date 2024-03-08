# Завдання 1

from datetime import datetime, timedelta, date
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data
    current_date = date.today()
    birthdays = defaultdict(list)

    # Iterate through users
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days >= 0 and delta_days < 7:
            day_of_week = (current_date + timedelta(days=delta_days)).strftime('%A')
            birthdays[day_of_week].append(name)

    # Print the result
    for day, celebrants in birthdays.items():
        print(f"{day}: {', '.join(celebrants)}")

# Example users list with birthdays
users = [
    {"name": "John Smith", "birthday": date(1990, 10, 31)},
    {"name": "Tesolkina Kateryna", "birthday": date(1990, 4, 12)},
    {"name": "Alex Marx", "birthday": date(1990, 10, 30)},
    {"name": "Natalia Tesolkina", "birthday": date(1940, 4, 12)},
    {"name": "Riedl Marlene", "birthday": date(1939, 1, 30)}
]

# Call the function with the users list to get birthdays for the next week
get_birthdays_per_week(users)

# Завдання 2

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command.")
        elif command == "change":
            if len(args) == 2:
                name, phone = args
                print(change_contact(contacts, name, phone))
            else:
                print("Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                result = show_phone(contacts, name)
                print(result)
            else:
                print("Invalid command.")
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
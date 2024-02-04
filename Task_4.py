#Четверте завдання
#Функція parse_input розбиває введений рядок на слова, використовуючи пробіл як розділювач
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

#додавання нового контакту до словника контактів
def add_contact(args, contacts): #
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."
# оновлює дані контакта
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new_phone]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    return ""

def main():
    contacts = {} #словник з контактами
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

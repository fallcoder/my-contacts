contacts = [ ('matar', "123-456-7890"), 
            ('amy', "234-567-8901"), 
            ('john', "345-678-9012"), 
            ('angele', "456-789-0123"), 
            ('mama', "567-890-1234") ] 

contacts = dict(contacts)

def add_contact():
    name = input("enter name to add: ").strip().lower()
    phone = input("enter phone number (format: XXX-XXX-XXXX): ").strip()
    contacts[name] = phone
    print(f"added {name} with phone {phone}")

def show_contact():
    name = input("enter name to search: ").strip().lower()
    if name in contacts:
        print(f"{name}'s phone is {contacts[name]}")
    else:
        print("not found")

def show_all_contacts():
    if contacts:
        print("\n All contacts:")
        print
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else: 
        print("no contacts available")

def delete_contact():
    name = input("enter name to delete: ").strip().lower()
    if name in contacts:
        del contacts[name]
        print(f"deleted {name}")
    else:
        print("not found")

def show_menu():
    print("\n------ BIENVENUE ------")
    print("1. Search for a contact")
    print("2. Add a new contact")
    print("3. Show all contacts")
    print("4. Delete a contact")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("enter you choice: ").strip()
        if choice == "1":
            show_contact()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            show_all_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalide choice, please try again")


if __name__ == "__main__":
    main()
        
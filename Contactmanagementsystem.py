# Contact Manager Program

# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts in the list.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input("Enter new phone number (or press enter to keep the same): ")
        email = input("Enter new email address (or press enter to keep the same): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def save_contacts_to_file():
    with open("contacts.txt", "w") as f:
        for name, info in contacts.items():
            f.write(f"{name},{info['phone']},{info['email']}\n")
    print("Contacts saved to file successfully!")

def load_contacts_from_file():
    global contacts
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
        print("Contacts loaded from file successfully!")
    except FileNotFoundError:
        print("No contacts file found.")

def main():
    load_contacts_from_file()
    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts_to_file()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

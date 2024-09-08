import os
import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Validate name (only alphabets)
def validate_name(name):
    if name.isalpha():
        return True
    print("Error: Name should only contain alphabets.")
    return False

# Validate phone number (exactly 10 digits)
def validate_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    print("Error: Phone number must contain exactly 10 digits.")
    return False

# Validate email (must contain @gmail.com)
def validate_email(email):
    if email.endswith("@gmail.com"):
        return True
    print("Error: Email must end with '@gmail.com'.")
    return False

# Validate ID (only digits and unique)
def validate_id(id, contacts):
    if not id.isdigit():
        print("Error: ID should be a number.")
        return False
    if id in (contact['id'] for contact in contacts.values()):
        print("Error: ID already exists.")
        return False
    return True

# Add a new contact
def add_contact(contacts):
    id = input("Enter contact ID: ").strip()
    if not validate_id(id, contacts):
        return
    name = input("Enter contact name: ").strip()
    if not validate_name(name):
        return
    if name in contacts:
        print("Error: Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    if not validate_phone(phone):
        return

    email = input("Enter email address: ").strip()
    if not validate_email(email):
        return

    address = input("Enter address: ").strip()
    
    contacts[name] = {"id": id, "phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("Contact added successfully.")

# Search for a contact by name
def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"ID: {contact['id']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found.")

# Update a contact's information
def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    id = input("Enter new ID: ").strip()
    if not validate_id(id, contacts):
        return

    phone = input("Enter new phone number: ").strip()
    if not validate_phone(phone):
        return

    email = input("Enter new email address: ").strip()
    if not validate_email(email):
        return

    address = input("Enter new address: ").strip()
    
    contacts[name] = {"id": id, "phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print("Contact updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

# Display all contacts in a table format
def display_all_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print(f"{'ID':<10} {'Name':<20} {'Phone':<15} {'Email':<30} {'Address':<30}")
        print("-" * 105)
        for name, details in contacts.items():
            print(f"{details['id']:<10} {name:<20} {details['phone']:<15} {details['email']:<30} {details['address']:<30}")

# Display the menu
def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

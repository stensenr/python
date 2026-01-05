class Contact:
    """Represents a single contact with name, phone, and email."""
    
    def __init__(self, name, phone, email):
        """Initialize a new contact.
        
        Args:
            name: Contact's full name
            phone: Contact's phone number
            email: Contact's email address
        """
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        """Return a string representation of the contact."""
        return f"{self.name} | {self.phone} | {self.email}"
    
    def to_dict(self):
        """Convert contact to dictionary for JSON storage."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

class ContactBook:
    """Manages a collection of contacts."""
    
    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts = []
    
    def add_contact(self, contact):
        """Add a contact to the book."""
        self.contacts.append(contact)
        print(f"✓ Added: {contact.name}")
    
    def view_all_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("\nNo contacts in your book yet!")
            return
        
        print("\n=== ALL CONTACTS ===")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")
        print("=" * 50)
    
    def search_contacts(self, search_term):
        """Search for contacts by name, phone, or email."""
        search_term = search_term.lower()
        results = []
        
        for contact in self.contacts:
            if (search_term in contact.name.lower() or 
                search_term in contact.phone.lower() or 
                search_term in contact.email.lower()):
                results.append(contact)
        
        if not results:
            print(f"\nNo contacts found matching '{search_term}'")
            return
        
        print(f"\n=== SEARCH RESULTS for '{search_term}' ===")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. {contact}")
        print("=" * 50)
    
    def get_contact_count(self):
        """Return the number of contacts."""
        return len(self.contacts)
    
    def delete_contact(self, index):
        """Delete a contact by index (1-based).
        
        Args:
            index: The position of the contact to delete (starting from 1)
        
        Returns:
            True if deleted successfully, False otherwise
        """
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"✓ Deleted: {deleted_contact.name}")
            return True
        else:
            print(f"Error: Invalid contact number. Please enter 1-{len(self.contacts)}")
            return False
    
    def update_contact(self, index, new_name=None, new_phone=None, new_email=None):
        """Update a contact's information.
        
        Args:
            index: The position of the contact to update (starting from 1)
            new_name: New name (optional, keeps old if None)
            new_phone: New phone (optional, keeps old if None)
            new_email: New email (optional, keeps old if None)
        
        Returns:
            True if updated successfully, False otherwise
        """
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            
            # Update only if new value is provided
            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            
            print(f"✓ Updated: {contact}")
            return True
        else:
            print(f"Error: Invalid contact number. Please enter 1-{len(self.contacts)}")
            return False

def display_menu():
    """Display the main menu."""
    print("\n" + "="*40)
    print("       CONTACT BOOK MANAGER")
    print("="*40)
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    print("="*40)


def get_contact_info():
    """Get contact information from user."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    
    if not name or not phone or not email:
        print("Error: All fields are required!")
        return None
    
    return Contact(name, phone, email)


def get_contact_index(book):
    """Get a valid contact index from user."""
    book.view_all_contacts()
    
    if book.get_contact_count() == 0:
        return None
    
    try:
        index = int(input(f"\nEnter contact number (1-{book.get_contact_count()}): "))
        if 1 <= index <= book.get_contact_count():
            return index
        else:
            print(f"Invalid number. Please enter 1-{book.get_contact_count()}")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main():
    """Main function to run the contact book application."""
    print("Welcome to Contact Book Manager!")
    
    # Create a new contact book
    book = ContactBook()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            # Add new contact
            print("\n--- ADD NEW CONTACT ---")
            contact = get_contact_info()
            if contact:
                book.add_contact(contact)
        
        elif choice == "2":
            # View all contacts
            book.view_all_contacts()
        
        elif choice == "3":
            # Search contacts
            search_term = input("\nEnter search term (name, phone, or email): ").strip()
            if search_term:
                book.search_contacts(search_term)
            else:
                print("Search term cannot be empty!")
        
        elif choice == "4":
            # Update contact
            print("\n--- UPDATE CONTACT ---")
            index = get_contact_index(book)
            if index:
                print("Leave blank to keep current value")
                new_name = input("New name: ").strip() or None
                new_phone = input("New phone: ").strip() or None
                new_email = input("New email: ").strip() or None
                
                if new_name or new_phone or new_email:
                    book.update_contact(index, new_name, new_phone, new_email)
                else:
                    print("No changes made.")
        
        elif choice == "5":
            # Delete contact
            print("\n--- DELETE CONTACT ---")
            index = get_contact_index(book)
            if index:
                confirm = input(f"Are you sure you want to delete contact #{index}? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y']:
                    book.delete_contact(index)
                else:
                    print("Deletion cancelled.")
        
        elif choice == "6":
            # Exit
            print(f"\nThank you for using Contact Book Manager!")
            print(f"Total contacts: {book.get_contact_count()}")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-6.")


# Test the Contact class
if __name__ == "__main__":
        main()
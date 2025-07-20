from contact_manager import ContactManager
from contact import Contact
from utils import validate_phone, validate_email, get_valid_input

class ContactMasterApp:
    def __init__(self):
        self.manager = ContactManager()
    
    def display_menu(self):
        """Display main menu options"""
        print("\n" + "="*40)
        print("        CONTACT MASTER")
        print("="*40)
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        print("="*40)
    
    def add_contact(self):
        """Add a new contact"""
        print("\n--- Add New Contact ---")
        
        name = get_valid_input("Enter name: ")
        phone = get_valid_input("Enter phone number: ", validate_phone)
        email = get_valid_input("Enter email (optional): ", validate_email, required=False)
        address = get_valid_input("Enter address (optional): ", required=False)
        
        contact = Contact(name, phone, email, address)
        if self.manager.add_contact(contact):
            print(f"\n✓ Contact '{name}' added successfully!")
        else:
            print("\n✗ Failed to add contact.")
    
    def view_all_contacts(self):
        """Display all contacts"""
        contacts = self.manager.get_all_contacts()
        
        if not contacts:
            print("\nNo contacts found.")
            return
        
        print(f"\n--- All Contacts ({len(contacts)} total) ---")
        for i, contact in enumerate(contacts, 1):
            print(f"\n{i}. {contact}")
            print("-" * 30)
    
    def search_contacts(self):
        """Search for contacts"""
        query = get_valid_input("\nEnter search term (name, phone, or email): ")
        results = self.manager.search_contacts(query)
        
        if not results:
            print(f"\nNo contacts found matching '{query}'.")
            return
        
        print(f"\n--- Search Results ({len(results)} found) ---")
        for i, contact in enumerate(results, 1):
            print(f"\n{i}. {contact}")
            print("-" * 30)
    
    def delete_contact(self):
        """Delete a contact"""
        identifier = get_valid_input("\nEnter name or phone number to delete: ")
        deleted_contact = self.manager.delete_contact(identifier)
        
        if deleted_contact:
            print(f"\n✓ Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print(f"\n✗ No contact found with '{identifier}'.")
    
    def run(self):
        """Main application loop"""
        print("Welcome to ContactMaster!")
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == "1":
                    self.add_contact()
                elif choice == "2":
                    self.view_all_contacts()
                elif choice == "3":
                    self.search_contacts()
                elif choice == "4":
                    self.delete_contact()
                elif choice == "5":
                    print("\nThank you for using ContactMaster!")
                    break
                else:
                    print("\n✗ Invalid choice. Please enter 1-5.")
                    
            except KeyboardInterrupt:
                print("\n\nExiting ContactMaster...")
                break
            except Exception as e:
                print(f"\n✗ An error occurred: {e}")

if __name__ == "__main__":
    app = ContactMasterApp()
    app.run()
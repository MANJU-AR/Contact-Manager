import json
import os
from contact import Contact

class ContactManager:
    def __init__(self, data_file="data/contacts.json"):
        self.data_file = data_file
        self.contacts = []
        self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    self.contacts = [Contact.from_dict(contact_data) for contact_data in data]
        except Exception as e:
            print(f"Error loading contacts: {e}")
            self.contacts = []
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as file:
                data = [contact.to_dict() for contact in self.contacts]
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving contacts: {e}")
    
    def add_contact(self, contact):
        """Add a new contact"""
        self.contacts.append(contact)
        self.save_contacts()
        return True
    
    def delete_contact(self, identifier):
        """Delete contact by name or phone"""
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == identifier.lower() or contact.phone == identifier:
                deleted_contact = self.contacts.pop(i)
                self.save_contacts()
                return deleted_contact
        return None
    
    def search_contacts(self, query):
        """Search contacts by name, phone, or email"""
        results = []
        query = query.lower()
        for contact in self.contacts:
            if (query in contact.name.lower() or 
                query in contact.phone or 
                query in contact.email.lower()):
                results.append(contact)
        return results
    
    def get_all_contacts(self):
        """Get all contacts"""
        return self.contacts
# ContactMaster 📇

A user-friendly Python application for managing personal or business contacts with full CRUD functionality and persistent data storage.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## 🎯 Project Overview

ContactMaster is a command-line contact management system designed to help users efficiently organize their personal and business contacts. Built with Python, it demonstrates fundamental programming concepts including object-oriented design, file I/O operations, and data validation.

### ✨ Key Features

- ➕ **Add Contacts** - Create new contacts with name, phone, email, and address
- 🔍 **Smart Search** - Find contacts by name, phone number, or email address
- 📋 **View All** - Display complete contact list with formatted output
- 🗑️ **Delete Contacts** - Remove contacts by name or phone number
- 💾 **Data Persistence** - Automatic save/load using JSON file storage
- ✅ **Input Validation** - Phone and email format validation

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- No additional dependencies required (uses only standard library)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MANJU-AR/Contact-Manager.git
   cd Contact-Manager
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

That's it! No pip installs needed.

## 📁 Project Structure

```
ContactMaster/
├── main.py              # Main application and user interface
├── contact.py           # Contact data model
├── contact_manager.py   # Contact management logic
├── utils.py            # Input validation utilities
├── data/
│   └── contacts.json   # Contact data storage
├── sample_data.json    # Sample contacts for testing
└── README.md          # Project documentation
```

## 🎮 Usage

### Main Menu Options

```
========================================
        CONTACT MASTER
========================================
1. Add New Contact
2. View All Contacts
3. Search Contacts
4. Delete Contact
5. Exit
========================================
```

### Adding a Contact

1. Select option 1 from the main menu
2. Enter contact details:
   - **Name** (required)
   - **Phone** (required, validated format)
   - **Email** (optional, validated format)
   - **Address** (optional)

### Searching Contacts

- Search by partial name match
- Search by phone number
- Search by email address
- Case-insensitive search

### Sample Usage

```python
# Example contact entry
Name: John Smith
Phone: +1-555-0101
Email: john.smith@email.com
Address: 123 Oak Street, Springfield, IL 62701
```

## 🔧 Technical Details

### Data Validation

- **Phone numbers**: Supports international formats with + prefix
- **Email addresses**: RFC-compliant email validation
- **Required fields**: Name and phone number
- **Optional fields**: Email and address

### Data Storage

- Contacts stored in JSON format
- Automatic file creation and management
- Data persists between application sessions
- Located in `data/contacts.json`

### Error Handling

- Graceful handling of file I/O errors
- Input validation with user-friendly error messages
- Keyboard interrupt handling (Ctrl+C)

## 🧪 Testing

### Load Sample Data

To quickly test the application with sample data:

1. Copy the contents of `sample_data.json`
2. Paste into `data/contacts.json`
3. Restart the application

### Test Scenarios

- [ ] Add valid contact
- [ ] Add contact with invalid phone/email
- [ ] Search existing contacts
- [ ] Search non-existent contacts
- [ ] Delete existing contact
- [ ] Delete non-existent contact
- [ ] View empty contact list
- [ ] Restart app to verify data persistence

## 🛠️ Development

### Code Organization

- **Object-Oriented Design**: Clean separation of concerns
- **Single Responsibility**: Each class has a focused purpose
- **Error Handling**: Comprehensive exception management
- **Input Validation**: Robust data validation using regex

### Key Classes

- `Contact`: Data model for individual contacts
- `ContactManager`: Handles CRUD operations and file I/O
- `ContactMasterApp`: User interface and application flow

## 🚀 Future Enhancements

- [ ] **Export/Import**: CSV and vCard support
- [ ] **Contact Groups**: Organize contacts into categories
- [ ] **Advanced Search**: Multiple criteria filtering
- [ ] **Edit Contacts**: Update existing contact information
- [ ] **Backup System**: Automatic data backup
- [ ] **GUI Version**: Tkinter or web-based interface
- [ ] **Contact Photos**: Image support for contacts
- [ ] **Duplicate Detection**: Find and merge duplicate entries


## 📝 Learning Objectives

This project is ideal for learning:

- **Python Fundamentals**: Classes, functions, data structures
- **File I/O Operations**: Reading and writing JSON files
- **Data Validation**: Using regular expressions
- **Error Handling**: Try-catch blocks and graceful failures
- **User Interface Design**: Menu-driven applications
- **Code Organization**: Project structure and modularity


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**MANJU A R**
- GitHub: [@MANJU-AR](https://github.com/MANJU-AR)
- Email: mr.manju.a.r@example.com

## 🙏 Acknowledgments

- Python community for excellent documentation
- Contributors and testers
- Open source community for inspiration

---

**Made with ❤️ for learning Python programming**

*If you found this project helpful, please consider giving it a ⭐️*

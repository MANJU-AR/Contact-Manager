import re

def validate_phone(phone):
    """Validate phone number format"""
    phone_pattern = re.compile(r'^[\+]?[1-9][\d]{0,15}$')
    return phone_pattern.match(phone.replace('-', '').replace(' ', ''))

def validate_email(email):
    """Validate email format"""
    if not email:  # Email is optional
        return True
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return email_pattern.match(email)

def get_valid_input(prompt, validator=None, required=True):
    """Get validated input from user"""
    while True:
        user_input = input(prompt).strip()
        
        if not user_input and required:
            print("This field is required. Please enter a value.")
            continue
        
        if not user_input and not required:
            return ""
        
        if validator and not validator(user_input):
            print("Invalid format. Please try again.")
            continue
        
        return user_input
import re

def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if re.match(email_pattern, email):
        return True
    else:
        return False
    

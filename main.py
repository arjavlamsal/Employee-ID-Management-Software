import random
import string
import json
import os

def generate_empID(length=10):
        characters = string.ascii_letters + string.digits
        empID = ''.join(random.choice(characters) for _ in range(length))
        return empID

def is_empID_unique(empID):
    if not os.path.exists(EMPLOYEE_ID_CHECK_FILE):
        return True
    with open(EMPLOYEE_ID_CHECK_FILE, 'r') as f:
        existing_empIDs = {line.strip() for line in f}
    return empID not in existing_empIDs

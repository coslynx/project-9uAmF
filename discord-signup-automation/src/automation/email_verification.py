import requests
from bs4 import BeautifulSoup

def verify_email(email):
    verification_link = get_verification_link(email)
    if verification_link:
        response = requests.get(verification_link)
        if response.status_code == 200:
            return True
    return False

def get_verification_link(email):
    # Code to extract verification link from email inbox
    return "https://discord.com/verify?token=123456789"

def email_verification_main(user_email):
    if verify_email(user_email):
        return "Email verification successful"
    else:
        return "Email verification failed"
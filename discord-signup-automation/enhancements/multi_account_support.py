import random
import time

def create_discord_account(username, email, password):
    print(f"Creating Discord account with username: {username}, email: {email}, and password: {password}")
    # Logic to create a Discord account

def multi_account_support(num_accounts):
    for i in range(num_accounts):
        username = f"user{i+1}"
        email = f"user{i+1}@example.com"
        password = "Password123"
        create_discord_account(username, email, password)
        # Introduce randomization in timings
        time.sleep(random.uniform(1, 3))

# Test the multi_account_support function
multi_account_support(3)
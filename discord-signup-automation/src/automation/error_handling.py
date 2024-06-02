import logging

def handle_error(error_code):
    error_messages = {
        1: "Invalid email format. Please provide a valid email address.",
        2: "Password is too weak. Please use a stronger password.",
        3: "Captcha could not be solved. Please try again later.",
        4: "Unexpected error occurred. Please try again.",
        5: "Email verification failed. Please verify your email address.",
        6: "Account creation failed. Please try again later."
    }
    
    if error_code in error_messages:
        logging.error(f"Error: {error_messages[error_code]}")
    else:
        logging.error("An unknown error occurred. Please try again later.")

# Test error handling
handle_error(1)
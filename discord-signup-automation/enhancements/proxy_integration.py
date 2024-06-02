import requests
import random
from src.api_integration.selenium_webdriver import WebDriver
from src.api_integration.2captcha_api import CaptchaSolver

class ProxyIntegration:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list

    def select_random_proxy(self):
        return random.choice(self.proxy_list)

    def create_account_with_proxy(self, user_info):
        proxy = self.select_random_proxy()
        webdriver = WebDriver(proxy)
        captcha_solver = CaptchaSolver()

        # Implement the account creation process using the selected proxy
        # This can include filling out the form, verifying email, handling captchas, etc.

        # Example:
        webdriver.fill_form(user_info)
        email_verification_status = webdriver.verify_email()
        if not email_verification_status:
            return "Email verification failed"

        captcha_solution = captcha_solver.solve_captcha()
        if not captcha_solution:
            return "Captcha solving failed"

        account_creation_status = webdriver.create_account(captcha_solution)
        if not account_creation_status:
            return "Account creation failed"

        return "Account created successfully with proxy: {}".format(proxy)
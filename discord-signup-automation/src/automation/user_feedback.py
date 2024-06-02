import logging

class UserFeedback:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(logging.StreamHandler())

    def notify_user(self, message):
        self.log.info(message)

    def log_error(self, error_message):
        self.log.error(error_message)
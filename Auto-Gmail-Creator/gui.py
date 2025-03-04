import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import requests
import csv
import string

# Your SMS-Activate API key
API_KEY = "8e49fdB90d0209c085dd1df56cedf00e"
COUNTRY_CODE = "175"

sms_activate_url = "https://sms-activate.org/stubs/handler_api.php"
phone_request_params = {
    "api_key": API_KEY,
    "action": "getNumber",
    "country": COUNTRY_CODE,
    "service": "go",
}

class GmailCreatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gmail Account Creator')
        layout = QVBoxLayout()

        self.firstNameInput = QLineEdit(self)
        self.firstNameInput.setPlaceholderText('First Name')
        layout.addWidget(self.firstNameInput)

        self.lastNameInput = QLineEdit(self)
        self.lastNameInput.setPlaceholderText('Last Name')
        layout.addWidget(self.lastNameInput)

        self.createButton = QPushButton('Create Account', self)
        self.createButton.clicked.connect(self.createAccount)
        layout.addWidget(self.createButton)

        self.logOutput = QTextEdit(self)
        self.logOutput.setReadOnly(True)
        layout.addWidget(self.logOutput)

        self.setLayout(layout)

    def createAccount(self):
        first_name = self.firstNameInput.text()
        last_name = self.lastNameInput.text()
        self.logOutput.append(f'Creating account for {first_name} {last_name}...')
        # Here you would call the account creation logic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GmailCreatorApp()
    ex.show()
    sys.exit(app.exec_())

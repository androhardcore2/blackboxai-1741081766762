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

def generatePassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))

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
        password = generatePassword()
        self.logOutput.append(f'Creating account for {first_name} {last_name}...')
        
        # Initialize the WebDriver
        driver = self.setDriver()
        
        # Example account creation logic
        driver.get('https://accounts.google.com/signup')
        time.sleep(2)  # Wait for the page to load

        # Here you would add the logic to fill in the form using Selenium
        # For example:
        # driver.find_element_by_name('firstName').send_keys(first_name)
        # driver.find_element_by_name('lastName').send_keys(last_name)
        # driver.find_element_by_name('username').send_keys(f"{first_name}.{last_name}{random.randint(100, 999)}")
        # driver.find_element_by_name('Passwd').send_keys(password)
        # driver.find_element_by_name('ConfirmPasswd').send_keys(password)

        driver.quit()  # Close the driver after the operation

    def setDriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GmailCreatorApp()
    ex.show()
    sys.exit(app.exec_())

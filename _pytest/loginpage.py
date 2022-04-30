from _pytest.selenium_wrapper import Selenium_Wrapper

class LoginPage(Selenium_Wrapper):
    def __init__(self, driver):
        super().__init__(driver)

    # Class variables
    _txt_email = ("name", "Email")
    _txt_password = ("name", "Password")
    _btn_login = ("xpath", "//input[@value='Log in']")

    def login_enter_email(self, email):
        self.enter_text(LoginPage._txt_email, value=email)
    
    def login_enter_password(self, password):
        self.enter_text(LoginPage._txt_password, value=password)
    
    def login_click_login(self):
        self.click_element(LoginPage._btn_login)




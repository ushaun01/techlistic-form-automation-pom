import pytest
from selenium import webdriver

from base_pages.login_form import LoginForm


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_login(driver):

    login_form = LoginForm(driver)

    login_form.open_page("https://www.techlistic.com/p/selenium-practice-form.html")

    login_form.enter_firstname("Usha")
    login_form.enter_lastname("Nazare")
    login_form.enter_sex()
    login_form.enter_experience()
    login_form.enter_date("20-5-2025")
    login_form.enter_profession()
    login_form.enter_tool()
    login_form.enter_drp1()
    login_form.enter_drp2()

    login_form.enter_image(
        r"D:\OneDrive\Pictures\Screenshots\Screenshot 2026-05-05 192527.png"
    )

    login_form.enter_submit()

    driver.save_screenshot(".\\screenshots\\successful_login.png")
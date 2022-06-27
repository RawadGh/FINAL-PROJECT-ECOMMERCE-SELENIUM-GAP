import time
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxOptions


@pytest.fixture()
def driver():
    Firefox_driver_binary = r"./drivers/geckodriver"
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=414")
    fire_fox_options.add_argument("--height=896")
    fire_fox_options.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS "
                                                                  "X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                                                  "Version/14.0.3 Mobile/15E148 Safari/604.1")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    yield driver
    driver.close()


def test_testInvalidEmailAddress(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#customer-login-link").click()
    time.sleep(6)
    driver.find_element(By.CSS_SELECTOR, "#email-login").click()
    driver.find_element(By.CSS_SELECTOR, "#email-login").send_keys("rawadgh#gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#send2-login > span:nth-child(1)").click()
    assert driver.find_element(By.CSS_SELECTOR,
                               "#email-login-error").text == 'דוא״ל - Please enter a valid email address (Ex: johndoe@domain.com).'


def test_testVerifyErrorMessagesForEnteringIncorrectValuesInFields(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    driver.find_element(By.ID, "customer-login-link").click()
    driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
    driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
    driver.find_element(By.ID, "send2-login").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#customer-account-link").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > div.block-content > ul > li.account-link > a").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div > div > "
                                         "div.customer-dashboard-navigation > div > div.user-nav-wrap > "
                                         "div.address > a > div.title").click()
    driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div > div > "
                                         "div.customer-dashboard-content > "
                                         "div.customer-dashboard-content-body > "
                                         "div.actions-toolbar.box-actions > div > a > span").click()
    time.sleep(5)
    driver.find_element(By.ID, "telephone").send_keys("abc")
    driver.find_element(By.ID, "city").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "#form-address-edit > div > div > button > span").click()
    # assert self.driver.find_element(By.ID, "telephone-error").text == "מספר טלפון - מספר טלפון נייד לא תקין"
    # assert self.driver.find_element(By.ID, "city-error").text == "עיר - שדה זה הוא חובה."
    assert driver.find_element(By.ID, "telephone-error").is_displayed()
    assert driver.find_element(By.ID, "city-error").is_displayed()


def test_testVerifyErrorMessagesForMandatoryFields(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)

    driver.find_element(By.ID, "customer-login-link").click()
    driver.find_element(By.CSS_SELECTOR, "#customer-popup-registration > span").click()
    driver.find_element(By.ID, "register_email_address").send_keys("rawadgh000@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".actions-toolbar-submit:nth-child(1) > .action").click()
    # assert self.driver.find_element(By.ID, "firstname-error").text == "שם פרטי - שדה זה הוא חובה."
    # assert self.driver.find_element(By.ID, "lastname-error").text == "שם משפחה - שדה זה הוא חובה."
    # assert self.driver.find_element(By.ID, "register_password-error").text == "סיסמה - שדה זה הוא חובה."

    assert driver.find_element(By.ID, "firstname-error").is_displayed()
    assert driver.find_element(By.ID, "lastname-error").is_displayed()
    assert driver.find_element(By.ID, "register_password-error").is_displayed()


def test_testPositiveRegistration(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    driver.find_element(By.ID, "customer-login-link").click()
    driver.find_element(By.CSS_SELECTOR, "#customer-popup-registration > span").click()
    driver.find_element(By.ID, "firstname").send_keys("rawad")
    driver.find_element(By.ID, "lastname").send_keys("ghname")
    fake = Faker()
    proper_email = fake.ascii_email()
    driver.find_element(By.ID, "register_email_address").send_keys(proper_email)
    driver.find_element(By.ID, "register_password").send_keys("Vd89651**")
    driver.find_element(By.CSS_SELECTOR, ".label:nth-child(2) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".actions-toolbar-submit:nth-child(1) span").click()
    time.sleep(15)
    driver.find_element(By.CSS_SELECTOR, "#customer-account-link").click()
    time.sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,
                               "#ui-id-5 > div.block-title.customer-name > span").text == 'היי, rawad'


def test_testSearchProduct(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "label.page-header-navigation-toggle").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "li.child_count_13:nth-child(2) > a:nth-child(1)").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "li.child_count_3:nth-child(4) > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR,
                        "li.child_count_3:nth-child(4) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(3) > li:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)").click()
    p1 = driver.find_element(By.CSS_SELECTOR,
                             ".product-item-details_439336 > div:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)").text
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".header-search-toggle").click()
    driver.find_element(By.CSS_SELECTOR, ".header-search-toggle").send_keys(p1)
    driver.find_element(By.CSS_SELECTOR, "#submit_search").click()
    time.sleep(5)
    # p1.is_displayed()
    driver.find_element(By.CSS_SELECTOR,
                        "#product_category_439336 > form:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1)").is_displayed()


def test_testBuyProduct(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    driver.find_element(By.ID, "customer-login-link").click()
    element = driver.find_element(By.ID, "customer-login-link")
    driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
    driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
    driver.find_element(By.CSS_SELECTOR, "#send2-login > span").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".page-header-navigation-toggle:nth-child(2)").click()
    driver.find_element(By.LINK_TEXT, "נשים").click()
    element = driver.find_element(By.LINK_TEXT, "נשים")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".category-item:nth-child(2) p:nth-child(1) strong").click()
    element = driver.find_element(By.CSS_SELECTOR, "#product_category_439342 .product-image-photo")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, "#product_category_439342 .prod_name .action").click()
    time.sleep(5)
    driver.find_element(By.ID, "option-label-color-93-439342-item-255").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,261.6000061035156)")
    driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-439342-item-169 > .show-text").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,261.6000061035156)")

    driver.find_element(By.NAME, "qty").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".input-select > option:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "לתשלום").click()
    time.sleep(5)
    element = driver.find_element(By.ID, "shipping_method_bar2go_bar2go_0")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, ".checkout-step-shipping_method > .checkout-step-title")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.ID, "shipping_method_bar2go_bar2go_0").click()
    driver.find_element(By.CSS_SELECTOR, ".checkout-step-actions:nth-child(3) .action").click()
    driver.execute_script("window.scrollTo(0,124.80000305175781)")
    time.sleep(5)
    driver.find_element(By.ID, "shipping_city").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".checkout-step-shipping > .checkout-step-content").click()
    driver.find_element(By.ID, "shipping_city").send_keys("נצרת")
    driver.find_element(By.ID, "shipping_city").click()
    driver.find_element(By.ID, "shipping_street").click()
    driver.find_element(By.CSS_SELECTOR, ".checkout-index-index").click()
    driver.find_element(By.ID, "shipping_street").click()
    driver.find_element(By.ID, "shipping_street").send_keys("רח 4085")
    driver.find_element(By.ID, "shipping_number").click()
    driver.find_element(By.ID, "shipping_number").send_keys("1")
    driver.find_element(By.ID, "shipping_apartment").click()
    driver.find_element(By.ID, "shipping_apartment").send_keys("1")
    driver.find_element(By.ID, "shipping_telephone").click()
    driver.find_element(By.ID, "shipping_telephone").send_keys("0549193810")
    driver.find_element(By.CSS_SELECTOR, ".checkout-step-actions:nth-child(5) .action").click()
    driver.execute_script("window.scrollTo(0,261.6000061035156)")
    assert driver.find_element(By.CSS_SELECTOR, ".grand_total-sum-83 > .amount > span").text == "83.00 ₪"


def test_testAddToWishlist(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".page-header-navigation-toggle:nth-child(2)").click()
    element = driver.find_element(By.ID, "page-header-navigation-toggle")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title").click()
    driver.find_element(By.CSS_SELECTOR, ".category-item:nth-child(2) p:nth-child(1) strong").click()
    time.sleep(5)
    element = driver.find_element(By.CSS_SELECTOR, "#product_category_439342 .product-image-photo")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "OMG! I WISH!").click()
    element = driver.find_element(By.LINK_TEXT, "OMG! I WISH!")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".icon").click()
    element = driver.find_element(By.CSS_SELECTOR, ".icon")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "#product_wishlist_439343 .product-image-photo")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.execute_script("window.scrollTo(0,184.8000030517578)")
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.LINK_TEXT, "מכנסיים קצרים | חליפת צ’יירס")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.LINK_TEXT, "מכנסיים קצרים | חליפת צ’יירס").click()
    driver.execute_script("window.scrollTo(0,598.4000244140625)")
    time.sleep(5)
    driver.find_element(By.ID, "option-label-color-93-439343-item-270").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-439343-item-303 > .show-text").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".to_checkout_button > a:nth-child(1)").click()
    time.sleep(3)
    assert driver.find_element(By.CSS_SELECTOR, ".checkout-login-title .main-title").text == "התחברות/ הרשמה"


def test_TestShoppingCartSummary(driver):
    driver.get("https://www.urbanica-wh.com/")
    time.sleep(5)
    element = driver.find_element(By.ID, "customer-login-link")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.ID, "customer-login-link").click()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.ID, "email-login").click()
    driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
    driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
    element = driver.find_element(By.CSS_SELECTOR, "#send2-login > span")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, "#send2-login > span").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".page-header-navigation-toggle:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title").click()
    element = driver.find_element(By.CSS_SELECTOR, ".category-item:nth-child(2) p:nth-child(1) strong")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".category-item:nth-child(2) p:nth-child(1) strong").click()
    driver.find_element(By.CSS_SELECTOR, "#product_category_439342 .prod_name .action").click()
    driver.execute_script("window.scrollTo(0,124.80000305175781)")

    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-439342-item-303 > .show-text").click()
    time.sleep(5)
    driver.find_element(By.ID, "option-label-color-93-439342-item-221").click()
    time.sleep(5)

    driver.find_element(By.ID, "product-addtocart-button").click()
    driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) > .value").click()
    driver.find_element(By.CSS_SELECTOR, ".showcart").click()
    element = driver.find_element(By.CSS_SELECTOR, ".showcart")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".to_cart .text").click()
    q1 = driver.find_element(By.CSS_SELECTOR,
                             "div.checkout-cart-totals-wrapper:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "div.product-item-qty:nth-child(1) > select:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR,
                        "div.product-item-qty:nth-child(1) > select:nth-child(2) > option:nth-child(2)").click()
    time.sleep(5)
    q2 = driver.find_element(By.CSS_SELECTOR,
                             "div.checkout-cart-totals-wrapper:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
    assert q1 != q2

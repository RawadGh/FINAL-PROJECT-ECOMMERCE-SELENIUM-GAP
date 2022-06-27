from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome import webdriver
from faker import Faker
from selenium.webdriver.edge import webdriver
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By



class TestTestUrbanicaFireFoxTisting():

    def setup_method(self, method):
        edge_driver_binary = "./drivers/msedgedriver"
        ser_edge = EdgeService(edge_driver_binary)
        self.driver = webdriver.Edge(service=ser_edge)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testInvalidEmailAddress(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.ID, "email-login").click()
        self.driver.find_element(By.ID, "email-login").send_keys("rawadgh#gmail.com")
        self.driver.find_element(By.ID, "send2-login").click()
        assert self.driver.find_element(By.ID,
                                        "email-login-error").text == 'דוא״ל - כתובת האימייל שהזנת אינה תקינה (לדוגמא: example@example.co.il).'


    def test_testVerifyErrorMessagesForEnteringIncorrectValuesInFields(self):
        self.driver.get("https://www.urbanica-wh.com/")
        time.sleep(10)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
        self.driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
        self.driver.find_element(By.ID, "send2-login").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#customer-account-link").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#ui-id-5 > div.block-content > ul > li.account-link > a").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div > div > "
                                                  "div.customer-dashboard-navigation > div > div.user-nav-wrap > "
                                                  "div.address > a > div.title").click()
        self.driver.find_element(By.CSS_SELECTOR, "#maincontent > div.columns > div > div > "
                                                  "div.customer-dashboard-content > "
                                                  "div.customer-dashboard-content-body > "
                                                  "div.actions-toolbar.box-actions > div > a > span").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "telephone").send_keys("abc")
        time.sleep(4)
        self.driver.find_element(By.ID, "city").send_keys("0")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#form-address-edit > div > div > button > span").click()
        assert self.driver.find_element(By.ID, "telephone-error").text == "מספר טלפון - מספר טלפון נייד לא תקין"
        assert self.driver.find_element(By.ID, "city-error").text == "עיר - שדה זה הוא חובה."
        time.sleep(4)
        # assert self.driver.find_element(By.CSS_SELECTOR, "#telephone-error").is_displayed()
        # assert self.driver.find_element(By.CSS_SELECTOR, "#city-error").is_displayed()

    def test_testVerifyErrorMessagesForMandatoryFields(self):
        self.driver.get("https://www.urbanica-wh.com/")
        time.sleep(10)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.CSS_SELECTOR, "#customer-popup-registration > span").click()
        self.driver.find_element(By.ID, "register_email_address").send_keys("rawadgh000@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".actions-toolbar-submit:nth-child(1) > .action").click()
        # assert self.driver.find_element(By.ID, "firstname-error").text == "שם פרטי - שדה זה הוא חובה."
        # assert self.driver.find_element(By.ID, "lastname-error").text == "שם משפחה - שדה זה הוא חובה."
        # assert self.driver.find_element(By.ID, "register_password-error").text == "סיסמה - שדה זה הוא חובה."

        assert self.driver.find_element(By.ID, "firstname-error").is_displayed()
        assert self.driver.find_element(By.ID, "lastname-error").is_displayed()
        assert self.driver.find_element(By.ID, "register_password-error").is_displayed()

    def test_testPositiveRegistration(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.CSS_SELECTOR, "#customer-popup-registration > span").click()
        self.driver.find_element(By.ID, "firstname").send_keys("rawad")
        self.driver.find_element(By.ID, "lastname").send_keys("ghname")
        fake = Faker()
        proper_email = fake.ascii_email()
        self.driver.find_element(By.ID, "register_email_address").send_keys(proper_email)
        self.driver.find_element(By.ID, "register_password").send_keys("Vd89651**")
        self.driver.find_element(By.CSS_SELECTOR, ".label:nth-child(2) > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".actions-toolbar-submit:nth-child(1) span").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,"#customer-account-link").click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "#ui-id-5 > div.block-title.customer-name > span").text == 'היי, rawad'

    def test_testSearchProduct(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        Women = self.driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title")
        hover = ActionChains(self.driver).move_to_element(Women)
        hover.perform()
        time.sleep(3)
        Tshirt = self.driver.find_element(By.CSS_SELECTOR, "#page-header-navigation > nav > div > ul > "
                                                           "li.category-item.child_count_13"
                                                           ".menu_item_layout_cols_banner.level_0.parent > div > div "
                                                           "> "
                                                           "div.page-header-navigation-dropdown-nav.page-header"
                                                           "-navigation-dropdown-nav_1 > ul > li:nth-child(4) > a > "
                                                           "span > span")
        Tshirt.click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#product_category_436789 > form > div > div.prod_info.padding_hf_h "
                                                  "> div.prod_name.margin_hf_v > h2 > a").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "חפש").click()
        self.driver.find_element(By.ID, "header-search-input").send_keys("חולצת אלמה")
        self.driver.find_element(By.ID, "header-search-input").send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#product_category_436789 > form > div > div.prod_info.padding_hf_h "
                                                  "> div.prod_name.margin_hf_v > h2 > a").is_displayed()

    def test_testBuyProduct(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
        self.driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
        self.driver.find_element(By.ID, "send2-login").click()
        time.sleep(10)
        Women = self.driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title")
        hover = ActionChains(self.driver).move_to_element(Women)
        hover.perform()
        time.sleep(3)
        Tshirt = self.driver.find_element(By.CSS_SELECTOR, "#page-header-navigation > nav > div > ul > "
                                                           "li.category-item.child_count_13"
                                                           ".menu_item_layout_cols_banner.level_0.parent > div > div "
                                                           "> "
                                                           "div.page-header-navigation-dropdown-nav.page-header"
                                                           "-navigation-dropdown-nav_1 > ul > li:nth-child(4) > a > "
                                                           "span > span")
        Tshirt.click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_category_402567 > form > div > div.prod_info.padding_hf_h > "
                                 "div.prod_name.margin_hf_v > h2 > a").click()
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-color-93-402567-item-5564").click()
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-402567-item-170 > span.show-text").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_addtocart_form > div > div.prod_wrap > "
                                 "div.prod_shop.dt_sticky.inline.padding_db.sp_padding_qt_h.sp_w_100.top.w_35 > "
                                 "div.product-item-quantity.field > div > select").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_addtocart_form > div > div.prod_wrap > "
                                 "div.prod_shop.dt_sticky.inline.padding_db.sp_padding_qt_h.sp_w_100.top.w_35 > "
                                 "div.product-item-quantity.field > div > select > option:nth-child(2)").click()

        time.sleep(10)
        self.driver.find_element(By.ID, "product-addtocart-button").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#minicart-content-wrapper > div > div.minicart_content > div.buttons_wrap > "
                                 "div.to_checkout > div > a").click()
        self.driver.find_element(By.CSS_SELECTOR, "#shipping_method_bar2go_bar2go_0").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#checkout > div.checkout-container > "
                                 "div.checkout-container-steps.inline.padding.top > div.steps > "
                                 "div.checkout-step.checkout-step-shipping_method.is__open > "
                                 "div.checkout-step-content > div.checkout-step-actions > div > button").click()
        time.sleep(4)

        self.driver.find_element(By.CSS_SELECTOR,
                                 "#checkout > div.checkout-container > "
                                 "div.checkout-container-steps.inline.padding.top > div.steps > "
                                 "div.checkout-step.checkout-step-shipping.is__open > div.checkout-step-content > "
                                 "div.address-field.fields-container > div.city.inline.top.w_100").click()
        self.driver.find_element(By.ID, "shipping_city").send_keys("נצרת")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#shipping_city").click()

        self.driver.find_element(By.CSS_SELECTOR, ".checkout-index-index").click()
        self.driver.find_element(By.ID, "shipping_street").send_keys("רח 4000")
        self.driver.find_element(By.ID, "shipping_number").send_keys("1")
        self.driver.find_element(By.ID, "shipping_apartment").send_keys("1")

        self.driver.find_element(By.ID, "shipping_telephone").send_keys("0549193810")
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#checkout > div.checkout-container > "
                                 "div.checkout-container-steps.inline.padding.top > div.steps > "
                                 "div.checkout-step.checkout-step-shipping.is__open > div.checkout-step-content > "
                                 "div.checkout-step-actions > div > button > span").click()
        time.sleep(10)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "#cart-totals > div.grand_total-total.grand_total-sum-99 > div.amount > span").text == "99.00 ₪"

    def test_testAddToWishlist(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        time.sleep(5)

        Women = self.driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title")
        hover = ActionChains(self.driver).move_to_element(Women)
        hover.perform()
        time.sleep(3)

        Tshirt = self.driver.find_element(By.CSS_SELECTOR, "#page-header-navigation > nav > div > ul > "
                                                           "li.category-item.child_count_13"
                                                           ".menu_item_layout_cols_banner.level_0.parent > div > div "
                                                           "> "
                                                           "div.page-header-navigation-dropdown-nav.page-header"
                                                           "-navigation-dropdown-nav_1 > ul > li:nth-child(4) > a > "
                                                           "span > span")
        Tshirt.click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#cbar_POP2_36044 > img").click()
        time.sleep(10)

        product1 = self.driver.find_element(By.CSS_SELECTOR, "#product_category_402567")
        hover = ActionChains(self.driver).move_to_element(product1)
        hover.perform()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#product_category_402567 > form > div > div.prod_image.padding_hf "
                                                  "> div.prod_mylist.padding_hf > div > a").click()
        time.sleep(10)

        self.driver.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > header > div > div.header_container.ltr "
                                                  "> "
                                                  "div.header_right.inline.middle.padding_hf_h.padding_v.rtl.w_33"
                                                  ".padding_hf > "
                                                  "div.header_wishlist.inline.middle.padding_hf.sp_padding_qt > div > "
                                                  "div > a").click()
        self.driver.find_element(By.LINK_TEXT, "חולצת אוברסייז ROCK").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-color-93-402567-item-5564").click()
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-402567-item-170 > span.show-text").click()

        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.page-wrapper > header > div > div.header_container.ltr > div.header_right.inline.middle.padding_hf_h.padding_v.rtl.w_33.padding_hf > div.header_cart.inline.middle.padding_hf.sp_padding_hf_r.sp_padding_qt > div > div > a").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 " #minicart-content-wrapper > div > div.minicart_content > div.buttons_wrap > div.to_checkout > div > a > span").click()
        time.sleep(10)
        assert self.driver.find_element(By.CSS_SELECTOR, "#checkout > div.checkout-container > "
                                                         "div.checkout-container-steps.inline.padding.top > "
                                                         "div.checkout-container-panel.grid.grid_2.grid_gap.sp_grid_1"
                                                         ".tb_p_grid_1 > div.block_register > div > "
                                                         "div.checkout-login-wraper > div.checkout-login-content > "
                                                         "div > a.button.primary.action.login-link").text == \
               "התחברות/הרשמה"

    def TestTestShoppingCartSummary(self):
        self.driver.get("https://www.urbanica-wh.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "customer-login-link").click()
        self.driver.find_element(By.ID, "email-login").send_keys("rawadgh592@gmail.com")
        self.driver.find_element(By.ID, "pass-login").send_keys("vd89651**")
        self.driver.find_element(By.ID, "send2-login").click()
        time.sleep(10)
        Women = self.driver.find_element(By.CSS_SELECTOR, ".child_count_13:nth-child(2) > .nav_link .title")
        hover = ActionChains(self.driver).move_to_element(Women)
        hover.perform()
        time.sleep(3)
        Tshirt = self.driver.find_element(By.CSS_SELECTOR, "#page-header-navigation > nav > div > ul > "
                                                           "li.category-item.child_count_13"
                                                           ".menu_item_layout_cols_banner.level_0.parent > div > div "
                                                           "> "
                                                           "div.page-header-navigation-dropdown-nav.page-header"
                                                           "-navigation-dropdown-nav_1 > ul > li:nth-child(4) > a > "
                                                           "span > span")
        Tshirt.click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#cbar_POP2_36044 > img").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_category_402567 > form > div > div.prod_info.padding_hf_h > "
                                 "div.prod_name.margin_hf_v > h2 > a").click()
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-color-93-402567-item-5564").click()
        self.driver.find_element(By.CSS_SELECTOR, "#option-label-size-141-402567-item-169 > span.show-text").click()
        time.sleep(10)

        self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.page-wrapper > header > div > div.header_container.ltr > div.header_right.inline.middle.padding_hf_h.padding_v.rtl.w_33.padding_hf > div.header_cart.inline.middle.padding_hf.sp_padding_hf_r.sp_padding_qt > div > div > a").click()
        time.sleep(10)

        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#minicart-content-wrapper > div > div.minicart_content > div.buttons_wrap > div.to_cart").click()
        time.sleep(10)
        q1 = self.driver.find_element(By.CSS_SELECTOR,
                                      "#cart-totals > div.subtotal-total.subtotal-sum-40 > div.amount > span").text

        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_addtocart_form > div > div.prod_wrap > "
                                 "div.prod_shop.dt_sticky.inline.padding_db.sp_padding_qt_h.sp_w_100.top.w_35 > "
                                 "div.product-item-quantity.field > div > select").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#product_addtocart_form > div > div.prod_wrap > "
                                 "div.prod_shop.dt_sticky.inline.padding_db.sp_padding_qt_h.sp_w_100.top.w_35 > "
                                 "div.product-item-quantity.field > div > select > option:nth-child(2)").click()
        time.sleep(10)

        q2 = self.driver.find_element(By.CSS_SELECTOR,
                                      "#cart-totals > div.subtotal-total.subtotal-sum-40 > div.amount > span").text
        assert q1 != q2

        time.sleep(4)

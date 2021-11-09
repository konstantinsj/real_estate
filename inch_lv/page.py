from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inch_lv.locators import Locators
from crypto_api.main import Crypto


class InchLv(object):
    """
    Inch.lv data parser.
    """

    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver')  # path to chromedriver
        self.wait = WebDriverWait(self.browser, 10)
        self.scroll_into_view = "arguments[0].scrollIntoView();"

    def get_data(self, url='https://inch.lv/browse?',
                 type='apartment',
                 priceTo="",
                 deal_type='sale',
                 districts='R%C4%ABga',
                 subdistricts='Centrs%2CVecr%C4%ABga',
                 crypto='BTC'):
        """
        returns list of results
        """

        self.browser.get(
            f"{url}type={type}&districts={districts}&subdistricts={subdistricts}&priceTo={priceTo}&dealType={deal_type}");
        result = list()
        while True:
            try:
                self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'browse-card-list__data')))
                elements = self.browser.find_element(*Locators.CARD_LIST)
                ads = elements.find_elements(*Locators.CARDS)
                print(f"Got {len(ads)} results on this page")
                convert = Crypto()  # getting crypto rates
                for i in range(len(ads)):  # iterating elements on page
                    price = int(''.join(j for j in ads[i].find_element(*Locators.COST_PRICE).text if j.isdigit()))
                    crypto_price = convert.get_price_in_crypto(price, "EUR", crypto)    #converting to crypto
                    result.append({'address': ads[i].find_element(*Locators.ADDRESS).text,
                                   'price': f"{price} EUR",
                                   'crypto price': f"{crypto_price}"})
                    self.browser.execute_script(self.scroll_into_view, ads[i])  # need to scroll otherwise no result
                try:
                    self.browser.find_element(*Locators.NEXT_PAGE_DISABLED).is_displayed()
                    print("No next page!")
                    break
                except (TimeoutException, WebDriverException):
                    try:
                        self.browser.find_element(*Locators.NEXT_PAGE).click()
                    except (TimeoutException, WebDriverException):
                        break
            except (TimeoutException, WebDriverException):  # 0 results
                print("No data found")
                break

        print(f"Total results: {len(result)}")
        self.close()
        return result

    def close(self):
        if self.browser is not None:
            print("Closing browser")
            self.browser.close()
            self.browser.quit()

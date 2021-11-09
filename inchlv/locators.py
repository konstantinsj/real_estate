from selenium.webdriver.common.by import By

class Locators(object):
    """A class for main page locators. All main page locators should come here"""

    NEXT_PAGE = By.CLASS_NAME, "browse__pagination__next"
    CARD_LIST = By.CLASS_NAME, 'browse-card-list__data'
    CARDS = By.CLASS_NAME, "browse-card-wrapper"
    COST_PRICE = By.CLASS_NAME, "browse-card__cost__price"
    NEXT_PAGE_DISABLED = By.CLASS_NAME, "browse__pagination__border.browse__pagination__border--disabled"
    ADDRESS = By.CLASS_NAME, 'browse-card__address__text'
from inch_lv.page import InchLv
from inch_lv.helpers import Helpers as h
from ss_com import ss_scraping


def main():
    # get data from inch.lv and save it:
    page = InchLv()
    result = page.get_data(subdistricts="Centrs", priceTo="100000", crypto="BTC")
    h.save_file(result, "output.txt")

    # get data from ss.lv and save it:
    ss_scraping.scrape("https://www.ss.com/lv/real-estate/flats/ogre-and-reg/sell/", "dzivokli_ogre.txt")


if __name__ == "__main__":
    main()

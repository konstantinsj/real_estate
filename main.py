import time
from inchlv.page import InchLv
from inchlv.helpers import Helpers as h


def main():
    page = InchLv()
    result = page.get_data(subdistricts="Pļavnieki", crypto="BTC")
    print(result)
    h.save_file(result, "output.txt")


if __name__ == "__main__":
    main()

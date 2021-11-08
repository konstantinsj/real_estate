import time
from page import InchLv
from crypto_api.main import Crypto


def main():
    start_time = time.time()
    page = InchLv()
    result = page.get_data(subdistricts="Pļavnieki")
    page.close()
    print(result)
    save_file(result, "output.txt")
    print("--- %s seconds ---" % (time.time() - start_time))


def save_file(result, output="output.txt", encoding="utf-8"):
    with open(output, mode="w", encoding=encoding) as w:
        w.writelines(f"{str(result)}\n")
        print(f"Result saved in {output}")


if __name__ == "__main__":
    main()

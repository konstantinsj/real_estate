class Helpers():

    def save_file(result, output="output.txt", encoding="utf-8"):
        with open(output, mode="w", encoding=encoding) as w:
            w.writelines(f"{str(result)}\n")
            print(f"Result saved in {output}")
class Helpers():

    def save_file(self, output="output.txt", encoding="utf-8"):
        with open(output, mode="w", encoding=encoding) as w:
            w.writelines(f"{str(self)}\n")
            print(f"Result saved in {output}")

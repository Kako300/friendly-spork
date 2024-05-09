class MultiplicationTable:
    @classmethod
    def print_table(cls, size=12):
        for i in range(1, size + 1):
            print(" ".join(f"{i * j:4}" for j in range(1, size + 1)))

MultiplicationTable.print_table()
# pattern_generator.py
# Hacktoberfest Python Practice - Sparsh Gupta
# Program to print a pyramid pattern using nested loops

def pyramid(rows: int):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

if __name__ == "__main__":
    rows = 5
    print("Pyramid Pattern Generator\n")
    pyramid(rows)

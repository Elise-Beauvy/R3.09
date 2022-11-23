import sys
from PyQt5.QtWidgets import QMessageBox


"""def divEntier(x: int, y: int) -> int:
    try:
        if x < y:
            print("x inferieur", "x:", x, "y:", y)
            print(0)

    except ValueError:
        return "Valeur incorrect"

    else:
        print("x superieur", "x:", x, "y:", y)
        x = x - y
        return divEntier(x, y) + 1"""
def divEntier(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError("entier pas divisible par 0")
    if x < y:
        return 0
    else:
         x = x - y
         return divEntier(x, y) + 1


if __name__ == "__main__":
    try:
        x = int(input("x:"))
        y = int(input("y:"))
    except ValueError:
        print("n'est pas un entier")
    except (ValueError, TypeError, ZeroDivisionError) as err:
        print(err)
    else:
        print(divEntier(x, y))
    sys.exit()


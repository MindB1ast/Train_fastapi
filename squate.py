import argparse
import math


def solve_complex(a: float, b: float, c: float):
    if a != 0:
        D = b ** 2 - 4 * a * c
        x1 = complex((-b + D ** 0.5) / (2 * a))
        x2 = complex((-b - D ** 0.5) / (2 * a))
        return x1, x2
    else:
        return None, None


def solve(a: float, b: float, c: float):
    if a != 0:
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return x1, x2
        else:
            return None, None
    else:
        return None, None


def main():
    parser = argparse.ArgumentParser(description='Решение квадратного уравнения, Ax^2+Bx+c')

    parser.add_argument("-A", required=True, type=float, dest="A", help="A")
    parser.add_argument("-B", required=True, type=float, dest="B", help="B")
    parser.add_argument("-C", required=True, type=float, dest="C", help="C")
    parser.add_argument("--complex", action='store_const', const=True, default=False, dest="complex",
                        help="При вводе даного значения расщитывает комплексные результаты уравнения")

    args = parser.parse_args()

    if args.complex:
        result = solve_complex(args.A, args.B, args.C)
    else:
        result = solve(args.A, args.B, args.C)
    if result is not None:
        for i in result:
            print(i)
    else:
        print("error")


if __name__ == "__main__":
    main()

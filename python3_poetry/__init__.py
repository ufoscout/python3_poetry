"""main file"""

__version__ = '0.1.0'


def main() -> None:
    """main"""
    print("Hello World!")


if __name__ == "__main__":
    main()


def multiply(x_arg: float, y_arg: float) -> float:
    """multiply"""
    print("First value is: " + str(x_arg))
    print("Second value is: " + str(y_arg))
    return x_arg * y_arg

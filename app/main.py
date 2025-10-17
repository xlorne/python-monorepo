from lib import Math


def main():
    result = Math.add(3, 5)
    print(f"3 + 5 = {result}")
    result = Math.sub(5, 3)
    print(f"5 - 3 = {result}")
    result = Math.mul(5, 3)
    print(f"5 * 3 = {result}")
    result = Math.div(5, 3)
    print(f"5 / 3 = {result}")


if __name__ == "__main__":
    main()

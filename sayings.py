def main():
    hello("world")
    goodbye("world")

print("this is at main function")
def hello(name):
    print(f"hello, {name}")

print("below def hello")
def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    print(__name__ + "at the top")
    main()

print(__name__ + "at the bottom")
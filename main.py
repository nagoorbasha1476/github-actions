import os

def main():
    print("Hello, world!")
    print("The value of the MY_SECRET environment variable is:", os.environ.get('MY_SECRET'))

if __name__ == "__main__":
    main()

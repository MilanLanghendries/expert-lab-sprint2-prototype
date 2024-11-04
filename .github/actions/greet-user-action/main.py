import os

def main():
    name = os.getenv('INPUT_NAME')  # Get the input from the GitHub Action
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

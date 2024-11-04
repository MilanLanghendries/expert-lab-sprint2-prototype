import os

def main():
    name = os.getenv('INPUT_NAME', 'GitHub User')
    print(f"Hello, {name}! Welcome to the repository!")

if __name__ == "__main__":
    main()

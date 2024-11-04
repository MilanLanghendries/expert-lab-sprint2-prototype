from app import create_app  # Import the create_app function

app = create_app()  # Create an instance of the app

if __name__ == "__main__":
    app.run()  # This is for local testing (not needed when using Waitress)

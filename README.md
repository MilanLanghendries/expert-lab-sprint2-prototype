# My Flask App

This is a simple Flask web application that serves a greeting page. The application is set up with GitHub Actions for testing and deployment. It also includes a custom GitHub Action to greet users.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [GitHub Actions](#github-actions)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Custom Action](#custom-action)
- [Documention](#documentation)
- [Contributing](#contributing)

## Features

- A simple web page that greets users.
- Unit tests to ensure code quality.
- Automated testing and deployment using GitHub Actions.
- Custom GitHub Action to greet users.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

3. Install the required packages:
    ```bash
    pip install -r requirements.txt

## Usage

To run the Flask application locally, execute the following command:
    ```bash
    python -m venv venv


## GitHub Actions

### Testing

The application includes a GitHub Action that automatically runs tests whenever changes are pushed to the repository. The workflow file for testing is located at `.github/workflows/test.yml`. It checks for any issues in the code and runs the unit tests defined in the `tests/test_routes.py` file.

### Deployment

Deployment to Render is automated through a GitHub Action. The workflow file for deployment is located at `.github/workflows/deploy.yml`. To successfully deploy your application, ensure you have the following:

1. **Render API Key**: You must set your Render API key as a secret in your GitHub repository. This allows the GitHub Action to authenticate and deploy to your Render service.

2. **Service ID**: You need to specify your Render service ID in the deployment workflow. This is essential for the action to know where to deploy your application.

### Custom Action

The repository also contains a custom GitHub Action located at `.github/actions/greet-user-action/`. This action is designed to greet users by name. The action configuration is specified in the `action.yml` file within this directory. Here are the key components of the custom action:

- **Inputs**: The action accepts a `name` input, which is used to personalize the greeting.
- **Execution**: The action is set up to run a Python script (`main.py`) that generates the greeting message.


## Documentation

Here are some resources that may have been used for reference or inspiration while developing this project:

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/) - Official documentation for Flask, a web framework for Python.
- [GitHub Actions Documentation](https://docs.github.com/en/actions) - Learn how to create and manage GitHub Actions workflows.
- [GitHub Actions Custom Actions](https://docs.github.com/en/actions/creating-actions) - Information on creating custom actions for GitHub workflows.
- [Python Official Documentation](https://docs.python.org/3/) - The official Python documentation.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.


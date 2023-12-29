# Account Knocking Tool

## Overview

The Account Knocking Tool is an automated testing tool that uses Selenium to check whether an account exists on popular websites such as Quora, Spotify, eBay, ESPN, and Pinterest. The tool takes advantage of web automation to perform account existence checks efficiently.

## Approach

### Selenium Automation

The tool leverages the Selenium framework for web automation, allowing it to interact with the websites programmatically. Selenium provides a convenient way to simulate user actions and extract information from web pages, making it ideal for account checking scenarios.

### Command-Line Interface (CLI)

The tool is equipped with a user-friendly Command-Line Interface (CLI) that requires two arguments: `-email` for the email address to check and `-url` for the target website (Quora, Spotify, eBay, ESPN, Pinterest).

## Why This Method

Automating the account-checking process with Selenium offers several advantages:

- **Efficiency:** The tool quickly checks account existence without manual intervention.
- **Consistency:** Automated tests provide consistent and repeatable results.
- **Scalability:** Easily extendable to support additional websites or functionalities.

## Requirements

- [Typer](https://github.com/tiangolo/typer)
- [Selenium](https://www.selenium.dev/)

## Setup

1. Install [Poetry](https://python-poetry.org/docs/).
2. Clone the repository: `git clone https://github.com/chanleeip/Account_knocking.git`
3. Run `poetry install` to install project dependencies.

## Usage

```bash
poetry run python3 cli.py --email user@example.com --url quora
```
## Sample Output
1. If the account exists: ``` Account exists```
2. If the account does not exist: ```Account does not exist```
3. If an invalid URL is provided: ``` Invalid URL```

## Note

Make sure to adapt the URLs and specific details according to your project structure and requirements.


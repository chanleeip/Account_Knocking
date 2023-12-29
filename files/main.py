from ebay import check_ebay_account
from espn import check_account_espn
from pinterest import check_pinterest_account
from quora import check_account_quora
from spotify import check_account_spotify

def main(email, url):
    if url == "ebay":
        if check_ebay_account(email):
            print("Account exists")
        else:
            print("Account does not exist")
    elif url == "espn":
        if check_account_espn(email):
            print("Account exists")
        else:
            print("Account does not exist")
    elif url == "pinterest":
        if check_pinterest_account(email):
            print("Account exists")
        else:
            print("Account does not exist")
    elif url == "quora":
        if check_account_quora(email):
            print("Account exists")
        else:
            print("Account does not exist")
    elif url == "spotify":
        if check_account_spotify(email):
            print("Account exists")
        else:
            print("Account does not exist")
    else:
        print("Error: Invalid URL")

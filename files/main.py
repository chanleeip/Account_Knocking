from files.ebay import check_ebay_account
from files.espn import check_account_espn
from files.pinterest import check_pinterest_account
from files.quora import check_account_quora
from files.spotify import check_account_spotify

def print_box(message):
    border = '+' + '-' * (len(message) + 2) + '+'
    content = '| ' + message + ' |'
    print(border)
    print(content)
    print(border)

def main(email, url):
    if url == "ebay":
        if check_ebay_account(email):
            print_box("Account exists")
        else:
            print_box("Account does not exist")
    elif url == "espn":
        if check_account_espn(email):
            print_box("Account exists")
        else:
            print_box("Account does not exist")
    elif url == "pinterest":
        if check_pinterest_account(email):
            print_box("Account exists")
        else:
            print_box("Account does not exist")
    elif url == "quora":
        if check_account_quora(email):
            print_box("Account exists")
        else:
            print("Account does not exist")
    elif url == "spotify":
        if check_account_spotify(email):
            print_box("Account exists")
        else:
            print_box("Account does not exist")
    else:
        print_box("Error: Invalid URL")

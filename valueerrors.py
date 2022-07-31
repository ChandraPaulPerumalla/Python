balance = 1000
amount ="300"

def take_card():
    print("Take the card out of ATM")
try:
    if balance>=int(amount):
        print("withdraw")
    else:
        print("Invalid amount")
except TypeError:
    print("Type error occurred")
except valueError:
    print("Value Error occurred")
except:
    print("some error occurred")
finally:
    take_card()
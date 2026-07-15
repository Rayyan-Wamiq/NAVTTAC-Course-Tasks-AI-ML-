def withdraw_amount(balance,amount):
    if balance<amount:
        raise ValueError ("Invalid Value ")
    return amount, balance
try:
    print(withdraw_amount(600,120))
except ValueError as e:
    print(e)
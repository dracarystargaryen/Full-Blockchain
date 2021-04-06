def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('----')
    print("recipient: " + dict['recipient'])
    print('----')
    print("value: " + str(dict['value']))
    print('----')
    print("time: " + str(dict['time']))
    print ('----')

transactions = []

Bob = Client()
Joe = Client()
Tom = Client()
Tim = Client()

t1 = Transaction(
    Bob,
    Joe.identity,
    15.0
)
t1.sign_transaction()
transactions.append(t1)

t2 = Transaction(
    Bob,
    Tom.identity,
    5.0
)

t2.sign_transaction()
transactions.append(t2)


t3 = Transaction(
    Bob,
    Tim.identity,
    4.0
)

t3.sign_transaction()
transactions.append(t3)


t4 = Transaction(
    Joe,
    Bob.identity,
    16.0
)

t4.sign_transaction()
transactions.append(t4)


t5 = Transaction(
    Joe, 
    Tom.identity,
    9.0
)

t5.sign_transaction()
transactions.append(t5)


t6 = Transaction(
    Joe,
    Tim.identity,
    6.0
)

t6.sign_transaction()
transactions.append(t6)


t7 = Transaction(
    Tom,
    Bob.identity,
    18.0
)

t7.sign_transaction()
transactions.append(t7)


t8 = Transaction(
    Tom,
    Joe.identity,
    1.0
)

t8.sign_transaction()
transactions.append(t8)


t9 = Transaction(
    Tom, 
    Tim.identity,
    5.0
)

t9.sign_transaction()
transactions.append(t9)


t10 = Transaction(
    Tim,
    Bob.identity,
    3.0
)

t10.sign_transaction()
transactions.append(t10)

for transaction in transactions:
    display_transaction (transaction)
    print('-----------------')
def dump_blockchain (self):
    print("Number of blocks in the chain: " + str(len (self)))
    for x in range (len(TPCoins)):
        block_temp = TPCoins[x]
        print ("block #" + str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction (transaction)
            print("--------------")
        print ("======================================")

TPCoins.append (block0)

dump_blockchain(TPCoins)
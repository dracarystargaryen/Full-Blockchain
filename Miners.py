def mine(message, difficulty = 1):
    assert difficulty >= 1
    prefix = '1' * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print ("after " + str(i) + " iterations found nonce: "+ digest)
        return digest 

block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    block.verified_transactions.append (temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash
block_Nonce = mine (block, 2)
digest = hash (block)
TPCoins.append (block)
last_block_hash = digest

block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    block.verified_transactions.append (temp_transaction)
    last_transaction_index += 1

block.previous_block_hash = last_block_hash
block_Nonce = mine(block, 2)
digest = hash (block)

TPCoins.append (block)
last_block_hash = digest

dump_blockchains(TPCoins)
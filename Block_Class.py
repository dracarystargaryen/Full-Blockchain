class Block:
    def _init_(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""
        
last_block_hash = ""

Bob = Client()

t0 = Transaction(
    "Genesis",
    Bob.identify,
    500.0
)

block0 = Block()

block0.previous_block_hash = None
Nonce = None

block0.verified_transactions.append(t0)

digest = hash (block0)
last_block_hash = digest
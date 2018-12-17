import datetime
import hashlib

class Block:
	blockNum = 0
	data = None
	nextBlock = None
	hash = None
	nonce = 0
	previous_hash = 0x0
	timestamp = datetime.datetime.now()
	
	def __init__(self, data):
		self.data = data

	def hash(self):
		h = hashlib.sha256()
		h.update(
			str(self.nonce).encode('utf-8') +
			str(self.data).encode('utf-8') +
			str(self.previous_hash).encode('utf-8') +
			str(self.timestamp).encode('utf-8') +
			str(self.blockNum).encode('utf-8')
		)
		return h.hexdigest()

	def __str__(self):
		return "Block hash: " + str(self.hash()) + "\nBlock Num: " +  \
str(self.blockNum)+ "\nBlock Data: " + str(self.data) + "\nHashes " + str(self.nonce) + "\n---------------------"

class Blockchain:
	difficulty = 20
	maxNonce = 2**32
	target = 2 ** (256-difficulty)
	
	block = Block("Genesis")
	dummy = head = block
	
	def add(self, block):
		block.previous_hash = self.block.hash()
		block.blockNum = self.block.blockNum + 1
		
		self.block.nextBlock = block
		self.block =  self.block.nextBlock

	def mine(self, block):
		for n in range(self.maxNonce):
			if int(block.hash(), 16) <= self.target:
				self.add(block)
				print(block)
				break
			else:
				block.nonce += 1


blockchain = Blockchain()
for n in range(10):
	blockchain.mine(Block("My block " + str(n+1)))

while blockchain.head != None:
	print(blockchain.head)
	blockchain.head = blockchain.head.nextBlock


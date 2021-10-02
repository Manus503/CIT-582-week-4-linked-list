import hashlib
class Block:
    def __init__(self, index, timestamp, content, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.content = content
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
   
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(str(self.index).encode('utf-8') + 
                 str(self.timestamp).encode('utf-8') + 
                 str(self.content).encode('utf-8') + 
                 str(self.previous_hash).encode('utf-8'))
      return sha.hexdigest()
      
M4BlockChain = []

from datetime import datetime
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")
    
M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
def next_block(last_block):
    new_block = last_block(index, timestamp, content, previous_hash)
    if last_block.index == None:
        last_block.index = new_block
    else:
        curr=self.index
        while (curr.previous_hash):
            curr=curr.previous_hash
        curr.previous_hash=new_block
    pass
    
# append 5 blocks to the blockchain
def app_five(block_list):
    block_list = block_list(index, timestamp, content, previous_hash)
    if new_block.index == None:
        new_block.index = new_block
    else:
        curr=self.index
        while (curr.previous_hash):
            curr=curr.previous_hash
        curr.previous_hash=new_block
    pass

class DataBlocksManager:
    def __init__(self):
        self.blocks = {}

    def add_block(self, block_id, data):
        self.blocks[block_id] = data

    def get_block(self, block_id):
        return self.blocks.get(block_id)

from block import Block

#declaration of the diffrent positions of the Blocks
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0:[(0,2), (1,0), (1,1), (1,2)],
            1:[(0,1), (1,1),(2,1), (2,2)],
            2:[(1,0), (1,1), (1,2), (2,0)],
            3:[(0,0), (0,1), (1,1), (2,1)]
        }
        self.move(0,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0:[(0,0), (1,0),(1,1), (1,2)],
            1:[(0,1), (0,2), (1,1), (2,1)],
            2:[(1,0), (1,1), (1,2), (2,2)],
            3:[(0,1), (1,1), (2,0), (2,1)]
        }
        self.move(0,3)

class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0:[(1,0), (1,1), (1,2), (1,3)],
            1:[(0,2), (1,2), (2,2), (3,2)],
            2:[(2,0), (2,1), (2,2), (2,3)],
            3:[(0,1), (1,1), (2,1), (3,1)]
        }
        self.move(-1,3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0:[(0,0), (0,1), (1,0), (1,1)],
            1:[(0,0), (0,1), (1,0), (1,1)],
            2:[(0,0), (0,1), (1,0), (1,1)],
            3:[(0,0), (0,1), (1,0), (1,1)]
        }
        self.move(0,4)

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0:[(0,1), (0,2), (1,0), (1,1)],
            1:[(0,1), (1,1), (1,2), (2,2)],
            2:[(1,1), (1,2), (2,0), (2,1)],
            3:[(0,0), (1,0), (1,1), (2,1)]
        }
        self.move(0,3)

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0:[(0,1), (1,0), (1,1), (1,2)],
            1:[(0,1), (1,1), (1,2), (2,1)],
            2:[(1,0), (1,1), (1,2), (2,1)],
            3:[(0,1), (1,0), (1,1), (2,1)]
        }
        self.move(0,3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0:[(0,0), (0,1), (1,1), (1,2)],
            1:[(0,2), (1,1), (1,2), (2,1)],
            2:[(1,0), (1,1), (2,1), (2,2)],
            3:[(0,1), (1,0), (1,1), (2,0)]
        }
        self.move(0,3)
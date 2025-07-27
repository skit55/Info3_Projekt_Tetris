class Colors: 
    dark_grey = (26, 31, 40)
    blue = (47, 23, 240)
    red = (255, 16, 16)
    orange = (126, 126, 20)
    yellow = (220, 220, 3)
    purple = (166, 2, 247)
    cyan = (21, 204, 209)
    pink = (255, 190, 201)
    white = (255,255,255)
    dark_green = (44, 127, 44)
    brown = (133, 101, 62)
    black = (0,0,0)

    @classmethod
    def get_cell_colors(cls):
            #index = color ID
            return[cls.dark_grey, cls.blue, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.pink]

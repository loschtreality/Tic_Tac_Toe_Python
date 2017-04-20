class Player(object):
    """
    Player class containing methods to place pieces on board and ask for input
    """
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def place_piece(self):
        resp = input("select your coordinates: ")
        return list(map(lambda num: int(num), resp.split(",")))

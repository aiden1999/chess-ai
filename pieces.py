# piece class
# current position
# colour
# ID

# subclasses
# moveset

class Piece:
    def __init__(self, position, colour, id):
        self.position = position
        self.colour = colour
        self.id = id


class Pawm(Piece):
    def __init__(self, position, colour, id, moveset):
        super().__init__(position, colour, id)
        self.moveset = moveset

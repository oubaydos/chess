
"""
working on Knight ;
done with : legal moves, move method, eat method for knight
-----
next : pawn
-----
07/03/2021 : 00:00 to 01;16
worked on pawn : problem on eat function
-----
15/03/2021 :
working on pawn,
editing knight to be initialized with __init__
"""
filled_squares = [
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False],
                     [False, False, False, False, False, False, False, False]
                  ]


whitePoints=0
blackPoints=0
def isLegal( a, b):
    return (a <= 'h' and a >= 'a' and b <= 8 and b >= 1 and not filled_squares[0][0])

class knight():
    def __init__(self):
        self.importance = 3
        self.initial_position = ('b', 1)#hna rah hadi ghatbdl 3la kol knignt
        self.position = self.initial_position
        self.White = True
        self.eaten = False


    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) + 1), b + 2), (chr(ord(a) + 2), b + 1), (chr(ord(a) - 1), b + 2),
                         (chr(ord(a) - 2), b + 1),
                         (chr(ord(a) - 2), b - 1), (chr(ord(a) - 1), b - 2), (chr(ord(a) + 1), b - 2),
                         (chr(ord(a) + 2), b - 1)]
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, a, b):
        L=self.legal_moves()
        if (a, b) in L and not filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] :
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
            return True
        print("this move is not legal")
        return False
    def eat(self,eatenPiece,a,b):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) + 1), b + 2), (chr(ord(a) + 2), b + 1), (chr(ord(a) - 1), b + 2),
                         (chr(ord(a) - 2), b + 1),
                         (chr(ord(a) - 2), b - 1), (chr(ord(a) - 1), b - 2), (chr(ord(a) + 1), b - 2),
                         (chr(ord(a) + 2), b - 1)]
        global whitePoints, blackPoints
        if (a,b) in possibilities and filled_squares[ord(a)-97][b-1]:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            eatenPiece.eaten = True
            if self.White :
                 whitePoints += eatenPiece.importance
            else :
                blackPoints += eatenPiece.importance
            return True
        return False
class leftWhiteKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('b', 1)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
class rightWhiteKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('g', 1)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
class leftBlackKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('b', 8)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
        self.White = False

class rightBlackKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('g', 8)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
        self.White = False
class Pawn:
    def __init__(self,arg1):
        self.importance = 1
        self.first = True
        self.passant = False
        self.eaten = False
        self.White = True
        self.increment = 1 #how much a pawn can move (-1 for black pawns)
        self.initial_position = (arg1, 2)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, b + self.increment)]
        if self.first :
            possibilities.append((a,b + 2 * self.increment))
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, a, b):
        L = self.legal_moves()
        if (a, b) in L:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True
            return True
        return False
    def eat(self,eatenPiece,a,b):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a)-1),b+ self.increment),(chr(ord(a)+1),b+ self.increment)]
        global whitePoints, blackPoints
        if (a,b) in possibilities and filled_squares[ord(a)-97][b-1] :
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            eatenPiece.eaten = True
            if self.White :
                 whitePoints += eatenPiece.importance
            else :
                blackPoints += eatenPiece.importance
class blackPawn(Pawn):
    increment = -1
    def __init__(self, arg1):
        self.initial_position=(arg1,7)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = True


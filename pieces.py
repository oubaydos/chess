
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

pawn :
    move is good
    need to work on upgrading

filled square : may change from bool to having False + pieces

i didnt know how to seperate static attributes from super/sub classes
so i made a class for the white pawn and a class for the black one
and repeated too much code !!
-----
i think everything is okay:
    i need Passant method for pawns
    then move to rook or bishop

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
    return 'h' >= a >= 'a' and 8 >= b >= 1 and filled_squares[ord(a) - 97][b - 1] is False

class knight():
    def __init__(self):

        self.initial_position = ('b', 1)#hna rah hadi ghatbdl 3la kol knignt
        self.position = self.initial_position
        self.White = True
        self.eaten = False

    """static variables : importance and type"""
    importance = 3
    type = "WK"


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
        if (a, b) in L and filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] is False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
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
        if (a,b) in possibilities and filled_squares[ord(a)-97][b-1] is not False:
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
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
class rightWhiteKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('g', 1)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
class leftBlackKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('b', 8)
        self.position = self.initial_position
        self.type = "BK"
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
        self.White = False

class rightBlackKnight(knight):
    def __init__(self):
        knight.__init__(self)
        self.initial_position = ('g', 8)
        self.position = self.initial_position
        self.type = "BK"
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
        self.White = False
class Pawn:
    def __init__(self,arg1):#whiteOrBlack = True if white else false
        self.first = True
        self.passant = False
        self.eaten = False
        self.White = True
        self.increment = 1 #how much a pawn can move (-1 for black pawns)
        self.initial_position = (arg1, 2)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    #static
    importance = 1
    type = "WP"


    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, b + self.increment)]
        if self.first:
            possibilities.append((a,b + 2 * self.increment))
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, b):
        L = self.legal_moves()
        a = self.position[0]
        if self.first:
            self.first = False
        if (a, b) in L:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        return False
    def eat(self,eatenPiece,e,f):
        a = self.position[0]
        b = self.position[1]
        if a!='a' and a!='h':
            possibilities = [(chr(ord(a)-1),b+ self.increment),(chr(ord(a)+1),b+ self.increment)]
        elif a == 'a':
            possibilities = [(chr(ord(a) + 1), b + self.increment)]
        else :
            possibilities = [(chr(ord(a) - 1), b + self.increment)]

        if (e,f) in possibilities and filled_squares[ord(e)-97][f-1] is not False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            filled_squares[ord(e)-97][f-1] = self.type
            self.position = (e, f)
            eatenPiece.eaten = True
            global whitePoints, blackPoints
            if self.White == True:
                 whitePoints = eatenPiece.importance
            else :
                blackPoints += eatenPiece.importance

class blackPawn:
    def __init__(self,arg1):#whiteOrBlack = True if white else false
        self.first = True
        self.passant = False
        self.eaten = False
        self.White = False
        self.increment = -1 #how much a pawn can move (-1 for black pawns)
        self.initial_position = (arg1, 7)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    #static
    importance = 1
    type = "BP"


    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, b + self.increment)]
        if self.first:
            possibilities.append((a,b + 2 * self.increment))
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, b):
        L = self.legal_moves()
        a = self.position[0]
        if self.first:
            self.first = False
        if (a, b) in L:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        return False
    def eat(self,eatenPiece,e,f):
        a = self.position[0]
        b = self.position[1]
        if a!='a' and a!='h':
            possibilities = [(chr(ord(a)-1),b+ self.increment),(chr(ord(a)+1),b+ self.increment)]
        elif a == 'a':
            possibilities = [(chr(ord(a) + 1), b + self.increment)]
        else :
            possibilities = [(chr(ord(a) - 1), b + self.increment)]

        if (e,f) in possibilities and filled_squares[ord(e)-97][f-1] is not False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            filled_squares[ord(e)-97][f-1] = self.type
            self.position = (e, f)
            eatenPiece.eaten = True
            global whitePoints, blackPoints
            if self.White == True:
                 whitePoints = eatenPiece.importance
            else :
                blackPoints += eatenPiece.importance

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
----
21/03/2021 :
    done with Passant method for Pawns
-
07/04/2021 :
so i figured out that i forgot to handle the condition that bishops/rooks ... cannot jump
and i created a function : wayisclear ; but i found many errors so i m leaving it later
however now 3 bishops are defined / wayisclear
--->
next time :
    wayisclear for bishops
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

whitePoints = 0
blackPoints = 0


def isLegal(a, b):
    return 'h' >= a >= 'a' and 8 >= b >= 1 and filled_squares[ord(a) - 97][b - 1] is False


class knight():
    def __init__(self):

        self.initial_position = ('b', 1)  # hna rah hadi ghatbdl 3la kol knignt
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

    def move(self, a : str, b : int):
        
        L = self.legal_moves()
        if (a, b) in L and filled_squares[ord(a) - 97][b - 1] is False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        print("this move is not legal")
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        if (eatenPiece.type[0] == self.type[0]):
            print("same time : error")
            return False
        possibilities = [(chr(ord(a) + 1), b + 2), (chr(ord(a) + 2), b + 1),
                         (chr(ord(a) - 1), b + 2), (chr(ord(a) - 2), b + 1),
                         (chr(ord(a) - 2), b - 1), (chr(ord(a) - 1), b - 2),
                         (chr(ord(a) + 1), b - 2), (chr(ord(a) + 2), b - 1)]
        global whitePoints, blackPoints
        if (e, f) in possibilities and filled_squares[ord(a) - 97][b - 1] is not False:
            filled_squares[ord(a) - 97][b - 1] = False
            self.position = (e, f)
            eatenPiece.eaten = True
            if self.White:
                whitePoints += eatenPiece.importance
            else:
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
    def __init__(self, arg1):  # whiteOrBlack = True if white else false
        self.first = True
        self.passant = 0
        self.eaten = False
        self.increment = 1  # how much a pawn can move (-1 for black pawns)
        self.initial_position = (arg1, 2)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    # static
    importance = 1
    type = "WP"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, b + self.increment)]
        if self.first and filled_squares[ord(a) - 97][b] is False:
            possibilities.append((a, b + 2 * self.increment))
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, b:int):
        
        L = self.legal_moves()
        a = self.position[0]

        if (a, b) in L:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            self.first = False
            self.passant += 1
            return True
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        if eatenPiece.type[0] == self.type[0]:
            print("same time : error")
            return False
        if a != 'a' and a != 'h':
            possibilities = [(chr(ord(a) - 1), b + self.increment), (chr(ord(a) + 1), b + self.increment)]
        elif a == 'a':
            possibilities = [(chr(ord(a) + 1), b + self.increment)]
        else:
            possibilities = [(chr(ord(a) - 1), b + self.increment)]

        if (e, f) in possibilities and filled_squares[ord(e) - 97][f - 1] is not False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            filled_squares[ord(e) - 97][f - 1] = self.type
            self.first = False
            self.position = (e, f)
            self.passant += 1
            eatenPiece.eaten = True
            global whitePoints
            whitePoints = eatenPiece.importance

    def Passant(self, eatenPiece):  # 21/03/2021
        if not isinstance(eatenPiece, blackPawn):
            print("Passant not possible : not blackPawn")
            return
        if eatenPiece.passant != 1:
            print("not the first move")
            return
        if self.position[1] != 5 or eatenPiece.position[1] != 5:
            print("error : one of the pieces is not on the fifth line")
            return
        openentSquare = eatenPiece.position
        if openentSquare[0] == chr(ord(self.position[0]) + 1) or openentSquare[0] == chr(ord(self.position[0]) - 1):
            if not filled_squares[ord(openentSquare[0]) - 97][5]:  # 2nd arg is the square bellow eatenPiece
                filled_squares[ord(self.position[0]) - 97][4] = False
                filled_squares[ord(openentSquare[0]) - 97][4] = False
                self.position = (openentSquare[0], 6)
                filled_squares[ord(openentSquare[0]) - 97][5] = self.type
                eatenPiece.passant += 1
                eatenPiece.first = False
                global whitePoints
                whitePoints = eatenPiece.importance


class blackPawn:
    def __init__(self, arg1):  # whiteOrBlack = True if white else false
        self.first = True
        self.passant = 0
        self.eaten = False
        self.increment = -1  # how much a pawn can move (-1 for black pawns)
        self.initial_position = (arg1, 7)
        self.position = self.initial_position
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    # static
    importance = 1
    type = "BP"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, b + self.increment)]
        if self.first and filled_squares[ord(a) - 97][b - 2] is False:
            possibilities.append((a, b + 2 * self.increment))
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def move(self, b:int):
        
        L = self.legal_moves()
        a = self.position[0]

        if (a, b) in L:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            self.first = False
            self.passant += 1
            return True
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        if eatenPiece.type[0] == self.type[0]:
            print("same time : error")
            return False
        if a != 'a' and a != 'h':
            possibilities = [(chr(ord(a) - 1), b + self.increment), (chr(ord(a) + 1), b + self.increment)]
        elif a == 'a':
            possibilities = [(chr(ord(a) + 1), b + self.increment)]
        else:
            possibilities = [(chr(ord(a) - 1), b + self.increment)]

        if (e, f) in possibilities and filled_squares[ord(e) - 97][f - 1] is not False:
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.first = False
            filled_squares[ord(e) - 97][f - 1] = self.type
            self.position = (e, f)
            eatenPiece.eaten = True
            self.passant += 1
            global blackPoints
            blackPoints += eatenPiece.importance

    def Passant(self, eatenPiece):  # 21/03/2021
        if not isinstance(eatenPiece, Pawn):
            print("Passant not possible : not WhitePawn")
            return
        if eatenPiece.passant != 1:
            print("not the first move")
            return
        if self.position[1] != 4 or eatenPiece.position[1] != 4:
            print("error : one of the pieces is not on the fourth line")
            return
        openentSquare = eatenPiece.position
        if openentSquare[0] == chr(ord(self.position[0]) + 1) or openentSquare[0] == chr(ord(self.position[0]) - 1):
            if not filled_squares[ord(openentSquare[0]) - 97][2]:  # 2nd arg is the square bellow eatenPiece
                filled_squares[ord(self.position[0]) - 97][3] = False
                filled_squares[ord(openentSquare[0]) - 97][3] = False
                self.position = (openentSquare[0], 6)
                filled_squares[ord(openentSquare[0]) - 97][2] = self.type
                eatenPiece.passant += 1
                eatenPiece.first = False
                global blackPoints
                blackPoints = eatenPiece.importance


class Rook:
    def __init__(self):
        self.initial_position = ('a', 1)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    """static variables : importance and type"""
    importance = 5
    type = "WR"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, x) for x in range(1, 9)]
        possibilities += [(chr(ord('a') + i), b) for i in range(1, 9)]
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def wayisclear(self, a, b, eat=False):
        
        if eat:
            if a == self.position[0]:
                for i in range(min(self.position[1] + 1, b + 1), max(b, self.position[1] + 1)):
                    if i != b and filled_squares[ord(a) - 97][i - 1] is not False:
                        print("way not clear")
                        return False
            if b == self.position[1]:
                for i in range(min(ord(self.position[0]), ord(a) + 1), max(ord(a), ord(self.position[0]))):
                    if i != ord(a) and filled_squares[i - 97][b - 1] is not False:
                        print("way not clear")
                        return False
            return True
        else:
            if a == self.position[0]:
                for i in range(min(self.position[1] + 1, b), max(b + 1, self.position[1] + 1)):
                    if filled_squares[ord(a) - 97][i - 1] is not False:
                        print("way not clear")
                        return False
            if b == self.position[1]:
                for i in range(min(ord(self.position[0]) + 1, ord(a)), max(ord(a) + 1, ord(self.position[0]) + 1)):
                    if filled_squares[i - 97][b - 1] is not False:
                        print("way not clear")
                        return False
            return True

    def move(self, a:str, b:int):
        
        L = self.legal_moves()
        if (a, b) in L and filled_squares[ord(a) - 97][b - 1] is False:
            if not self.wayisclear(a, b):
                return False
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        print("this move is not legal")
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        if (eatenPiece.type[0] == self.type[0]):
            print("same time : error")
            return False
        if not self.wayisclear(e, f, True):
            return False
        possibilities = [(a, x) for x in range(1, 9)]
        possibilities += [(chr(ord('a') + i), b) for i in range(1, 9)]
        global whitePoints, blackPoints
        if (e, f) in possibilities and filled_squares[ord(a) - 97][b - 1] is not False and (e, f) != (a, b):
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (e, f)
            filled_squares[ord(e) - 97][f - 1] = self.type
            eatenPiece.eaten = True
            whitePoints += eatenPiece.importance
            return True
        return False


class lastWhiteRook(Rook):
    def __init__(self):
        self.initial_position = ('h', 1)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.White = True
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type


class BlackfirstRook:
    def __init__(self):
        self.initial_position = ('a', 8)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    """static variables : importance and type"""
    importance = 5
    type = "BR"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(a, x) for x in range(1, 9)]
        possibilities += [(chr(ord('a') + i), b) for i in range(1, 9)]
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def wayisclear(self, a, b, eat=False):
        
        if eat:
            if a == self.position[0]:
                for i in range(min(self.position[1] + 1, b + 1), max(b, self.position[1] + 1)):
                    if i != b and filled_squares[ord(a) - 97][i - 1] is not False:
                        print("way not clear")
                        return False
            if b == self.position[1]:
                for i in range(min(ord(self.position[0]), ord(a) + 1), max(ord(a), ord(self.position[0]))):
                    if i != ord(a) and filled_squares[i - 97][b - 1] is not False:
                        print("way not clear")
                        return False
            return True
        else:
            if a == self.position[0]:
                for i in range(min(self.position[1] + 1, b), max(b + 1, self.position[1] + 1)):
                    if filled_squares[ord(a) - 97][i - 1] is not False:
                        print("way not clear")
                        return False
            if b == self.position[1]:
                for i in range(min(ord(self.position[0]) + 1, ord(a)), max(ord(a) + 1, ord(self.position[0]) + 1)):
                    if filled_squares[i - 97][b - 1] is not False:
                        print("way not clear")
                        return False
            return True

    def move(self, a:str, b:int):
        
        L = self.legal_moves()
        if (a, b) in L and filled_squares[ord(self.position[0]) - 97][
            self.position[1] - 1] is False and self.wayisclear(a, b):
            if not self.wayisclear(a, b):
                return False
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        print("this move is not legal")
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        if (eatenPiece.type[0] == self.type[0]) or not self.wayisclear(e, f, True):
            print("same type || way not clear : error")
            return False
        if not self.wayisclear(a, b, True):
            return False
        possibilities = [(a, x) for x in range(1, 9)]
        possibilities += [(chr(ord('a') + i), b) for i in range(1, 9)]
        global whitePoints, blackPoints
        if (e, f) in possibilities and filled_squares[ord(a) - 97][b - 1] is not False and (e, f) != (a, b):
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (e, f)
            eatenPiece.eaten = True
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            blackPoints += eatenPiece.importance
            return True
        return False


class BlackLastRook(BlackfirstRook):
    def __init__(self):
        self.initial_position = ('h', 8)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type


class whitefirstBishop:
    def __init__(self):
        self.initial_position = ('c', 1)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    """static variables : importance and type"""
    importance = 3
    type = "WFB"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) - x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) - x), b - x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b - x) for x in range(1, 9)]
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L
    def wayisclear(self,a,b,eat = False):#####doing wayisclear function hh
        
        if eat:
            return self.wayisclear(self,chr(ord(a)+1),b+1)
        if b > self.position[1]:
            L = [j for j in range(min(ord(self.position[0])+1,ord(a)),max(ord(self.position[0]),ord(a)+1))]
            j = 0
            for i in range(self.position[1]+1,b+1):
                if filled_squares[L[j]-97][i] is not False:
                    return False
                j+=1
            return True
        else:
            L = [j for j in range(min(ord(self.position[0]) + 1, ord(a)), max(ord(self.position[0]), ord(a) + 1))]
            j = 0
            for i in range( b + 1,self.position[1] ):
                if filled_squares[L[j] - 97][i] is not False:
                    return False
                j += 1
            return True
                    

    def move(self, a:str, b:int):
        
        L = self.legal_moves()
        if (a, b) in L and filled_squares[ord(a) - 97][b - 1] is False and self.wayisclear(a,b):
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        print("this move is not legal")
        return False

    def eat(self, eatenPiece, e:str, f:int):
        
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) - x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) - x), b - x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b - x) for x in range(1, 9)]
        global whitePoints
        if (e, f) in possibilities and filled_squares[ord(e) - 97][f - 1] is not False and (e, f) != (a, b) and self.wayisclear(e,f,True):
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (e, f)
            filled_squares[ord(e) - 97][f - 1] = self.type
            eatenPiece.eaten = True
            whitePoints += eatenPiece.importance
            return True
        return False


class whiteSecondBishop(whitefirstBishop):
    def __init__(self):
        self.initial_position = ('f', 1)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    """static variables : importance and type"""
    importance = 3
    type = "WSB"


class blackfirstBishop:
    def __init__(self):
        self.initial_position = ('c', 8)  # hna rah hadi ghatbdl 3la kol rook
        self.position = self.initial_position
        self.eaten = False
        filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type

    """static variables : importance and type"""
    importance = 3
    type = "BFB"

    def legal_moves(self):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) - x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) - x), b - x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b - x) for x in range(1, 9)]
        L = []
        for x in possibilities:
            if isLegal(x[0], x[1]):
                L.append((x[0], x[1]))
        return L

    def wayisclear(self, a, b, eat=False):  #####doing wayisclear function hh
        
        if eat:
            return self.wayisclear(self, chr(ord(a) + 1), b + 1)
        if b > self.position[1]:
            L = [j for j in range(min(ord(self.position[0]) + 1, ord(a)), max(ord(self.position[0]), ord(a) + 1))]
            j = 0
            for i in range(self.position[1] + 1, b + 1):
                if filled_squares[L[j] - 97][i] is not False:
                    return False
                j += 1
            return True
        else:
            L = [j for j in range(min(ord(self.position[0]) + 1, ord(a)), max(ord(self.position[0]), ord(a) + 1))]
            j = 0
            for i in range(b + 1, self.position[1]):
                if filled_squares[L[j] - 97][i] is not False:
                    return False
                j += 1
            return True

    def move(self, a:str, b:int):
        
        L = self.legal_moves()
        if (a, b) in L and filled_squares[ord(a) - 97][b - 1] is False and self.wayisclear(a,b):
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
            self.position = (a, b)
            filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = self.type
            return True
        print("this move is not legal")
        return False

    def eat(self, eatenPiece, e:str, f:int):
        a = self.position[0]
        b = self.position[1]
        possibilities = [(chr(ord(a) - x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b + x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) - x), b - x) for x in range(1, 9)]
        possibilities += [(chr(ord(a) + x), b - x) for x in range(1, 9)]
        global blackPoints
        if (e, f) in possibilities :
            if filled_squares[ord(e) - 97][f - 1] is not False and self.wayisclear(e,f,True):
                if (e, f) != (a, b):
                    filled_squares[ord(self.position[0]) - 97][self.position[1] - 1] = False
                    self.position = (e, f)
                    filled_squares[ord(e) - 97][f - 1] = self.type
                    eatenPiece.eaten = True
                    blackPoints += eatenPiece.importance
                    return True
        return False


from pieces import *
import pieces

"""
    we need to first have
    ***   a class of each piece {
                * how they move
                * how they eat hh ( pawn )
    }
    ***   ( with a super class defining the pieces' shared methods )
    ***   drawing the board and the pieces
    ***   main function
"""
def f(): # just print the filled squares
    for i in range(8):
        print(filled_squares[i])
    print()
def printp():
    print("white : ", pieces.whitePoints, "\n black : ", pieces.blackPoints)
def main():
    #test
    t = leftWhiteKnight()
    p = leftBlackKnight()
    c = rightWhiteKnight()
    d = rightBlackKnight()
    r1 = Rook()
    r2 = lastWhiteRook()
    r3 = BlackfirstRook()
    r4 = BlackLastRook()
    b1 = whitefirstBishop()
    b2 = whiteSecondBishop()
    b3 = blackfirstBishop()
    L=[None]*8
    L1 =[None]*8
    """for i in range(7):
        L[i] = Pawn(chr(i+97))
        L1[i] = blackPawn(chr(i+97))"""
    b3.move('e',6)
    b3.move('a',2)
    f()
    b3.eat(t,'b',1)
    paw = Pawn('c')
    pw = Pawn('d')
    pw.move(3)
    f()
    b3.eat(pw,'d',3)
    printp()
if __name__ == '__main__':
    main()


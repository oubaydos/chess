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
def printf(): # just print the filled squares
    for i in range(8):
        print(filled_squares[i])
    print()
def main():
    #test
    t = leftWhiteKnight()
    p = leftBlackKnight()
    c = rightWhiteKnight()
    d = rightBlackKnight()

    L=[None]*8
    L1 =[None]*8
    for i in range(8):
        L[i] = Pawn(chr(i+97))
        L1[i] = blackPawn(chr(i+97))

    printf()
    for i in range(4,6):
        L[0].move(i)
        printf()
    L1[1].move(5)
    printf()
    L[0].Passant(L1[1])
    printf()

    for i in range(5, 3, -1):
        L1[3].move(i)
        printf()

    L[4].move(4)
    L[2].move(4)
    printf()
    L1[3].Passant(L[4])
    printf()
    print(pieces.whitePoints, pieces.blackPoints)
if __name__ == '__main__':
    main()


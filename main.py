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
    for i in range(4,8):
        L[0].move(i)
        printf()

    printf()
    print(pieces.whitePoints,pieces.blackPoints)
if __name__ == '__main__':
    main()


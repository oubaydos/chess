from pieces import *
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

def main():
    #test
    t = leftWhiteKnight()
    p = leftBlackKnight()
    c = rightWhiteKnight()
    d = rightBlackKnight()
    L = [x for x in range(8)]
    J = L[:]
    for i in range(8):
        L[i] = blackPawn(chr(96+i))
        J[i] = Pawn(chr(96+i))



    print(d.legal_moves())

    for i in range(8):
        print(filled_squares[i])



if __name__ == '__main__':
    main()


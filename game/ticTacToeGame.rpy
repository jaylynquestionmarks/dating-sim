default turn = "x"
default board = [["", "", ""], ["", "", ""],["", "", ""]]

transform shrink:
    zoom 0.4

screen ticTacToeGame:
    
    imagemap:
        xpos 400
        ypos 200
        ground "board.png"
        at shrink

        if turn == "x":
            hotspot(300, 300, 300, 400) action Show("x0")
            hotspot(700, 300, 500, 400) action Show("x1")
            hotspot(1200, 300, 500, 400) action Show("x2")

            $ turn = "o"
        else:
            hotspot(300, 300, 300, 400) action Show("o0")
            hotspot(700, 300, 500, 400) action Show("o1")
            hotspot(1200, 300, 500, 400) action Show("o2")
            $ turn = "x"
        
    
    
    textbutton "Submit":
        action Return()

screen x0():
    if board[0][0] != "o":
        add "x0.png" at shrink xpos 400 ypos 200
        $ board[0][0] = "x"

screen x1():
    if board[0][1] != "o":
        add "x1.png" at shrink xpos 400 ypos 200
        $ board[0][1] = "x"


screen x2():
    if board[0][2] != "o":
        add "x2.png" at shrink xpos 400 ypos 200
        $ board[0][2] = "x"

screen x3():
    if board[1][0] != "o":
        add "x3.png" at shrink xpos 400 ypos 200
        $ board[1][0] = "x"

screen x4():
    if board[1][1] != "o":
        add "x4.png" at shrink xpos 400 ypos 200
        $ board[1][1] = "x"

screen x5():
    if board[1][2] != "o":
        add "x5.png" at shrink xpos 400 ypos 200
        $ board[1][2] = "x"

screen x6():
    if board[2][0] != "o":
        add "x6.png" at shrink xpos 400 ypos 200
        $ board[2][0] = "x"

screen x7():
    if board[2][1] != "o":
        add "x7.png" at shrink xpos 400 ypos 200
        $ board[2][1] = "x"

screen x8():
    if board[2][2] != "o":
        add "x8.png" at shrink xpos 400 ypos 200
        $ board[2][2] = "x"



screen o0():
    if board[0][0] != "x":
        add "o0.png" at shrink xpos 400 ypos 200
        $ board[0][0] = "o"

screen o1():
    if board[0][1] != "x":
        add "o1.png" at shrink xpos 400 ypos 200
        $ board[0][1] = "o"

screen o2():
    if board[0][2] != "x":
        add "o2.png" at shrink xpos 400 ypos 200
        $ board[0][2] = "o"

screen o3():
    if board[1][0] != "x":
        add "o3.png" at shrink xpos 400 ypos 200
        $ board[1][0] = "o"

screen o4():
    if board[1][1] != "x":
        add "o4.png" at shrink xpos 400 ypos 200
        $ board[1][1] = "o"

screen o5():
    if board[1][2] != "x":
        add "o5.png" at shrink xpos 400 ypos 200
        $ board[1][2] = "o"

screen o6():
    if board[2][0] != "x":
        add "o6.png" at shrink xpos 400 ypos 200
        $ board[2][0] = "o"

screen o7():
    if board[2][1] != "x":
        add "o7.png" at shrink xpos 400 ypos 200
        $ board[2][1] = "o"

screen o8():
    if board[2][2] != "x":
        add "o8.png" at shrink xpos 400 ypos 200
        $ board[2][2] = "o"
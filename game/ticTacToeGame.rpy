#flip tiles game?

default board = [["", "", ""], ["", "", ""], ["", "", ""]]
default turn = "o"
default win = False

transform shrink:
    zoom 0.4

screen ticTacToeGame:

    imagemap:
        xpos 400
        ypos 200
        ground "board.png"
        at shrink

        #if win != True:
        if turn == "x":
            hotspot(238, 176, 407, 552) action [Show("x0"), Hide("o0")]
            hotspot(684, 175, 512, 552) action [Show("x1"), Hide("o1")]
            hotspot(1227, 175, 500, 548) action [Show("x2"), Hide("o2")]
            hotspot(226, 757, 422, 498) action [Show("x3"), Hide("o3")]
            hotspot(679, 760, 523, 488) action [Show("x4"), Hide("o4")]
            hotspot(1230, 757, 499, 491) action [Show("x5"), Hide("o5")]
            hotspot(214, 1285, 434, 487) action [Show("x6"), Hide("o6")]
            hotspot(680, 1285, 523, 489) action [Show("x7"), Hide("o7")]
            hotspot(1233, 1278, 501, 490) action [Show("x8"), Hide("o8")]    

            $ turn = "o"
        
        else:
            hotspot(238, 176, 407, 552) action [Show("o0"), Hide("x0")]
            hotspot(684, 175, 512, 552) action [Show("o1"), Hide("x1")]
            hotspot(1227, 175, 500, 548) action [Show("o2"), Hide("x2")]
            hotspot(226, 757, 422, 498) action [Show("o3"), Hide("x3")]
            hotspot(679, 760, 523, 488) action [Show("o4"), Hide("x4")]
            hotspot(1230, 757, 499, 491) action [Show("o5"), Hide("x5")]
            hotspot(214, 1285, 434, 487) action [Show("o6"), Hide("x6")]
            hotspot(680, 1285, 523, 489) action [Show("o7"), Hide("x7")]
            hotspot(1233, 1278, 501, 490) action [Show("o8"), Hide("x8")]

            $ turn = "x"

        text "[board[0][0]] [board[0][1]] [board[0][2]]\n[board[1][0]] [board[1][1]] [board[1][2]]\n[board[2][0]] [board[2][1]] [board[2][2]]" ypos 100

        if (board[0][0] != "" and board[0][0] == board [1][1] and board[1][1] == board[2][2]) or (board[0][2] != "" and board[0][2] == board [1][1] and board[1][1] == board[2][0]) or (board[0][0] != "" and board[0][0] == board [0][1] and board[0][1] == board[0][2]) or (board[1][0] != "" and board[1][0] == board [1][1] and board[1][1] == board[1][2]) or (board[2][0] != "" and board[2][0] == board [2][1] and board[2][1] == board[2][2]) or (board[0][0] != "" and board[0][0] == board [1][0] and board[1][0] == board[2][0]) or (board[0][1] != "" and board[0][1] == board [1][1] and board[1][1] == board[2][1]) or (board[0][2] != "" and board[0][2] == board [1][2] and board[1][2] == board[2][2]):
            $ win = True
            if turn == "x":
                text "X WINS!"
            else:
                text "O WINS!"
        elif board[0][0] != "" and board[0][1] != "" and board[0][2] != "" and board[1][0] != "" and board[1][1] != "" and board[1][2] != "" and board[2][0] != "" and board[2][1] != "" and board[2][2] != "":
            text "TIE!"
        
    
    textbutton "Clear Board":
        xpos 420
        ypos 220
        action Hide("x0"), Hide("x1"), Hide("x2"), Hide("x3"), Hide("x4"), Hide("x5"), Hide("x6"), Hide("x7"), Hide("x8"), Hide("o0"), Hide("o1"), Hide("o2"), Hide("o3"), Hide("o4"), Hide("o5"), Hide("o6"), Hide("o7"), Hide("o8"), SetScreenVariable("win", True)

    textbutton "Submit":
        xpos 1050
        ypos 220
        action Hide("x0"), Hide("x1"), Hide("x2"), Hide("x3"), Hide("x4"), Hide("x5"), Hide("x6"), Hide("x7"), Hide("x8"), Hide("o0"), Hide("o1"), Hide("o2"), Hide("o3"), Hide("o4"), Hide("o5"), Hide("o6"), Hide("o7"), Hide("o8"), Return()

screen x0():
    add "x0.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x0"):
        $ board[0][0] = "x"

screen x1():
    add "x1.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x1"):
        $ board[0][1] = "x"

screen x2():
    add "x2.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x2"):
        $ board[0][2] = "x"

screen x3():
    add "x3.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x3"):
        $ board[1][0] = "x"

screen x4():
    add "x4.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x4"):
        text "x showing"
        $ board[1][1] = "x"

screen x5():
    add "x5.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x5"):
        $ board[1][2] = "x"

screen x6():
    add "x6.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x6"):
        $ board[2][0] = "x"

screen x7():
    add "x7.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x7"):
        $ board[2][1] = "x"

screen x8():
    add "x8.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("x8"):
        $ board[2][2] = "x"


screen o0():
    add "o0.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o0"):
        $ board[0][0] = "o"

screen o1():
    add "o1.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o1"):
        $ board[0][1] = "o"

screen o2():
    add "o2.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o2"):
        $ board[0][2] = "o"

screen o3():
    add "o3.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o3"):
        $ board[1][0] = "o"

screen o4():
    add "o4.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o4"):
        $ board[1][1] = "o"

screen o5():
    add "o5.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o5"):
        $ board[1][2] = "o"

screen o6():
    add "o6.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o6"):
        $ board[2][0] = "o"

screen o7():
    add "o7.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o7"):
        $ board[2][1] = "o"

screen o8():
    add "o8.png" at shrink xpos 400 ypos 200
    if renpy.get_screen("o8"):
        $ board[2][2] = "o"
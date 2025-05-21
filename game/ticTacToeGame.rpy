#flip tiles game?

transform shrink:
    zoom 0.4

screen ticTacToeGame:

    #board
    default i0 = ""
    default i1 = ""
    default i2 = ""
    default i3 = ""
    default i4 = ""
    default i5 = ""
    default i6 = ""
    default i7 = ""
    default i8 = ""

    default turn = "o"
    default win = False

    imagemap:
        xpos 400
        ypos 200
        ground "board.png"
        at shrink

        if (i0 != "" and i0 == i4 and i4 == i8) or (i2 != "" and i2 == i4 and i4 == i6) or (i0 != "" and i0 == i1 and i1 == i2) or (i3 != "" and i3 == i4 and i4 == i5) or (i6 != "" and i6 == i7 and i7 == i8) or (i0 != "" and i0 == i3 and i3 == i6) or (i1 != "" and i1 == i4 and i4 == i7) or (i2 != "" and i2 == i5 and i5 == i8):
            $ win = True
            if turn == "o":
                text "{size=*3}X WINS!{/size}" xpos 740 ypos 1800
            else:
                text "{size=*3}O WINS!{/size}" xpos 740 ypos 1800
        elif i0 != "" and i1 != "" and i2 != "" and i3 != "" and i4 != "" and i5 != "" and i6 != "" and i7 != "" and i8 != "":
            text "TIE!"

        #hotspots are areas on an image that you can click on to make the game do stuff
        #the $ indicates that the following line is a line of python
        if win == False:
            if turn == "x":
                hotspot(238, 176, 407, 552) action [Show("x0"), Hide("o0"), SetScreenVariable("i0", "x")]
                hotspot(684, 175, 512, 552) action [Show("x1"), Hide("o1"), SetScreenVariable("i1", "x")]
                hotspot(1227, 175, 500, 548) action [Show("x2"), Hide("o2"), SetScreenVariable("i2", "x")]
                hotspot(226, 757, 422, 498) action [Show("x3"), Hide("o3"), SetScreenVariable("i3", "x")]
                hotspot(679, 760, 523, 488) action [Show("x4"), Hide("o4"), SetScreenVariable("i4", "x")]
                hotspot(1230, 757, 499, 491) action [Show("x5"), Hide("o5"), SetScreenVariable("i5", "x")]
                hotspot(214, 1285, 434, 487) action [Show("x6"), Hide("o6"), SetScreenVariable("i6", "x")]
                hotspot(680, 1285, 523, 489) action [Show("x7"), Hide("o7"), SetScreenVariable("i7", "x")]
                hotspot(1233, 1278, 501, 490) action [Show("x8"), Hide("o8"), SetScreenVariable("i8", "x")] 

                $ turn = "o"
            
            else:
                hotspot(238, 176, 407, 552) action [Show("o0"), Hide("x0"), SetScreenVariable("i0", "o")]
                hotspot(684, 175, 512, 552) action [Show("o1"), Hide("x1"), SetScreenVariable("i1", "o")]
                hotspot(1227, 175, 500, 548) action [Show("o2"), Hide("x2"), SetScreenVariable("i2", "o")]
                hotspot(226, 757, 422, 498) action [Show("o3"), Hide("x3"), SetScreenVariable("i3", "o")]
                hotspot(679, 760, 523, 488) action [Show("o4"), Hide("x4"), SetScreenVariable("i4", "o")]
                hotspot(1230, 757, 499, 491) action [Show("o5"), Hide("x5"), SetScreenVariable("i5", "o")]
                hotspot(214, 1285, 434, 487) action [Show("o6"), Hide("x6"), SetScreenVariable("i6", "o")]
                hotspot(680, 1285, 523, 489) action [Show("o7"), Hide("x7"), SetScreenVariable("i7", "o")]
                hotspot(1233, 1278, 501, 490) action [Show("o8"), Hide("x8"), SetScreenVariable("i8", "o")]

                $ turn = "x"
    
        textbutton "{size=*2}Clear Board{/size}":
            xpos 50
            ypos 100
            action Hide("x0"), Hide("x1"), Hide("x2"), Hide("x3"), Hide("x4"), Hide("x5"), Hide("x6"), Hide("x7"), Hide("x8"), Hide("o0"), Hide("o1"), Hide("o2"), Hide("o3"), Hide("o4"), Hide("o5"), Hide("o6"), Hide("o7"), Hide("o8"), SetScreenVariable("i0", ""), SetScreenVariable("i1", ""), SetScreenVariable("i2", ""), SetScreenVariable("i3", ""), SetScreenVariable("i4", ""), SetScreenVariable("i5", ""), SetScreenVariable("i6", ""), SetScreenVariable("i7", ""), SetScreenVariable("i8", ""), SetScreenVariable("win", False)

        textbutton "{size=*2}Submit{/size}":
            xpos 1700
            ypos 100
            action Hide("x0"), Hide("x1"), Hide("x2"), Hide("x3"), Hide("x4"), Hide("x5"), Hide("x6"), Hide("x7"), Hide("x8"), Hide("o0"), Hide("o1"), Hide("o2"), Hide("o3"), Hide("o4"), Hide("o5"), Hide("o6"), Hide("o7"), Hide("o8"), Return()

screen x0():
    add "x0.png" at shrink xpos 400 ypos 200

screen x1():
    add "x1.png" at shrink xpos 400 ypos 200

screen x2():
    add "x2.png" at shrink xpos 400 ypos 200

screen x3():
    add "x3.png" at shrink xpos 400 ypos 200

screen x4():
    add "x4.png" at shrink xpos 400 ypos 200

screen x5():
    add "x5.png" at shrink xpos 400 ypos 200

screen x6():
    add "x6.png" at shrink xpos 400 ypos 200

screen x7():
    add "x7.png" at shrink xpos 400 ypos 200

screen x8():
    add "x8.png" at shrink xpos 400 ypos 200


screen o0():
    add "o0.png" at shrink xpos 400 ypos 200

screen o1():
    add "o1.png" at shrink xpos 400 ypos 200

screen o2():
    add "o2.png" at shrink xpos 400 ypos 200

screen o3():
    add "o3.png" at shrink xpos 400 ypos 200

screen o4():
    add "o4.png" at shrink xpos 400 ypos 200

screen o5():
    add "o5.png" at shrink xpos 400 ypos 200

screen o6():
    add "o6.png" at shrink xpos 400 ypos 200

screen o7():
    add "o7.png" at shrink xpos 400 ypos 200

screen o8():
    add "o8.png" at shrink xpos 400 ypos 200

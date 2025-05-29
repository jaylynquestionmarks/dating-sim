init python:
    import time

image bug:
    "bug.png"
    zoom 0.3

image bg_comp:
    "pc.jpg"
    xpos 20
    ypos 100
    zoom 0.2

default bug_score = 0
default bug_pos = -1
default bugging = False
default bug_coord = [(140, 200), (420, 200), (720, 200), (140, 420), (440, 420), (720, 420)]
default bug_start_time = 0
default wab_fixed = False

label start_whack_a_bug():
    $ bug_score = 0
    $ bugging = True
    call bug_countdown
    $ bug_start_time = time.time()
    show screen whack_a_bug
    jump bug_loop

label bug_countdown:
    show screen bug_countdown_screen("3")
    $ renpy.pause(1.0)
    show screen bug_countdown_screen("2")
    $ renpy.pause(1.0)
    show screen bug_countdown_screen("1")
    $ renpy.restart_interaction()
    $ renpy.pause(1.0)
    hide screen bug_countdown_screen
    return

label bug_loop:
    while bugging:
        $ bug_pos = renpy.random.randint(0, len(bug_coord) - 1)
        $ renpy.pause(0.6)
        $ bug_pos = -1
        if time.time() - bug_start_time >= 15:
            $ bugging = False
    jump bug_game_over

label bug_game_over:
    $ bugging = False
    "Game Over! Your score was [bug_score]. (click/space to continue)"
    if wab_fixed != True:
        call fixBug(ic, 5, "77", 'SetVariable("bug_score", bug_score + 1)')
        $ wab_fixed = True
        hide screen whack_a_bug
        return
    else:
        if bug_score < 4:
            sa "Don't sweat it, try again!"
        elif bug_score < 7:
            sa "Close, close! One more try!"
        elif bug_score < 10:
            sa "Awww, suuuuper close!! You got this!"
        else:
            ic "My god, you're good."
            hide screen whack_a_bug
            return
    

screen whack_a_bug():
    add "bg_comp"
    text "score: [bug_score]" xpos 20 ypos 20
    if int(15 - (time.time() - bug_start_time)) >= 0:
        text "Time Left: [int(15 - (time.time() - bug_start_time))]s" xpos 400 ypos 20
    if bug_pos != -1:
        imagebutton:
            idle "bugx"
            xpos bug_coord[bug_pos][0]
            ypos bug_coord[bug_pos][1]
            action [SetVariable("bug_score", bug_score + 1), SetVariable("bug_pos", -1), Return()]
    if bugging:
        timer 1.0 action SetVariable("bug_pos", -1) repeat False
    else:
        textbutton "Replay?":
            xpos 500
            ypos 650
            action Call("start_whack_a_bug")
        if wab_fixed:
            textbutton "Continue":
                xpos 500
                ypos 700
                action Return()

screen bug_countdown_screen(number):
    frame:
        align (0.5, 0.5)
        padding (50, 50)
        background "#0008"
        text number size 100 color "#fff"
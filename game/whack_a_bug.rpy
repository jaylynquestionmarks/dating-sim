init python:
    import time

image bug = "bug.png"
image bg_grass:
    "bg_grass.jpg"
    zoom 10

default bug_score = 0
default bug_pos = -1
default bugging = False
default bug_coord = [(100, 200), (300, 200), (500, 200), (100, 400), (300, 300), (500, 300)]
default bug_start_time = 0

label start_whack_a_bug:
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
        $ renpy.pause(0.3)
        if time.time() - bug_start_time >= 15:
            $ bugging = False
    jump bug_game_over

label bug_game_over:
    $ bugging = False
    "Game Over! Your score was [bug_score]."
    hide screen whack_a_bug
    return

screen whack_a_bug():
    add "bg_grass"
    text "score: [bug_score]" xpos 20 ypos 20
    text "Time Left: [int(15 - (time.time() - bug_start_time))]s" xpos 400 ypos 20
    if bug_pos != -1:
        imagebutton:
            idle "bug"
            xpos bug_coord[bug_pos][0]
            ypos bug_coord[bug_pos][1]
            focus_mask True
            action [SetVariable("bug_score", bug_score + 1), SetVariable("bug_pos", -1)]
    if bugging:
        timer 1.0 action SetVariable("bug_pos", -1) repeat False

screen bug_countdown_screen(number):
    frame:
        align (0.5, 0.5)
        padding (50, 50)
        background "#0008"
        text number size 100 color "#fff"
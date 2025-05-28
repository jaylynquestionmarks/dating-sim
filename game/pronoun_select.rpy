screen select():
    text "Choose your pronouns:":
        xalign 0.5
        yalign 0.4
    textbutton "she/her":
        xalign 0.25
        yalign 0.5
        action SetVariable("title", "Miss "), Return()
    textbutton "he/him":
        xalign 0.50
        yalign 0.5
        action SetVariable("title", "Mister "), Return()
    textbutton "they/them":
        xalign 0.75
        yalign 0.5
        action Return()
init python:
    def name_func(newstring):
        store.firstname = newstring

        
    def lastname_func(newstring):
        store.lastname = newstring

init:
    default firstname = " "
    default lastname = " "

screen fixBug():

    frame:
        #xysize (300,200)
        xpos 250
        ypos 100
        vbox:
            hbox:
                text "{size=+5}First Name"
                button:
                    xysize (250,25)
                    action NullAction()
                    #hover_sound ""
                    add Input(hover_color="#3399ff",size=28, color="#000", default=firstname, changed=name_func, length=10, button=renpy.get_widget("text_input_screen","input_1")) yalign 1.0
            hbox:
                text "{size=+5}Last Name"
                button:
                    xysize (250,25)
                    action NullAction()
                    #hover_sound ""
                    add Input(hover_color="#3399ff",size=28, color="#000", default=lastname, changed=lastname_func, length=10, button=renpy.get_widget("text_input_screen","input_2")) yalign 1.0

# input: list of line numbers that allow input, correct answer

'''

label fixBug:
    #probably put all the bgs and left/right chars and line numbers and answers in lists lol

    show text "{color=#f00}There's a bug in the game!{/color}" at truecenter
    while fixed != True:
        $ line = renpy.input("What line # is the bug in?")
        # affection w/ character increases if right
        
        if line == lineAns:
            player "There's the issue!"
            while userInput != codeAns:
                $ userInput = renpy.input("Enter Code (Java): ", multiline=True)
                if userInput != codeAns:
                    player "Wait, that's not right..."
                    #affection w/ character decreases if wrong + secretly increase affection w sahi 
            # affection w/ character increases if right
            $ fixed = True
        else:
            #affection w/ character decreases if wrong + secretly increase affection w sahi 
            player "Hold on-- that's not it."
    $ fixed = False
    hide text
    
    player "I did it!"
'''

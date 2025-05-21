label fixBug(loveInterest, amount, lineAns, codeAns):
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
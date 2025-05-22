default fixed = False
default userInput = ""

label fixBug(loveInterest, amount, lineAns, codeAns):
    #probably put all the bgs and left/right chars and line numbers and answers in lists lol
    
    while fixed != True:
        $ line = renpy.input("What line # is the bug in?")
        # affection w/ character increases if right
        
        if line == lineAns:
            p "There's the issue!"
            while userInput != codeAns:
                $ userInput = renpy.input("Enter Code: ", multiline=True)
                if userInput != codeAns:
                    p "Wait, that's not right..."
                    #affection w/ character decreases if wrong + secretly increase affection w sahi 
            # affection w/ character increases if right
            $ fixed = True
        else:
            #affection w/ character decreases if wrong + secretly increase affection w sahi 
            p "Hold on-- that's not it."
    $ fixed = False
    hide text
    
    p "I did it!"
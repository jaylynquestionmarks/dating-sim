default fixed = False
default userInput = ""

label fixBug(loveInterest, amount, lineAns, codeAns):
    #probably put all the bgs and left/right chars and line numbers and answers in lists lol
    
    while fixed != True:

        default line = "0"

        $ input_yalign = 1.0
        $ line = renpy.input("What line # is the bug in?")
        # affection w/ character increases if right
        
        if line == lineAns:
            p "There's the issue!"

            if wab_fixed != True:
                "Tip: If entering brackets, you will need to type the open brackets twice (as in [[ and ]) due to the limitations of RenPy"
            while userInput != codeAns:
                $ userInput = renpy.input("Enter Code: ", multiline=True)
                if userInput != codeAns:
                    p "Wait, that's not right..."
                    $ loveInterest.likability -= (amount / 3)
                    show screen likability_bar(loveInterest.likability, False)
                    pause
                    hide screen likability_bar
                    $ sahi.likability += (amount / 3) 
            $ loveInterest.likability += amount
            $ fixed = True
        else:
            $ loveInterest.likability -= (amount / 3)
            show screen likability_bar(loveInterest.likability, False)
            pause
            hide screen likability_bar
            $ sahi.likability += (amount / 3)
            p "Hold on-- that's not it."
    $ fixed = False
    hide text
    
    p "I did it!"
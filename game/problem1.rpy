#https://www.reddit.com/r/RenPy/comments/1d8hbdf/make_input_write_on_multiple_lines/

default note = ""

screen problem1:
    textbutton "Close Notebook" action Return()
    
    
    frame:
        xsize 500 
        ysize 500
        xalign 0.5
        yalign 0.5
        
        text "Code":
            xalign 0.5
            yalign 0.5
            yoffset -300


    frame:
        xsize 500 
        ysize 500
        xalign 0.5
        yalign 0.5
        
        has vbox
        hbox:
            box_wrap True
            text "{color=#000}Write new entry:{/color}"
            input:   
                default ""
                value VariableInputValue('note') #This updates the note variable (defined above) with what the player enters
                length 1000 #How many characters the player may enter
                color "#fff"
                multiline True
                copypaste True
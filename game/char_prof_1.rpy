screen docDesc:
    modal True
    zorder 20
    frame:
        background Frame("gui/overlay/confirm.png")
        # background Frame("gui/assets/blackscreen.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    textbutton "close":
        action [ToggleScreen("docDesc", fade)]

    #hotspot to control x button 

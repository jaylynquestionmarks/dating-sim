style description:
    font "fonts/Lexend-VariableFont_wght.ttf"
    size 25

screen docDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("docDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Dr. Peter Polymorphism":
        size 37
        xpos 900
        ypos 85
 
screen isaacDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("isaacDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Isaac Integer":
        size 37
        xpos 900
        ypos 85
    
    vbox:
        xysize (400, 300)
        xpos 900
        ypos 200
        spacing 10
        text "top":
            style "description"
            yalign 0.0
        
        text "top":
            yalign 1.0
    
    image "isaac_normal.png":
        zoom 0.37
        xcenter 0.33
        yalign 0.5
 
screen damianDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("damianDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Damian Double":
        size 37
        xpos 900
        ypos 85
        
    image "damian_normal.png":
        zoom 0.37
        xcenter 0.34
        yalign 0.5

screen sierraDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("sierraDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Sierra String":
        size 37
        xpos 900
        ypos 85
        
    image "sierra_normal.png":
        zoom 0.27
        xcenter 0.33
        yalign 0.5   

screen sahiDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("sahiDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "SDK Sahi":
        size 37
        xpos 900
        ypos 85
 
screen raphDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("raphDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Raphael Recursion":
        size 37
        xpos 900
        ypos 85
    
    vbox:
        xysize (400, 300)
        xpos 900
        ypos 200
        spacing 10
        text "top":
            style "description"
            yalign 0.0
        
        text "top":
            yalign 1.0
    
    image "isaac_normal.png":
        zoom 0.37
        xcenter 0.33
        yalign 0.5
 
screen icarDesc:
    modal True
    zorder 15
    frame:
        background Frame("gui/overlay/confirm.png")
    
    image "gui/assets/profile_back.png":
            xpos 350
            yalign 0.5
            zoom 1.25

    imagebutton:
        auto "gui/assets/close_button_%s.png"
        action [ToggleScreen("icarDesc")]
        xsize 50
        ysize 50
        xpos 1411
        ypos 80

    text "Icarus Inheritance":
        size 37
        xpos 900
        ypos 85
        
    image "icarus_normal.png":
        zoom 0.33
        xcenter 0.325
        yalign 0.5
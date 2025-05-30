style desc_text:
    font "fonts/Lexend-VariableFont_wght.ttf"

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
        style "desc_text"
        size 37
        xpos 900
        ypos 85

    vbox:
        style_prefix "desc"
        text "doctor/infirmary technician":
            xpos 940 ypos 170
            size 23
        text "6'2\"":
            xpos 980 ypos 192
            size 23
        text "29":
            xpos 1090 ypos 164
            size 23
        text "> favorite meal: lunch (big sandwich)\n> got into medicine after watching House (2004)":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    
    use likability_bar(doc.likability)
    image "doc_normal.png":
        zoom 0.35
        xcenter 0.33 yalign 0.5
 
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
        style "desc_text"
        size 37
        xpos 900
        ypos 85
    
    vbox:
        style_prefix "desc"
        text "cleanup specialist":
            xpos 940 ypos 170
            size 23
        text "5'6\"":
            xpos 980 ypos 192
            size 23
        text "21":
            xpos 1090 ypos 164
            size 23
        text "> favorite game: Untitled Goose Game\n> favorite subject: math":
            xpos 920 ypos 335
            size 23
            xsize 500

    use likability_bar(i.likability)    
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
        style "desc_text"
        size 37
        xpos 900
        ypos 85
    
    vbox:
        style_prefix "desc"
        text "mission strategist":
            xpos 940 ypos 170
            size 23
        text "5'11\"":
            xpos 975 ypos 192
            size 23
        text "23":
            xpos 1080 ypos 164
            size 23
        text "> favorite flavor: lemon\n> had an emo phase at one point\n> also had a chess phase\n> yes they did overlap":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    use likability_bar(d.likability)
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
        style "desc_text"
        size 37
        xpos 900
        ypos 85

    vbox:
        style_prefix "desc"
        text "journalist / report writer":
            xpos 940 ypos 170
            size 23
        text "5'10\"":
            xpos 975 ypos 192
            size 23
        text "26":
            xpos 1080 ypos 164
            size 23
        text "> graduated top of her class + a year early":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    use likability_bar(si.likability)
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
        style "desc_text"
        size 37
        xpos 900
        ypos 85

    vbox:
        style_prefix "desc"
        text "software specialist":
            xpos 940 ypos 170
            size 23
        text "5'6\"":
            xpos 980 ypos 192
            size 23
        text "25":
            xpos 1090 ypos 164
            size 23
        text "> obsessed with cute clothes!!!":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    use likability_bar(sa.likability)

    image "sahi_normal.png":
        zoom 0.27
        xcenter 0.34
        yalign 0.5
 
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
        style_prefix "desc"
        text "weapons handler/specialist":
            xpos 940 ypos 170
            size 23
        text "6'1\"":
            xpos 980 ypos 192
            size 23
        text "27":
            xpos 1090 ypos 164
            size 23
        text "> definitely a nepo baby\n> if he weren't an agent he would be an idol fs":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    use likability_bar(r.likability)
    
    image "fake_raphael":
        zoom 1.00
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
        style "desc_text"
        size 37
        xpos 900
        ypos 85
    
    vbox:
        style_prefix "desc"
        text "mechanic / engineer":
            xpos 940 ypos 170
            size 23
        text "6'3\"":
            xpos 980 ypos 192
            size 23
        text "32":
            xpos 1080 ypos 164
            size 23
        text "> has a 2 year old son\n> makes trinkets and gadgets for each member of the team in his free time":
            xpos 920 ypos 335
            size 23
            xsize 500
    
    use likability_bar(ic.likability)

    image "icarus_normal.png":
        zoom 0.33
        xcenter 0.325
        yalign 0.5
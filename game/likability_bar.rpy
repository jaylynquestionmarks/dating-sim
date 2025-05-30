image bar_idle = "gui/bar/right_bar.png"
image bar_hover = "gui/bar/right_bar_hover.png"

screen likability_bar(val, in_char_screen = True):
    bar:
        value val
        range 100
        left_bar "gui/bar/left_bar.png"
        right_bar "gui/bar/right_bar.png"
        xysize(300, 40)
        if in_char_screen:
            xalign 0.63
            yalign 0.79
        else:
            xalign 0.8
            yalign 0.1
image bar_idle = "gui/bar/right_bar.png"
image bar_hover = "gui/bar/right_bar_hover.png"

screen likability_bar(val):
    imagebutton:
        idle "bar_idle"
        hover "bar_hover"
        xalign 0.5
        yalign 0.5
        focus_mask "bar_idle"
    bar:
        value val
        range 100
        left_bar "gui/bar/left_bar.png"
        right_bar "gui/bar/right_bar.png"
        xysize(300, 40)
        xalign 0.5
        yalign 0.5
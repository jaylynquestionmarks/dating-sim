# character objects 
init python:
    class character_obj:
        def __init__(self, char, likability = 35):
            self.char = char
            self.likability = likability
        def __call__(self, text):
            self.char(text)

define n = Character("", color = "#0080ff", window_background = Frame("gui/assets/ntextbox.png"), what_xalign=0.5, what_yalign=0.5)
define preShiftp = Character("[playerName]", color = "#ffffff", window_background=Frame("gui/textbox1.png", 1, 1), namebox_xpos=220)
define p = Character("[playerName]", color = "#ffffff", window_background=Frame("gui/assets/ourTextbox.png", ypos = -20), namebox_xpos=220)
default playerName = "You"

define doc_char = Character("[docName]", color = "#0d0e13")
default docName = "???"
define doc = character_obj(doc_char)

define i_char = Character("[iName]", color = "#ff8800")
default iName = "???"
define i = character_obj(i_char, 40)

define d_char = Character("[dName]", color = "#000000")
default dName = "Damian Double"
define d = character_obj(d_char, 25)
default dLikability = 25

define si_char = Character("[siName]", color = '#979797')
default siName = "Sierra String"
define si = character_obj(si_char)
define siMet = False

define sa_char = Character("[saName]", color = '#9000ff')
default saName = "SDK Sahi"
define sa = character_obj(sa_char)
define saMet = False

define r_char = Character("[rName]", color = "#3bf441")
default rName = "Raphael Recursion"
define r = character_obj(r_char)
define raMet = False

define ic_char = Character ("[icName]", color = '#fecb3f')
default icName = "???"
define ic = character_obj(ic_char)
define icMet = False

#plot structure variable
default equip = False
default office = False

# characters and backgroounds  
image mc:
    "mc.png"
image golf_kart_kun:
    "golf_kart_kun.png"
    zoom 1.75

image bg school:
    "bg_school.jpg"
    zoom 0.49
image bg hallway:
    "bg_hallway.jpg"
    zoom 0.53
image bg infirmary:
    "bg_infirmary.jpeg"
    zoom 3.00
    xalign 0.5
    yalign 0.5
image bg main room:
    "bg_main_room.jpg"
    zoom 1.30
image bg office:
    "bg_office.jpg"
    xalign 0.5 yalign 0.5 
    zoom 3.00
image bg armoury:
    "bg_armoury.jpg"
    xalign 0.5 yalign 0.5
    zoom 3.00

image doc normal:
    "doc_normal.png"
    xalign 0.5 yalign 0.5
    zoom 0.4
image doc happy:
    "doc_happy.png"
    xalign 0.5 yalign 0.5
    zoom 0.4
image doc nervous:
    "doc_nervous.png"
    xalign 0.5 yalign 0.5
    zoom 0.4
image doc speaking:
    "doc_speaking.png"
    xalign 0.5 yalign 0.5
    zoom 0.4

image isaac normal:
    "isaac_normal.png"
    zoom 0.4
image isaac happy:
    "isaac_happy.png"
    zoom 0.4
image isaac speaking:
    "isaac_speaking.png"
    zoom 0.4

image damian normal:
    "damian_normal.png"
    zoom 0.4
image damian happy:
    "damian_happy.png"
    zoom 0.4
image damian speaking:
    "damian_speaking.png"
    zoom 0.4

image sierra normal:
    "sierra_normal.png"
    zoom 0.4
image sierra happy:
    "sierra_happy.png"
    zoom 0.4
image sierra speaking:
    "sierra_speaking.png"
    zoom 0.4

image sahi normal:
    "sahi_normal.png"
    zoom 0.4
image sahi happy:
    "sahi_happy.png"
    zoom 0.4
image sahi speaking:
    "sahi_speaking.png"
    zoom 0.4

image icarus normal:
    "icarus_normal.png"
    zoom 0.4
image icarus speaking:
    "icarus_speaking.png"
    zoom 0.4

image raphael:
    "fake_raphael.png"
    zoom 1
# image raphael_normal:
#     "raphael_normal.png"
#     zoom 0.4
# image raphael_speaking:
    "raphael_speaking.png"
    zoom 0.4

# character alignments 
transform one:
    xcenter 0.1
    yalign 1.0

transform short:
    xcenter 0.5
    ycenter 0.65

transform two:
    xcenter 0.25
    yalign 1.0
    
transform three:
    xcenter 0.33
    yalign 1.0

transform five:
    xalign 0.66
    yalign 1.0

transform six:
    xcenter 0.33
    yalign 1.0
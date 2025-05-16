# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playerName]", color = "#bebebe")
default playerName = "You"
define doc = Character("[doc1]", color = "#5877ff")
default doc1 = "???"

image Doctor:
    "doctor.png"
    zoom 1.75
    
image MC:
    "mc.png"
    yalign 2.0

image golf kart kun:
    "golf kart kun.png"
    zoom 1.75

image bg school:
    "bg school.jpg"
    zoom 3.75

image bg doctors office:
    "bg doctors office.jpg"
    zoom 6.00


label splashscreen:
    scene black
    with Pause(1)

    show text "group name studios presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:

    # animation of eye opening slowly - apparently this can be a movie file 
    doc "You're awake! How are you feeling?"
    player "ugh... I'm okay I guess. Who are you?"
    doc "I'm Dr. Polymorphism."
    $ doc1 = "Dr. Polymorphism"

    "3 hours ago..." with hpunch

    scene bg school
    show mc at left 

    player "Oh no! I only have a minute to get to class! I gotta present my final project in Ms. Patil's class today!!!"
    

    show golf kart kun 
    with zoomin

    player "AAHHHHHHHH!!!"
    "HONK HONK!!!!! SCREEEEECHHHH!!! SSDRJFSUDHICJDKJS"

    scene black

    "Present"

    scene bg doctors office
    show MC at left 
    show Doctor at right 

    player "What...? Polymorphism?"
    doc "My last name, huh? My family is pretty well known for our diverse careers."
    doc "You may have heard of my cousin, the idol Paisley Polymorphism. Yes, I'm one of the Polymorphisms."
    player "... Did I get freaking isekai'd???"
    doc "Sorry, what?"
    player "No, hold on. Where am I? What is this place?"
    doc "You're at __ Care Center here at the AP CSA, Miss..."

    $ playerName = renpy.input("What is your name?")

    doc "Well Miss [playerName], you were admitted for a near fatal code crash, but we managed to bring you back."
    player "... code crash?"
    player "{i}am i... in a computer science world?{/i}"
    doc "Miss [playerName]? Are you alright?"  
    player "Yeah, sorry. I blanked out for a second."
    doc "Oh, that's okay. So, about your situation. Your code suddenly crashed, but we couldn't figure out the exact cause."
    doc "Our team here was debating whether it was a stack overflow but you didn't show any signs of internal spasming, so we're not exactly sure."
    player "{i}A stack overflow? How does that happen to a person??{/i}"
    doc "Because of your unusual situation, your particular case is of interest to the Agent Patil's Corporation of Secret Agents, or the APCSA."
    doc "They've decided they want to keep you under their watch. Unfortunately, this is a nonnegotiable order."
    player "..."
    player "What."
    doc "You have the benefit of being a guest agent here, though. You'll be reset if we decide to let you go because this is confidential information."
    player "..."
    doc "If you're feeling up for it, we can go on a tour of the facility right now!"

    menu:
        "<fess up and reveal you think you've been isekai'd>":
            jump cowardEnding

        "<play along! this is way more exciting than my old life!>":
            pass


label cowardEnding:

    player "I'm sorry, Dr. P. I think I've been isekai'ed into this world."
    doc "Huh? Sorry, I'm not sure what you mean…"
    player "I mean that I think I've been transported here from my old life. I think I'm not from this world."
    player "I got into some sort of accident in my previous life and just woke up here."
    player "I really want to go back, I have a really important project to present in class!"
    doc "..."
    doc "......"
    doc "Ohh!!! That's why your code crashed so strangely!! Why didn't you say so earlier?? I've got just the thing for you."
    doc "You're very lucky we found you; we have access to a state-of-the-art Returner here!!"
    doc "Come with me, we'll return you to your own world."
    player "{i}Dang. That was so easy.{/i}"
    doc "It's a shame we have to part so early. But thank you for being clear with me. Goodbye!!"
    # zap to real world

    scene bg school
    show mc at left

    player "I'm back!! Oh no, how much time do I have to get back to class? ONE MINUTE??? I better run!"
    player "..."
    player "Maybe I'll wait for that golf cart to pass, though."

    scene black
    "Ending 01: Coward >:("
    $ MainMenu(confirm = False)()# The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return

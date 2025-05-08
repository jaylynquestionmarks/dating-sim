# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playerName]", color = "#d851d4")
default playerName = "You"
define doc = Character("[doc1]", color = "#c02e50")
default doc1 = "???"


# The game starts here.

label start:

    doc "You're awake! How are you feeling?"
    player "ugh... I'm okay I guess. Who are you?"
    doc "I'm Dr. Polymorphism"
    $ doc1 = "Dr. Polymorphism"

    "3 horse ago..."
    player "Oh no! I only have a minute to get to class! I gotta present my final project in Ms. Patil's class today!!!"
    #all the golf cart crash stuff
    "Present"

    player "What...? Polymorphism?"
    doc "Oh yeah, our family is pretty well known for our diverse careers You may have heard of my cousin, the idol Paisly Polymorphism. Yeah, I'm one of them"
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
    doc "Oh, that\’s okay. So, about your situation. Your code suddenly crashed, but we couldn\’t figure out the exact cause."
    doc "Our team here was debating whether it was a stack overflow but you didn\’t show any signs of internal spasming, so we\’re not exactly sure."
    player "{i}A stack overflow? How does that happen to a person LMAO.{/i}"
    doc "Because of your unusual situation, your particular case is of interest to the Agent Patil's Coroporation of Secrent Agents"
    doc "They\’ve decided they want to keep you under their watch. Unfortunately, this is a nonnegotiable order."
    player "What."
    doc "You have the benefit of being a guest agent here, though. You\’ll be reset if we decide to let you go because this is confidential information."
    player "..."
    doc "If you\’re feeling up for it, we go on a tour of the facility right now!"

    menu:
        "<fess up and reveal you think you've been isekai'd>":
            jump cowardEnding

        "<play along! this is way more exceiting than my old life!>":
            pass



label cowardEnding:

    player "I\’m sorry, Dr. P. I think I\’ve been isekai\’ed into this world."
    doc "Huh? Sorry, I\’m not sure what you mean…"
    player "I mean that I think I\’ve been transported here from my old life. I think I\’m not from this world."
    player "I got into some sort of accident in my previous life and just woke up here."
    player "I really want to go back, I have a really important project to present in class!"
    doc "..."
    doc "......"
    doc "Ohh!!! That\’s why your code crashed so strangely!! Why didn\’t you say so earlier?? I\’ve got just the thing for you."
    doc "You\’re very lucky we found you; we have access to a state-of-the-art Returner here!!"
    doc "Come with me, we\’ll return you to your own world."
    player "{i}Dang. That was so easy.{/i}"
    doc "It’s a shame we have to part so early. But thank you for being clear with me. Goodbye!!"
    # zap to real world
    player "I\’m back!! Oh no, how much time do I have to get back to class? ONE MINUTE??? I better run!"
    player "..."
    player "Maybe I'll wait for that golf cart to pass, though."

    "Ending: Coward >:("
    $ MainMenu(confirm = False)()

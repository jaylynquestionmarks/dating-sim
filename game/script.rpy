image char_menu_idle = im.Scale("gui/char_menu_idle.png", 100, 100)
image char_menu_hover = im.Scale("gui/char_menu_hover.png", 100, 100)

image crash:
    Movie(play = "images/crash.webm")
    zoom 1.8

define title = ""
image darken:
    "gui/overlay/confirm.png"
    xalign 0.5
    yalign 0.5
    zoom 3

label splashscreen:
    scene black
    with Pause(1)

    show text "our group studios presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label crash_scene:
    show crash
    pause(0.6)
    play sound "audio/crash_sfx.mp3"
    pause(2)

    return

label start:

    call screen select()
    # animation of eye opening slowly - apparently this can be a movie file 
    doc "You're awake! How are you feeling?"
    p "ugh... I'm okay I guess. Who are you?"
    doc "I'm Dr. Polymorphism."
    $ docName = "Dr. Polymorphism"
    p  "..." 
    p  "huh???"

    centered "3 hours ago..." with hpunch

    scene bg school with dissolve
    centered "{color=#0000ffff}05/30/25 \n1:25 pm{/color}"

    scene bg hallway with dissolve
    show mc at left 

    preShiftp  "Oh no! I only have a minute to get to class! I gotta present my final project in Mrs. Patil's class today!!!"

    preShiftp  "AAHHHHHHHH!!!"
    centered "HONK HONK!!!!! SCREEEEECHHHH!!! SSDRJFSUDHICJDKJS" #replace with audio & video maybe??

    call crash_scene

    scene black
    centered "Present" with hpunch

    scene bg infirmary
    show mc at one 
    show doctor at right 

    p  "What...? Polymorphism?"
    doc "My last name, huh? My family is pretty well known for our diverse careers."
    doc "You may have heard of my cousin, the idol Paisley Polymorphism. Yes, I'm one of the Polymorphisms."
    p  "... Did I get freaking isekai'd???"
    doc "Sorry, what?"
    p  "No, hold on. Where am I? What is this place?"
    doc "You're at Code Care Center here at the AP CSA, [title]..."

    $ input_align = 0.5
    $ playerName = renpy.input("What is your name?")

    doc "Well [title][playerName], you were admitted for a near fatal code crash, but we managed to bring you back."
    p "... code crash?"
    doc "Miss [playerName]? Are you alright?"  
    p "Yeah, sorry. I blanked out for a second."
    doc "Oh, that's okay. So, about your situation. Your code suddenly crashed, but we couldn't figure out the exact cause."
    doc "Our team here was debating whether it was a stack overflow but you didn't show any signs of internal spasming, so we're not exactly sure."
    p "{i}A stack overflow? How does that happen to a person??{/i}"
    doc "From your medical record, it looks like it's been a recurring issue."
    doc "Apparently you're an intern at a branch of the AP CSA? That's Agent Patil's Corporation of Secret Agents, in case your memory's still spotty."
    doc "They've decided they want to keep you under their watch, so they're...putting you on our team???"
    doc "That makes no sense. But unfortunately, it's a nonnegotiable order."
    p "What."
    doc "You have the benefit of being a guest agent here, though. You'll be reset if we decide to let you go because this is confidential information."
    p "..."
    doc "If you're feeling up for it, we can go on a tour of our facility right now!"
    menu:
        "fess up and reveal you think you've been isekai'd":
            jump cowardEnding

        "play along! this is way more exciting than my old life!":
            jump playAlong

label cowardEnding:

    p "I'm sorry, Dr. P. I think I've been isekai'ed into this world."
    doc "Huh? Sorry, I'm not sure what you mean…"
    p "I mean that I think I've been transported here from my old life. I think I'm not from this world."
    p "I got into some sort of accident in my previous life and just woke up here."
    p "I really want to go back, I have a really important project to present in class!"
    doc "..."
    doc "......"
    doc "Ohh!!! That's why your code crashed so strangely!! Why didn't you say so earlier?? I've got just the thing for you."
    doc "You're very lucky we found you; we have access to a state-of-the-art Returner here!!"
    doc "Come with me, we'll return you to your own world."
    p "{i}dang. that was so easy.{/i}"
    doc "It's a shame we have to part so early. But thank you for being clear with me. Goodbye!!"
    # zap to real world

    scene bg school
    show mc at left

    preShiftp "I'm back!! Oh no, how much time do I have to get back to class? ONE MINUTE??? I better run!"
    preShiftp "..."
    preShiftp "Maybe I'll wait for that golf cart to pass, though."

    scene black
    show darken with dissolve
    show screen announce("Ending 01: Coward >:(","")
    centered ""
    hide darken
    hide screen announce
    
    $ MainMenu(confirm = False)()# The script of the game goes in this file.
return 

label playAlong:
    p "{i} you know what. this is WAY more exciting than presenting my project in class. i'm a secret agent now! {/i}"
    p "Sure!"
    $ docLikability += 3
    p "{i} wait what? likability points? what are these?? {/i}"
    doc "Alright! Let's go into our main room then."
    "Dr. Polymorphism glances down at his tablet and looks confused."
    p "..Is everything alright?"
    doc "So."
    doc "This is a bit awkward, but I was on break playing a game before you were brought in."
    doc "I was trying to pull up a map of the place, but my tablet won't let me exit the game app.."
    menu:
        "Look at Dr. Polymorphism's tablet":
            "It's a tic tac toe board....."
            p "Were you playing tic tac toe with yourself...?"
            doc "..."
            doc "Anyways..."
            doc "Well, the board started glitching when you came in..."
            doc "Can you {color=#f00}fix the bug{/color}? You can try {color=#f00}playing the game{/color} to figure it out."
            menu:
                "Investigate!":
                    show screen ticTacToeGame(False)
                    call fixBug(doc, 3, "64", "$ turn = \"x\"")
                    hide screen ticTacToeGame
                    hide screen o0
                    hide screen o1
                    hide screen o2
                    hide screen o3
                    hide screen o4
                    hide screen o5
                    hide screen o6
                    hide screen o7
                    hide screen o8
    call screen ticTacToeGame(True)
    doc "Whoa, you actually fixed it?"
    p "Yeah...It was kinda easy to be honest.."
    doc "Don't you know how rare skills like those are? With that talent, you might make a fine addition to the team after all!"
    doc "You'll see once you meet the team - let's go!"

    scene bg main room with dissolve
    show mc at left
    show doctor at right
    
    doc "This is the common area, where we gather for our main missions from Agent Patil, our supervisor."
    show isaac happy at center
    i "HEY PETEY!!!! {i} *GASPPPP!!*{/i}"
    i "oh"
    i "my"
    i "GODDDD!!! Petey, is this our new agent???"
    doc "{i} *sigh* {/i}"
    doc "Hello, Isaac. Yes, this is our new agent,[title][playerName]. [title][playerName], this is our resident cleanup agent, Isaac Integer."
    $ iName = "Isaac Integer"
    p "Hello!" 
    p "{i}...integer? is everyone here named this way?{/i}"
    
    show isaac speaking
    i "HIII!!! It's so nice to meet you, [title][playerName]! Oh wow, you have such a nice name!"
    $ iName = "Isaac"
    
    p "Thanks! You have such a pretty face!"
    $ iLikability += 5
    i "Thanks!!!!"
    p "{i}wait the doc went from 35 to 38 because i agreed to be an agent{/i}"
    p "{i}this guy went from 40 to 45 because i said his face was nice…{/i}"
    p "{i}are these...relationship points?{/i}"

    #custom screen we made to announce the character menu
    show darken with dissolve
    show screen announce("You've unlocked the Character Menu!","Click on the button at the top right to see everyone you've met!") 
    centered ""
    hide darken
    hide screen announce

    show screen charMenuButton
    # $ renpy.pause(hard = True)

    show damian normal at three 
    i "Oh, and this is my brother Damian!"
    $ dName = "Damian"
    
    show isaac normal
    show damian speaking 
    
    d "You can call me Mr. Double. I am the action strategist here at the A.P.C.S.A."
    $ dName = "Mr. Double"
    
    show damian normal
    
    p "{i}eek he's so menacing… i really don't want to die again today{/i}"
    p "Nice to meet you, Mr. Double."
    
    show isaac speaking
    
    i "Are you guys going on a tour? Can I come??"
    
    show isaac happy
    show doctor at right
    
    doc "{i} sigh {/i}"
    doc "I mean, if you want to. Let's keep moving then."
    
    show isaac happy
    
    doc "[title][playerName], do you want to see our equipment room first or see our main reporting office?"
    menu:
        "\"The equipment room sounds pretty cool!\"":
            p "The equipment room sounds pretty cool!"
            d "Well, then. I need to head over to the office. See you later."
            i "Alright, let's go!!!"
            $ equip = True
            jump meetEquipment

        "\"Um, the office?\"":
            p "Um, the office?"
            
            show damian speaking
            
            d "I'll suppose I'll join you as well."
            $ dLikability += 2

            show damian normal
            
            p "{i}what's with this guy?{/i}"
            p "{i}is there someone he wants to murder there?{/i}"
            
            show isaac speaking
            i "Awesome, let's go!!!"
            $ office = True
            jump meetOffice

label meetOffice:
    scene bg office with dissolve
    show doctor at right 
    show mc at one 
    show damian normal at two 
    show isaac normal at three

    doc "Here we are, in the main reporting office." 
    doc "..."
    doc "Well it looks empty right now, but there are usually more people here."
    
    show sierra normal at five
    
    doc "Oh, this is Sierra String. She's our journalist. Sierra, this is [playerName]. She's our new guest agent."
    
    show sierra speaking
    
    si  "Hello."
    
    show sierra normal
    
    p "{i}what… another murderous looking person already? why?{/i}"
    p "i'd better address her with a formality like the other guy."
    p "Nice to meet you, Ms. String."
    $ siMet = True

    show sierra happy
    
    si "[playerName], huh? Sierra is fine."
    $ siName = "Sierra"
    
    show isaac speaking
    show sierra normal
    
    i "Ice cold as always, isn't she. She scared me too the first time I saw her. Don't worry, you'll get used to it."
    menu:
        "No, no, not at all.":
            p "No, no, not at all. {i}sweat{/i}"
            $ siLikability += 2

            show sierra happy 
            show isaac normal
            
            si "I have a feeling we are going to get along very well, [playerName]"
            
        "Don't worry, I like them cold.":
        
            show isaac normal
            p "Don't worry, I like them cold."
            $ dLikability += 2

    
    show doctor at right
    show sahi normal  

    doc "Oh, this is SDK Sahi, our on-base support. Sahi, this is [playerName]."

    show sahi speaking
    sa "Hello! Nice to meet you [playerName].\nIf there's anything at all that you need here, just tell me and I'll see if I can take care of it for you!"
    $ saMet = True

    show sahi happy

    sa "Oh, and just Sahi is fine!"
    $ saName = "Sahi"

    show sahi normal

    p "{i}finally, someone who doesn't look like they want to murder me{/i}"
    p "Thank you, I appreciate it!"

    if equip: 
        jump mission1
    else:
        doc "Alright [playerName], let's get you stocked up. We're going to the equipment room next."
        show damian speaking
        d "You guys go ahead. I'll stay here with Sierra."
        show sahi speaking
        sa "I have some things to do too. Sorry I can't come with you. But we'll see each other again soon!"
        show isaac speaking
        i "Let's go!"
        jump meetEquipment

label meetEquipment:
    scene bg armoury with dissolve
    show doctor at right 
    show isaac normal at two 
    show mc at left 

    doc "Here's our equipment room, where we store weapons and gadgets."
    doc "And, uh, this is Raphael Recursion. He's a field agent. Raphael, this is [title][playerName]."
    $ raMet = True
    
    p "Nice to meet y-"
    r "[playerName], huh. Well I don't really know who you are, but I'm sure you've heard of me." 
    p "..."
    r "Recursion?? Ring a bell?"
    p "..-"
    r "{i}sigh{/i} I guess I'll just have to educate you then. My dad, Richard Recursion, is the owner of one of the biggest corporations in the country and -"
    
    menu:
        "cut him off: \"I really didn't ask but okay.\"":
            p "{i}he's so…full of himself. ew. such a nice face wasted on such a terrible personality. {i}"
            $ dLikability += 5
            p "{i}wow so even doctors can dislike people…{/i}" #something more witty than this
    
    show icarus speaking
    ic "Oh, who's this?"

    show icarus normal
    show isaac speaking 
    i "Oh hey Icarus! This is [playerName]. She's a guest agent!"
    
    show isaac normal 
    show icarus speaking
    
    ic "Hello [playerName]. It's nice to meet you. I'm Icarus Inheritance."
    $ icName = "Icarus Inheritance"
    $ icMet = True
    show icarus normal

    show isaac speaking
    i "We call him Dorito though."
    show isaac normal
    
    menu:
        "Let me guess, because of the bag of doritos?":
            p "Let me guess, because of the bag of doritos?"
            i "No silly, because of his dorito build obviously!"
            p "Oh, yes. Obviously."
        
        "Because of his dorito build or…":
            p "Because of his dorito build or…"
            show isaac speaking
            i "AHAHAHAHAHA!!!" with hpunch  
            $ iLikability += 5
            # You are now FRIENDS with isaac! (but only if you also did the other +5 option)
            show isaac happy
            i "You're so funny [playerName]. I have a feeling we're going to be great friends!!"

    
    if office: 
        jump mission1
    else:
        doc "[title][playerName], let's visit the reporting office next."
        
        show isaac happy
        i "Do you two wanna come?"
        
        # show raphael speaking
        r "I have to tend to Anastasia here, she's a little busted up after last mission. My poor baby."
        
        show icarus speaking
        ic "Sorry, I have some repairing to do too. As you can see, these steam pipes are still a bit leaky."
        show icarus normal

        i "Let's go!"
        jump meetOffice

label mission1:
    doc "Let's go back to the lobby, [title][playerName]. I have to give you some other orientation materials."
    p "Sure!"
    scene bg main room
    show doctor at right
    show mc at left
    doc "Here's the mandatory brochure, the free pin, and the map. That should be all."
    centered "WEEEEE OOOOOOOOO WEEEEE OOOOOOOOO" with vpunch
    #(shake effect) (or lights flicker if you know how to do that)
    show isaac normal # ill try to make like a concerned face 
    i "Hey, something’s wrong with our systems!"
    r "Ugh! Our repair systems are down, too!!"
    show damian speaking at two
    d "Your whack-a-bug isn’t working?"
    n "Icarus shakes the device around, and his brows furrow."
    d "From the looks of it, this isn’t a hardware issue."
    ic "Haha, just our luck, right, [playerName]? The first day we’re here, we get our systems hacked, including our repair devices. and they targeted our one weakness – software!!"
    
    p "..."
    p "I think I can help."
    
    n "The team looks at you, surprised." with hpunch
    
    d "..."
    ic "Well, go at it."
    #Icarus hands you the device”
    call start_whack_a_bug

    ic "Well, since you fixed it, do you want to give it a try?"
    p "Sure!"

    call start_whack_a_bug
    ic "Good to have you on the team, [playerName]."

# (you fix the bug)
# (sahi likability increase by 1 each time you fail, lines like “You got this!” and “Everyone makes mistakes!”)

# ic “wow, i’m impressed. do you want to give it a try?”
# call start_whack_a_bug()
# (sahi likability increase if you fail– the team takes over, like someone says “dont worry, we got it. thanks for your help!”)
# (ic likability increase if you succeed)




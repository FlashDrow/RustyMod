label jerk_off:
    $ cum_on_panties = True #True when choose to cum on Hermione's panties.
#    m "Hm... Who shall be my target?"
#    menu:
#        "\"Princess Jasmine!\"":
#            m "Yes, the princess... That dirty slut!"
#            $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
#            pass
#        "\"Lara Croft\"":
#            $ jerking_off_to_lara = True
#            pass
#        "-Cancel-":
#            jump desk
#    m "How should I finish this thing?"   
#    label how_to_finish:
#    menu:
#        "-On the floor!-":
#            $ cum_on_the_floor = True #TRUE when chosen to cum on the floor.
#            pass
#        "-Item # 1-" if not request_03:
#            ">You lack the item required for this option."
#            jump  how_to_finish
#        "{color=#858585}...(LOCKED)...{/color}" if not request_03: #True when Hermione has no panties on.:
#            ">You lack the item required for this option."
#            jump  how_to_finish
#        "-Hermione's panties-" if request_03: #True when Hermione has no panties on.
#            $ cum_on_panties = True #True when choose to cum on Hermione's panties.
#        "-Cancel-":
#            jump jerk_off


### JERKING OFF ###
show screen blkfade
with d5
">Вы решили провести время за мастурбацией..."
if jerking_off_to_jasmine:
    ">Вы фантазируете о принцессе Жасмин..."
if jerking_off_to_lara:
    ">Вы фантазируете о Ларре Крофт..."

">Вы готовы кончить..."
if cum_on_the_floor:
    ">Вы кончили на пол."
if cum_on_panties:
    $ have_cum_soaced_panties = True #TRUE when you have the panties in your possession (before you return them to Hermione).
    ">Вы кончили на трусики Гермионы, а затем протерли ими пол..."
    ">Вы получили предмет: \"Трусики пропитанные спермой\"."
 
hide screen blkfade
with d5
#m "This was a pretty sweet jerk-off session..."
    
### SETTING ALL THE FLAGS BACK TO DEFAULT ###
$ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
$ jerking_off_to_lara = False 
$ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
$ cum_on_panties = False #True when choose to cum on Hermione's panties.



if daytime:
    jump night_start
else: 
    jump day_start

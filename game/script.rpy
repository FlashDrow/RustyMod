


init:



    # DDAPHNE ____________________________________________________________________________

    image ch_dap = "dap/dap_blink_a1.png"
    image ch_dap2 = "dap/dap_walk_b4.png"

    image dap_av = "dap/daphne_body.png"
    # DEMON +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



    # CHJOU +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # HARRY +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    image side ronald = "f/ron.png"

    image hog = "f/hog.png"
    image hog2 = "f/hog2.png"

    image side hagr = "f/hagr.png"

    image title2 = "title2.jpg"

    ### Disposable flags ###
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False

    $ d_points = 0



    $ renpy.music.register_channel("bg_sounds", "sfx", True)
    $ renpy.music.register_channel("weather", "sfx", True)

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbulb2 = Fade(1, 0.5, 1, color='#fff')
    $ flashbulb3 = Fade(1.5, 0.5, 1, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')

    #NVLE STUFF
    $ nvle = Character(color="#000", what_color="#ffffff", kind=nvl)
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve


    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['hide_windows'].remove('h')


#define m = Character(None, window_left_padding=200, image="mage", color="#402313", ctc="ctc3", ctc_position="fixed")



label splashscreen:
    $ renpy.pause(0)
    scene black
    with Pause(0.9)
    $ renpy.play('sounds/start.mp3')
    show image "logo/logo07.jpg"
    pause 1
    with dissolve
    with Pause(2.0)

    scene black
    with dissolve
    with Pause(1.0)

    return


###TRANSITIONS###########
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)

###HARRY POTTER CHARACTERS###
image ch_hem 01 = "03_hp/animation/h_walk_01.png"

image mkg_stay = "f/mkg1.png"
image mkg_walk = Animation("f/mkg2.png", 0.3, "f/mkg3.png", 0.3)

image bld2 = "slavem/bld2.png"
image bld = "slavem/bld.png"
image bg lp = "lpotion/lpfinal00.jpg"
image bg meadow = "meadow.jpg"
image bg magic = "meadowmagic.jpg"
image magic = "magic1.png"
image magic2 = "magic2.png"
image magic3 = "magic3.png"
image magic4 = "magic4.png"
image magic5 = "magic5.png"
image white = "white.jpg"
image tension = "quest01/fight.png"
image ctc3 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2, xpos=0.97, ypos=0.929, xanchor=1.0, yanchor=1.0)
image ctc4 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2, xpos=0.99, ypos=0.995, xanchor=0.8, yanchor=1.0)
image ctc7 = Animation("ctc00.png", 0.2, "ctc01.png", 0.2, "ctc02.png", 0.2, "ctc03.png", 0.2, "ctc04.png", 0.5, "ctc03.png", 0.2, "ctc02.png", 0.2, "ctc01.png", 0.2,)
image whitefade = "whitefade.png"
image ariel1 = "ariel1.png"
image arielmad = "arielmad1.png"
image arielscream = "arielscream.png"
image asilent = "arielsilent.png"
image asulky = "arielsulky.png"
image threetits = "threetits/threetits01.png"
image threenormal = "threetits/threetits02.png"
image threetitsmad = "threetits/baretitsmad.png"
image threetitsmad2 = "threetits/baretitsmad2.png"
image slave02 = "slave/slave02.png"
image slave03 = "slave/slave03.png"
image slave04 = "slave/slave04.png"
image slave06 = "slave/slave01_04.png"
image threetitsmad4 = "threetits/baretitsmad4.png"
image blkfade = "blackfade.png"
image blk50 = im.Alpha("blackfade.png", 0.5)

image okn1 = "end/1.png"
image okn2 = "end/2.png"
image ve1 = "end/ve1.png"
image ve2 = "end/ve2.png"
image ve3 = "end/ve3.png"
image ve4 = "end/ve4.png"
image ve4 = "end/ve5.png"
image ve4 = "end/ve6.png"
image ve4 = "end/ve7.png"
image ve4 = "end/ve8.png"
image ve4 = "end/ve9.png"
image ve4 = "end/ve10.png"
image ve4 = "end/ve11.png"
image ve4 = "end/ve12.png"
image ve4 = "end/ve13.png"
image vechel = "end/1chel.png"









    ### INTRO MOVIE ANIMATIONS ###


image stadium_def:
    "new/stad2.png"
    pause 0.8
    "new/stad3.png"
    pause 0.8
    "new/stad2.png"
    pause 0.8
    "new/stad5.png"
    pause 0.8
    "new/stad2.png"
    pause 0.8
    "new/stad7.png"
    pause 0.8
    repeat

image chm_min:
    "new/chm1/1.png"
    pause 0.5
    "new/chm1/1-1.png"
    pause 0.5
    repeat

image chm_min2:
    "new/chm1/3.png"
    pause 0.5
    "new/chm1/3-1.png"
    pause 0.5
    repeat

image chm_min22:
    "new/chm1/3cc.png"
    pause 0.5
    "new/chm1/3-1cc.png"
    pause 0.5
    repeat

image chm_min3:
    "new/chm1/3-2.png"
    pause 0.5
    "new/chm1/3-3.png"
    pause 0.5
    repeat

image chm_min33:
    "new/chm1/3-2cc.png"
    pause 0.5
    "new/chm1/3-3cc.png"
    pause 0.5
    repeat



image title_ani: #Main title animation.
    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/13.png"
    pause.1
    "03_hp/23_title/14.png"
    pause.1
    "03_hp/23_title/13.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

### second cercle.
    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/02.png"
    pause.1
    "03_hp/23_title/03.png"
    pause.1
    "03_hp/23_title/04.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    "03_hp/23_title/01.png"
    pause.1
    "03_hp/23_title/13.png"
    pause.1
    "03_hp/23_title/14.png"
    pause.1
    "03_hp/23_title/13b.png"
    pause.1
    "03_hp/23_title/05b.png"
    pause.1
    "03_hp/23_title/06b.png"
    pause.1
    "03_hp/23_title/07b.png"
    pause.1
    "03_hp/23_title/08b.png"
    pause.1
    "03_hp/23_title/09b.png"
    pause.1
    "03_hp/23_title/10b.png"
    pause.1
    "03_hp/23_title/11b.png"
    pause.1
    "03_hp/23_title/12b.png"
    pause.1

    "03_hp/23_title/01b.png"
    pause.1
    "03_hp/23_title/02b.png"
    pause.1
    "03_hp/23_title/03b.png"
    pause.1
    "03_hp/23_title/04b.png"
    pause.1
    "03_hp/23_title/05b.png"
    pause.1
    "03_hp/23_title/06b.png"
    pause.1
    "03_hp/23_title/07b.png"
    pause.1
    "03_hp/23_title/08b.png"
    pause.1
    "03_hp/23_title/09b.png"
    pause.1
    "03_hp/23_title/10b.png"
    pause.1
    "03_hp/23_title/11b.png"
    pause.1
    "03_hp/23_title/12b.png"
    pause.1

    "03_hp/23_title/01b.png"
    pause.1
    "03_hp/23_title/13b.png"
    pause.1
    "03_hp/23_title/14.png"
    pause.1
    "03_hp/23_title/13.png"
    pause.1
    "03_hp/23_title/05.png"
    pause.1
    "03_hp/23_title/06.png"
    pause.1
    "03_hp/23_title/07.png"
    pause.1
    "03_hp/23_title/08.png"
    pause.1
    "03_hp/23_title/09.png"
    pause.1
    "03_hp/23_title/10.png"
    pause.1
    "03_hp/23_title/11.png"
    pause.1
    "03_hp/23_title/12.png"
    pause.1

    repeat
image intro_01:
    "03_hp/20_intro/01_01.png"
    pause 1
    "03_hp/20_intro/01_02.png"
    pause 1
    repeat

image intro_02:
    "03_hp/20_intro/02_01.png"
    pause 1
    "03_hp/20_intro/02_02.png"
    pause 1
    "03_hp/20_intro/02_01.png"
    pause 1
    "03_hp/20_intro/02_02.png"
    pause 1
    "03_hp/20_intro/02_03.png"
    pause.08
    "03_hp/20_intro/02_02.png"
    pause.08
    "03_hp/20_intro/02_03.png"
    pause.08
    repeat

image intro_03:
    "03_hp/20_intro/03_01.png"
    pause 1
    "03_hp/20_intro/03_02.png"
    pause 1
    repeat

image intro_04:
    "03_hp/20_intro/04_01.png"
    pause 1
    "03_hp/20_intro/04_02.png"
    pause 1
    repeat

image intro_05:
    "03_hp/20_intro/05_01.png"
    pause 1
    "03_hp/20_intro/05_02.png"
    pause 1
    repeat

image intro_06:
    "03_hp/20_intro/06_01.png"
    pause 1
    "03_hp/20_intro/06_02.png"
    pause 1
    repeat

###HARRY POTTER ANIMATIONS###

### BROKEN GLASS ###
image glass: # Animation that shows a broken glass effect when the duel starts.
    "03_hp/21_fight/01.png"
    pause 1.3
    "03_hp/21_fight/02.png"
    pause.3
    "03_hp/21_fight/03.png"
    pause.3
    "03_hp/21_fight/04.png"
    pause.3
    "03_hp/21_fight/05.png"
    pause.3
    "03_hp/21_fight/06.png"
    pause.3
    "03_hp/21_fight/07.png"


image demon walk:
    "f/dem4.png"
    pause.08
    "f/dem5.png"
    pause.08
    "f/dem4.png"
    pause.08
    "f/dem1.png"
    pause.08
    "f/dem2.png"
    pause.08
    "f/dem3.png"
    pause.08
    "f/dem2.png"
    pause.08
    "f/dem1.png"
    repeat


image dap_govor:
    "dap/dap_govor.png"
    pause 0.7
    "dap/d_wha.png"


image mkg_walkf:
    im.Flip("f/mkg2.png", horizontal = True)
    pause 0.3
    im.Flip("f/mkg3.png", horizontal = True)
    pause 0.3
    repeat

image dap_hem_walk_01f:
    im.Flip("dap/dap_walk_a1.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_a2.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_a3.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_a4.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_a5.png", horizontal=True)
    pause.08
    repeat

image harry_walk:
    "f/ha_3.png"
    pause.15
    "f/ha_2.png"
    pause.15
    "f/ha_5.png"
    pause.15
    "f/ha_4.png"
    pause.15
    repeat

image harry_walkf:
    im.Flip("f/ha_2.png", horizontal=True)
    pause.08
    im.Flip("f/ha_5.png", horizontal=True)
    pause.08
    im.Flip("f/ha_3.png", horizontal=True)
    pause.08
    im.Flip("f/ha_4.png", horizontal=True)
    pause.08
    repeat

image dap_hem_walk_01:
    "dap/dap_walk_a1.png"
    pause.08
    "dap/dap_walk_a2.png"
    pause.08
    "dap/dap_walk_a3.png"
    pause.08
    "dap/dap_walk_a4.png"
    pause.08
    "dap/dap_walk_a5.png"
    pause.08
    repeat

image dap_hem_walk_02:
    "dap/dap_walk_b1.png"
    pause.08
    "dap/dap_walk_b2.png"
    pause.08
    "dap/dap_walk_b3.png"
    pause.08
    "dap/dap_walk_b4.png"
    pause.08
    "dap/dap_walk_b5.png"
    pause.08
    repeat

image dap_hem_walk_02f:
    im.Flip("dap/dap_walk_b1.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_b2.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_b3.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_b4.png", horizontal=True)
    pause.08
    im.Flip("dap/dap_walk_b5.png", horizontal=True)
    pause.08
    repeat

image ch_chim walk_01:
    "f/ch_walk1.png"
    pause.08
    "f/ch_walk2.png"
    pause.08
    "f/ch_walk3.png"
    pause.08
    "f/ch_walk2.png"
    pause.08
    "f/ch_walk1.png"
    pause.08
    "f/ch_walk4.png"
    pause.08
    "f/ch_walk5.png"
    pause.08
    "f/ch_walk4.png"
    pause.08
    repeat


image ch_chim walk_02:
    "f/ch_walk11.png"
    pause.08
    "f/ch_walk22.png"
    pause.08
    "f/ch_walk33.png"
    pause.08
    "f/ch_walk22.png"
    pause.08
    "f/ch_walk11.png"
    pause.08
    "f/ch_walk44.png"
    pause.08
    "f/ch_walk55.png"
    pause.08
    "f/ch_walk44.png"
    pause.08
    repeat


image ch_hem walk_01:
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_02.png"
    pause.08
    "03_hp/animation/h_walk_03.png"
    pause.08
    "03_hp/animation/h_walk_02.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_04.png"
    pause.08
    "03_hp/animation/h_walk_05.png"
    pause.08
    "03_hp/animation/h_walk_04.png"
    pause.08
    repeat

image ch_hem robe: # Hermione chibi. Wearing a robe.
    "03_hp/animation/01.png"
    pause.08
    "03_hp/animation/02.png"
    pause.08
    "03_hp/animation/03.png"
    pause.08
    "03_hp/animation/04.png"
    pause.08
    "03_hp/animation/05.png"
    pause.08
    "03_hp/animation/06.png"
    pause.08
    "03_hp/animation/07.png"
    pause.08
    "03_hp/animation/08.png"
    pause.08
    repeat

image ch_hem robe_f: # Hermione chibi. Wearing a robe.
    im.Flip("03_hp/animation/01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/03.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/04.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/05.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/06.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/07.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/08.png", horizontal=True)
    pause.08
    repeat

image ch_hem walk_01_f: #GErmione walking animation. Facing right.
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_02.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_05.png", horizontal=True)
    pause.08
    im.Flip("03_hp/animation/h_walk_04.png", horizontal=True)
    pause.08
    repeat


image ch_hem run_f:
    "03_hp/animation/h_run_01f.png"
    pause.07
    "03_hp/animation/h_run_02f.png"
    pause.07
    "03_hp/animation/h_run_03f.png"
    pause.07
    "03_hp/animation/h_run_02f.png"
    pause.07
    "03_hp/animation/h_run_01f.png"
    pause.07
    "03_hp/animation/h_run_04f.png"
    pause.07
    "03_hp/animation/h_run_05f.png"
    pause.07
    "03_hp/animation/h_run_04f.png"
    pause.07
    repeat


image ch_hem blink:
    "03_hp/animation/h_walk_01.png"
    pause 2
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause 5
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause.08
    "03_hp/animation/h_walk_06.png"
    pause.08
    "03_hp/animation/h_walk_01.png"
    pause 3
    repeat

image snape_walk_01: #Default Snape walk animation.
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_03.png"
    pause.18
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_05.png"
    pause.18
    repeat

image snape_walk_01_f: #Default Snape walk animation.
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_03.png", horizontal=True)
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_05.png", horizontal=True)
    pause.18
    repeat

image genie_walk_ani: #Default Genie walk animation.
    "03_hp/05_props/walk_01.png"
    pause.18
    "03_hp/05_props/walk_02.png"
    pause.18
    "03_hp/05_props/walk_03.png"
    pause.18
    "03_hp/05_props/walk_04.png"
    pause.18
    repeat



image rum:
    "03_hp/animation/rum_01.png"
    pause.3
    "03_hp/animation/rum_02.png"
    pause.3
    "03_hp/animation/rum_03.png"
    pause.3
    "03_hp/animation/rum_04.png"
    pause 1
    "03_hp/animation/rum_03.png"
    pause.3
    "03_hp/animation/rum_02.png"
    pause.3
    repeat



### Harry Potter DUEL ANIMATIONS ###

image smoke:
    "03_hp/08_animation_02/smoke_01.png"
    pause.1
    "03_hp/08_animation_02/smoke_02.png"
    pause.1
    "03_hp/08_animation_02/smoke_03.png"
    pause.1
    "03_hp/08_animation_02/smoke_04.png"
    pause.1

image ch_sna duel_01:
    "03_hp/04_duel/snape_01.png"
    pause.1
    "03_hp/04_duel/snape_02.png"
    pause.1
    "03_hp/04_duel/snape_03.png"
    pause.1
    "03_hp/04_duel/snape_02.png"
    pause.1
    repeat


image ch_phoenix duel_01:
    "new/duel/true_fen2.png"
    
    #repeat


image ch_gen duel_01:
    "03_hp/04_duel/gen_01.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    "03_hp/04_duel/gen_03.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    repeat

image ch_gen_my:
    "03_hp/04_duel/gen_01.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    "03_hp/04_duel/gen_03.png"
    pause.1
    "03_hp/04_duel/gen_02.png"
    pause.1
    repeat


image ch_gen guard:
    "03_hp/04_duel/guard_01.png"
    pause.1
    "03_hp/04_duel/guard_02.png"
    pause.1
    "03_hp/04_duel/guard_03.png"
    pause.1
    "03_hp/04_duel/guard_02.png"
    pause.1
    repeat

image ch_gen barb:
    "03_hp/04_duel/barb_01.png"
    pause.15
    "03_hp/04_duel/barb_02.png"
    pause.15
    repeat

image ogn1:
    "f/kr3.png"
    pause 0.3
    "f/kr2.png"
    pause 0.3
    "f/kr1.png"
    pause 0.3
    "f/kr.png"
    pause 90.0

image ogn2:
    "f/kr.png"
    pause 0.3
    "f/kr1.png"
    pause 0.3
    "f/kr2.png"
    pause 0.3
    "f/kr3.png"
    pause 0.3

image ogn_2:
    "f/he1.png"
    pause 2.0
    "f/he2.png"
    pause 0.3
    "f/he3.png"
    pause 0.3
    "f/he4.png"
    pause 0.3
    "f/he5.png"
    pause 0.3
    repeat

image ogn_3:
    "f/he6.png"
    pause 0.4
    "f/he7.png"
    pause 0.4
    repeat

image ogn_4:
    "f/he8.png"
    pause 0.4
    "f/he9.png"
    pause 0.4
    repeat

image phoenix_attack:
    "new/duel/fen_casting1.png"
    pause.1
    "new/duel/fen_casting2.png"
    pause.1
    "new/duel/fen_casting3.png"
    pause.1
    "new/duel/fen_casting4.png"
    pause.1
    "new/duel/fen_casting5.png"
    pause.1
    "new/duel/fen_casting6.png"
    pause.1
    "new/duel/fen_casting7.png"
    pause.1
    "new/duel/fen_casting8.png"
    pause.1
    "new/duel/fen_casting9.png"
    pause.5
    "new/duel/fen_casting10.png"
    pause.4
    "new/duel/fen_casting9.png"
    pause.9
    


image dooms_gool:
    "new/stad3.png"
    pause 1.0
    "new/stad4.png"
    pause 2.0
    #"new/stad2.png"

image hogw_gool:
    "new/stad5.png"
    pause 1.0
    "new/stad6.png"
    pause 2.0
    "new/stad2.png"

image phoenix_attack_guard:
    "new/duel/sna_attack_guard_01.png"
    pause.1
    "new/duel/sna_attack_guard_02.png"
    pause.1
    "new/duel/sna_attack_guard_03.png"
    pause.1
    "new/duel/sna_attack_guard_04.png"
    pause.1
    "new/duel/sna_attack_guard_05.png"
    pause.1
    "new/duel/sna_attack_guard_06.png"
    pause.1
    "new/duel/sna_attack_guard_07.png"
    pause.1
    "new/duel/sna_attack_guard_08.png"
    pause.1
    "new/duel/sna_attack_guard_09.png"
    pause.5
    "new/duel/sna_attack_guard_10.png"
    pause.4
    "new/duel/sna_attack_guard_09.png"
    pause.9





image ch_sna defend:
    "03_hp/04_duel/snape_defend_01.png"
    pause.1
    "03_hp/04_duel/snape_defend_02.png"
    pause.1
    "03_hp/04_duel/snape_defend_03.png"
    pause.1
    "03_hp/04_duel/snape_defend_02.png"
    pause.1
    repeat

image snape_attack:
    "03_hp/04_duel/sna_attack_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_10.png"
    pause.08
    repeat

image snape_attack1:
    "03_hp/04_duel/sna_attack_011.png"
    pause.08
    "03_hp/04_duel/sna_attack_021.png"
    pause.08
    "03_hp/04_duel/sna_attack_031.png"
    pause.08
    "03_hp/04_duel/sna_attack_041.png"
    pause.08
    "03_hp/04_duel/sna_attack_031.png"
    pause.08
    "03_hp/04_duel/sna_attack_021.png"
    pause.08
    "03_hp/04_duel/sna_attack_011.png"
    pause.08
    "03_hp/04_duel/sna_attack_041.png"
    pause.08
    "03_hp/04_duel/sna_attack_101.png"
    pause.08


image snape_attack_guard:
    "03_hp/04_duel/sna_attack_guard_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_10.png"
    pause.08
    repeat

image snape_attack_guard: # CREDITS VERSION, with a longer pause.
    "03_hp/04_duel/sna_attack_guard_01.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_02.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_03.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_04.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_05.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_06.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_07.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_08.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_09.png"
    pause.08
    "03_hp/04_duel/sna_attack_guard_10.png"
    pause.5
    repeat

image genie_attack:
    "03_hp/04_duel/genie_attack_01.png"
    pause.15
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_01.png"
    pause.15
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_01.png"
    pause.15
    "03_hp/04_duel/genie_attack_02.png"
    pause.15
    "03_hp/04_duel/genie_attack_03.png"
    pause.15
    "03_hp/04_duel/genie_attack_04.png"
    pause.15
    "03_hp/04_duel/genie_attack_05.png"
    pause.15
    "03_hp/04_duel/genie_attack_06.png"
    pause.15
    "03_hp/04_duel/genie_attack_07.png"
    pause.15
    "03_hp/04_duel/genie_attack_08.png"
    pause.15
    "03_hp/04_duel/genie_attack_09.png"
    pause.15
    "03_hp/04_duel/genie_attack_10.png"
    pause.15
    "03_hp/04_duel/genie_attack_11.png"
    pause.15
    "03_hp/04_duel/genie_attack_12.png"
    pause.15
    "03_hp/04_duel/genie_attack_13.png"
    pause.15
    "03_hp/04_duel/genie_attack_14.png"
    pause.15
    "03_hp/04_duel/genie_attack_15.png"
    pause.15
    "03_hp/04_duel/genie_attack_14.png"
    pause.15
    "03_hp/04_duel/genie_attack_15.png"
    pause.15
    repeat


image genie_attack_ph:
    "new/duel/genie_attack_01.png"
    pause.15
    "new/duel/genie_attack_02.png"
    pause.15
    "new/duel/genie_attack_01.png"
    pause.15
    "new/duel/genie_attack_02.png"
    pause.15
    "new/duel/genie_attack_01.png"
    pause.15
    "new/duel/genie_attack_02.png"
    pause.15
    "new/duel/genie_attack_03.png"
    pause.15
    "new/duel/genie_attack_04.png"
    pause.15
    "new/duel/genie_attack_05.png"
    pause.15
    "new/duel/genie_attack_06.png"
    pause.15
    "new/duel/genie_attack_07.png"
    pause.15
    "new/duel/genie_attack_08.png"
    pause.15
    "new/duel/genie_attack_09.png"
    pause.15
    "new/duel/genie_attack_10.png"
    pause.15
    "new/duel/genie_attack_11.png"
    pause.15
    "new/duel/genie_attack_12.png"
    pause.15
    "new/duel/genie_attack_13.png"
    pause.15
    "new/duel/genie_attack_14.png"
    pause.15
    "new/duel/genie_attack_15.png"
    pause.15
    "new/duel/genie_attack_14.png"
    pause.15
    "new/duel/genie_attack_15.png"
    pause.15
    repeat

image snape_defend: #Snape is in defense stance. Barbarian throws axes at him.
    "03_hp/04_duel/sna_block_01.png"
    pause.15
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_01.png"
    pause.15
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_01.png"
    pause.15
    "03_hp/04_duel/sna_block_02.png"
    pause.15
    "03_hp/04_duel/sna_block_03.png"
    pause.15
    "03_hp/04_duel/sna_block_04.png"
    pause.15
    "03_hp/04_duel/sna_block_05.png"
    pause.15
    "03_hp/04_duel/sna_block_06.png"
    pause.15
    "03_hp/04_duel/sna_block_07.png"
    pause.15
    "03_hp/04_duel/sna_block_08.png"
    pause.15
    "03_hp/04_duel/sna_block_09.png"
    pause.15
    "03_hp/04_duel/sna_block_10.png"
    pause.15
    "03_hp/04_duel/sna_block_11.png"
    pause.15
    "03_hp/04_duel/sna_block_12.png"
    pause.15
    "03_hp/04_duel/sna_block_13.png"
    pause.15
    repeat


image pentogram:
    "03_hp/04_duel/pen_05.png"
    pause.1
    "03_hp/04_duel/pen_04.png"
    pause.1
    "03_hp/04_duel/pen_03.png"
    pause.1
    "03_hp/04_duel/pen_02.png"
    pause.1
    "03_hp/04_duel/pen_01.png"
    pause.1
    "03_hp/04_duel/pen_02.png"
    pause.1
    "03_hp/04_duel/pen_03.png"
    pause.1
    "03_hp/04_duel/pen_04.png"
    pause.1
    "03_hp/04_duel/pen_05.png"
    pause.1
    repeat

image hand: #Hand appears.
    "03_hp/04_duel/hand_01.png"
    pause.1
    "03_hp/04_duel/hand_02.png"
    pause.1
    "03_hp/04_duel/hand_03.png"
    pause.1
    "03_hp/04_duel/hand_04.png"
    pause.1
    "03_hp/04_duel/hand_05.png"
    pause.1
    "03_hp/04_duel/hand_06.png"
    pause.1
    "03_hp/04_duel/hand_07.png"
    pause.1
    "03_hp/04_duel/hand_08.png"
    pause.1
    "03_hp/04_duel/hand_09.png"
    pause.1
    "03_hp/04_duel/hand_10.png"
    pause.1
    "03_hp/04_duel/hand_11.png"
    pause.1
    "03_hp/04_duel/hand_12.png"
    pause.1
    "03_hp/04_duel/hand_13.png"
    pause.1
    "03_hp/04_duel/hand_14.png"
    pause.1
    "03_hp/04_duel/hand_15.png"
    pause.1
    "03_hp/04_duel/hand_16.png"
    pause.1
    repeat

image hand_genie: #Hand attacks Genie.
    "03_hp/04_duel/hand_genie_01.png"
    pause.1
    "03_hp/04_duel/hand_genie_02.png"
    pause.1
    "03_hp/04_duel/hand_genie_03.png"
    pause.1
    "03_hp/04_duel/hand_genie_04.png"
    pause.1
    "03_hp/04_duel/hand_genie_05.png"
    pause.1
    "03_hp/04_duel/hand_genie_06.png"
    pause.1
    "03_hp/04_duel/hand_genie_07.png"
    pause.1
    "03_hp/04_duel/hand_genie_08.png"
    pause.1
    "03_hp/04_duel/hand_genie_09.png"
    pause.1
    "03_hp/04_duel/hand_genie_10.png"
    pause.1
    "03_hp/04_duel/hand_genie_11.png"
    pause.1
    "03_hp/04_duel/hand_genie_12.png"
    pause.1
    "03_hp/04_duel/hand_genie_13.png"
    pause.1


image hand_guard: #Hand attacks the guard.
    "03_hp/04_duel/hand_guard_01.png"
    pause.1
    "03_hp/04_duel/hand_guard_02.png"
    pause.1
    "03_hp/04_duel/hand_guard_03.png"
    pause.1
    "03_hp/04_duel/hand_guard_04.png"
    pause.1
    "03_hp/04_duel/hand_guard_05.png"
    pause.1
    "03_hp/04_duel/hand_guard_06.png"
    pause.1
    "03_hp/04_duel/hand_guard_07.png"
    pause.1
    "03_hp/04_duel/hand_guard_08.png"
    pause.1
    "03_hp/04_duel/hand_guard_09.png"
    pause.1
    "03_hp/04_duel/hand_guard_10.png"
    pause.1
    "03_hp/04_duel/hand_guard_11.png"
    pause.1
    "03_hp/04_duel/hand_guard_12.png"
    pause.1
    "03_hp/04_duel/hand_guard_13.png"
    pause.1
    "03_hp/04_duel/hand_guard_14.png"
    pause.1
    "03_hp/04_duel/hand_guard_11.png"
    pause.1
    "03_hp/04_duel/hand_guard_12.png"
    pause.1
    "03_hp/04_duel/hand_guard_13.png"
    pause.1





### DAMAGE ###

image minus_50:
    "03_hp/14_damage/50_01.png"
    pause.2
    "03_hp/14_damage/50_02.png"
    pause.2
    "03_hp/14_damage/50_03.png"
    pause.2
    "03_hp/14_damage/50_04.png"
    pause.2
    "03_hp/14_damage/50_05.png"
    pause.2
    "03_hp/14_damage/50_06.png"
    pause.2
    "03_hp/14_damage/50_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2


image minus_100: #Hand attacks the guard.
    "03_hp/14_damage/100_01.png"
    pause.2
    "03_hp/14_damage/100_02.png"
    pause.2
    "03_hp/14_damage/100_03.png"
    pause.2
    "03_hp/14_damage/100_04.png"
    pause.2
    "03_hp/14_damage/100_05.png"
    pause.2
    "03_hp/14_damage/100_06.png"
    pause.2
    "03_hp/14_damage/100_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2

image minus_300:
    "03_hp/14_damage/300_01.png"
    pause.2
    "03_hp/14_damage/300_02.png"
    pause.2
    "03_hp/14_damage/300_03.png"
    pause.2
    "03_hp/14_damage/300_04.png"
    pause.2
    "03_hp/14_damage/300_05.png"
    pause.2
    "03_hp/14_damage/300_06.png"
    pause.2
    "03_hp/14_damage/300_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2

image plus_300:
    "03_hp/14_damage/plus_300_01.png"
    pause.2
    "03_hp/14_damage/plus_300_02.png"
    pause.2
    "03_hp/14_damage/plus_300_03.png"
    pause.2
    "03_hp/14_damage/plus_300_04.png"
    pause.2
    "03_hp/14_damage/plus_300_05.png"
    pause.2
    "03_hp/14_damage/plus_300_06.png"
    pause.2
    "03_hp/14_damage/plus_300_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2


image minus_400: #Hand attacks the guard.
    "03_hp/14_damage/400_01.png"
    pause.2
    "03_hp/14_damage/400_02.png"
    pause.2
    "03_hp/14_damage/400_03.png"
    pause.2
    "03_hp/14_damage/400_04.png"
    pause.2
    "03_hp/14_damage/400_05.png"
    pause.2
    "03_hp/14_damage/400_06.png"
    pause.2
    "03_hp/14_damage/400_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2

image minus_500: #Hand attacks the guard.
    "03_hp/14_damage/500_01.png"
    pause.2
    "03_hp/14_damage/500_02.png"
    pause.2
    "03_hp/14_damage/500_03.png"
    pause.2
    "03_hp/14_damage/500_04.png"
    pause.2
    "03_hp/14_damage/500_05.png"
    pause.2
    "03_hp/14_damage/500_06.png"
    pause.2
    "03_hp/14_damage/500_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2


image minus_0: #Hand attacks the guard.
    "03_hp/14_damage/0_01.png"
    pause.2
    "03_hp/14_damage/0_02.png"
    pause.2
    "03_hp/14_damage/0_03.png"
    pause.2
    "03_hp/14_damage/0_04.png"
    pause.2
    "03_hp/14_damage/0_05.png"
    pause.2
    "03_hp/14_damage/0_06.png"
    pause.2
    "03_hp/14_damage/0_07.png"
    pause.2
    "03_hp/14_damage/00.png"
    pause.2



### HARRY POTTER EMOTICONS ANIMATIONS ###

image newanimation2 = Animation("03_hp/05_props/12_genie_01.png", 0.25,
                            "03_hp/05_props/11_genie_02.png", 0.25)



image newanimation:
    "03_hp/05_props/12_genie_01.png"
    pause.1
    "03_hp/05_props/12_genie_02.png"
    pause.1
    "03_hp/05_props/12_genie_03.png"
    pause.1
    "03_hp/05_props/12_genie_02.png"
    pause.1
    "03_hp/05_props/12_genie_01.png"
    pause 5
    "03_hp/05_props/12_genie_01.png"
    pause.15
    "03_hp/05_props/12_genie_04.png"
    pause.15
    "03_hp/05_props/12_genie_01.png"
    pause.15
    "03_hp/05_props/12_genie_04.png"
    pause.15
    "03_hp/05_props/12_genie_01.png"
    pause 6
    repeat

image exclaim_01: #Exclamation mark.
    "03_hp/06_emo/exlaim_01.png"
    pause.1
    "03_hp/06_emo/exlaim_02.png"
    pause.1
    "03_hp/06_emo/exlaim_03.png"
    pause.1
    "03_hp/06_emo/exlaim_04.png"
    pause.1
    "03_hp/06_emo/exlaim_03.png"
    pause 2
    "03_hp/06_emo/exlaim_05.png"
    pause.08
    "03_hp/06_emo/exlaim_06.png"
    pause.08
    "03_hp/06_emo/exlaim_07.png"

image sad_01: #SAD SMILEY USED WHEN PETTING PHOENIX.
    "03_hp/06_emo/exlaim_01.png"
    pause.1
    "03_hp/06_emo/sad_01.png"
    pause.1
    "03_hp/06_emo/sad_02.png"
    pause.1
    "03_hp/06_emo/sad_03.png"
    pause 1
    "03_hp/06_emo/sad_04.png"
    pause.1
    "03_hp/06_emo/sad_03.png"
    pause.1
    "03_hp/06_emo/sad_04.png"
    pause.1
    "03_hp/06_emo/sad_03.png"
    pause 3
    "03_hp/06_emo/sad_02.png"
    pause.1
    "03_hp/06_emo/sad_01.png"
    pause.1
    "03_hp/06_emo/exlaim_07.png"

image hoot: #OWL'S "HOOT!".
    "03_hp/06_emo/hoot_01.png"
    pause.07
    "03_hp/06_emo/hoot_02.png"
    pause.07
    "03_hp/06_emo/hoot_03.png"
    pause.07
    "03_hp/06_emo/hoot_04.png"
    pause.07
    "03_hp/06_emo/hoot_05.png"
    pause.07
    "03_hp/06_emo/hoot_06.png"
    pause.07
    "03_hp/06_emo/hoot_07.png"
    pause 3
    "03_hp/06_emo/exlaim_07.png"

image notes: #A bunch of notes poping out with a "win" sound effect.
    "03_hp/08_animation_02/notes_01.png"
    pause.08
    "03_hp/08_animation_02/notes_02.png"
    pause.08
    "03_hp/08_animation_02/notes_03.png"
    pause.08
    "03_hp/08_animation_02/notes_04.png"
    pause.08
    "03_hp/08_animation_02/notes_05.png"
    pause.08
    "03_hp/08_animation_02/notes_06.png"
    pause.08
    "03_hp/08_animation_02/notes_07.png"
    pause.08
    "03_hp/08_animation_02/notes_08.png"
    pause.08
    "03_hp/08_animation_02/notes_09.png"
    pause.08

image thought: #Thinking emotion over a chibi.
    "03_hp/06_emo/thought_02.png"
    pause.5
    "03_hp/06_emo/thought_01.png"
    pause.5
    repeat





### ADDING HOUSE POINTS ###
image ass_03_points:
    "03_hp/11_misc/03_points.png"
    pause 3
    "03_hp/11_misc/03_points_75.png"
    pause.08
    "03_hp/11_misc/03_points_50.png"
    pause.08
    "03_hp/11_misc/03_points_25.png"
    pause.08
    "03_hp/11_misc/points_00.png"

image what_01_points:
    "03_hp/11_misc/01_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/01_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/01_points.png", 0.0)

image what_02_points:
    "03_hp/11_misc/02_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/02_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/02_points.png", 0.0)

image what_03_points:
    "03_hp/11_misc/03_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/03_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/03_points.png", 0.0)

image what_04_points:   #<============================================== 4 POINTS
    "03_hp/11_misc/04.png"
    pause 3
    im.Alpha("03_hp/11_misc/04.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/04.png", 0.0)

image what_05_points: # <================================================ 5 POINTS
    "03_hp/11_misc/05_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/05_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/05_points.png", 0.0)

image what_06_points: # <================================================ 6 POINTS
    "03_hp/11_misc/06.png"
    pause 3
    im.Alpha("03_hp/11_misc/06.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/06.png", 0.0)


image what_07_points: # <================================================ 7 POINTS
    "03_hp/11_misc/07.png"
    pause 3
    im.Alpha("03_hp/11_misc/07.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/07.png", 0.0)

image what_08_points: # <================================================ 8 POINTS
    "03_hp/11_misc/08.png"
    pause 3
    im.Alpha("03_hp/11_misc/08.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/08.png", 0.0)

image what_09_points: # <================================================ 9 POINTS
    "03_hp/11_misc/09.png"
    pause 3
    im.Alpha("03_hp/11_misc/09.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/09.png", 0.0)

image what_10_points: # <================================================ 10 POINTS
    "03_hp/11_misc/10.png"
    pause 3
    im.Alpha("03_hp/11_misc/10.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/10.png", 0.0)

image what_11_points: # <================================================ 11 POINTS
    "03_hp/11_misc/11.png"
    pause 3
    im.Alpha("03_hp/11_misc/11.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/11.png", 0.0)

image what_12_points: # <================================================ 12 POINTS
    "03_hp/11_misc/12.png"
    pause 3
    im.Alpha("03_hp/11_misc/12.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/12.png", 0.0)

image what_13_points: # <================================================ 13 POINTS
    "03_hp/11_misc/13.png"
    pause 3
    im.Alpha("03_hp/11_misc/13.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/13.png", 0.0)

image what_14_points: # <================================================ 14 POINTS
    "03_hp/11_misc/14.png"
    pause 3
    im.Alpha("03_hp/11_misc/14.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/14.png", 0.0)

image what_15_points: # <================================================ 15 POINTS
    "03_hp/11_misc/15_points.png"
    pause 3
    im.Alpha("03_hp/11_misc/15_points.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/15_points.png", 0.0)

image what_16_points: # <================================================ 16 POINTS
    "03_hp/11_misc/16.png"
    pause 3
    im.Alpha("03_hp/11_misc/16.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/16.png", 0.0)

image what_17_points: # <================================================ 17 POINTS
    "03_hp/11_misc/17.png"
    pause 3
    im.Alpha("03_hp/11_misc/17.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/17.png", 0.0)

image what_18_points: # <================================================ 18 POINTS
    "03_hp/11_misc/18.png"
    pause 3
    im.Alpha("03_hp/11_misc/18.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/18.png", 0.0)

image what_19_points: # <================================================ 19 POINTS
    "03_hp/11_misc/19.png"
    pause 3
    im.Alpha("03_hp/11_misc/19.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.0)

image what_19_points: # <================================================ 19 POINTS
    "03_hp/11_misc/19.png"
    pause 3
    im.Alpha("03_hp/11_misc/19.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/19.png", 0.0)

image what_20_points: # <================================================ 20 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/20.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/20.png", 0.0)

image what_21_points: # <================================================ 21 POINTS
    "03_hp/11_misc/21.png"
    pause 3
    im.Alpha("03_hp/11_misc/21.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/21.png", 0.0)

image what_22_points: # <================================================ 22 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/22.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/22.png", 0.0)

image what_23_points: # <================================================ 23 POINTS
    "03_hp/11_misc/23.png"
    pause 3
    im.Alpha("03_hp/11_misc/23.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/23.png", 0.0)

image what_24_points: # <================================================ 24 POINTS
    "03_hp/11_misc/24.png"
    pause 3
    im.Alpha("03_hp/11_misc/24.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/24.png", 0.0)

image what_25_points: # <================================================ 25 POINTS
    "03_hp/11_misc/25.png"
    pause 3
    im.Alpha("03_hp/11_misc/25.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/25.png", 0.0)

image what_26_points: # <================================================ 26 POINTS
    "03_hp/11_misc/26.png"
    pause 3
    im.Alpha("03_hp/11_misc/26.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/26.png", 0.0)

image what_27_points: # <================================================ 27 POINTS
    "03_hp/11_misc/27.png"
    pause 3
    im.Alpha("03_hp/11_misc/27.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/27.png", 0.0)

image what_28_points: # <================================================ 28 POINTS
    "03_hp/11_misc/28.png"
    pause 3
    im.Alpha("03_hp/11_misc/28.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/28.png", 0.0)

image what_29_points: # <================================================ 29 POINTS
    "03_hp/11_misc/20.png"
    pause 3
    im.Alpha("03_hp/11_misc/29.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/29.png", 0.0)

image what_30_points: # <================================================ 30 POINTS
    "03_hp/11_misc/30.png"
    pause 3
    im.Alpha("03_hp/11_misc/30.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/30.png", 0.0)

image what_31_points: # <================================================ 31 POINTS
    "03_hp/11_misc/31.png"
    pause 3
    im.Alpha("03_hp/11_misc/31.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/31.png", 0.0)

image what_32_points: # <================================================ 32 POINTS
    "03_hp/11_misc/32.png"
    pause 3
    im.Alpha("03_hp/11_misc/32.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/32.png", 0.0)

image what_33_points: # <================================================ 33 POINTS
    "03_hp/11_misc/33.png"
    pause 3
    im.Alpha("03_hp/11_misc/33.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/33.png", 0.0)

image what_34_points: # <================================================ 34 POINTS
    "03_hp/11_misc/34.png"
    pause 3
    im.Alpha("03_hp/11_misc/34.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/34.png", 0.0)

image what_35_points: # <================================================ 35 POINTS
    "03_hp/11_misc/35.png"
    pause 3
    im.Alpha("03_hp/11_misc/35.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/35.png", 0.0)

image what_36_points: # <================================================ 36 POINTS
    "03_hp/11_misc/36.png"
    pause 3
    im.Alpha("03_hp/11_misc/36.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/36.png", 0.0)

image what_37_points: # <================================================ 37 POINTS
    "03_hp/11_misc/37.png"
    pause 3
    im.Alpha("03_hp/11_misc/37.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/37.png", 0.0)

image what_38_points: # <================================================ 38 POINTS
    "03_hp/11_misc/38.png"
    pause 3
    im.Alpha("03_hp/11_misc/38.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/38.png", 0.0)

image what_39_points: # <================================================ 39 POINTS
    "03_hp/11_misc/39.png"
    pause 3
    im.Alpha("03_hp/11_misc/39.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/39.png", 0.0)

image what_40_points: # <================================================ 40 POINTS
    "03_hp/11_misc/40.png"
    pause 3
    im.Alpha("03_hp/11_misc/40.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/40.png", 0.0)

image what_41_points: # <================================================ 41 POINTS
    "03_hp/11_misc/41.png"
    pause 3
    im.Alpha("03_hp/11_misc/41.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/41.png", 0.0)

image what_42_points: # <================================================ 42 POINTS
    "03_hp/11_misc/42.png"
    pause 3
    im.Alpha("03_hp/11_misc/42.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/42.png", 0.0)

image what_43_points: # <================================================ 43 POINTS
    "03_hp/11_misc/43.png"
    pause 3
    im.Alpha("03_hp/11_misc/43.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/43.png", 0.0)

image what_44_points: # <================================================ 44 POINTS
    "03_hp/11_misc/44.png"
    pause 3
    im.Alpha("03_hp/11_misc/44.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/44.png", 0.0)

image what_45_points: # <================================================ 45 POINTS
    "03_hp/11_misc/45.png"
    pause 3
    im.Alpha("03_hp/11_misc/45.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/45.png", 0.0)

image what_46_points: # <================================================ 46 POINTS
    "03_hp/11_misc/46.png"
    pause 3
    im.Alpha("03_hp/11_misc/46.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/46.png", 0.0)

image what_47_points: # <================================================ 47 POINTS
    "03_hp/11_misc/47.png"
    pause 3
    im.Alpha("03_hp/11_misc/47.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/47.png", 0.0)

image what_48_points: # <================================================ 48 POINTS
    "03_hp/11_misc/48.png"
    pause 3
    im.Alpha("03_hp/11_misc/48.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/48.png", 0.0)

image what_49_points: # <================================================ 49 POINTS
    "03_hp/11_misc/49.png"
    pause 3
    im.Alpha("03_hp/11_misc/49.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/49.png", 0.0)

image what_50_points: # <================================================ 50 POINTS
    "03_hp/11_misc/50.png"
    pause 3
    im.Alpha("03_hp/11_misc/50.png", 0.75)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.5)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.25)
    pause.08
    im.Alpha("03_hp/11_misc/50.png", 0.0)





#############################################################
image feather_old: #Falling feather.
    "03_hp/animation/pho_22.png"
    pause 10
    "03_hp/animation/pho_01.png"
    pause.15
    "03_hp/animation/pho_02.png"
    pause.15
    "03_hp/animation/pho_03.png"
    pause.15
    "03_hp/animation/pho_04.png"
    pause.15
    "03_hp/animation/pho_05.png"
    pause.15
    "03_hp/animation/pho_06.png"
    pause.15
    "03_hp/animation/pho_07.png"
    pause.15
    "03_hp/animation/pho_08.png"
    pause.15
    "03_hp/animation/pho_09.png"
    pause.15
    "03_hp/animation/pho_10.png"
    pause.15
    "03_hp/animation/pho_11.png"
    pause.15
    "03_hp/animation/pho_12.png"
    pause.15
    "03_hp/animation/pho_13.png"
    pause.15
    "03_hp/animation/pho_14.png"
    pause.15
    "03_hp/animation/pho_15.png"
    pause.15
    "03_hp/animation/pho_16.png"
    pause.15
    "03_hp/animation/pho_17.png"
    pause.15
    "03_hp/animation/pho_18.png"
    pause 10
    "03_hp/animation/pho_19.png"
    pause.1
    "03_hp/animation/pho_20.png"
    pause.1
    "03_hp/animation/pho_21.png"
    pause.1
    "03_hp/animation/pho_22.png"
    pause 20
    repeat

image feather: #Falling feather.
    "03_hp/animation/pho_22.png"
    pause 5
    "03_hp/animation/pho_01.png"
    pause.15
    "03_hp/animation/pho_02.png"
    pause.15
    "03_hp/animation/pho_03.png"
    pause.15
    "03_hp/animation/pho_04.png"
    pause.15
    "03_hp/animation/pho_05.png"
    pause.15
    "03_hp/animation/pho_06.png"
    pause.15
    "03_hp/animation/pho_07.png"
    pause.15
    "03_hp/animation/pho_08.png"
    pause.15
    "03_hp/animation/pho_09.png"
    pause.15
    "03_hp/animation/pho_10.png"
    pause.15
    "03_hp/animation/pho_11.png"
    pause.15
    "03_hp/animation/pho_12.png"
    pause.15
    "03_hp/animation/pho_13.png"
    pause.15
    "03_hp/animation/pho_14.png"
    pause.15
    "03_hp/animation/pho_15.png"
    pause.15
    "03_hp/animation/pho_16.png"
    pause.15
    "03_hp/animation/pho_17.png"
    pause.15
    "03_hp/animation/pho_18.png"
    pause 300
    "03_hp/animation/pho_19.png"
    pause.1
    "03_hp/animation/pho_20.png"
    pause.1
    "03_hp/animation/pho_21.png"
    pause.1
    "03_hp/animation/pho_22.png"
    pause 5
    repeat
    
    

image pho_01: #Phoenix idile animation
    "03_hp/animation/phoenix_01.png"
    pause 2
    "03_hp/animation/phoenix_02.png"
    pause.15
    "03_hp/animation/phoenix_03.png"
    pause.15
    "03_hp/animation/phoenix_02.png"
    pause.15
    "03_hp/animation/phoenix_01.png"
    pause.15
    "03_hp/animation/phoenix_02.png"
    pause.15
    "03_hp/animation/phoenix_03.png"
    pause.15
    "03_hp/animation/phoenix_02.png"
    pause.15
    "03_hp/animation/phoenix_01.png"
    pause 10
    repeat

image paperwork_02: #Genie working behind his desk.
    "03_hp/animation/working_01.png"
    pause.15
    "03_hp/animation/working_02.png"
    pause.15
    "03_hp/animation/working_01.png"
    pause.15
    "03_hp/animation/working_02.png"
    pause.15
    "03_hp/animation/working_01.png"
    pause.15
    "03_hp/animation/working_02.png"
    pause 1
    "03_hp/animation/working_03.png"
    pause.15
    "03_hp/animation/working_04.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause.15
    "03_hp/animation/working_05.png"
    pause.15
    "03_hp/animation/working_06.png"
    pause 1
    "03_hp/animation/working_07.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_09.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_07.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_09.png"
    pause.15
    "03_hp/animation/working_08.png"
    pause.15
    "03_hp/animation/working_03.png"
    pause.15
    "03_hp/animation/working_02.png"
    pause.15
    repeat

image reading: #Genie reading.
    im.Flip("03_hp/animation/reading_01.png", horizontal=True)
    pause 2
    im.Flip("03_hp/animation/reading_06.png", horizontal=True)
    pause.15
    im.Flip("03_hp/animation/reading_05.png", horizontal=True)
    pause.15
    im.Flip("03_hp/animation/reading_04.png", horizontal=True)
    pause.15
    im.Flip("03_hp/animation/reading_03.png", horizontal=True)
    pause.15
    im.Flip("03_hp/animation/reading_02.png", horizontal=True)
    pause.15
    im.Flip("03_hp/animation/reading_01.png", horizontal=True)
    pause 2
    repeat


image reading_near_fire: #Genie reading near the fireplace.
    "03_hp/animation/reading_01.png"
    pause 2
    "03_hp/animation/reading_06.png"
    pause.15
    "03_hp/animation/reading_05.png"
    pause.15
    "03_hp/animation/reading_04.png"
    pause.15
    "03_hp/animation/reading_03.png"
    pause.15
    "03_hp/animation/reading_02.png"
    pause.15
    "03_hp/animation/reading_01.png"
    pause 2
    repeat

image genie_jerking_off: #Genie sitting behind his desk and jerking off...
    "03_hp/animation/jerking_off_01.png"
    pause.2
    "03_hp/animation/jerking_off_02.png"
    pause.2
    "03_hp/animation/jerking_off_03.png"
    pause.2
    "03_hp/animation/jerking_off_02.png"
    pause.2
    repeat

image genie_jerking_sperm_ani: #Sperm after jerking off.
    "03_hp/animation/jerking_sperm_01.png"
    pause.1
    "03_hp/animation/jerking_sperm_02.png"
    pause.1
    "03_hp/animation/jerking_sperm_03.png"
    pause.1
    "03_hp/animation/jerking_sperm_04.png"
    pause.1
    "03_hp/animation/jerking_sperm_05.png"
    pause.1
    "03_hp/animation/jerking_sperm_06.png"
    pause.1
    "03_hp/animation/jerking_sperm_07.png"
    pause.1
    "03_hp/animation/jerking_sperm_08.png"
    pause.1
    "03_hp/animation/jerking_sperm_09.png"
    pause.1
    "03_hp/animation/jerking_sperm_10.png"
    pause.1
    "03_hp/animation/jerking_sperm_11.png"
    pause 2
    repeat

### FAVORS ###
### GROPINGS ###
image groping_01: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/grope_01.png"
    pause.2
    "03_hp/animation/grope_02.png"
    pause.2
    "03_hp/animation/grope_03.png"
    pause.5
    "03_hp/animation/grope_02.png"
    pause.2
    "03_hp/animation/grope_01.png"
    pause.2
    repeat

image groping_02: #Genie groping Hermione under her skirt. Hermione's behind is facing Genie.
    "03_hp/animation/grope_b_01.png"
    pause.2
    "03_hp/animation/grope_b_02.png"
    pause.2
    "03_hp/animation/grope_b_03.png"
    pause.5
    "03_hp/animation/grope_b_02.png"
    pause.2
    "03_hp/animation/grope_b_01.png"
    pause.2
    repeat


image groping_01_blinking: #Animation of Hermione blinking her eyes.
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    repeat

image groping_02_blinking: #Animation of Hermione blinking her eyes.
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause.1
    "03_hp/animation/grope_b_04.png"
    pause.1
    "03_hp/animation/00.png"
    pause 3
    repeat

### GROPING TITS FULLY CLOTHED ###
image groping_03_ani: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/molest_01.png"
    pause.2
    "03_hp/animation/molest_02.png"
    pause.2
    "03_hp/animation/molest_03.png"
    pause.2
    "03_hp/animation/molest_04.png"
    pause.2
    "03_hp/animation/molest_05.png"
    pause.2
    "03_hp/animation/molest_06.png"
    pause.2
    "03_hp/animation/molest_07.png"
    pause.2
    "03_hp/animation/molest_08.png"
    pause.2
    repeat

### GROPING NAKED TITS ###
image groping_naked_tits_ani: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "03_hp/animation/tit_molester_naked_01.png"
    pause.2
    "03_hp/animation/tit_molester_naked_02.png"
    pause.2
    "03_hp/animation/tit_molester_naked_03.png"
    pause.2
    "03_hp/animation/tit_molester_naked_04.png"
    pause.2
    "03_hp/animation/tit_molester_naked_05.png"
    pause.2
    "03_hp/animation/tit_molester_naked_06.png"
    pause.2
    "03_hp/animation/tit_molester_naked_07.png"
    pause.2
    "03_hp/animation/tit_molester_naked_08.png"
    pause.2
    repeat


### JERKING OFF ###
image jerking_off_ani: #Genie jerking off in front of topless Hermione.
    "03_hp/animation/07_jerking_off_01.png"
    pause.2
    "03_hp/animation/07_jerking_off_02.png"
    pause.2
    "03_hp/animation/07_jerking_off_03.png"
    pause.2
    "03_hp/animation/07_jerking_off_04.png"
    pause.2
    repeat

image jerking_off_02_ani: #Genie jerking off in front of dancing on a desk Hermione. (Difference is that the dick is aimed higher.)
    "03_hp/08_animation_02/06_jerking_01.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_02.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_03.png"
    pause.2
    "03_hp/08_animation_02/06_jerking_04.png"
    pause.2
    repeat

image jerking_off_03_ani: #SNape jerking off in front of dancing on a desk Hermione.
    "03_hp/08_animation_02/10_jerking_01.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_02.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_03.png"
    pause.2
    "03_hp/08_animation_02/10_jerking_04.png"
    pause.2
    repeat

### CUM ###
image jerking_off_cum_ani: #Sperm.
    "03_hp/animation/08_cum_01.png"
    pause.1
    "03_hp/animation/08_cum_02.png"
    pause.1
    "03_hp/animation/08_cum_03.png"
    pause.1
    "03_hp/animation/08_cum_04.png"
    pause.1
    "03_hp/animation/08_cum_05.png"
    pause.1
    "03_hp/animation/08_cum_06.png"
    pause.1
    "03_hp/animation/08_cum_07.png"
    pause.1
    "03_hp/animation/08_cum_08.png"
    pause.1
    "03_hp/animation/08_cum_09.png"
    pause.1
    "03_hp/animation/08_cum_10.png"
    pause.1
    "03_hp/animation/08_cum_11.png"
    pause.1
    "03_hp/animation/08_cum_12.png"
    pause.1
    "03_hp/animation/08_cum_13.png"
    pause 3
    "03_hp/animation/08_cum_14.png"
    pause.1
    "03_hp/animation/08_cum_15.png"
    pause.1
    "03_hp/animation/08_cum_16.png"
    pause.1
    repeat

### CUM_02 ###
image genie_cum_03: #Genie cuming on Hermione after she is done striping.
    "03_hp/08_animation_02/09_cum_01.png"
    pause.1
    "03_hp/08_animation_02/09_cum_02.png"
    pause.1
    "03_hp/08_animation_02/09_cum_03.png"
    pause.1
    "03_hp/08_animation_02/09_cum_04.png"
    pause.1
    "03_hp/08_animation_02/09_cum_05.png"
    pause.1
    "03_hp/08_animation_02/09_cum_06.png"
    pause.1
    "03_hp/08_animation_02/09_cum_07.png"
    pause.1
    "03_hp/08_animation_02/09_cum_08.png"
    pause.1
    "03_hp/08_animation_02/09_cum_09.png"
    pause.1
    "03_hp/08_animation_02/09_cum_10.png"
    pause.1
    "03_hp/08_animation_02/09_cum_11.png"
    pause.1
    "03_hp/08_animation_02/09_cum_12.png"
    pause.1
    "03_hp/08_animation_02/09_cum_13.png"
    pause.1
    "03_hp/08_animation_02/09_cum_14.png"
    pause.1
    "03_hp/08_animation_02/09_cum_15.png"
    pause.1
    "03_hp/08_animation_02/09_cum_16.png"
    pause.1
    "03_hp/08_animation_02/09_cum_17.png"
    pause.1
    "03_hp/08_animation_02/09_cum_18.png"
    pause 2
    "03_hp/08_animation_02/09_cum_19.png"
    pause.1
    "03_hp/08_animation_02/09_cum_20.png"
    pause.1
    "03_hp/08_animation_02/00.png"
    pause.5
    repeat

### CUM_03 ###
image snape_cum_01: #Snape cumming on Hermione after she is done striping.
    "03_hp/08_animation_02/11_cum_01.png"
    pause.1
    "03_hp/08_animation_02/11_cum_02.png"
    pause.1
    "03_hp/08_animation_02/11_cum_03.png"
    pause.1
    "03_hp/08_animation_02/11_cum_04.png"
    pause.1
    "03_hp/08_animation_02/11_cum_05.png"
    pause.1
    "03_hp/08_animation_02/11_cum_06.png"
    pause.1
    "03_hp/08_animation_02/11_cum_07.png"
    pause.1
    "03_hp/08_animation_02/11_cum_08.png"
    pause.1
    "03_hp/08_animation_02/11_cum_09.png"
    pause.1
    "03_hp/08_animation_02/11_cum_10.png"
    pause.1
    "03_hp/08_animation_02/11_cum_11.png"
    pause.1
    "03_hp/08_animation_02/11_cum_12.png"
    pause.1
    "03_hp/08_animation_02/11_cum_13.png"
    pause.1
    "03_hp/08_animation_02/11_cum_14.png"
    pause.1
    "03_hp/08_animation_02/11_cum_15.png"
    pause.1
    "03_hp/08_animation_02/11_cum_16.png"
    pause.1
    "03_hp/08_animation_02/11_cum_17.png"
    pause.1
    "03_hp/08_animation_02/11_cum_18.png"
    pause 2
    "03_hp/08_animation_02/11_cum_19.png"
    pause.1
    "03_hp/08_animation_02/11_cum_20.png"
    pause.1
    "03_hp/08_animation_02/00.png"
    pause.5
    repeat



### HERMIONE DANCING FULLY CLOTHED ###
image clothed_dance_ani:
    "03_hp/08_animation_02/01_dancing_01.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_02.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_03.png"
    pause.1
    "03_hp/08_animation_02/01_dancing_04.png"
    pause.1
    repeat


### HERMIONE DANCING NO VEST###
image no_vest_dance_ani:
    "03_hp/08_animation_02/02_no_vest_01.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_02.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_03.png"
    pause.1
    "03_hp/08_animation_02/02_no_vest_04.png"
    pause.1
    repeat

### HERMIONE DANCING NO SKIRT###
image no_skirt_dance_ani:
    "03_hp/08_animation_02/04_no_skirt_01.png"
    pause.1
    "03_hp/08_animation_02/04_no_skirt_02.png"
    pause.1
    "03_hp/08_animation_02/04_no_skirt_03.png"
    pause.1
    "03_hp/08_animation_02/04_no_skirt_04.png"
    pause.1
    repeat

### HERMIONE DANCING NO SHIRT###
image no_shirt_dance_ani:
    "03_hp/08_animation_02/03_no_shirt_01.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_02.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_03.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_04.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_05.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_06.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_07.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_08.png"
    pause.1
    "03_hp/08_animation_02/03_no_shirt_09.png"
    pause.1
    repeat

### HERMIONE DANCING NO PANTIES###
image no_panties_dance_ani:
    "03_hp/08_animation_02/07_dance_01.png"
    pause.1
    "03_hp/08_animation_02/07_dance_02.png"
    pause.1
    "03_hp/08_animation_02/07_dance_03.png"
    pause.1
    "03_hp/08_animation_02/07_dance_04.png"
    pause.1
    "03_hp/08_animation_02/07_dance_05.png"
    pause.1
    "03_hp/08_animation_02/07_dance_06.png"
    pause.1
    "03_hp/08_animation_02/07_dance_07.png"
    pause.1
    "03_hp/08_animation_02/07_dance_08.png"
    pause.1
    "03_hp/08_animation_02/07_dance_09.png"
    pause.1
    repeat



### HERMIONE DANCING NO SHIRT NO SKIRT###
image no_shirt_no_skirt_dance_ani:
    "03_hp/08_animation_02/05_panties_01.png"
    pause.1
    "03_hp/08_animation_02/05_panties_02.png"
    pause.1
    "03_hp/08_animation_02/05_panties_03.png"
    pause.1
    "03_hp/08_animation_02/05_panties_04.png"
    pause.1
    "03_hp/08_animation_02/05_panties_05.png"
    pause.1
    "03_hp/08_animation_02/05_panties_06.png"
    pause.1
    "03_hp/08_animation_02/05_panties_07.png"
    pause.1
    "03_hp/08_animation_02/05_panties_08.png"
    pause.1
    "03_hp/08_animation_02/05_panties_09.png"
    pause.1
    repeat


############################
image cho_blowjob:
    "new/chm1.png"
    pause .1
    "new/chm2.png"
    pause .1
    "new/chm3.png"
    pause .1
    "new/chm4.png"
    pause .1
    "new/chm5.png"
    pause .1
    "new/chm6.png"
    pause .1
    "new/chm7.png"
    pause .1
    "new/chm8.png"
    pause .1
    "new/chm9.png"
    pause .1
    "new/chm8.png"
    pause .1
    "new/chm7.png"
    pause .1
    "new/chm6.png"
    pause .1
    "new/chm5.png"
    pause .1
    "new/chm4.png"
    pause .1
    "new/chm3.png"
    pause .1
    "new/chm2.png"
    pause .1
    repeat


image cho_minet2:
    "new/chh1.png"
    pause .1
    "new/chh2.png"
    pause .1
    "new/chh3.png"
    pause .1
    "new/chh4.png"
    pause .1
    "new/chh5.png"
    pause .1
    "new/chh6.png"
    pause .1
    "new/chh7.png"
    pause .1
    "new/chh6.png"
    pause .1
    "new/chh5.png"
    pause .1
    "new/chh4.png"
    pause .1
    "new/chh3.png"
    pause .1
    "new/chh2.png"
    pause .1
    repeat



image cho_sex:
    "f/21_sex_01.png"
    pause .1
    "f/21_sex_02.png"
    pause .1
    "f/21_sex_03.png"
    pause .1
    "f/21_sex_04.png"
    pause .1
    "f/21_sex_05.png"
    pause .1
    "f/21_sex_06.png"
    pause .1
    "f/21_sex_07.png"
    pause .1
    repeat
image cho_sex_cum:
    "f/22_cum_01.png"
    pause .1
    "f/22_cum_02.png"
    pause .1
    "f/22_cum_03.png"
    pause .1
    "f/22_cum_04.png"
    pause .1
    "f/22_cum_05.png"
    pause .1
    "f/22_cum_06.png"
    pause .1
    "f/22_cum_07.png"
    pause .1
    "f/22_cum_08.png"
    pause .1
    "f/22_cum_09.png"
    pause .1
    "f/22_cum_10.png"
    pause .1
    "f/22_cum_11.png"
    pause .1
    "f/22_cum_12.png"
    pause .1
    "f/22_cum_13.png"
    pause .1
    "f/22_cum_14.png"
    pause .1
    "f/22_cum_15.png"
    pause .1
    "f/22_cum_16.png"
    pause .1
    "f/22_cum_17.png"
    pause .1
    "f/22_cum_18.png"
    pause .1
    "f/22_cum_19.png"
    pause .1
    "f/22_cum_20.png"
    pause .1
    "f/22_cum_21.png"
    pause .1
    "f/22_cum_22.png"
    pause .1
    "f/22_cum_23.png"
    pause .1
    "f/22_cum_24.png"
    pause .1




image tripple:
    "new/ch1.png"
    pause .1
    "new/ch2.png"
    pause .1
    "new/ch3.png"
    pause .1
    "new/ch4.png"
    pause .1
    "new/ch5.png"
    pause .1
    "new/ch6.png"
    pause .1
    "new/ch5.png"
    pause .1
    "new/ch4.png"
    pause .1
    "new/ch3.png"
    pause .1
    "new/ch2.png"
    pause .1
    "new/ch1.png"
    pause .1
    "new/ch7.png"
    pause .1
    "new/ch8.png"
    pause .1
    "new/ch9.png"
    pause .1
    "new/ch10.png"
    pause .1
    "new/ch11.png"
    pause .1
    "new/ch10.png"
    pause .1
    "new/ch9.png"
    pause .1
    "new/ch8.png"
    pause .1
    "new/ch7.png"
    pause .1
    repeat

### Daphne porn

image blowjob_daph:
    "da/17_blow_01.png"
    pause.1
    "da/17_blow_02.png"
    pause.1
    "da/17_blow_03.png"
    pause.1
    "da/17_blow_04.png"
    pause.1
    "da/17_blow_05.png"
    pause.1
    "da/17_blow_06.png"
    pause.1
    "da/17_blow_07.png"
    pause.1
    "da/17_blow_08.png"
    pause.1
    "da/17_blow_09.png"
    pause.1
    "da/17_blow_10.png"
    pause.1
    "da/17_blow_11.png"
    pause.1
    "da/17_blow_12.png"
    pause.1
    repeat



image daph_handjob:
    "dap/dap_fap_a5.png"
    pause .4
    "dap/dap_fap_a6.png"
    pause .4
    repeat

image daphne_tits = "dap/dap_tits_a1.png"

image daphne_but:
    "da/but3.png"
    pause.3
    "da/but4.png"
    pause.3
    "da/but5.png"
    pause.3
    "da/but4.png"
    pause.3
    repeat

image dasex_ani:
    "da/21_sex_01.png"
    pause.1
    "da/21_sex_02.png"
    pause.1
    "da/21_sex_03.png"
    pause.1
    "da/21_sex_04.png"
    pause.1
    "da/21_sex_05.png"
    pause.1
    "da/21_sex_06.png"
    pause.1
    "da/21_sex_07.png"
    pause.1
    repeat

### HERMIONE FAST SPEED SEX ###
image dasex2_ani:
    "da/21_sex_01.png"
    pause.05
    "da/21_sex_02.png"
    pause.05
    "da/21_sex_03.png"
    pause.05
    "da/21_sex_04.png"
    pause.05
    "da/21_sex_05.png"
    pause.05
    "da/21_sex_06.png"
    pause.05
    "da/21_sex_07.png"
    pause.05
    repeat



### HERMIONE SEX LOW SPEED ###
image dasex_slow_ani:
    "da/21_sex_01.png"
    pause.15
    "da/21_sex_02.png"
    pause.15
    "da/21_sex_03.png"
    pause.15
    "da/21_sex_04.png"
    pause.15
    "da/21_sex_05.png"
    pause.15
    "da/21_sex_06.png"
    pause.15
    "da/21_sex_07.png"
    pause.15
    repeat

### HERMIONE SEX CUM OUTSIDE ###
image dasex_cum_out_ani:
    "da/22_cum_01.png"
    pause.1
    "da/22_cum_02.png"
    pause.1
    "da/22_cum_03.png"
    pause.1
    "da/22_cum_04.png"
    pause.1
    "da/22_cum_05.png"
    pause.1
    "da/22_cum_06.png"
    pause.1
    "da/22_cum_07.png"
    pause.1
    "da/22_cum_08.png"
    pause.1
    "da/22_cum_09.png"
    pause.1
    "da/22_cum_10.png"
    pause.1
    "da/22_cum_11.png"
    pause.1
    "da/22_cum_12.png"
    pause.1
    "da/22_cum_13.png"
    pause.1
    "da/22_cum_14.png"
    pause.1
    "da/22_cum_15.png"
    pause.1
    "da/22_cum_16.png"
    pause.1
    "da/22_cum_17.png"
    pause.1
    "da/22_cum_18.png"
    pause.1
    "da/22_cum_19.png"
    pause 1
    "da/22_cum_20.png"
    pause.1
    "da/22_cum_21.png"
    pause.1
    "da/22_cum_22.png"
    pause.1
    "da/22_cum_23.png"
    pause 3.0

### HERMIONE SEX CUM OUTSIDE BLINKING###
image dasex_cum_out_blink_ani:
    "da/22_cum_19.png"
    pause 1
    "da/22_cum_24.png" #closed
    pause.1
    "da/22_cum_19.png"
    pause.1
    "da/22_cum_24.png" #closed
    pause.1
    "da/22_cum_19.png"
    pause 2
    "da/22_cum_24.png" #closed
    pause.1
    "da/22_cum_19.png"
    pause 2
    repeat


### Daphne SEX CUM INSIDE###
image dasex_cum_in_ani2:
    "da/23_cum_01.png"
    pause.1
    "da/23_cum_02.png"
    pause.1
    "da/23_cum_03.png"
    pause.1
    "da/23_cum_04.png"
    pause.1
    "da/23_cum_05.png"
    pause.1
    "da/23_cum_06.png"
    pause.1
    "da/23_cum_07.png"
    pause.1
    "da/23_cum_08.png"
    pause.1
    "da/23_cum_09.png"
    pause.1
    "da/23_cum_10.png"
    pause.1
    "da/23_cum_11.png"
    pause.1
    "da/23_cum_12.png"
    pause.1
    "da/23_cum_13.png"
    pause.1
    "da/23_cum_14.png"
    pause.1
    "da/23_cum_15.png"
    pause.1
    "da/23_cum_16.png"
    pause.1
    "da/23_cum_17.png"
    pause.1
    "da/23_cum_18.png"
    pause.1
    "da/23_cum_19.png"
    pause 3
    "da/23_cum_20.png"
    pause.1
    "da/23_cum_21.png"
    pause.1
    "da/23_cum_22.png"
    pause.1
    "da/23_cum_23.png"
    pause.1







### HERMIONE GIVING GENIE A HANDJOB ###
image handjob_ani:
    "03_hp/08_animation_02/12_handjob_01.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_02.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_03.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_04.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_05.png"
    pause.1
    "03_hp/08_animation_02/12_handjob_06.png"
    pause.1
    repeat

### HERMIONE GIVING A KISS TO GENIE'S COCK ###
image kiss_ani:
    "03_hp/08_animation_02/13_kiss_01.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_02.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_03.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_04.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_05.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_06.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_07.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_08.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_09.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_10.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_11.png"
    pause.1
    "03_hp/08_animation_02/13_kiss_12.png"
    pause.1
    repeat

### HERMIONE HANDJOB CUMMING UNDER THE SHIRT ###
image undershirt_cum_ani:
    "03_hp/08_animation_02/14_finish_01.png"
    pause 1
    "03_hp/08_animation_02/14_finish_02.png"
    pause.1
    "03_hp/08_animation_02/14_finish_03.png"
    pause.1
    "03_hp/08_animation_02/14_finish_04.png"
    pause.1
    "03_hp/08_animation_02/14_finish_05.png"
    pause.1
    "03_hp/08_animation_02/14_finish_06.png"
    pause.1
    "03_hp/08_animation_02/14_finish_07.png"
    pause.1
    "03_hp/08_animation_02/14_finish_08.png"
    pause.1
    "03_hp/08_animation_02/14_finish_09.png"
    pause.1
    "03_hp/08_animation_02/14_finish_10.png"
    pause 2
    "03_hp/08_animation_02/14_finish_11.png"
    pause.1
    "03_hp/08_animation_02/14_finish_12.png"
    pause.1
    "03_hp/08_animation_02/14_finish_13.png"
    pause.1
    repeat

### HERMIONE HANDJOB CUMMING ON THE SHIRT ###
image on_shirt_cum_ani:
    "03_hp/08_animation_02/15_cum_00.png"
    pause.1
    "03_hp/08_animation_02/15_cum_01.png"
    pause.1
    "03_hp/08_animation_02/15_cum_02.png"
    pause.1
    "03_hp/08_animation_02/15_cum_03.png"
    pause.1
    "03_hp/08_animation_02/15_cum_04.png"
    pause.1
    "03_hp/08_animation_02/15_cum_05.png"
    pause.1
    "03_hp/08_animation_02/15_cum_06.png"
    pause.1
    "03_hp/08_animation_02/15_cum_07.png"
    pause.1
    "03_hp/08_animation_02/15_cum_08.png"
    pause.1
    "03_hp/08_animation_02/15_cum_09.png"
    pause.1
    "03_hp/08_animation_02/15_cum_10.png"
    pause.1
    "03_hp/08_animation_02/15_cum_11.png"
    pause.1
    "03_hp/08_animation_02/15_cum_12.png"
    pause.1
    "03_hp/08_animation_02/15_cum_13.png"
    pause.1
    "03_hp/08_animation_02/15_cum_14.png"
    pause.1
    "03_hp/08_animation_02/15_cum_15.png"
    pause.1
    "03_hp/08_animation_02/15_cum_16.png"
    pause.1
    "03_hp/08_animation_02/15_cum_17.png"
    pause.1
    "03_hp/08_animation_02/15_cum_18.png"
    pause.1
    "03_hp/08_animation_02/15_cum_19.png"
    pause.1
    "03_hp/08_animation_02/15_cum_20.png"
    pause.1
    "03_hp/08_animation_02/15_cum_21.png"
    pause 1
    "03_hp/08_animation_02/15_cum_22.png"
    pause.1
    "03_hp/08_animation_02/15_cum_21.png"
    pause.1
    "03_hp/08_animation_02/15_cum_22.png"
    pause .1
    "03_hp/08_animation_02/15_cum_21.png"
    pause 1
    "03_hp/08_animation_02/15_cum_23.png"
    pause.1
    "03_hp/08_animation_02/15_cum_24.png"
    pause.1
    "03_hp/08_animation_02/15_cum_25.png"
    pause.1
    "03_hp/08_animation_02/15_cum_00.png"
    pause.7
    repeat


### HERMIONE HANDJOB KISS DRINKING CUM FROM COCK ###
image kiss_cum_ani:
    "03_hp/08_animation_02/16_cum_01.png"
    pause.1
    "03_hp/08_animation_02/16_cum_02.png"
    pause.1
    "03_hp/08_animation_02/16_cum_03.png"
    pause.1
    "03_hp/08_animation_02/16_cum_04.png"
    pause.1
    "03_hp/08_animation_02/16_cum_05.png"
    pause.1
    "03_hp/08_animation_02/16_cum_06.png"
    pause.1
    "03_hp/08_animation_02/16_cum_07.png"
    pause.1
    repeat


### HERMIONE BLOWJOB ###
image blowjob_ani:
    "03_hp/08_animation_02/17_blow_01.png"
    pause.1
    "03_hp/08_animation_02/17_blow_02.png"
    pause.1
    "03_hp/08_animation_02/17_blow_03.png"
    pause.1
    "03_hp/08_animation_02/17_blow_04.png"
    pause.1
    "03_hp/08_animation_02/17_blow_05.png"
    pause.1
    "03_hp/08_animation_02/17_blow_06.png"
    pause.1
    "03_hp/08_animation_02/17_blow_07.png"
    pause.1
    "03_hp/08_animation_02/17_blow_08.png"
    pause.1
    "03_hp/08_animation_02/17_blow_09.png"
    pause.1
    "03_hp/08_animation_02/17_blow_10.png"
    pause.1
    "03_hp/08_animation_02/17_blow_11.png"
    pause.1
    "03_hp/08_animation_02/17_blow_12.png"
    pause.1
    repeat

### HERMIONE BLOWJOB NOT SUCKING ###
image hand_ani:
    "03_hp/08_animation_02/18_hand_01.png"
    pause 3
    "03_hp/08_animation_02/18_hand_02.png"
    pause.1
    "03_hp/08_animation_02/18_hand_03.png"
    pause.1
    "03_hp/08_animation_02/18_hand_04.png"
    pause.1
    repeat

### HERMIONE BLOWJOB CUM IN MOUTH ###
image cum_in_mouth_ani:
    "03_hp/08_animation_02/19_mouth_cum_01.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_02.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_03.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_04.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_05.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_06.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_07.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_08.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_09.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_10.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_11.png"
    pause 1
    "03_hp/08_animation_02/19_mouth_cum_12.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_13.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_14.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_15.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_16.png"
    pause.1
    "03_hp/08_animation_02/19_mouth_cum_17.png"
    pause 2
    "03_hp/08_animation_02/19_mouth_cum_18.png"
    pause.2
    "03_hp/08_animation_02/19_mouth_cum_01.png"
    pause 1
    repeat

### HERMIONE BLOWJOB CUM ON FACE ###
image cum_on_face_ani:
    "03_hp/08_animation_02/20_face_cum_01.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_02.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_03.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_04.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_05.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_06.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_07.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_08.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_09.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_10.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_11.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_12.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_13.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_14.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_15.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_16.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_17.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_18.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_19.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_20.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_21.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 2
    repeat

### HERMIONE CUM COVERED FACE BLINKING ###
image cum_on_face_blink_ani:
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_22.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_23.png"
    pause.1
    "03_hp/08_animation_02/20_face_cum_24.png"
    pause 2
    repeat


### HERMIONE SEX ###
image sex_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.1
    "03_hp/08_animation_02/21_sex_02.png"
    pause.1
    "03_hp/08_animation_02/21_sex_03.png"
    pause.1
    "03_hp/08_animation_02/21_sex_04.png"
    pause.1
    "03_hp/08_animation_02/21_sex_05.png"
    pause.1
    "03_hp/08_animation_02/21_sex_06.png"
    pause.1
    "03_hp/08_animation_02/21_sex_07.png"
    pause.1
    repeat

### HERMIONE FAST SPEED SEX ###
image sex2_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.05
    "03_hp/08_animation_02/21_sex_02.png"
    pause.05
    "03_hp/08_animation_02/21_sex_03.png"
    pause.05
    "03_hp/08_animation_02/21_sex_04.png"
    pause.05
    "03_hp/08_animation_02/21_sex_05.png"
    pause.05
    "03_hp/08_animation_02/21_sex_06.png"
    pause.05
    "03_hp/08_animation_02/21_sex_07.png"
    pause.05
    repeat



### HERMIONE SEX LOW SPEED ###
image sex_slow_ani:
    "03_hp/08_animation_02/21_sex_01.png"
    pause.15
    "03_hp/08_animation_02/21_sex_02.png"
    pause.15
    "03_hp/08_animation_02/21_sex_03.png"
    pause.15
    "03_hp/08_animation_02/21_sex_04.png"
    pause.15
    "03_hp/08_animation_02/21_sex_05.png"
    pause.15
    "03_hp/08_animation_02/21_sex_06.png"
    pause.15
    "03_hp/08_animation_02/21_sex_07.png"
    pause.15
    repeat

### HERMIONE SEX CUM OUTSIDE ###
image sex_cum_out_ani:
    "03_hp/08_animation_02/22_cum_01.png"
    pause.1
    "03_hp/08_animation_02/22_cum_02.png"
    pause.1
    "03_hp/08_animation_02/22_cum_03.png"
    pause.1
    "03_hp/08_animation_02/22_cum_04.png"
    pause.1
    "03_hp/08_animation_02/22_cum_05.png"
    pause.1
    "03_hp/08_animation_02/22_cum_06.png"
    pause.1
    "03_hp/08_animation_02/22_cum_07.png"
    pause.1
    "03_hp/08_animation_02/22_cum_08.png"
    pause.1
    "03_hp/08_animation_02/22_cum_09.png"
    pause.1
    "03_hp/08_animation_02/22_cum_10.png"
    pause.1
    "03_hp/08_animation_02/22_cum_11.png"
    pause.1
    "03_hp/08_animation_02/22_cum_12.png"
    pause.1
    "03_hp/08_animation_02/22_cum_13.png"
    pause.1
    "03_hp/08_animation_02/22_cum_14.png"
    pause.1
    "03_hp/08_animation_02/22_cum_15.png"
    pause.1
    "03_hp/08_animation_02/22_cum_16.png"
    pause.1
    "03_hp/08_animation_02/22_cum_17.png"
    pause.1
    "03_hp/08_animation_02/22_cum_18.png"
    pause.1
    "03_hp/08_animation_02/22_cum_19.png"
    pause 2
    "03_hp/08_animation_02/22_cum_20.png"
    pause.1
    "03_hp/08_animation_02/22_cum_21.png"
    pause.1
    "03_hp/08_animation_02/22_cum_22.png"
    pause.1
    "03_hp/08_animation_02/22_cum_23.png"
    pause.1
    repeat

### HERMIONE SEX CUM OUTSIDE BLINKING###
image sex_cum_out_blink_ani:
    "03_hp/08_animation_02/22_cum_19.png"
    pause 1
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1
    "03_hp/08_animation_02/22_cum_19.png"
    pause.1
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1
    "03_hp/08_animation_02/22_cum_19.png"
    pause 2
    "03_hp/08_animation_02/22_cum_24.png" #closed
    pause.1
    "03_hp/08_animation_02/22_cum_19.png"
    pause 2
    repeat


### HERMIONE SEX CUM INSIDE###
image sex_cum_in_ani:
    "03_hp/08_animation_02/23_cum_01.png"
    pause.1
    "03_hp/08_animation_02/23_cum_02.png"
    pause.1
    "03_hp/08_animation_02/23_cum_03.png"
    pause.1
    "03_hp/08_animation_02/23_cum_04.png"
    pause.1
    "03_hp/08_animation_02/23_cum_05.png"
    pause.1
    "03_hp/08_animation_02/23_cum_06.png"
    pause.1
    "03_hp/08_animation_02/23_cum_07.png"
    pause.1
    "03_hp/08_animation_02/23_cum_08.png"
    pause.1
    "03_hp/08_animation_02/23_cum_09.png"
    pause.1
    "03_hp/08_animation_02/23_cum_10.png"
    pause.1
    "03_hp/08_animation_02/23_cum_11.png"
    pause.1
    "03_hp/08_animation_02/23_cum_12.png"
    pause.1
    "03_hp/08_animation_02/23_cum_13.png"
    pause.1
    "03_hp/08_animation_02/23_cum_14.png"
    pause.1
    "03_hp/08_animation_02/23_cum_15.png"
    pause.1
    "03_hp/08_animation_02/23_cum_16.png"
    pause.1
    "03_hp/08_animation_02/23_cum_17.png"
    pause.1
    "03_hp/08_animation_02/23_cum_18.png"
    pause.1
    "03_hp/08_animation_02/23_cum_19.png"
    pause 3
    "03_hp/08_animation_02/23_cum_20.png"
    pause.1
    "03_hp/08_animation_02/23_cum_21.png"
    pause.1
    "03_hp/08_animation_02/23_cum_22.png"
    pause.1
    "03_hp/08_animation_02/23_cum_23.png"
    pause.1
    repeat


















### HANGING WITH SNAPE ###
image genie_jerking_sperm: #Genie and Snape sitting in front of fireplace...
    "03_hp/animation/hanging_with_snape_01.png"
    pause 2
    "03_hp/animation/hanging_with_snape_02.png"
    pause.2
    "03_hp/animation/hanging_with_snape_03.png"
    pause.2
    "03_hp/animation/hanging_with_snape_04.png"
    pause 1
    "03_hp/animation/hanging_with_snape_03.png"
    pause.2
    "03_hp/animation/hanging_with_snape_01.png"
    pause 3
    repeat

### Harry Potter Weather ###
image cloud_01: #Cloud behind the window.
    pause 2
    "03_hp/07_weather/01cloud_01.png"
    pause 2
    "03_hp/07_weather/01cloud_02.png"
    pause 2
    "03_hp/07_weather/01cloud_03.png"
    pause 2
    "03_hp/07_weather/01cloud_04.png"
    pause 2
    "03_hp/07_weather/01cloud_05.png"
    pause 2
    "03_hp/07_weather/01cloud_06.png"
    pause 2
    "03_hp/07_weather/01cloud_07.png"
    pause 2
    "03_hp/07_weather/01cloud_08.png"
    pause 2
    "03_hp/07_weather/01cloud_09.png"
    pause 2
    "03_hp/07_weather/01cloud_10.png"
    pause 2
    "03_hp/07_weather/01cloud_11.png"
    pause 2
    "03_hp/07_weather/01cloud_12.png"
    pause 2
    "03_hp/07_weather/01cloud_13.png"
    pause 2
    "03_hp/07_weather/01cloud_14.png"
    pause 2
    "03_hp/07_weather/01cloud_15.png"
    pause 2
    "03_hp/07_weather/01cloud_16.png"
    pause 2
    "03_hp/07_weather/01cloud_17.png"
    pause 2
    "03_hp/07_weather/01cloud_18.png"
    pause 2
    "03_hp/07_weather/01cloud_19.png"
    pause 2
    "03_hp/07_weather/01cloud_20.png"
    pause 2
    "03_hp/07_weather/01cloud_21.png"
    pause 2
    "03_hp/07_weather/01cloud_22.png"
    pause 2
    "03_hp/07_weather/01cloud_23.png"
    pause 2
    "03_hp/07_weather/01cloud_24.png"
    pause 2
    "03_hp/07_weather/01cloud_25.png"
    pause 2
    "03_hp/07_weather/01cloud_26.png"
    pause 2
    "03_hp/07_weather/01cloud_27.png"
    pause 2
    "03_hp/07_weather/01cloud_28.png"
    pause 2
    "03_hp/07_weather/01cloud_29.png"
    pause 2
    "03_hp/07_weather/01cloud_30.png"
    pause 2
    "03_hp/07_weather/01cloud_31.png"
    pause 2
    "03_hp/07_weather/01cloud_32.png"
    pause 2
    "03_hp/07_weather/01cloud_01.png"
    pause 9
    repeat


image rain: #Rain.
    "03_hp/07_weather/rain_01.png"
    pause.1
    "03_hp/07_weather/rain_02.png"
    pause.1
    "03_hp/07_weather/rain_03.png"
    pause.1
    repeat


image candle_fire: #Candle fire.
    "03_hp/05_props/fire_01.png"
    pause.1
    "03_hp/05_props/fire_02.png"
    pause.1
    "03_hp/05_props/fire_03.png"
    pause.1
    "03_hp/05_props/fire_04.png"
    pause.1
    "03_hp/05_props/fire_05.png"
    pause.1
    "03_hp/05_props/fire_06.png"
    pause.1
    "03_hp/05_props/fire_07.png"
    pause.1
    "03_hp/05_props/fire_08.png"
    pause.1
    "03_hp/05_props/fire_09.png"
    pause.1
    "03_hp/05_props/fire_10.png"
    pause.1
    repeat

image candle_fire_02: #Candle fire.
    "03_hp/05_props/fire_01.png"
    pause.1
    "03_hp/05_props/fire_04.png"
    pause.1
    "03_hp/05_props/fire_03.png"
    pause.1
    "03_hp/05_props/fire_02.png"
    pause.1
    "03_hp/05_props/fire_08.png"
    pause.1
    "03_hp/05_props/fire_06.png"
    pause.1
    "03_hp/05_props/fire_07.png"
    pause.1
    "03_hp/05_props/fire_05.png"
    pause.1
    "03_hp/05_props/fire_10.png"
    pause.1
    "03_hp/05_props/fire_09.png"
    pause.1
    repeat


image lightening: #Lightening during rain behind the window.
    pause 20
    "03_hp/07_weather/lightining_01.png"
    pause.1
    "03_hp/07_weather/lightining_02.png"
    pause.1
    "03_hp/07_weather/lightining_03.png"
    pause.1
    "03_hp/07_weather/lightining_04.png"
    pause.1
    "03_hp/07_weather/lightining_05.png"
    pause.1
    "03_hp/07_weather/lightining_06.png"
    pause.1
    "03_hp/07_weather/lightining_05.png"
    pause.1
    "03_hp/07_weather/lightining_06.png"
    pause.1
    "03_hp/07_weather/lightining_05.png"
    pause 20
    repeat


image fireplace_fire: #Fireplace fire.
    "03_hp/05_props/fireplace_fire_01.png"
    pause.1
    "03_hp/05_props/fireplace_fire_02.png"
    pause.1
    "03_hp/05_props/fireplace_fire_03.png"
    pause.1
    "03_hp/05_props/fireplace_fire_04.png"
    pause.1
    "03_hp/05_props/fireplace_fire_05.png"
    pause.1
    "03_hp/05_props/fireplace_fire_06.png"
    pause.1
    "03_hp/05_props/fireplace_fire_07.png"
    pause.1
    "03_hp/05_props/fireplace_fire_08.png"
    pause.1
    repeat


image feeding: #FEEDING THE PHOENIX.
    "03_hp/animation/feeding_01.png"
    pause.5
    "03_hp/animation/feeding_02.png"
    pause.1
    "03_hp/animation/feeding_03.png"
    pause.1
    "03_hp/animation/feeding_04.png"
    pause.1
    "03_hp/animation/feeding_05.png"
    pause.5
    "03_hp/animation/feeding_03.png"
    pause.1
    "03_hp/animation/feeding_02.png"
    pause.1
    "03_hp/animation/feeding_01.png"


image petting: #PETTING THE PHOENIX.
    "03_hp/animation/petting_01.png"
    pause 1
    "03_hp/animation/petting_02.png"
    pause.1
    "03_hp/animation/petting_03.png"
    pause.1
    "03_hp/animation/petting_04.png"
    pause.1
    "03_hp/animation/petting_05.png"
    pause.1
    "03_hp/animation/petting_06.png"
    pause.2
    "03_hp/animation/petting_05.png"
    pause.2
    "03_hp/animation/petting_06.png"
    pause.2
    "03_hp/animation/petting_05.png"
    pause.2
    "03_hp/animation/petting_06.png"
    pause.2
    "03_hp/animation/petting_05.png"
    pause.2
    "03_hp/animation/petting_04.png"
    pause.1
    "03_hp/animation/petting_03.png"
    pause.1
    "03_hp/animation/petting_02.png"
    pause.1
    "03_hp/animation/petting_01.png"
    pause.1

image petting2: #PETTING THE PHOENIX.
    "03_hp/animation/petting_012.png"
    pause 1
    "03_hp/animation/petting_022.png"
    pause.1
    "03_hp/animation/petting_032.png"
    pause.1
    "03_hp/animation/petting_042.png"
    pause.1
    "03_hp/animation/petting_052.png"
    pause.1
    "03_hp/animation/petting_062.png"
    pause.2
    "03_hp/animation/petting_052.png"
    pause.2
    "03_hp/animation/petting_062.png"
    pause.2
    "03_hp/animation/petting_052.png"
    pause.2
    "03_hp/animation/petting_062.png"
    pause.2
    "03_hp/animation/petting_052.png"
    pause.2
    "03_hp/animation/petting_042.png"
    pause.1
    "03_hp/animation/petting_032.png"
    pause.1
    "03_hp/animation/petting_022.png"
    pause.1
    "03_hp/animation/petting_012.png"
    pause.1


image owl_01: #OWL WITH ENVELOPE IN IT'S MOUTH, BLINKING.
    "03_hp/05_props/owl_01.png"
    pause.1
    "03_hp/05_props/owl_02.png"
    pause.1
    "03_hp/05_props/owl_03.png"
    pause.15
    "03_hp/05_props/owl_02.png"
    pause.1
    "03_hp/05_props/owl_01.png"
    pause 7
    repeat


## ANIMATIONS


image harry_demon:
    "new/chm1/7-27.png"
    pause 1.0
    "new/chm1/7-28.png"
    pause 0.3
    "new/chm1/7-29.png"
    pause 0.3
    "new/chm1/7-30.png"
    pause 0.3
    "new/chm1/7-31.png"
    pause 0.3
    "new/chm1/7-32.png"
    pause 0.3
    "new/chm1/7-33.png"
    pause 0.3
    "new/chm1/7-34.png"
    pause 0.3
    "new/chm1/7-35.png"
    pause 0.3
    "new/chm1/7-37.png"
    pause 0.3
    



#############################################

image heal:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06

image heal_02: # Smaller version of heal. 40% of the original size.
    "magic_02/heal01.png"
    pause.06
    "magic_02/heal02.png"
    pause.06
    "magic_02/heal03.png"
    pause.06
    "magic_02/heal04.png"
    pause.06
    "magic_02/heal05.png"
    pause.06
    "magic_02/heal06.png"
    pause.06
    "magic_02/heal07.png"
    pause.06
    "magic_02/heal08.png"
    pause.06
    "magic_02/heal09.png"
    pause.06
    "magic_02/heal10.png"
    pause.06
    "magic_02/heal11.png"
    pause.06
    "magic_02/heal12.png"
    pause.06
    "magic_02/heal13.png"
    pause.06
    "magic_02/heal14.png"
    pause.06
    "magic_02/heal15.png"
    pause.06
    "magic_02/heal16.png"
    pause.06
    "magic_02/heal17.png"
    pause.06
    "magic_02/heal18.png"
    pause.06


image slap:
    "slave/slap01.png"
    pause.06
    "slave/slap02.png"
    pause.06
    "slave/slap03.png"
    pause.06
    "slave/slap04.png"
    pause.06
    "slave/slap05.png"
    pause.06
    "slave/slap06.png"
    pause.06
    "slave/slap07.png"
    pause.06

image slave:
    "slave/slave01.png"
    pause.02
    "slave/slave01_02.png"
    pause.02
    "slave/slave01_03.png"
    pause.02
    "slave/slave01_04.png"
    pause.2
    "slave/slave01_03.png"
    pause.02
    "slave/slave01_02.png"
    pause.02
    "slave/slave01.png"
    pause 5
    repeat





image akaani:
    "akaani/akaani01.png"
    pause.1
    "akaani/akaani02.png"
    pause.1
    "akaani/akaani03.png"
    pause.1
    "akaani/akaani04.png"
    pause.1
    "akaani/akaani05.png"
    pause.1
    "akaani/akaani06.png"
    pause.1
    repeat

image akaani2:
    "akaani2/aka_ani2_01.png"
    pause.2
    "akaani2/aka_ani2_02.png"
    pause.2
    "akaani2/aka_ani2_03.png"
    pause.2
    "akaani2/aka_ani2_04.png"
    pause.2
    repeat



image titjob_ani_pause:
    "new/tj_sex_01.png"

image titjob_ani:
    "new/tj_sex_01.png"
    pause 0.3
    "new/tj_sex_02.png"
    pause 0.3
    "new/tj_sex_03.png"
    pause 0.3
    "new/tj_sex_04.png"
    pause 0.3
    repeat

image titjob_mouth_ani:
    "new/tj_cum_mouth_01.png"
    pause 0.1
    "new/tj_cum_mouth_02.png"
    pause 0.1
    "new/tj_cum_mouth_03.png"
    pause 0.1
    "new/tj_cum_mouth_04.png"
    pause 0.1
    "new/tj_cum_mouth_05.png"
    pause 0.1
    "new/tj_cum_mouth_06.png"
    pause 0.1
    "new/tj_cum_mouth_07.png"
    pause 0.1
    "new/tj_cum_mouth_08.png"
    pause 0.1
    "new/tj_cum_mouth_09.png"
    pause 0.1
    "new/tj_cum_mouth_10.png"
    pause 0.1
    "new/tj_cum_mouth_11.png"
    pause 0.1
    "new/tj_cum_mouth_12.png"
    pause 0.1
    "new/tj_cum_mouth_13.png"
    pause 0.1
    "new/tj_cum_mouth_14.png"
    pause 0.1
    "new/tj_cum_mouth_15.png"
    pause 0.1
    "new/tj_cum_mouth_16.png"
    pause 0.1
    "new/tj_cum_mouth_17.png"
    pause 0.1
    "new/tj_cum_mouth_18.png"
    pause 0.1
    repeat


image titjob_chest_ani:
    "new/tj_cum_chest_01.png"
    pause 0.1
    "new/tj_cum_chest_02.png"
    pause 0.1
    "new/tj_cum_chest_03.png"
    pause 0.1
    "new/tj_cum_chest_04.png"
    pause 0.1
    "new/tj_cum_chest_05.png"
    pause 0.1
    "new/tj_cum_chest_06.png"
    pause 0.1
    "new/tj_cum_chest_07.png"
    pause 0.1
    "new/tj_cum_chest_08.png"
    pause 0.1
    "new/tj_cum_chest_09.png"
    pause 0.1
    "new/tj_cum_chest_10.png"
    pause 0.1
    "new/tj_cum_chest_11.png"
    pause 0.1
    "new/tj_cum_chest_12.png"
    pause 0.1
    "new/tj_cum_chest_13.png"
    pause 0.1
    "new/tj_cum_chest_14.png"
    pause 0.1
    "new/tj_cum_chest_15.png"
    pause 0.1
    "new/tj_cum_chest_16.png"
    pause 0.1
    "new/tj_cum_chest_17.png"
    pause 0.1
    "new/tj_cum_chest_18.png"
    pause 0.1
    "new/tj_cum_chest_19.png"
    pause 0.1
    "new/tj_cum_chest_20.png"
    pause 0.1
    "new/tj_cum_chest_21.png"
    pause 0.1
    repeat

image cho_head:
    "f/cho1.png"
    pause 0.7
    "f/cho2.png"
    pause 0.7
    "f/cho3.png"
    pause 0.7
    "f/cho4.png"
    pause 0.7
    "f/cho5.png"
    pause 0.7
    "f/cho_gipn_evil.png"


image dap_cum1:
    "end/ve30.png"
    pause 0.8
    "end/ve31.png"
    pause 0.8
    "end/ve32.png"
    pause 0.8
    "end/ve33.png"
    pause 0.8
    "end/ve34.png"
    pause 0.8
    "end/ve35.png"
    pause 0.8
        
image dap_cum2:
    "end/ve35.png"
    pause 0.8
    "end/ve36.png"
    pause 0.8
    "end/ve37.png"
    pause 0.8
    "end/ve38.png"
    pause 0.8
    "end/ve39.png"
    pause 0.8
    
image dap_cum3:
    "end/ve39.png"
    pause 0.8
    "end/ve40.png"
    pause 0.8
    "end/ve41.png"
    pause 0.8
    "end/ve42.png"
    pause 0.8
    "end/ve43.png"
    pause 0.8
    "end/ve44.png"
    pause 0.8




image fenix_minet:
    "new/f1.png"
    pause 0.2
    "new/f2.png"
    pause 0.2
    "new/f3.png"
    pause 0.2
    "new/f4.png"
    pause 0.2
    "new/f5.png"
    pause 0.2
    "new/f4.png"
    pause 0.2
    "new/f3.png"
    pause 0.2
    "new/f2.png"
    pause 0.2
    repeat

image fenix_stol:
    "new/fst1.png"
    pause .2
    "new/fst2.png"
    pause .2
    "new/fst1.png"
    pause .2
    "new/fst3.png"
    pause .2
    repeat

image fenix_sex1:
    "new/ff1.png"
    pause .15
    "new/ff2.png"
    pause .15
    "new/ff3.png"
    pause .15
    "new/ff4.png"
    pause .15
    "new/ff5.png"
    pause .15
    "new/ff4.png"
    pause .15
    "new/ff3.png"
    pause .15
    "new/ff2.png"
    pause .15
    repeat


image chimi_end:
    "new/chm1/7.png"
    pause 0.3
    "new/chm1/7-1.png"
    pause 0.3
    "new/chm1/7-3.png"
    pause 0.3
    "new/chm1/7-4.png"
    pause 0.3
    "new/chm1/7-3.png"
    pause 0.3
    "new/chm1/7-1.png"
    pause 0.3
    repeat


image chimi_end2:
    "new/chm1/ch1.png"
    pause 0.3
    "new/chm1/ch2.png"
    pause 0.3
    "new/chm1/ch3.png"
    pause 0.3
    "new/chm1/ch4.png"
    pause 0.3
    "new/chm1/ch3.png"
    pause 0.3
    "new/chm1/ch2.png"
    pause 0.3
    repeat

image chim_grup:
    "new/chm1/6.png"
    pause 0.5
    "new/chm1/60.png"
    pause 0.5
    repeat

image chim_grup2:
    "new/chm1/6-5.png"
    pause 0.5
    "new/chm1/6-50.png"
    pause 0.5
    repeat


image chim_grup3:
    "new/chm1/6-8.png"
    pause 0.5
    "new/chm1/6-81.png"
    pause 0.5
    repeat

image fenix_sex11:
    "new/fs6.png"
    pause .1
    "new/fs7.png"
    pause .1
    "new/fs8.png"
    pause .1
    "new/fs9.png"
    pause .1
    "new/fs10.png"
    pause .1
    "new/fs11.png"
    pause .1
    "new/fs12.png"
    pause .1
    "new/fs11.png"
    pause .1
    "new/fs10.png"
    pause .1
    "new/fs9.png"
    pause .1
    "new/fs8.png"
    pause .1
    "new/fs7.png"
    pause .1

    repeat

image fenix_sex2:
    "new/fk1.png"
    pause 1
    "new/fk2.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk6.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk2.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk6.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk2.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk6.png"
    pause .1
    "new/fk5.png"
    pause .1
    "new/fk4.png"
    pause .1
    "new/fk3.png"
    pause .1
    "new/fk2.png"
    pause .1
    repeat

image fenix_minet2:
    "new/fn1.png"
    pause .1
    "new/fn2.png"
    pause .1
    "new/fn3.png"
    pause .1
    "new/fn4.png"
    pause .1
    "new/fn5.png"
    pause .1
    "new/fn6.png"
    pause .1
    "new/fn5.png"
    pause .1
    "new/fn4.png"
    pause .1
    "new/fn3.png"
    pause .1
    "new/fn2.png"
    pause .1
    repeat


image schooled:
    "slavem/schooled01.png"
    pause 1
    "slavem/schooled02.png"
    pause.1
    "slavem/schooled01.png"
    pause 3
    "slavem/schooled02.png"
    pause.1
    "slavem/schooled01.png"
    pause.1
    "slavem/schooled02.png"
    pause.1
    "slavem/schooled01.png"
    pause 5
    repeat
image obedience01:
    "slavem/obed01_1.png"
    pause 1
    "slavem/obed01_2.png"
    pause.1
    "slavem/obed01_1.png"
    pause 3
    "slavem/obed01_2.png"
    pause.1
    "slavem/obed01_1.png"
    pause.1
    "slavem/obed01_2.png"
    pause.1
    "slavem/obed01_1.png"
    pause 5
    repeat
image obedience01b:
    "slavem/obed01_1b.png"
    pause 1
    "slavem/obed01_2b.png"
    pause.1
    "slavem/obed01_1b.png"
    pause 3
    "slavem/obed01_2b.png"
    pause.1
    "slavem/obed01_1b.png"
    pause.1
    "slavem/obed01_2b.png"
    pause.1
    "slavem/obed01_1b.png"
    pause 5
    repeat
image obedience02:
    "slavem/obed02_1.png"
    pause 1
    "slavem/obed02_2.png"
    pause.1
    "slavem/obed02_1.png"
    pause 3
    "slavem/obed02_2.png"
    pause.1
    "slavem/obed02_1.png"
    pause.1
    "slavem/obed02_2.png"
    pause.1
    "slavem/obed02_1.png"
    pause 5
    repeat
image obedience03:
    "slavem/obed03_1.png"
    pause 1
    "slavem/obed03_2.png"
    pause.1
    "slavem/obed03_1.png"
    pause 3
    "slavem/obed03_2.png"
    pause.1
    "slavem/obed03_1.png"
    pause.1
    "slavem/obed03_2.png"
    pause.1
    "slavem/obed03_1.png"
    pause 3
    repeat


image sleeping:
    "slavem/sleep01.png"
    pause.1
    "slavem/sleep02.png"
    pause.1
    "slavem/sleep03.png"
    pause.1
    "slavem/sleep04.png"
    pause.1
    "slavem/sleep05.png"
    pause.1
    repeat

image sleeping2:
    "slavem/sleep201.png"
    pause.15
    "slavem/sleep202.png"
    pause.15
    "slavem/sleep203.png"
    pause.15
    "slavem/sleep204.png"
    pause.15
    "slavem/sleep205.png"
    pause.15
    repeat

image courage:
    "slavem/courage01.png"
    pause.3
    "slavem/courage02.png"
    pause.3
    repeat

image banana03:
    "slavem/banana03.png"
    pause.4
    "slavem/banana04.png"
    pause.4
    repeat

image rest03:
    "slavem/rest01.png"
    pause 2
    "slavem/rest05.png"
    pause.1
    "slavem/rest01.png"
    pause.1
    "slavem/rest05.png"
    pause.1
    "slavem/rest01.png"
    pause 10
    "slavem/rest05.png"
    pause.1
    "slavem/rest01.png"
    pause 5
    repeat

image btits:
    "slavem/btits01.png"
    pause 3
    "slavem/btits02.png"
    pause 1
    "slavem/btits01.png"
    pause 1
    "slavem/btits03.png"
    pause.08
    "slavem/btits04.png"
    pause.08
    "slavem/btits05.png"
    pause.08
    "slavem/btits06.png"
    pause.08
    "slavem/btits07.png"
    pause.08
    "slavem/btits08.png"
    pause.08
    "slavem/btits09.png"
    pause.04
    "slavem/btits10.png"
    pause 4
    "slavem/btits09.png"
    pause.08
    "slavem/btits10.png"
    pause.08
    repeat



############################################
#######EMOTIONS #^_^# ########################
############################################

image emo01:
    "emotions/ex01.png"
    pause.1
    "emotions/ex02.png"
    pause.1
    "emotions/ex03.png"
    pause.1
    "emotions/ex04.png"
    pause 2
    "emotions/ex01.png"
    pause.1
    "emotions/ex00.png"

image emo02:
    "emotions/exl01.png"
    pause.05
    "emotions/exl02.png"
    pause.05
    "emotions/exl03.png"
    pause.05
    "emotions/exl04.png"
    pause.05
    "emotions/exl05.png"
    pause.05
    "emotions/exl06.png"

image emoq:
    "emotions/q1.png"
    pause.05
    "emotions/q2.png"
    pause.05
    "emotions/q3.png"
    pause.05
    "emotions/q4.png"
    pause.05
    "emotions/q1.png"
    pause.05
    "emotions/q2.png"
    pause.05
    "emotions/q3.png"
    pause.05
    "emotions/q4.png"

image emom:
    "emotions/emo00.png"
    pause.08
    "emotions/emo01.png"

image excl:
    "emotions/excl01.png"
    pause.08
    "emotions/excl02.png"
    pause.08
    "emotions/excl03.png"
    pause.08
    "emotions/excl04.png"
    pause.08

image qu:
    "emotions/que1.png"
    pause.08
    "emotions/que2.png"
    pause.08
    "emotions/que3.png"
    pause.08
    "emotions/que4.png"
    pause.08
    "emotions/que5.png"
    pause.08
    "emotions/que6.png"

image an:
    "emotions/an1.png"
    pause.2
    "emotions/an2.png"
    pause.2
    "emotions/an3.png"
    pause.2
    "emotions/an2.png"
    pause.2
    repeat

image sal:
    "emotions/s1.png"
    pause.08
    "emotions/s2.png"
    pause.2
    "emotions/s3.png"
    pause.08
    "emotions/s4.png"
    pause.2
    "emotions/s5.png"
    pause.08
    "emotions/s6.png"
    pause 1
    "emotions/00.png"
    pause.08
    repeat

image th:
    "emotions/t1.png"
    pause.2
    "emotions/t2.png"
    pause.2
    "emotions/t3.png"
    pause.2
    "emotions/t4.png"
    pause.2
    repeat

image emo7:
    "emotions/emotion00.png"
    pause.2
    "emotions/emotion01.png"
    pause.2
    "emotions/emotion00.png"
    pause.08
    "emotions/emotion01.png"
    pause.08
    "emotions/emotion00.png"
    pause.08
    "emotions/emotion01.png"
    pause.08

image emo8:
    "emotions/emotion00.png"
    pause.2
    "emotions/emotion03.png"
    pause.2
    "emotions/emotion00.png"
    pause.08
    "emotions/emotion03.png"
    pause.08
    "emotions/emotion00.png"
    pause.08
    "emotions/emotion03.png"
    pause.08

image sur:
    "emotions/sur1.png"
    pause.08
    "emotions/sur2.png"
    pause.08
    "emotions/sur3.png"
    pause.08
    "emotions/sur4.png"
    pause.08
    "emotions/sur5.png"
    pause.08
    "emotions/sur6.png"
    pause.08

###################
####SEX############
###################

image hjob:
    "ani01/hj01.png"
    pause.08
    "ani01/hj02.png"
    pause.08
    "ani01/hj03.png"
    pause.08
    "ani01/hj04.png"
    pause.08
    "ani01/hj05.png"
    pause.08
    repeat

image hjobcum:
    "ani01/cum01.png"
    pause.08
    "ani01/cum02.png"
    pause.08
    "ani01/cum03.png"
    pause.08
    "ani01/cum04.png"
    pause.08
    "ani01/cum05.png"
    pause.08
    "ani01/cum06.png"
    pause.08
    "ani01/cum07.png"
    pause.08
    "ani01/cum08.png"
    pause.08
    "ani01/cum09.png"
    pause.08
    "ani01/cum10.png"
    pause.08
    "ani01/cum11d.png"
    pause 1
    repeat

image hjobover:
    "ani01/ac01.png"
    pause.08
    "ani01/ac02.png"
    pause.08
    "ani01/ac03.png"
    pause.08
    "ani01/ac4.png"
    pause.08
    "ani01/ac5.png"
    pause.08
    "ani01/ac6d.png"
    pause 2
    repeat

image heart:
    "ani01/h01.png"
    pause.1
    "ani01/h02.png"
    pause.1
    repeat
##########################SEX################


image side mage = "mage.png"
image side mage2 = "mage2.png"
image side mage3 = "mage3.png"
image side mage4 = "mage4.png"
image side mage5 = "mage5.png"
image side mage6 = "mage6.png"
image side mage7 = "mage7.png"
image side mage8 = "mage8.png"
image side mage9 = "mage9.png"
image side mage10 = "mage10.png"
image side mage11 = "mage11.png"
image side mage13 = "mage12.png"
image side mage12 = "mage13.png"
image side aka1 = "aka.png"
image side aka2 = "aka2.png"
image side aka3 = "aka3.png"
image side aka4 = "aka4.png"
image side aka5 = "aka5.png"
image side aka6 = "aka6.png"
image side aka7 = "aka7.png"
image side jaf1 = "jaf.png"
image side jaf2 = "jaf2.png"
image side jaf3 = "jaf3.png"
image side jaf4 = "jaf4.png"
image side jaf5 = "jaf5.png"
image side jaf6 = "jaf6.png"
image side jaf7 = "jaf7.png"
image side jaf8 = "jaf8.png"
image side jaf9 = "jaf9.png"
image side jaf10 = "jaf10.png"
image side jaf8b = "jaf8b.png"
image side jaf9b = "jaf9b.png"
image side jaf10b = "jaf10b.png"
image side jaf8c = "jaf8c.png"
image side jaf9c = "jaf9c.png"
image side jaf10c = "jaf10c.png"
image side jas1 = "jas1.png"
image side jas2 = "jas2.png"
image side jas3 = "jas3.png"
image side jas4 = "jas4.png"
image side jas5 = "jas5.png"
image side jas6 = "jas6.png"
image side jas7 = "jas7.png"
image side jas8 = "jas8.png"
image side jas9 = "jas9.png"
image side jas10 = "jas10.png"
image side jas11 = "jas11.png"
image side jas12 = "jas12.png"
image side jas13 = "jas13.png"
image side jas14 = "jas14.png"
image side jas15 = "jas15.png"
image side jas16 = "jas16.png"
image side jas17 = "jas17.png"
image side jas18 = "jas18.png"
image side jas19 = "jas19.png"
image side jas20 = "jas20.png"
image side jas21 = "jas21.png"
image side jas1b = "jas1b.png"
image side jas2b = "jas2b.png"
image side jas3b = "jas3b.png"
image side jas4b = "jas4b.png"
image side jas5b = "jas5b.png"
image side jas6b = "jas6b.png"
image side jas7b = "jas7b.png"
image side jas8b = "jas8b.png"
image side jas9b = "jas9b.png"
image side jas10b = "jas10b.png"
image side jas11b = "jas11b.png"
image side jas12b = "jas12b.png"
image side jas13b = "jas13b.png"
image side jas14b = "jas14b.png"
image side jas15b = "jas15b.png"
image side jas16b = "jas16b.png"
image side jas17b = "jas17b.png"
image side jas18b = "jas18b.png"
image side jas19b = "jas19b.png"
image side jas20b = "jas20b.png"
image side jas21b = "jas21b.png"
image side jas1c = "jas1c.png"
image side jas2c = "jas2c.png"
image side jas3c = "jas3c.png"
image side jas4c = "jas4c.png"
image side jas5c = "jas5c.png"
image side jas6c = "jas6c.png"
image side jas7c = "jas7c.png"
image side jas8c = "jas8c.png"
image side jas9c = "jas9c.png"
image side jas10c = "jas10c.png"
image side jas11c = "jas11c.png"
image side jas12c = "jas12c.png"
image side jas13c = "jas13c.png"
image side jas14c = "jas14c.png"
image side jas15c = "jas15c.png"
image side jas16c = "jas16c.png"
image side jas17c = "jas17c.png"
image side jas18c = "jas18c.png"
image side jas19c = "jas19c.png"
image side jas20c = "jas20c.png"

image side dum1 = "dum_01.png"
image side dum2 = "dum_02.png"
image side dum3 = "dum_03.png"
image side dum4 = "dum_04.png"
image side dum5 = "dum_05.png"






define au = Character("Author", window_left_padding=80, color="#402313", ctc="ctc3", ctc_position="fixed")

define sult = Character("Sultan", window_left_padding=80, color="#402313", ctc="ctc3", ctc_position="fixed")


define iris = Character("iris", window_left_padding=70, color="#402313", ctc="ctc3", ctc_position="fixed")

define jas = Character("Jasmine", window_left_padding=70, color="#402313", ctc="ctc3", ctc_position="fixed")

define qu = Character("Rolanda Hooch", window_left_padding=70, color="#402313", ctc="ctc3", ctc_position="fixed")


## CHARACTERS

define sch = Character('Rose the teacher',
    color="#402313",
    window_right_padding=240,
    show_side_image=Image("slavem/school.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch2 = Character('Azalea the store owner',
    color="#402313",
    window_right_padding=240,
    show_side_image=Image("slavem/school2.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch2n = Character('Azalea the store owner',
    color="#402313",
    window_right_padding=240,
    show_side_image=Image("slavem/school2n.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define sch3 = Character('Lily the mamma',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school3.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch300 = Character('Lily the mamma',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch4 = Character('Rasul captain of the guard',
    color="#402313",
    window_right_padding=300,
    show_side_image=Image("slavem/school4.png", xalign=0.985, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch5 = Character('Balsam the merchant',
    color="#402313",
    window_right_padding=300,
    show_side_image=Image("slavem/school5.png", xalign=1.0, yalign=0.98),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch600 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6_2 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6_3 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6_4 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9_4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch62 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6_5 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9_5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch6_6 = Character('Maslab the inn keeper',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school9_6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch7 = Character('Crocus the homeless',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school7.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch8 = Character('Crocus the homeless',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school8.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch9 = Character('Dahlia the whore',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch900 = Character('Dahlia the whore',
    color="#402313",
    window_right_padding=270,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define sch1000 = Character('Lola',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define aka1 = Character('none',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/aka1.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch10 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define sch10_1 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00_1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch10_2 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch10_3 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00_3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch10_4 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00_4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch10_5 = Character('Lola',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school00_5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")






define dah = Character('Dahlia',
    color="#402313",
    window_right_padding=90,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")









define dahr = Character(None,
    color="#402313",
    window_left_padding=230,
    show_side_image=Image("03_hp/18_store/dahr.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define raj02 = Character('Rajah',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("rajahface/raj02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define raj03 = Character('Rajah',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("rajahface/raj03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define raj04 = Character('Rajah',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("rajahface/raj04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")



define jas01 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas02 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define jas03 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define jas04 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas05 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j05.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas06 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j06.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas07 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j07.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas08 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j08.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas09 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j09.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas10 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j10.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas11 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j11.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas12 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j12.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas13 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j13.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas14 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j14.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas15 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j15.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas16 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j16.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas17 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j17.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas18 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j18.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas19 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j19.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas20 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j20.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas21 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j21.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas22 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j22.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas23 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j23.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas24 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j24.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas25 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j25.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define jas26 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j26.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas27 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j27.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define jas28 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j28.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas29 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j29.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")


define jas30 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j30.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas31 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j31.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas32 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j32.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas33 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j33.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define jas34 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("jasface/j34.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")





########################################
define gh1 = Character('Good Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/gh1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define gh2 = Character('Good Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/gh2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define gh3 = Character('Good Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/gh3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define gh4 = Character('Good Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/gh4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define gh5 = Character('Good Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/gh5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")



define bh1 = Character('Evil Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/bh1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define bh2 = Character('Evil Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/bh2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define bh3 = Character('Evil Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/bh3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define bh4 = Character('Evil Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/bh4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

define bh5 = Character('Evil Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("02goodevil/bh5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")



define sch12_2 = Character('Madder the City Guard',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school12_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch13 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school13.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sch13_2 = Character('Jasmine',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("slavem/school13_2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define sch14 = Character(None,
    color="#402313",
    window_right_padding=70,
    window_left_padding=250,
    show_side_image=Image("test/jas01.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define iris = Character(None, window_left_padding=250, image="test/sch11_2.png", color="#402313", ctc="ctc3", ctc_position="fixed")



define dah1 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah2 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah3 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah4 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah5 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d05.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah6 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d06.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah7 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d07.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah8 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d08.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah9 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d09.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah10 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d10.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah11 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d11.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dah12 = Character('Dahlia',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("dahlia_head/d12.png", xalign=1.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

###PATREON


define pat = Character('silvarius2000',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/11_misc/pat.png", xalign=1.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")





define s = Character(None, color="#402313", ctc="ctc3", ctc_position="fixed")
define m = Character(None, window_left_padding=200, image="mage", color="#402313", ctc="ctc3", ctc_position="fixed")
define g = Character(None, window_left_padding=300, image="mage2", color="#402313", ctc="ctc3", ctc_position="fixed")
define g2 = Character(None, window_left_padding=300, image="mage3", color="#402313", ctc="ctc3", ctc_position="fixed")
define g4 = Character(None, window_left_padding=200, image="mage4", color="#402313", ctc="ctc3", ctc_position="fixed")
define g5 = Character(None, window_left_padding=200, image="mage5", color="#402313", ctc="ctc3", ctc_position="fixed")
define g6 = Character(None, window_left_padding=200, image="mage6", color="#402313", ctc="ctc3", ctc_position="fixed")
define g7 = Character(None, window_left_padding=200, image="mage7", color="#402313", ctc="ctc3", ctc_position="fixed")
define g8 = Character(None, window_left_padding=200, image="mage8", color="#402313", ctc="ctc3", ctc_position="fixed")
define g9 = Character(None, window_left_padding=200, image="mage9", color="#402313", ctc="ctc3", ctc_position="fixed")
define g10 = Character(None, window_left_padding=200, image="mage10", color="#402313", ctc="ctc3", ctc_position="fixed")
define g11 = Character(None, window_left_padding=200, image="mage11", color="#402313", ctc="ctc3", ctc_position="fixed")
define g12 = Character(None, window_left_padding=200, image="mage12", color="#402313", ctc="ctc3", ctc_position="fixed")
define g13 = Character(None, window_left_padding=200, image="mage13", color="#402313", ctc="ctc3", ctc_position="fixed")
define a1 = Character(None, window_left_padding=220, image="aka1", color="#402313", ctc="ctc3", ctc_position="fixed")
define a2 = Character(None, window_left_padding=220, image="aka2", color="#402313", ctc="ctc3", ctc_position="fixed")
define a3 = Character(None, window_left_padding=220, image="aka3", color="#402313", ctc="ctc3", ctc_position="fixed")
define a4 = Character(None, window_left_padding=290, image="aka4", color="#402313", ctc="ctc3", ctc_position="fixed")
define a5 = Character(None, window_left_padding=220, image="aka5", color="#402313", ctc="ctc3", ctc_position="fixed")
define a6 = Character(None, window_left_padding=220, image="aka6", color="#402313", ctc="ctc3", ctc_position="fixed")
define a7 = Character(None, window_left_padding=220, image="aka7", color="#402313", ctc="ctc3", ctc_position="fixed")

define ron = Character(None, window_left_padding=220, image="ronald", color="#402313", ctc="ctc3", ctc_position="fixed")

define hag = Character(None, window_left_padding=260, image="hagr", color="#402313", ctc="ctc3", ctc_position="fixed")

define hilla = Character("Новая Гермиона??", window_left_padding=80, color="#402313", ctc="ctc3", ctc_position="fixed")
define dum = Character(None, window_left_padding=240, image="dum1", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum2 = Character(None, window_left_padding=240, image="dum2", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum3 = Character(None, window_left_padding=240, image="dum3", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum4 = Character(None, window_left_padding=240, image="dum4", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum5 = Character(None, window_left_padding=240, image="dum5", color="#402313", ctc="ctc3", ctc_position="fixed")



define eslow = Character(None, color="#402313", what_slow_cps=20)
define centertext = Character(None,
                          what_size=20, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],
                          #Gives an outline
                          what_slow_cps=20 #Speed at which the text appears (slow)
                          )

init-2:
    ### MENU PLACEMENT ###
    $ menu_x = 0.5


    image eileen alpha = im.Alpha("slavem/jas09.png", 0.5)

    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)



    # Declare an nvl-version of eileen.
    $ nvle = Character(color="#000", what_color="#ffffff", kind=nvl)


    $ who = Character('Female voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ whom = Character('Male voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ la = Character('Lara Croft', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ j = Character('Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ bj = Character('Evil Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ gj = Character('Good Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr1 = Character('Somebody from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr2 = Character('Another voice from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr3 = Character('female voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr4 = Character('somebody named mustafa', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr5 = Character('the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ cr6 = Character('many voices at once', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ ej = Character('Evil Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ gj = Character('Good Jasmine', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ a = Character('Aladdin', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sul = Character('Sultan', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ g3 = Character('Джин', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ ras = Character('Rasul', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ who2 = Character('???', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ jaf1 = Character('Jafar', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ fem = Character('Студентка', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal = Character('Студент # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal2 = Character('Студент # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal3 = Character('Студент # 3', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ mal4 = Character('Студент # 4', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ comm1 = Character('Комментатор # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ comm2 = Character('Комментатор # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ bogu = Character('Телохранитель', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ pl1 = Character("Игрок # 1", color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ pl2 = Character('Игрок # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ pl3 = Character('Игрок # 3', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    


    $ ann = Character('The Announcer', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sly1 = Character('Студент слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sly2 = Character('Другой студент Слизерина', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ aa = Character('AKABUR', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    $ angel = Character('Ангел', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ demoness = Character('Демонесса', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    $ elena_pts = 0

    ###HARRY POTTER CHARACTERS###
    $ her = Character('Гермиона', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ her2 = Character('Гермиона', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    $ sna = Character('Северус Снейп', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ sna2 = Character('Северус Снейп', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    $ vol = Character('Lord Voldemort', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ l = Character('Lola', color="#402313", window_right_padding=230, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    $ mkg = Character('Миневра Макгонгал', color="#402313", window_right_padding=130, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).

define ogn = Character('Огненная голова',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/face_calm.png", xalign=1.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define har_udivl = Character(None,
    color="#402313",
    window_left_padding=200,
    window_right_padding=170,
    show_side_image=Image("f/har_udivl.png", xalign=0.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define har_stesn = Character(None,
    color="#402313",
    window_left_padding=200,
    window_right_padding=170,
    show_side_image=Image("f/har_stesn.png", xalign=0.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define har_visod = Character(None,
    color="#402313",
    window_left_padding=200,
    window_right_padding=170,
    show_side_image=Image("f/har_visod.png", xalign=0.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


### SNAPE HEAD ###
define sna_01 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_02 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sna_03 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sna_04 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
define sna_05 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_05.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_06 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_06.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_07 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_07.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_08 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_08.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_09 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_09.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_10 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_10.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_11 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_11.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_12 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_12.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_13 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_13.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_14 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_14.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_15 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_15.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_16 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_16.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_17 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_17.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_18 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_18.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_19 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_19.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_20 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_20.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_21 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_21.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_22 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_22.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_23 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_23.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_24 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_24.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_25 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_25.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define sna_26 = Character('Северус Снейп',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/12_snape_head/head_26.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define dap_wha = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_wha.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define har_govor = Character(None,
    color="#402313",
    window_left_padding=200,
    window_right_padding=170,
    show_side_image=Image("f/har_morda.png", xalign=0.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define har_morda = Character(None,
    color="#402313",
    window_left_padding=200,
    window_right_padding=170,
    show_side_image=Image("f/har_govor.png", xalign=0.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_ispug = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_ispug.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_krik = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_krik.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap_left = Character('Daphne Gringrass',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_left.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap_smile = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_visod = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_visod.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_visod2 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_visod2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_bol = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_bol.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_plach = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_plach.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap_oh = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_oh.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap_smile3 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile4 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile5 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_gr = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_gr.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_sl = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_sl.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile4sl = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile4sl.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile2 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_yaz = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("d/dh_yaz.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_sperm = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_sperm.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_sperm2 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_sperm2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=150,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define dap1 = Character('Дафна Гринграсс',
    color="#402313",
    window_right_padding=150,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dem = Character('Демон',
    color="#402313",
    window_right_padding=130,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph = Character('Феникс',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define chi = Character('Чжоу Чанг',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define harr = Character('Гарри Поттер',
    color="#402313",
    window_right_padding=70,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")




# phoenix

define ph_1 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph_2 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph_3 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph_4 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h4.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph_5 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h5.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define ph_6 = Character('Phoenix',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/ph_h6.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



###### CHo Chang ____________________________________________________________________________
define chi_gipn = Character('Cho Chang',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/chi_head1.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define chi_sperm = Character('Cho Chang',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/chi_head2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define chi_evil = Character('Cho Chang',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("f/chi_head3.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



# Daphne head

define dap_ispug = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_ispug.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_krik = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_krik.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_smile2 = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_smile2.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_wha = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_wha.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dap_yaz = Character('Дафна',
    color="#402313",
    window_right_padding=170,
    show_side_image=Image("dap/dh_yaz.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



### HERMIONE HEAD ###

define her_01 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/01.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_02 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/02.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_03 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/03.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_04 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/04.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_05 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/05.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_06 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/06.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_07 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/07.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_08 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/08.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_09 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/09.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_10 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/10.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_11 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/11.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_12 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/12.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_13 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/13.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_14= Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/14.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_15 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/15.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_16 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/16.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_17 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/17.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_18 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/18.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_19 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/19.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_20 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/20.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_21 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/21.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_22 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/22.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_23 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/23.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_24 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/24.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_25 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/25.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_26 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/26.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_27 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/27.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_28 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/28.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_29 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/29.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_30 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/30.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_31 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/31.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define her_32 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/32.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_33 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/33.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define her_34 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/34.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_35 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/35.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define her_35 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/35.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define her_36 = Character('Гермиона',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/36.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")


define her_37 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/37.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_38 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/38.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_39 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/39.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_40 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/40.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_41 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/41.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_42 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/42.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_43 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/43.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_44 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/44.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_45 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/45.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")



define her_46 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/46.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_47 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/47.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_48 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/48.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_49 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/49.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_50 = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("03_hp/15_hermione_head/50.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")












## TRANSFORMATION


transform hhhar:
    yalign 1.0
    linear 5.0 yalign 0.5

transform hhhar2:
    yalign 0.5
    linear 2.0 yalign 0.2

transform basicfade:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.5 alpha 0.0

transform basicfade2:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0

transform basicfade3:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 0.8 alpha 0.0

transform basicfade4:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0

image demon_priz = Animation("f/smoke_03.png", 0.3, "f/smoke_02.png", 0.3, "f/smoke_01.png", 0.5, "f/smoke_04.png", 0.3, "f/smoke_05.png", 0.3, "f/smoke_06.png", 50.7)

label start:
    
    $ gold = 0
    $ pat = 0
    $ rum_times = 0 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.


# ================================================================= мои =====================================================================================
    $ herm_vopr = 0 # спросил у гарри про гермиону и дал 10 очков
    $ vopr1 = 0
    $ vopr2 = 0
    $ vopr3 = 0
    $ duels = 0
    $ devil = 0  # 1 - есть книга 2-6 - степень перевода, 7 - дьявол призван для эвента, 8 - эвент закончился,
    $ evil_days = 0
    $ ogon = 0 # триггер работы огня
    $ ogon2 = 0 # триггер первого диалога
    $ book_evil = 0 # переведена книга дьявола - 2, есть книга дьявола - 1
    $ chimi_event = 0 # - 1 - на нее напали, 2 - можно ее вызывать
    $ daphne_event = 0 # 1 - пришло письмо и он его прочитал, можно сказать об этом снейпу, 2 - он поговорил со снейпом и теперь можно вызвать дафну, 3 - он поговорил с дафной, 4 - пришло и он поговорил со снейпом, 5 - она пришла к нему заплаканная, 6 - она ушла от него и через день она согласится на все
    $ bought_feed = False
    $ daph_vopr = 0 # спросил у гарри про дафну первый раз
    $ mkg_trg = 0
    $ kamin = 0
    $ steroids = 0
    # Daphne:
    $ daph_pristav = 0
    $ daphne_moral = 5
    $ dap_level = 0
    $ dap_pod = 0
    $ hagpot = 0 # поушен превращения в хагрида

    $ daphne_publ_request = 0   # триггер публичных заданий дафны от 1 - трусы, 2 - флирт, 3 - свидание - 4 грудь, 5 - мацать, 6 - фап, 7 - минет, 8 - секс
    $ daphne_publ_level = 0
    $ dap_publ = 0   # разговор со снейпом про кубок
    $ harry_chimi = 0
    $ ingridients = 0 # заглушка для диалога с гарри про ингридиенты

    $ delivery_cheat = 0

    $ snape_fap = 0
    $ chimi_level = 0
    $ flirt_com = 0
    $ date_com = 0
    $ tits_com = 0
    $ fap_com = 0
    $ fuck_com = 0
    $ minet_com = 0
    $ mats_com = 0
    # phoenix
    $ pnx_stage = 0 # триггер для записки и стадии с фениксом
    $ phx_pot = 0 # триггер эвентов с превращением в хагрида
    $ phoenix_ev = 0 # триггер во время полной луны, т.е. если он подрочит, то вызовется феникс
    $ phoenix = 0 # сколько раз уже вызывался феникс
    $ quest_hagrid = 0
    $ hagrid_potion = 0
    $ harry_event = 0
    $ hermione_podd = 0
    $ hermione_pod_skirt = 0

    $ nhxalign = 0.7


    $ jasm = "jas03"

    $ titfuck_points = 0
    # нужно сделать еще что он должен сначала купить эту книгу
# ===================\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    $ mizul = 0
    $ ogon_first = 0
    $ resist = 0
    $ bought_maslo = False
###============================Xlj books=================================================================================
    $ previous_book = ""
    $ previous_book_name = ""

    $ books = []
    $ concentration = 0 #+1 for every completed book on concentration. Pops up during paperwork.
    $ speedwriting = 0 #+1 for every completed book on speedwriting. Pops up during paperwork.
    $ s_reading_lvl = 0 #+1 When complete first book on speed reading. +1 again when complete the second book.

    ### BOOKS ###

    ### WORK
    $ book_01_units = 0 #Monitors progress with this book.
    $ book_01_complete = False #Turns True when you finish reading book #1.
    $ book01 = "\"Copper book of spirit\"" #1/10 (tinny) chance of it to pop up. Completes extra chapter during work.

    $ book_02_units = 0 #Monitors progress with this book.
    $ book_02_complete = False #Turns True when you finish reading book #2.
    $ book02 = "\"Bronze book of spirit\"" #1/8 (small) chance of it to pop up. Completes extra chapter during work.

    $ book_03_units = 0 #Monitors progress with this book.
    $ book_03_complete = False #Turns True when you finish reading book #3.
    $ book03 = "\"Silver book of spirit\"" #1/6 (a) chance of it to pop up. Completes extra chapter during work.

    $ book_04_units = 0 #Monitors progress with this book.
    $ book_04_complete = False #Turns True when you finish reading book #4.
    $ book04 = "\"Golden book of spirit\"" #1/4 (decent) chance of it to pop up. Completes extra chapter during work.


    ### NON-FICTION BOOKS ###========================================================================================
    #BOOK 08
    $ book_08_units = 0 #Monitors progress with this book.
    $ book_08_complete = False #Turns True when you finish reading book #4.
    $ book08 = "\"Speed reading for dummies\"" #1/6 chance to complete an extra chapter during reading.

    #BOOK 09
    $ book_09_units = 0 #Monitors progress with this book.
    $ book_09_complete = False #Turns True when you finish reading book #4.
    $ book09 = "\"Speed reading for experts\"" #1/4 chance to complete an extra chapter during reading.
    # WORK===========================================================================================
    #BOOK 10
    $ book_10_units = 0 #Monitors progress with this book.
    $ book_10_complete = False #Turns True when you finish reading book #4.
    $ book10 = "\"Platinum book of spirit\"" #1/2 (big) chance of it to pop up. Completes extra chapter during work.
    #BOOK 11
    $ book_11_units = 0 #Monitors progress with this book.
    $ book_11_complete = False #Turns True when you finish reading book #4.
    $ book11 = "\"Adamantium book of spirit\"" # 1 (sure) chance of it to pop up. Completes extra chapter during work.

    #BOOK 12
    $ book_12_units = 0 #Monitors progress with this book.
    $ book_12_complete = False #Turns True when you finish reading book #12.
    $ book12 = "\"Speedwriting for dummies\"" # 1/10 chance of it to pop up. Completes extra chapter during work.

    #BOOK 13
    $ book_13_units = 0 #Monitors progress with this book.
    $ book_13_complete = False #Turns True when you finish reading book #13.
    $ book13 = "\"Speedwriting for beginners\"" # 1/8 chance of it to pop up. Completes extra chapter during work.

    #BOOK 14
    $ book_14_units = 0 #Monitors progress with this book.
    $ book_14_complete = False #Turns True when you finish reading book #14.
    $ book14 = "\"Speedwriting for intermediate\"" # 1/6 chance of it to pop up. Completes extra chapter during work.

    #BOOK 15
    $ book_15_units = 0 #Monitors progress with this book.
    $ book_15_complete = False #Turns True when you finish reading book #15.
    $ book15 = "\"Speedwriting for advanced\"" # 1/4 chance of it to pop up. Completes extra chapter during work.

    #BOOK 16
    $ book_16_units = 0 #Monitors progress with this book.
    $ book_16_complete = False #Turns True when you finish reading book #16.
    $ book16 = "\"Speedwriting for experts\"" # 1/2 chance of it to pop up. Completes extra chapter during work.

    #BOOK 17
    $ book_17_units = 0 #Monitors progress with this book.
    $ book_17_complete = False #Turns True when you finish reading book #17.
    $ book17 = "\"Speedwriting for maniacs\"" # 1 (sure) chance of it to pop up. Completes extra chapter during work.

###==============xlj books end=============================================================================================

    ### HERMIONE_MAIN SCREN FLAGS ###
    $ only_upper = False #When true, legs are not displayed in the hermione_main screen.
    $ autograph = False #Displays professor Lockhart's autograph on Hermione's leg.
    $ no_blinking = False #When True - blinking animation is not displayed.
    $ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    $ legs_02 = False # Turns TRUE when miniskirt is activated.
    $ h_tears = False #Displays a layer with tears.

    $ current_payout = 0 #Used when haggling about price of th favor.

    $ snape_invated_to_watch = False #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
    $ invited_snape_once_already = False #In the "Dance for me" event, after you send Hermione to invite Snape to watch for the first time - turns TRUE.

    $ uni_sperm = False #Triggers universal sperm to show on hermione_main screen.
    $ days_without_an_event = 0 #Counts days since last (any) event took place.

    $ ask_me_once = False #Turns true after Hermione asks you about your true identity, during sex.

    $ tiara = False #When TRUE tiara is displayed on h_head2 and hermione_main screens.

    $ public_whore_ending = False #If TRUE the game will end with "Public Whore Ending".

    $ p_level_02_active = False #When turns TRUE public favors of level 02 become available.
    $ p_level_03_active = False #When turns TRUE public favors of level 03 become available.
    $ p_level_04_active = False #When turns TRUE public favors of level 04 become available.
    $ p_level_05_active = False #When turns TRUE public favors of level 05 become available.
    $ p_level_06_active = False #When turns TRUE public favors of level 06 become available.
    $ p_level_07_active = False #When turns TRUE public favors of level 07 become available.


    $ lazy_aka_not_yet = True #In public events. Kiss a girl. Event level 03. Event # 3. "Lazy Akabur bug". Turns FALSE after that.
    $ sucked_off_ron = False #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
    $ suked_off_ron_and_har = False #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
    $ fucked_ron_and_har = False #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.





###HOUSE POINTS RELATED###
    $ snapes_support = 0 #Controls how much points is awarded to SLYTHERIN daily.



###HERMIONE STATS###
    $ mad = 0 #Every day -1.


### JERKING OFF FLAGS ###
    $ request_03 = False #True when Hermione has no panties on.
    $ have_cum_soaced_panties = False #TRUE when you have the panties in your possession (before you return them to Hermione).

    $ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
    $ jerking_off_to_lara = False
    $ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
    $ cum_on_panties = False #True when choose to cum on Hermione's panties.


### EVENTS ###
    $ event08_happened = False #Turns TRUE after event_08 (Hermone visits first time).
    $ event09 = False #Turns TRUE when you let Hermione in during event_09. Otherwise she will keep coming every morning.
    $ event10 = False #Turns TRUE when you let Hermione in during event_10. Otherwise she will keep coming every morning.
    $ event11_happened = False #Turns TRUE after event_11
    $ event12_happened = False #Turns TRUE after event_12
    $ event13_happened = False #Turns TRUE after event_13
    $ event14_happened = False #Turns TRUE after event_14
    $ event15_happened = False #Turns TRUE after event_15
    $ event16_happened = False #Turns TRUE after event_16

    $ request_30_a = False #Turns true when hermione fails to show up after her "Fuck a classmate" favor. Runs an event next morning.

### 27_FINAL_EVENTS ###
    $ event_chairman_happened = False #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    $ snape_against_chairman_hap = False # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ have_no_dress_hap = False #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ sorry_for_hesterics = False # Turns TRUE after Hermione comes and apologizes for the day (event) before.


    $ slytherin = 180 #Shows amount of points the Slytherin house has.
    $ gryffindor = 53 #Shows amount of points the Gryffindor house has.
    $ hufflepuff = 25 #Shows amount of points the Hufflepuff house has.
    $ ravenclaw = 31 #Shows amount of points the Ravenclaw house has.




### THE STORE ###
    $ bought_dust = False
    $ bought_jabri = False

    $ bought_ball_dress = False #Affects 15_mail.rpy
    $ bought_dress_already = False #Makes sure that you won't buy the dress twice.
    $ gave_the_dress = False #Turns True when Hermione has the dress.

### HEARTS ###

    $  new_request_01_01 = False # Talk to me.
    $  new_request_01_02 = False
    $  new_request_01_03 = False

    $ new_request_02_01 = False #SHOW ME YOUR PANTIES
    $ new_request_02_02 = False #SHOW ME YOUR PANTIES
    $ new_request_02_03 = False #SHOW ME YOUR PANTIES

    $ new_request_03_01 = False # "Give me your panties"
    $ new_request_03_02 = False # "Give me your panties"
    $ new_request_03_03 = False # "Give me your panties"

    $ new_request_04_01 = False # (Touch tits's through fabric.)
    $ new_request_04_02 = False # (Touch tits's through fabric.)
    $ new_request_04_03 = False # (Touch tits's through fabric.)

    $ new_request_05_01 = False # (BUTT MOLESTER).
    $ new_request_05_02 = False # (BUTT MOLESTER).
    $ new_request_05_03 = False # (BUTT MOLESTER).

    $ new_request_08_01 = False # (Show me tits).
    $ new_request_08_02 = False # (Show me tits).
    $ new_request_08_03 = False # (Show me tits).

    $ new_request_11_01 = False # (Dance for me.)
    $ new_request_11_02 = False # (Dance for me.)
    $ new_request_11_03 = False # (Dance for me.)

    $ new_request_12_01 = False # (Play with her tits.)
    $ new_request_12_02 = False # (Play with her tits.)
    $ new_request_12_03 = False # (Play with her tits.)

    $ new_request_16_01 = False #  (HANDJOB)
    $ new_request_16_02 = False #  (HANDJOB)
    $ new_request_16_03 = False #  (HANDJOB)

    $ new_request_22_01 = False #  (BLOWJOB)
    $ new_request_22_02 = False #  (BLOWJOB)
    $ new_request_22_03 = False #  (BLOWJOB)

    $ new_request_29_01 = False #  (SEX)
    $ new_request_29_02 = False #  (SEX)
    $ new_request_29_03 = False #  (SEX)

    $ new_request_31_01 = False #  (ANAL)
    $ new_request_31_02 = False #  (ANAL)
    $ new_request_31_03 = False #  (ANAL)


### MISC FLAGS ###

    $ lock_public_favors = False #Turns True if reached whoring level 05 while public
    $ touched_by_boy = False #Turns true if sent Hermione to get touched by a boy at least once.

    $ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once a day. Turns back to False every night.
    $ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.


### STORE BOOKS AND ITEMS ###

    $ bought_book_05_b = False #Affects 15_mail.rpy

    $ dear_waifu_completed_once = False # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
    $ found_dahrs_ticket_once = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
    $ vouchers = 0 #Shows the amount of DAHR's vouchers in your possession.


    ### GIFTS ###
    $ wine = 0 # Dumbledore's wine you find in the cupboard and use for "Snape dates".
    $ anal_lube = 0 #Amount of anal lubricant in possesion.
    $ bought_anal_lube = False #Affects 15_mail.rpy
    $ condoms = 0 #Amount.
    $ bought_condoms = False #Affects 15_mail.rpy
    $ candy = 0 #Amount.
    $ bought_candy = False #Affects 15_mail.rpy
    $ chocolate = 0 #Amount.
    $ bought_chocolate = False #Affects 15_mail.rpy
    $ vibrator = 0 #Amount.
    $ bought_vibrator = False #Affects 15_mail.rpy
    $ strapon = 0 #Amount.
    $ bought_strapon = False #Affects 15_mail.rpy
    $ ballgag = 0 #Amount.
    $ bought_ballgag = False #Affects 15_mail.rpy
    $ plug = 0 #Amount.
    $ bought_plug = False #Affects 15_mail.rpy
    $ mag1 = 0 #Amount.
    $ bought_mag1 = False #Affects 15_mail.rpy
    $ mag2 = 0 #Amount.
    $ bought_mag2 = False #Affects 15_mail.rpy
    $ mag3 = 0 #Amount.
    $ bought_mag3 = False #Affects 15_mail.rpy
    $ mag4 = 0 #Amount.
    $ bought_mag4 = False #Affects 15_mail.rpy
    $ beer = 0 #Amount.
    $ bought_beer = False #Affects 15_mail.rpy
    $ owl = 0 #Amount.
    $ bought_owl = False #Affects 15_mail.rpy
    $ sexdoll = 0 #Amount.
    $ bought_sexdoll = False #Affects 15_mail.rpy
    $ lingerie = 0 #Amount.
    $ bought_lingerie = False #Affects 15_mail.rpy
    $ broom = 0 #Amount.
    $ bought_broom = False #Affects 15_mail.rpy
    $ krum = 0 #Amount.
    $ bought_krum = False #Affects 15_mail.rpy
    $ badge_01 = 0 #Amount.
    $ bought_badge_01 = False #Affects 15_mail.rpy
    $ nets = 0 #Amount.
    $ bought_nets = False #Affects 15_mail.rpy


    $ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

    $ wine_not = False # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.

    $ robeon = False # When true - Hermione is wearing a robe.

    $ sfmax = False # Turns TRUE when friendship with Snape been maxed out.

    $ badges = False # Turns layer with a badgge on and off in hermione_main screen.
    $ ba_01 = False # Desplays a badge in hermione_main screen.
    $ ne = False # Desplays a fishnets LAYER in hermione_main screen.
    $ ne_01 = False # Desplays the fishnets in hermione_main screen.

    $ flip = False # When TRUE Hermione's full size sprite is flipped.






    ### DUEL ###
    $ potions = 0 #Amount of healing potions Genie has in stock.

    $ tut_happened = False # Turns TRUE after you click the tutoring button and see the message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.

    $ cataloug_found = False # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.

    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ work_unlock2 = False # Unlocks the "Paperwork" button.

    $ bird_interact = 0 # Counts how many times you have interacted with the bird.




    $ playwizard = 0
    $ paper_comand = 0
    $ paper_students = 0
    $ paper_prepods = 0
    $ paper_holm = 0
    $ paper_forest = 0
    $ paper_photo = 0
    $ paper_puffend = 0
    $ paper_kogt = 0
    $ paper_slytherin = 0
    $ paper_podder = 0
    $ paper_room = 0
    $ paper_level = 0
    $ paper = 0
    $ paper_money = 0
    $ photik = 0
    $ paper_fakults = 0
    $ paper_photed = 0
    $ bought_photo = 0
    $ paper_dost = 0
    $ paper_event = 0




    $ phx_name = None











     ### GIFTS ###
    $ wine = 0 # Dumbledore's wine you find in the cupboard and use for "Snape dates".
    $ anal_lube = 0 #Amount of anal lubricant in possesion.
    $ bought_anal_lube = False #Affects 15_mail.rpy
    $ condoms = 0 #Amount.
    $ bought_condoms = False #Affects 15_mail.rpy
    $ candy = 0 #Amount.
    $ bought_candy = False #Affects 15_mail.rpy
    $ chocolate = 0 #Amount.
    $ bought_chocolate = False #Affects 15_mail.rpy
    $ vibrator = 0 #Amount.
    $ bought_vibrator = False #Affects 15_mail.rpy
    $ strapon = 0 #Amount.
    $ bought_strapon = False #Affects 15_mail.rpy
    $ ballgag = 0 #Amount.
    $ bought_ballgag = False #Affects 15_mail.rpy
    $ plug = 0 #Amount.
    $ bought_plug = False #Affects 15_mail.rpy
    $ mag1 = 0 #Amount.
    $ bought_mag1 = False #Affects 15_mail.rpy
    $ mag2 = 0 #Amount.
    $ bought_mag2 = False #Affects 15_mail.rpy
    $ mag3 = 0 #Amount.
    $ bought_mag3 = False #Affects 15_mail.rpy
    $ mag4 = 0 #Amount.
    $ bought_mag4 = False #Affects 15_mail.rpy
    $ beer = 0 #Amount.
    $ bought_beer = False #Affects 15_mail.rpy
    $ owl = 0 #Amount.
    $ bought_owl = False #Affects 15_mail.rpy
    $ sexdoll = 0 #Amount.
    $ bought_sexdoll = False #Affects 15_mail.rpy
    $ lingerie = 0 #Amount.
    $ bought_lingerie = False #Affects 15_mail.rpy
    $ broom = 0 #Amount.
    $ bought_broom = False #Affects 15_mail.rpy
    $ krum = 0 #Amount.
    $ bought_krum = False #Affects 15_mail.rpy
    $ badge_01 = 0 #Amount.
    $ bought_badge_01 = False #Affects 15_mail.rpy
    $ nets = 0 #Amount.
    $ bought_nets = False #Affects 15_mail.rpy







    $ playwizard = 0
    $ paper_comand = 0
    $ paper_students = 0
    $ paper_prepods = 0
    $ paper_holm = 0
    $ paper_forest = 0
    $ paper_photo = 0
    $ paper_puffend = 0
    $ paper_kogt = 0
    $ paper_slytherin = 0
    $ paper_podder = 0
    $ paper_room = 0
    $ paper_level = 0
    $ paper = 0
    $ paper_money = 0
    $ photik = 0
    $ paper_fakults = 0
    $ paper_photed = 0
    $ bought_photo = 0
    $ paper_dost = 0
    $ paper_event = 0


    ### MINISKIRT ###
    $ bought_skirt_already = False # Turns TRUE after you redeem the voucher and get the mini skirt.
    $ bought_miniskirt = False #Affects 15_mail.rpy
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = False #Turns True when Hermione has the miniskirt.

    $ dress_code = False # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.

    show image "blackfade.png"
    if persistent.game_complete: # Offer for game+
        menu:
            "NEW GAME +" ">Would you like to carry over your gold, books and possessions from your previous playthrough into this one?"
            "\"Yes, please.\"":
                $ gold = gold + persistent.gold
                ">[persistent.gold] gold has been added to your founds."

                if persistent.lolipop >= 1:
                    $ candy = candy + persistent.lolipop # LOLIPOP.
                    ">[persistent.lolipop] pieces of candy have been added to your possessions."

                if persistent.choco >= 1:
                    $ chocloate = chocolate + persistent.choco # CHOCOLATE.
                    ">[persistent.choco] bars of chocolate have been added to your possessions."

                if persistent.owl >= 1:
                    $ owl = owl + persistent.owl # PLUSH OWL.
                    ">[persistent.owl] plush owls have been added to your possessions."

                if persistent.beer >= 1:
                    $ beer = beer + persistent.beer # Beer.
                    ">[persistent.beer] bottles of butterbeer have been added to your possessions."

                if persistent.mag1 >= 1:
                    $ mag1 = mag1 + persistent.mag1 # mag1.
                    ">[persistent.mag1] issues of Educational magazines have been added to your possessions."

                if persistent.mag2 >= 1:
                    $ mag2 = mag2 + persistent.mag2 # mag2.
                    ">[persistent.mag2] issues of girly magazines have been added to your possessions."

                if persistent.mag3 >= 1:
                    $ mag3 = mag3 + persistent.mag3 # mag3.
                    ">[persistent.mag3] issues of adult magazines have been added to your possessions."

                if persistent.mag4 >= 1:
                    $ mag4 = mag4 + persistent.mag4 # mag4.
                    ">[persistent.mag4] issues of porn magazines have been added to your possessions."

                if persistent.krum >= 1:
                    $ krum = krum + persistent.krum # VIKTOR KRUM POSTER.
                    ">[persistent.krum] posters of Viktor Krum have been added to your possessions."

                if persistent.lin >= 1:
                    $ lingerie = lingerie + persistent.lin # lin.
                    ">[persistent.lin] packs of sexy lingerie have been added to your possessions."

                if persistent.con >= 1:
                    $ condoms = condoms + persistent.con # CONDOMS.
                    ">[persistent.con] packs of condoms have been added to your possessions."

                if persistent.vib >= 1:
                    $ vibrator = vibrator + persistent.vib # VIBRATOR.
                    ">[persistent.vib] vibrators have been added to your possessions."

                if persistent.lube >= 1:
                    $ anal_lube = anal_lube + persistent.lube # ANAL LUBRICANT.
                    ">[persistent.lube] jars of anal lubricant have been added to your possessions."

                if persistent.gag >= 1:
                    $ ballgag = ballgag + persistent.gag # BALLGAG.
                    ">[persistent.gag] pairs of ball gags and handcuffs have been added to your possessions."

                if persistent.plug >= 1:
                    $ plug = plug + persistent.plug # ANAL PLUG.
                    ">[persistent.plug] assortments of anal plugs have been added to your possessions."

                if persistent.strap >= 1:
                    $ strapon = strapon + persistent.strap # STRAP-ON.
                    ">[persistent.strap] Thestral Strap-ons have been added to your possessions."

                if persistent.broom >= 1:
                    $ broom = broom + persistent.broom # BROOM.
                    ">[persistent.broom] \"Lady Speed Stick-2000\" brooms have been added to your possessions."

                if persistent.doll >= 1:
                    $ sexdoll = sexdoll + persistent.doll # SEXDOLL.
                    ">[persistent.doll] \"Joanne\" sex dolls have been added to your possessions."

                if persistent.wine >= 1:
                    $ wine = wine + persistent.wine # WINE.
                    ">[persistent.wine] bottles of Dumbledore's wine have been added to your possessions."


            ### THE SKIRT ###
                if persistent.haveskirt: # Makes sure you only need to buy the skirt once. Checked at the +new game screen.
                    $ dress_code = True # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.
                    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
                    ">School miniskirt has been added to Hermione's wardrobe."



#==============================XLJ books=================================================================:
                if persistent.book_01:
                    $books.append("book_01")
                    $book_01_units = 10
                    $concentration += 1
                    $book_01_complete = True
                    ">You remember that you read the book [book01] once. Moreover, it is stored in your personal library surely."


                if persistent.book_02:
                    $books.append("book_02")
                    $book_02_units = 10
                    $concentration += 1
                    $book_02_complete = True
                    ">You remember that you read the book [book02] once. Moreover, it is stored in your personal library surely."

                if persistent.book_03:
                    $books.append("book_03")
                    $book_03_units = 10
                    $concentration += 1
                    $book_03_complete = True
                    ">You remember that you read the book [book03] once. Moreover, it is stored in your personal library surely."


                if persistent.book_04:
                    $books.append("book_04")
                    $book_04_units = 10
                    $concentration += 1
                    $book_04_complete = True
                    ">You remember that you read the book [book04] once. Moreover, it is stored in your personal library surely."


                if persistent.book_08:
                    $books.append("book_08")
                    $book_08_units = 10
                    $s_reading_lvl += 1
                    $book_08_complete = True
                    ">You remember that you read the book [book08] once. Moreover, it is stored in your personal library surely."


                if persistent.book_09:
                    $books.append("book_09")
                    $book_09_units = 10
                    $s_reading_lvl += 1
                    $book_09_complete = True
                    ">You remember that you read the book [book09] once. Moreover, it is stored in your personal library surely."


                if persistent.book_12:
                    $books.append("book_12")
                    $book_12_units = 10
                    $speedwriting += 1
                    $book_12_complete = True
                    ">You remember that you read the book [book12] once. Moreover, it is stored in your personal library surely."


                if persistent.book_13:
                    $books.append("book_13")
                    $book_13_units = 10
                    $speedwriting += 1
                    $book_13_complete = True
                    ">You remember that you read the book [book13] once. Moreover, it is stored in your personal library surely."


                if persistent.book_14:
                    $books.append("book_14")
                    $book_14_units = 10
                    $speedwriting += 1
                    $book_14_complete = True
                    ">You remember that you read the book [book14] once. Moreover, it is stored in your personal library surely."


                if persistent.book_15:
                    $books.append("book_15")
                    $book_15_units = 10
                    $speedwriting += 1
                    $book_15_complete = True
                    ">You remember that you read the book [book15] once. Moreover, it is stored in your personal library surely."



#=======================================XLJ books end==============================================================================

























            "\"No need.\"":
                pass

    jump intro

#    menu:
#        "Вы желаете пропустить интро?"
#        "Начать интро.":
#            jump intro
#        "Пропустить интро.":
#            jump hp
#        "Перейти к дуэли.":
#            jump duel    
    
#    menu:
#        "Would you like to skip the intro?"
#        "Play the intro.":
#            jump intro
#        "Skip the intro.":
#            jump hp


label masterstart:
    stop music fadeout 1
    $ renpy.music.set_volume(1.0, .5, channel=7)

    scene bg meadow
    show sylvie smile
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    show whitefade at basicfade, center
    show magic at basicfade, center
    show magic2 at basicfade2, center
    show magic3 at basicfade3, center
    show magic4 at basicfade4, center
    hide magic
    hide magic2
    hide magic3
    hide magic4
    hide whitefade
    show heal

label masterstart2:
    stop music fadeout 1

    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7

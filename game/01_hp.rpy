label hp:
    stop music fadeout 1
#    $ select = renpy.imagemap("screens/s2pot04.png", "screens/s2pot04b.png", [
#                                            (492, 400, 637, 600, "no"),
#                                            (647, 400, 799, 600, "yes"),
#                                                ])
#    if select == "no":
#        jump fromcsoon
#    if select == "yes":
#        pass

    show screen blkfade

    show image "03_hp/01_bg/00.png"
    pause.1
    scene blkfade
    show image "03_hp/01_bg/00.png"
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    hide screen blkfade
    show magic5
    pause.05
    scene white
    pause.05
    pause.05
    scene white
    pause.05
    show image "03_hp/01_bg/00.png"
    show whitefade at basicfade, center
    #show magic at basicfade, center
    #show magic2 at basicfade2, center
    show magic3 at basicfade3, center
    #show magic4 at basicfade4, center # OVAL
    hide magic
    hide magic2
    hide magic3
    hide magic4
    #hide whitefade
    show heal
    stop music fadeout 1
    pause 1
    hide whitefade
    with d3
    pause 1






###THE GAME STARTS###

$ day = 0

$ ph_feather = 0
$ fullmoon = 0

### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
$ day_of_week = 0 #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
$ report_chapters = 0 #Shows how many chapters of a current report has been completed so far. Resets to zero when report is finished.
$ finished_report = 0 #Shows amount of completed reports.

$ got_mail = False #Turns true is you have WORK mail waiting. Owl will be displayed.
$ got_package = False #Turns TRUE when package from the "Muggle Oddities" catalog has arrived.
$ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
$ mail_from_her = False #Turns TRUE when there is a mail from Hermione. Basically the same as $ got_mail = True.
$ letter_text = []
$ letters = 0 #Shows how many letters are waiting to be read. +1 every new letter arrives. -1 Every time you read one letter.

### GETTING LETTERS ###
$ letter_from_hermione_02 = False #Turns true when you get second letter from Hermione.

###SNAPE STATS###
$ snape_busy = False #When True, you can't summon Snape.
$ snape_friendship = 0 #Get's +1 after every evening spent is Snape's company.
$ snape_events = 0 #Get's +1 point every time a special event with Snape happens.


$ level = "00" #Hermione's whoring level.

$ hermione_takes_classes = False #Turns True when Hermione becomes unavailable for summon after performing personal request in the morning.
$ hermione_sleeping = False



$ tutoring_events = 0 #Get's +1 point every time a tutoring special event happens.
$ knowledge = 0
$ whoring = 0 #Default: 0
$ teachers_pet = 0
$ classmates_pet = 0
$ being_mean = 0 #+1 every time you are being mean to hermione.



$ dates = 0 #Tracks how many times Hermione been tutored.



### CHITCHATS WITH SNAPE ###
$ chitchat_event_01_happened = False
$ chitchat_event_02_happened = False
$ chitchat_event_03_happened = False
$ chitchat_event_04_happened = False
$ chitchat_event_05_happened = False
$ chitchat_event_06_happened = False
$ chitchat_event_07_happened = False


### SPECIAL DATES WITH SNAPE ###

$ date_with_snape_02_happened = False #Second date with Snape. They decide to de-throne Hermione.
                                      #Turns true after event_09

###Miscellaneous flags###
$ hold_all_the_events_please = False #When TRUE all the story events will be put on hold.
$ jerk_off_session = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

$ tutoring_offer_made = False #If you offered her to tutor her (In event_12). Affects conversation in the next event.

$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.


$ snape_against_hermione = False #Turns True after event_01. Activates event_11 when hanging out with Snape next time.
$ snape_against_hermione_02 = False #Turns True after event_09. Activates second event when hanging out with Snape.

$ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (event_09)
$ hermione_is_waiting_02 = False #Turns True at the end of second special event with Snape. Triggers next visit from Hermione

$ phoenix_is_feed = False #When True the graphic of bird food being displayed on top of the phoenix food can.
$ fire_in_fireplace = False #When True there is a fire going in the fireplace.

$ summoning_hermione_unlocked = False #Unlocks after event_14. Adds "Summon Hermione" button to the door.
$ tutoring_hermione_unlocked = False #Unlocks after event_14.
$ buying_favors_from_hermione_unlocked = False


$ hanging_with_snape = False #Turns true when "hanging with Snape during the night time" becomes available. (Snape becomes available for summons).
$ have_catalogue = False #Turns True when you obtain "The muggle oddities" catalog. (The button shows).


$ gifts12 = []


#$ books = ["book_01", "book_02", "book_03", "book_04",  "book_05", "book_06", "book_07", "book_08", "book_09", "book_10", "book_11", "book_12", "book_13", "book_14", "book_15", "book_16", "book_17"]
#All books.

### GENIE STATS ###============================
$ imagination = 1 #+1 for every completed book. Unlocks new sexual favors to buy. 1 point of imagination = 1 level of whoring.
$ job_lvl = 1 #Show how many reports you are allowed to complete per week.
### ===========================================

### BOOKS ###

### FICTION=============================================================================================
$ book_05_units = 0 #Monitors progress with this book.
$ book_05_complete = False #Turns True when you finish reading book #5.
$ book05 = "\"The Tale of Galadriel. Book I.\""

$ book_05_b_units = 0 #Monitors progress with this book.
$ book_05_b_complete = False #Turns True when you finish reading book #5_b.
$ book05_b = "\"The Tale of Galadriel. Book II.\""

$ book_06_units = 0 #Monitors progress with this book.
$ book_06_complete = False #Turns True when you finish reading book #6.
$ book06 = "\"The game of Armchairs\""

$ book_07_units = 0 #Monitors progress with this book.
$ book_07_complete = False #Turns True when you finish reading book #7.
$ book07 = "\"My dear waifu\""
$ shea = 0 #Shows how many times you went on a date with your stepsister Shea.
$ shea_waifu = False #Turns True if you finish the book with Shea.
$ complited_shea_already = False #Turns TRUE when you finish with Shea once. Need so that when you finish with Shea again you don get +1 Imagination.

$ victoria = 0
$ victoria_waifu = False #Turns True if you finish the book with ms.Victoria.
$ complited_stevens_already = False #Turns TRUE when you finish with Ms.Stevens once. Need so that when you finish with Shea again you don get +1 Imagination.

$ leena = 0
$ leena_waifu = False #Completed the book with Leena.
$ complited_leena_already = False #Turns TRUE when you finish with Leena once. Need so that when you finish with Shea again you don get +1 Imagination.
$ waifu_book_completed = False #Turns TRUE when you unlock the harem ending.



### MUGGLE ODDITIES ### =========================================================================
$ order_placed = False #TRUE when and order has been placed on an item.
$ days_in_delivery = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ days_in_delivery2 = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ package_is_here = False # Turns true when days_in_delivery >= 5. Package is displayed.

$ bought_book_01 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_02 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_03 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_04 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_05 = False #Turns TRUE when bought book_05
$ bought_book_06 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_07 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_08 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_09 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_10 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_11 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_12 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_13 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_14 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_15 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_16 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_17 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_18 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_19 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_20 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_21 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_22 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_23 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_24 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_25 = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_book_26 = False #Turns TRUE when bought book_06 (15_mail.rpy)

$ viagra = 0
$ bought_jabri = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_lovepot = False #Turns TRUE when bought book_06 (15_mail.rpy)
$ bought_photo = False

### LEVELING UP PERSONAL REQUESTS ###
$ request_01 = 0 #Genie touches himself.
$ request_02 = 0 #"Lift your skirt".
$ request_02_b_points = 0 #"Flirt with 3 classmates".
$ request_02_c_points = 0 #"Flirt with a teacher".
$ request_03_points = 0 #"Give me your panties."
$ request_04_points = 0 #"Molest tits."
$ request_05_points = 0 #"Molest butt."
$ request_06_points = 0 #"Flash panties to a classmate."
$ request_07_points = 0 #"Flash panties to a teacher."
$ request_08_points = 0 #"Show me your tits."
$ request_09_points = 0 #"Show me your pussy."
$ request_10_points = 0 #"Flash nipple to a classmate."
$ request_11_points = 0 #"Get naked."
$ request_12_points = 0 #"Let me play with your tits."
$ request_15_points = 0 #(Flash a nipple to a teacher)
$ request_16_points = 0 #(Finger her pussy)
$ request_17_points = 0 #(Stick a finger up her butthole.)
$ request_18_points = 0 #(Handjob).
$ request_19_points = 0 #(Rub dick against her cheeks.)
$ request_20_points = 0 #(Grab a classmate's cock)
$ request_21_points = 0 #(Cum on tits).
$ request_22_points = 0 #(Blowjob).
$ request_23_points = 0 #(Give handjob to a classmate)
$ request_24_points = 0 #(Flash your tits to a teacher)
$ request_25_points = 0 #(Cum on face and with enough whoring send to class with face covered in cum.)
$ request_26_points = 0 #(Go to class with mouth full of cum).
$ request_27_points = 0 #(Blow two classamates).
$ request_28_points = 0 #(Give handjob to a teacher).
$ request_29_points = 0 #(Sex).
$ request_30_points = 0 #(Blow a teacher)
$ request_31_points = 0 #(Anal sex)
$ request_32_points = 0 #(Wear a very revealing outfit to class)



$ phx_ingr1 = 0
$ phx_ingr2 = 0
$ phx_ingr3 = 0
$ phx_ingr4 = 0


$ flirt_req = 0
$ date_req = 0
$ kiss_req = 0
$ mats_req = 0
$ fap_req = 0
$ minet_req = 0
$ fuck_req = 0


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




###PERSONAL REQUESTS#####
$ request_02_b = False #Flirt with 3 classmates.
$ request_02_c = False #Flirt with a teacher.
$ request_03 = False #Turns True when Hermione is sent on request No.3. (Goes to class without panties).
$ request_05 = False #Turns True when Hermione is sent on request No.5. (Flash panties to a classmate).
$ request_06 = False #Turns True when Hermione is sent on request No.6. (Flash panties to a teacher).
$ request_10 = False #Turns True when Hermione is sent on request No.10. (Flash a nipple to a classmate).
$ request_13 = False #Turns True when Hermione is sent on request No.13. (Wear a see-through shirt to class).
$ request_15 = False #Turns True when Hermione is sent on request No.15. (Flash a nipple to a teacher).
$ request_20 = False #Turns True when Hermione is sent on request No.20. (Grab a classmate's cock).
$ request_21 = False #Turns True when Hermione is sent on request No.21. (Jerk off on tits and put the clothes back on).
$ request_23 = False #Turns True when Hermione is sent on request No.23. (Give handjob to a classmate).
$ request_24 = False #Turns True when Hermione is sent on request No.24. (Flash your tits to a teacher).
$ request_25 = False #Turns True when Hermione is sent on request No.25. (Cum on face and send to class).
$ request_26 = False #Turns True when Hermione is sent on request No.26. (Go to class with mouth full of cum).
$ request_27 = False #Turns True when Hermione is sent on request No.27. (Blow two classamates).
$ request_28 = False #Turns True when Hermione is sent on request No.28. (Handjob to a teacher).
$ request_30 = False #Turns True when Hermione is sent on request No.30. (Blowjob to a teacher).
$ request_32 = False #Turns True when Hermione is sent on request No.32. (Put on a slutty dress and go to classes).
$ request_33 = False #Turns True when Hermione is sent on request No.33. (Go to classes with cum covered face).

# EVENTS #==============================================================================================================================================
### EVENT 01 ####
$ desk_examined = False #Turns True when you did examine you desk on day one.
$ cupboard_examined = False
$ bird_examined = False
$ door_examined = False
$ fireplace_examined = False

###SCREENS### NO NEED FOR THIS ONE ANYMORE. (SHOWS WHORING THOUGH).
screen statistics: #более подробно см. здесь http://www.renpy.org/doc/html/screens.html
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 630 ypos 20#отступ для текста, если надо прямо в левом углу — убираем его
        text "{size=-3}Day: [day]\nWhoring: [whoring]\nLevel: [level]\nKnowledge: [knowledge]\nSlytherin [slytherin]\nGryffindor [gryffindor]\nS.Freind: [snape_friendship]\nDay of week: [day_of_week]\nConcentration: [concentration]\nSpeedwriting: [speedwriting]{/size}" #сумма текстом



###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start:

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME
$ ogon = 0
$ chimi_chated = 0
$ harry_chated = 0
$ phoenix_ev = 0
$ daphne_chated = 0
$ phoenix_chated = 0
$ daph_publ = 0

# +++++++++++++++++++++++++++++++++==================================+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.

$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.


### MENU PLACEMENT ###
$ menu_x = 0.5 #Just to make sure that menu is displayed in the center of the screen by default.

### RESETING STUFF ###
$ only_upper = False #When true, legs are not displayed in the hermione_main screen.
$ autograph = False #Displays professor Lockhart's autograph on Hermione's leg.
$ no_blinking = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm = False #Shows cum stains on Hermione's uniform.

$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.
$ only_upper = False #When False legs are displayed in the hermione_main acreen.

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen phoenix_food
hide screen done_reading
hide screen done_reading_02
hide screen candlefire_01 #CANDLE FIRE.
hide screen candlefire_02 #CANDLE FIRE.
hide screen lightening #Hide lighting so it won't get stuck during clear sky weather and such.
hide screen cloud_night_01 #NIGHT CLOUDS.
hide screen cloud_night_02 #NIGHT CLOUDS.
hide screen cloud_night_03 #NIGHT CLOUDS.
hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.

if whoring >= 0 and whoring <= 2:
    $ level = "01"
if whoring >= 3 and whoring <= 5:
    $ level = "02"
if whoring >= 6 and whoring <= 8:
    $ level = "03"
if whoring >= 9 and whoring <= 11:
    $ level = "04"
if whoring >= 12 and whoring <= 14:
    $ level = "05"

if whoring >= 15 and whoring <= 17:
    $ level = "06"

if whoring >= 18 and whoring <= 20:
    $ level = "07"

if whoring >= 21 and whoring <= 23:
    $ level = "08"

if whoring >= 24 and whoring <= 26:
    $ level = "09"

if whoring >= 27 and whoring <= 29:
    $ level = "10"

if whoring >= 12 and not touched_by_boy: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached whoring level 05 while public event "Touched by boy" never attempted. Locks public events.



$ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
$ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
$ generating_points_gryffindor = renpy.random.randint(1, 10) #Addying point to Gryffindor (07_points_gry.rpy)
$ generating_points_hufflepuff = renpy.random.randint(1, 10) #Addying point to Hufflepuff (07_points_gry.rpy)
$ generating_points_ravenclaw = renpy.random.randint(1, 10) #Addying point to Ravenclaw (07_points_gry.rpy)

$ one_out_of_three = renpy.random.randint(1, 3) #Generating one number out of three for various porpoises.
$ i_of_iv = renpy.random.randint(1, 4) #Generating one number out of three for various porpoises.
$ one_of_five = renpy.random.randint(1, 5) #Generating one number out of three for various porpoises.
$ i_of_vii = renpy.random.randint(1, 7)
$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
$ one_of_tw = renpy.random.randint(1, 20) #Generating one number out of three for various porpoises.
$ cheatFastDelivery = False

### CUPBOARD MONEY GENERATOR ###

$ gold1 = renpy.random.randint(1, 10) # Money you find in the cupboard when Whoring Level: 1-2.
$ gold2 = renpy.random.randint(10, 40) # Money you find in the cupboard when Whoring Level: 3-4.
$ gold3 = renpy.random.randint(20, 50) # Money you find in the cupboard when Whoring Level: 5-6.
$ gold4 = renpy.random.randint(30, 90) # Money you find in the cupboard when Whoring Level: 7+.



$ daytime = True #True when it is daytime. Turns False during nighttime.
$ hermione_sleeping = False
$ hermione_takes_classes = False
$ snape_busy = False
$ fire_in_fireplace = False
hide screen fireplace_fire

### EVENTS RELATED FLAGS ###
$ days_without_an_event +=1


### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        #$ got_mail = True comented out because being replaced with $ letters += 1
$ day_of_week += 1

### HERMIONE ###
if mad >= 1:
    $ mad -= 1

if daphne_moral < 5:
    $ daphne_moral += 1

if (whoring > 8) and (mizul == 0):
    $ mizul = 1
    $ letters += 1

if (whoring > 12) and (letters == 0) and (paper_level == 0):
    $ letters += 1
    $ paper_level = 1

if (paper_money == 1) and (letters == 0):
    $ letters += 1

if playwizard == 4 and letters == 0:
    $ letters += 1
    

if paper_level >= 34 and letters == 0 and playwizard == 0:
    $ letters += 1
    $ playwizard = 1

if hermione_pod_skirt > 1:
    $ hermione_pod_skirt = 0

if (playwizard > 4) and (playwizard != 7):
    $ playwizard += 1
### MUGGLE ODDITIES RELATED FLAGS ###
#if order_placed: #TRUE when and order has been placed on an item.
#    $ days_in_delivery +=1
#    if days_in_delivery >= 3: # BY DEAFULT WAS 5. Changed for testing.
#        $ package_is_here = True
#        $ order_placed = False



### MUGGLE ODDITIES RELATED FLAGS ### VERSION TWO. This one randomizes delivery waiting days.
if order_placed: #TRUE when and order has been placed on an item.
    $ days_in_delivery2 -=1
    if days_in_delivery2 <= 0:
        $ package_is_here = True
        $ order_placed = False



scene black
$ raining = False #No rain before the weather has been chosen at the beginning of every day.
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.


$ wather_generator = renpy.random.randint(1, 100)
#$ wather_generator = 99 #THIS LINE IS FOR TESTING. 99 = Rain.
if wather_generator >= 81 and wather_generator <= 90: # RAIN
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 1 and wather_generator <= 40: # CLEAR WEATHER.
    show screen new_window # показываем заглушку за окном #<<<XALJIO------------------------------------------XALJIO!!!!!!!!!!!
    #show image "03_hp/01_bg/03_weather.png"
elif wather_generator >= 41 and wather_generator <= 60: #Floating cloud
    show screen new_window # показываем заглушку за окном #<<<XALJIO------------------------------------------XALJIO!!!!!!!!!!!
    show screen cloud #THE CLOUD.
    #show image "03_hp/01_bg/03_weather.png"
    #show cloud_01 at Position(xpos=280, ypos=215, xanchor="center", yanchor="center")
elif wather_generator >= 61 and wather_generator <= 80: # CLOUDY WEATHER
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 91 and wather_generator <= 100: # RAIN WITH LIGHTENING.
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation


#show image im.Alpha("03_hp/01_bg/01_main_room.png", 0.5) #Transparent Background.




hide screen room_night #Hiding NIGHT BG from last night.
show screen room #Showing main room BG.

hide screen door
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
if package_is_here:
    hide screen package


show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candle_02



### DAY MAIL ###
if day == 2:
    $ letter_from_hermione_02 = True #Turns true when you get second letter from Hermione.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if day == 12: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ work_unlock = True # Send a letter that will unlock an ability to write reports.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if package_is_here:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen package
show screen genie


if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl



if devil > 8:
    $ evil_days += 1

if (daphne_event >= 15) and (daphne_event < 21):
    $ daphne_event += 1
#hide screen statistics
#show screen statistics

hide screen points
show screen points

with fade

$ day +=1

### DAY EVENTS ###<============================================================================================================================================================


if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
    call chitchat_event_01 from _call_chitchat_event_01


if request_30_a: #Hermione does not show up. This sends to label where she shows up next morning.
    call new_request_30_complete_a from _call_new_request_30_complete_a

#NOT IN USE if day == 4: #Genie says: "I wonder what has become of that two-faced dude?"
#About two-faced dude    call event_04


if (dap_level == 2) and (daphne_event < 7):
    call daph_snape2 from _call_daph_snape2

#if chimi_event == 13:
#    call harry_demon

if daphne_event == 13:
    call last_jurnalist from _call_last_jurnalist

if (daphne_event > 17) and (daphne_event < 100) and (daytime == True):
    call after_all from _call_after_all


if chimi_event == 6:
    call chimi_after from _call_chimi_after

if devil == 8:
    call after_demon from _call_after_demon

if day == 8:
    call event_08 from _call_event_08 #Hermione shows up for the first time.
if day >= 9 and hermione_is_waiting_01 and not event09:
    call event_09 from _call_event_09 #Second visit from Hermione. Says she sent a letter to the Minestry.
                  #Takes place after first special event with Snape, where he just complains about Hermione.
if event13_happened and not event14_happened:
    call event_14 from _call_event_14

if whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    call want_to_rule from _call_want_to_rule

if whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    call against_the_rule from _call_against_the_rule

if whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    call crying_about_dress from _call_crying_about_dress # 27_final_events

if whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    call sorry_about_hesterics from _call_sorry_about_hesterics



### NOT IN USE
#if day == 10:
#    call event_08_02 #Hermione shows up for the second time. (Shorter skirts notion).
#if day == 11:
#    call event_08_03 #Hermione shows up for the third time. (Rules for teachers noton).
if day >= 12 and not event09 and hermione_is_waiting_01:
    call event_09 from _call_event_09_1 #Visit from Hermione after first Special event with Snape (Where Genie proposes plan against her).
### NOT IN USE
#if day >= 13 and not event10 and hermione_is_waiting_02:
#    call event_10 #Hermione shows up for the third time. Says that she started "MRM" and sent letter to the ministry.
if event13_happened and not event14_happened:
    call event_14 from _call_event_14_1

### EVENTS ### (COMMENTED OUT FOR THE TESTING PORPOISES) ===============================================================================================================================
if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
    call event_01 from _call_event_01


if chimi_event == 17:
    call harry_after_attack from _call_harry_after_attack



if snape_fap == 1:
    call snape_daph_chat from _call_snape_daph_chat

if (whoring > 6) and (duels == 0):
    call duels from _call_duels

if (daphne_event == 3) and (days_without_an_event >= 2):
    call daph_snape from _call_daph_snape

if (daphne_event == 4) and (days_without_an_event >= 2):
    call daph_second from _call_daph_second

if (daphne_event == 5) and (days_without_an_event >= 2):
    call daph_norm from _call_daph_norm



if (devil > 7) and (evil_days > 2) and (devil < 10) and (days_without_an_event >= 2):
    call snape_dial from _call_snape_dial

if (devil > 7) and (evil_days > 3) and (mkg_trg == 0) and (days_without_an_event >= 2):
    call thank_mak from _call_thank_mak

if (devil > 7) and (evil_days > 10) and (devil < 10) and (days_without_an_event >= 2):
    call fenix_rape from _call_fenix_rape

if phx_ingr2 == 3:
    call snape_ingr2 from _call_snape_ingr2

if phx_ingr3 == 3:
    call svinoril from _call_svinoril


if (devil > 7) and (evil_days > 10) and (devil < 11) and (days_without_an_event >= 2):
    call second_demon from _call_second_demon

if (evil_days > 4) and (harry_event == 0) and (days_without_an_event >= 2):
    call harry_first from _call_harry_first

if (evil_days > 14) and (harry_event == 1) and (days_without_an_event >= 2):
    call harry_2 from _call_harry_2



if chimi_event == 10:
    call snape_propaja from _call_snape_propaja

label day_main_menu:


if phoenix_is_feed:
    show screen phoenix_food



if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
    show screen bld1
    with d3
    m "It's getting darker already..."
    m "Did I just spend an entire day with examining this room?"
    hide screen bld1
    with d3
    jump night_start

















show screen animation_feather
call screen main_menu_01










####NIGHT STARTS HERE###<<<<<<<<<<<-----------------------------------------------------------------------------------------------------###
###=====================================================================================================================================###
label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC





$ daytime = False
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.


$ chimi_chated = 0
$ harry_chated = 0
$ daphne_chated = 0


stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

scene black

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen done_reading #Hiding genie sitting with closed book in his hands.
hide screen done_reading_02 #Done reading by the fire
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.

hide screen lightening #Hide lighting so it wouldn't get stuck during clear sky weather and such.
###WEATHER
if wather_generator >= 81 and wather_generator <= 90: # RAIN WITH LIGHTENING.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 1 and wather_generator <= 30: #Clear sky with stars.
    show image "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 41 and wather_generator <= 50: #Clear sky with stars 02. (floating cloud during the day).
    show image "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 31 and wather_generator <= 40: #CLEAR FULL MOON.
    $ phoenix_ev = 1
    show image "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 51 and wather_generator <= 60: #FULL MOON WITH CLOUDS
    $ phoenix_ev = 1
    show screen cloud_night_01
    show screen cloud_night_02
    show screen cloud_night_03
    show image "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 61 and wather_generator <= 80: #HEAVY CLOUDS.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Lighting

elif wather_generator >= 91 and wather_generator <= 100: #RAIN.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation





if package_is_here:
    hide screen package
hide screen room #Hiding main room BG.
show screen room_night #Showing main room NIGHT BG.
hide screen door
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02

show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candlefire_01 #CANDLE FIRE.
show screen candle_02
show screen candlefire_02 #CANDLE FIRE.
if package_is_here:
    show screen package
show screen genie

#hide screen statistics
#show screen statistics

hide screen points
show screen points

if got_mail or mail_from_her or letters >= 1:
    show screen owl
with fade







call points_changes from _call_points_changes #Makes changes in the Slytherin house points.
call points_changes_gryffindor from _call_points_changes_gryffindor #Makes changes in the Gryffindor (And the rest of the houses) house points. (07_points_gry.rpy)
# call snape_bonus # Not in use anymore.




### NIGHT REQUESTS ###

if request_02_b:
    call new_request_02_b_complete from _call_new_request_02_b_complete
if request_02_c:
    call new_request_02_c_complete from _call_new_request_02_c_complete
if request_03:
    call new_request_03_complete from _call_new_request_03_complete
if request_05:
    call new_request_05_complete from _call_new_request_05_complete
if request_06:
    call new_request_06_complete from _call_new_request_06_complete
if request_10:
    call new_request_10_complete from _call_new_request_10_complete
#if request_13: # SEE THROUGH SHIRT DURING CLASS. NOT USED.
#    call request_13_complete
if request_15: #(Flash a nipple to a teacher).
    call new_request_15_complete from _call_new_request_15_complete
if request_20: #(Grab a classmate's cock).
    call new_request_20_complete from _call_new_request_20_complete
if request_21: #(Jerk off on tits and put the clothes back on).
    call new_request_21_complete from _call_new_request_21_complete
if request_23: #(Give handjob to a classmate).
    call new_request_23_complete from _call_new_request_23_complete
if request_24: #(Flash your tits to a teacher).
    call new_request_24_complete from _call_new_request_24_complete
if request_25: #(Cum on face and send to class).
    call new_request_25_complete from _call_new_request_25_complete
if request_26: #(Go to class with mouth full of cum).
    call new_request_26_complete from _call_new_request_26_complete
if request_27: #(Blow two classmates).
    call new_request_27_complete from _call_new_request_27_complete
if request_28: #(Handjob to a teacher).
    call new_request_28_complete from _call_new_request_28_complete
if request_30: #(FUCK A CLASSMATE).
    call new_request_30_complete from _call_new_request_30_complete
if request_32: #(Put on a slutty dress and go to classes).
    call new_request_32_complete from _call_new_request_32_complete
if request_33: #(Go to classes with cum covered face).
    call new_request_33_complete from _call_new_request_33_complete



if daphne_publ_request == 1:
    call truci_completed from _call_truci_completed

if daphne_publ_request == 2:
    call flirt_completed from _call_flirt_completed

if daphne_publ_request == 3:
    call date_completed from _call_date_completed

if daphne_publ_request == 4:
    call grud_completed from _call_grud_completed

if daphne_publ_request == 5:
    call mats_completed from _call_mats_completed

if daphne_publ_request == 6:
    call fap_completed from _call_fap_completed

if daphne_publ_request == 7:
    call minet_completed from _call_minet_completed

if daphne_publ_request == 8:
    call fuck_completed from _call_fuck_completed

if quest_hagrid == 4:
    call harry_potion from _call_harry_potion

if quest_hagrid == 6:
    call hermione_potion2 from _call_hermione_potion2



if paper_students == 1:
    call paper_students_01 from _call_paper_students_01

if paper_students == 3:
    call paper_students_02 from _call_paper_students_02

if paper_students == 5:
    call paper_students_03 from _call_paper_students_03

if paper_prepods == 1:
    call paper_prepods_01 from _call_paper_prepods_01

if paper_prepods == 3:
    call paper_prepods_02 from _call_paper_prepods_02

if paper_prepods == 5:
    call paper_prepods_03 from _call_paper_prepods_03

if paper_prepods == 7:
    call paper_prepods_04 from _call_paper_prepods_04

if paper_prepods == 9:
    call paper_prepods_05 from _call_paper_prepods_05

if paper_podder == 1:
    call paper_podder_01 from _call_paper_podder_01


if paper_podder == 3:
    call paper_podder_02 from _call_paper_podder_02


if paper_podder == 5:
    call paper_podder_03 from _call_paper_podder_03


if paper_comand == 1:
    call paper_comand_01 from _call_paper_comand_01

if paper_comand == 3:
    call paper_comand_02 from _call_paper_comand_02

if paper_comand == 5:
    call paper_comand_03 from _call_paper_comand_03

if paper_comand == 7:
    call paper_comand_04 from _call_paper_comand_04

if paper_holm == 1:
    call paper_holm_01 from _call_paper_holm_01

if paper_holm == 3:
    call paper_holm_02 from _call_paper_holm_02
if paper_holm == 5:
    call paper_holm_03 from _call_paper_holm_03

if paper_forest == 1:
    call paper_forest_01 from _call_paper_forest_01
if paper_forest == 3:
    call paper_forest_02 from _call_paper_forest_02
if paper_forest == 5:
    call paper_forest_03 from _call_paper_forest_03

if paper_room == 1:
    call paper_room_01 from _call_paper_room_01
if paper_room == 3:
    call paper_room_02 from _call_paper_room_02

if paper_room == 5:
    call paper_room_03 from _call_paper_room_03

if paper_puffend == 1:
    call paper_puffend_01 from _call_paper_puffend_01

if paper_puffend == 3:
    call paper_puffend_02 from _call_paper_puffend_02

if paper_puffend == 5:
    call paper_puffend_03 from _call_paper_puffend_03

if paper_kogt == 1:
    call paper_kogt_01 from _call_paper_kogt_01

if paper_kogt == 3:
    call paper_kogt_02 from _call_paper_kogt_02
if paper_kogt == 5:
    call paper_kogt_03 from _call_paper_kogt_03
if paper_slytherin == 1:
    call paper_slytherin_01 from _call_paper_slytherin_01
if paper_slytherin == 3:
    call paper_slytherin_02 from _call_paper_slytherin_02
if paper_slytherin == 5:
    call paper_slytherin_03 from _call_paper_slytherin_03

if playwizard == 7:
    call herm_jurnal from _call_herm_jurnal




### NIGHT EVENTS ###


if daphne_event == 14:
    call daphne_last_event02 from _call_daphne_last_event02


if (phoenix_ev == 1) and (chimi_event == 13) and (ogon2 != 0):
    call cho_uznat from _call_cho_uznat

if phx_pot == 4:
    call hermione_phx_potion from _call_hermione_phx_potion

if phx_ingr2 == 3:
    call snape_ingr2 from _call_snape_ingr2_1




if day == 1:
    call event_02 from _call_event_02
if day == 2:
    call event_03 from _call_event_03
if day == 4:
    call event_05 from _call_event_05
if day == 5:
    call event_07 from _call_event_07

if (harry_event == 2) and (chimi_event == 0):
    call chimi_gang_bang from _call_chimi_gang_bang

if days_without_an_event >= 2 and hermione_is_waiting_02 and not event11_happened:
    call event_11 from _call_event_11
if days_without_an_event >= 2 and event11_happened and not event12_happened:
    call event_12 from _call_event_12
if days_without_an_event >= 2 and event12_happened and not event13_happened:
    call event_13 from _call_event_13
if days_without_an_event >= 2 and chitchat_event_01_happened and not event15_happened:
    call event_15 from _call_event_15



if gave_the_dress and days_without_an_event >= 2: #$ gave_the_dress = True #Turns True when Hermione has the dress.
    jump good_bye_snape















label night_main_menu:


if phoenix_is_feed:
    show screen phoenix_food

show screen animation_feather
call screen main_menu_01


pause
show ch_hem 01 at Position(xpos=732, ypos=350, xanchor="center", yanchor="center")
pause


show ch_hem walk_01 at Move((732, 350), (300, 350), 5.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)
pause 5.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause

show ch_hem run_f at Move((300, 350), (732, 350), 2.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)

pause 2.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause










### INIT ###

init -2:

    $ l_blush = False # Turns on blushing in the l_head screen. (Lola).
    $ l_things = False # Turns on cheerful emotion symbol in l_screen. (Lola).
    $ l_question = False # Turns on question mark emotion symbol in l_screen. (Lola).
    $ l_drop = False # Turns on drop emotion symbol in l_screen. (Lola).
    $ l_hearts = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_exclamation = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_tears = False # Turns on tears in l_screen. (Lola).

    $ config.autoreload = False

     ### SACRED SCROLLS ###

    $ sscroll_01 = False # Turns TRUE if the scroll had been bought.
    $ sscroll_02 = False
    $ sscroll_03 = False
    $ sscroll_04 = False
    $ sscroll_05 = False
    $ sscroll_06 = False
    $ sscroll_07 = False
    $ sscroll_08 = False
    $ sscroll_09 = False
    $ sscroll_10 = False

    $ sscroll_11 = False # Turns TRUE if the scroll had been bought.
    $ sscroll_12 = False
    $ sscroll_13 = False
    $ sscroll_14 = False
    $ sscroll_15 = False
    $ sscroll_16 = False
    $ sscroll_17 = False
    $ sscroll_18 = False
    $ sscroll_19 = False
    $ sscroll_20 = False

    $ sscroll_21 = False # Turns TRUE if the scroll had been bought.
    $ sscroll_22 = False
    $ sscroll_23 = False
    $ sscroll_24 = False
    $ sscroll_25 = False
    $ sscroll_26 = False
    $ sscroll_27 = False
    $ sscroll_28 = False
    $ sscroll_29 = False
    $ sscroll_30 = False

    $ scroll_01_name = "The room"
    $ scroll_02_name = "The calendar"
    $ scroll_03_name = "The girl"
    $ scroll_04_name = "Deeptroating"
    $ scroll_05_name = "Poster 01"
    $ scroll_06_name = "Poster 02"
    $ scroll_07_name = "Chibi-dancing"
    $ scroll_08_name = "Game items"
    $ scroll_09_name = "Panties no panties"
    $ scroll_10_name = "A lot of pegs"

    $ scroll_11_name = "House-elf brothel"
    $ scroll_12_name = "Me and Lola"
    $ scroll_13_name = "Hard training"
    $ scroll_14_name = "Wizard's Chess"
    $ scroll_15_name = "Tutoring books"
    $ scroll_16_name = "Extra gifts 01"
    $ scroll_17_name = "Extra gifts 02"
    $ scroll_18_name = "Fiction books"
    $ scroll_19_name = "Singer whore"
    $ scroll_20_name = "Casting"

    $ scroll_21_name = "Witch robe 01"
    $ scroll_22_name = "Witch robe 02"
    $ scroll_23_name = "Witch robe 03"
    $ scroll_24_name = "Witch robe 04"
    $ scroll_25_name = "The walk"
    $ scroll_26_name = "Durmstrang"
    $ scroll_27_name = "Gag ball"
    $ scroll_28_name = "New clothes 01"
    $ scroll_29_name = "New clothes 02"
    $ scroll_30_name = "The gang"











#методы движения через ATL надо объявлять в этом блоке
    transform cloud_move: #Метод ATL для задания движения облаков. Более продвинутый и современный, чем move. Про его возможности читать здесь: http://www.renpy.org/wiki/atl
        xpos 408 #координата X, из которой облако начинает движение
        choice: #Функция, для выбора случайного значение из (в данном случае) пяти заданных для высоты облака. Можно хоть 20 выборов задать.
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 7
        repeat # повтор движения


    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408 #координата X, из которой облако начинает движение
        choice:
            ypos 130
        choice:
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 150 #высота, на котором плывет облако
        linear 30.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения

    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408 #координата X, из которой облако начинает движение
        choice:
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 170 #высота, на котором плывет облако
        linear 70.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения

    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408 #координата X, из которой облако начинает движение
        ypos 160 #высота, на котором плывет облако
        linear 50.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения










label assmenu: # Sent here from "EXTRAS" menu. Basically just jumps to the title screen.
    return

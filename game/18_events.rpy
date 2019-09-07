label event_00:

    play music "music/Dark Fog.mp3" fadein 1 fadeout 1


    #show screen snape_01 #OWL SITTING ON A PACKAGE.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen snape_01 #Snape stands still.
    with Dissolve(.5)
    pause.3
    show screen bld1
    with d3
    g4 "{size=-3}(Коренные формы жизни!?){/size}"
    hide screen bld1
    with d3
    $ tt_xpos=650
    $ tt_ypos=180
    show screen thought
    with Dissolve(.3)
    pause 1
    show screen bld1
    with d3
    m "{size=-3}(Выглядит как человек...){/size}"
    m "{size=-3}(Может быть, если я буду вести себя тихо, оно уйдет...?){/size}"
    hide screen bld1
    with d3
    hide screen thought
    with Dissolve(.3)

    $ walk_xpos=610 #Animation of walking chibi. (From) 610
    $ walk_xpos2=360 #Coordinates of it's movement. (To) 360



    $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01
    pause 4
    show screen snape_02 #Snape stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    pause
    sna "Альбус...есть минута?"
    hide screen snape_main
    hide screen ctc

#    show screen ctc
#    pause
#    pat "I hate to ask but its been bugging me for awhile."
#    pat "What is your Guesstimated time of completion for the game?"
#    pat "No pressure to give an answer if you don't want to."
#    show screen snape_main
#    with d3
#    sna "Mister silvarius..."
#    sna "This is your first strike..."
#    sna "If I hear this question from you again, then it will cost your house 100 points."

#    hide screen snape_main
#    with d3
#    show screen emo
#    her "Professor... *gulp!* I-- I can't breathe!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I will be with you in a moment, мисс Грейнджер..."
#    hide screen snape_main
#    with d3
#    show screen emo
#    her "!!!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I hope we came to an understanding, here, mister silvarius."
#    sna "Didn't we?"


    #m "{size=-3}(\"Albus\"? Is that supposed to be my name or is that's just how the humans of this world greet one another?){/size}"
    menu:
        m "..."
        "\"На самом деле я немного занят.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main
            with d3
            sna "Но ведь не постоянно?"
        "\"Конечно. Что там?\"":
            pass
        "\"И Альбус тоже.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main
            with d3
            sna "Что?"
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            sna "Альбус, я не в настроении для ваших... издевательств."
        "\"Отведи меня к своему боссу.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main
            with d3
            sna "Что?"
            hide screen snape_main
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main
            with d3
            sna "Хм...?"
            sna "Вы имели в виду министра магии?"
            hide screen snape_main
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main
            with d3
            sna "Я хотел бы избежать каких-либо дел с этими бюрократами..."
            m "Ладно, проехали... Как я могу помочь тебе?"

    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "У меня есть важный разговор к тебе..."
    sna "Я думаю, нам стоит пересмотреть политику допуска."
    hide screen snape_main
    with d2
    m "................?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen snape_main
    with d2
    sna "Половина моих...так называемых \"учеников\" не что иное, как раздражающие личинки, которые портят мне жизнь день ото дня"
    hide screen snape_main
    with d2
    m "................"
    $ s_sprite = "03_hp/10_snape_main/snape_07.png"
    show screen snape_main
    sna "Большинство из них из \"Гриффиндора\", конечно же..."
    hide screen snape_main
    with d2
    m "......?"
    show screen snape_main
    sna "Несчастные Уизли, шумная Грейнджер и, конечно же, герой всех несовершеннолетних правонарушителей...."
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    sna "{size=+3}Мальчишка Поттер!{/size}"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Запомни мои слова, Альбус. \"Гриффиндор\" станет погибелью для это школы!"
    hide screen snape_main
    m "...................."
    show screen snape_main
    sna "Многие из них не представляют абсолютно ничего!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "И если этого не достаточно то вот: они распространили разные слухи о преподавателях!"
    sna "В частности и о вашем покорном слуге..."
    hide screen snape_main
    m "......................"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main
    sna "Вы ведь не верите в эти слухи, так, Альбус?"
    hide screen snape_main
    menu:
        m ".............."
        "\"Ну, нет конечно!\"":
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main
            sna "Хорошо..."
            sna "Вы знаете меня лучше, чем я сам. Меня бы не волновали такие вещи..."
        "\"Не бывает дыма без огня.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"
            show screen snape_main
            sna "Альбус!? Ты можешь быть серьезным!"
            sna "Я вам говорю, это все грязная ложь!"
    hide screen snape_main
    m "........................."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen snape_main
    sna "Ну, эти жалкие дети достали меня сегодня, я думаю, что следует отдохнуть от всего сегодня."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    sna "................"

    stop music fadeout 1.0

    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk) 360
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door) 610
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen. Default - .03
    show screen snape_walk_01_f
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f
    with d4
    pause.5
    show screen bld1
    with d3
    m "Хм..."
    m "И так, этот высокий задумчивый парень принял меня за другого...?"
    m "Следовательно я, по всей вероятности, под действием маскирующего заклинания..."
    m "........."
    m "В свою очерень я джинн, замаскированный под человека, который в свою очередь замаскирован под другого человека..."
    m "Нет, все это очень глупо..."
    a4 "Заткнись! Никто не понимает истинных гениев."

#    who2 "Professor Dumbldore, do you have a minute?"
#    m "{size=-3}(What? Another one?){/size}"
#    who2 "Let me speak to him!"
#    m "Excuse me?"
#    who2 "Y-yes master..."
#    who2 "Greetings to you, oh almighty genie..."
#    with hpunch
#    g4 "{size=+7}What the hell?!{/size}"
#    g4 "{size=+7}Stay away from me, you demon!!!{/size}"
#    g4 "{size=+7}Body snatchers are among us!\nI'm outta here!{/size}"
#    m "...wait a second."
#    m "How did you just call me?"
#    who2 "An almighty genie. That is what you are, is it not?"
#    g4 "How did you... Who the hell are you?"
#    who2 "Oh, but of course. Forgive me my poor manners..."
#    who2 "Master's name is Tom Riddle..."
#    who2 "No! You sniveling maggot! we hate that name!"
#    who2 "We want to be called Lord Voldemort!"
#    who2 "Forgive me, master..."
#    m "Эм... mr. Lord- -"
#    with hpunch
#    who2 "No! No! \"lord\" is not master's name, \"lord\" is master's title, you idiot!"
#    who2 "Watch your tone, worm! That is an immortal being before you."
#    who2 "He may look human, but his powers topple mine by far."
#    who2 "Please take no offense, oh almighty one. My servant is quite dim."
#    menu:
#        m "..."
#        "\"Does the sun take offense from an ant?\"":
#            who2 "And yet it is prudent for an ant to know it's place, wouldn't you agree?"
#        "\"Watch it, mortal! I'll smite you!\"":
#            who2 "My humble apologies. The worthless servant shall be punished properly."
#            who2 "M-master...?"
#        "\"Apology accepted. What do you want?\"":
#            who2 "You are unusually forgiving for a genie. But we shall not test your patience anymore..."

#    vol "Correct me if we are wrong, but you came to our world due to an accident..."
#    m ".................."
#    vol "And you find our world intriguing, do you not?"
#    m "You have two faces growing out of your head. So yeah, colour me curious."
#    who2 "Splendid..."
#    who2 "In that case we want to make you an offer..."
#    who2 "We...."
#    who2 "We...."
#    m "???"
#    who2 "We are tired... Cover us..."
#    who2 "Of course, master."
#    m "What? What's going on?"
#    vol "My apologies, oh immortal one. My master needs to rest now."
#    vol "We will visit you again soon..."
#    m "..................."
#    g4 "What the....?"
#    m "Ah, hell. May as well stay for one more day..."

    $ days_without_an_event = 0

    jump day_start




###############################################################################################################################################################

label event_01: #First event in the game. Gennie finds himself at the desk.


    show screen bld1
    with d3
    m "..................?"
    m "Ваше высочество?"
    m "......................................................."
    g4 "Я сделал это снова?"
    g4 "Телепортировал себя не понятно куда..."
    m "Что с этими ингредиентами?"
    m "Они кажется мощнее, чем я думал."
    m "Ну, не важно что это за место, дел у меня тут нет..."
    m "Лучше обернуть заклинание вспять, иначе принцесса будет снова злиться на меня..."
    m "....................."
    m "Хотя..."
    m "Есть в этом месте что-то странное... это..."
    m "Оно наполненно...."
    g4 "{size=+5}МАГИЕЙ?!{/size}"
    m "Да... магия, я чувствую. Такая мощная и в свою очередь..."
    m "....чужая."
    m "Интересно..."
    m "Я думаю, необходимо осмотреться здесь..."
    hide screen bld1
    with d3
    return
###############################################################################################################################################################
label event_02:
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
    #$ mail_from_her = True #Comented out because replaced with $ letters += 1
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl
    show screen bld1
    with d3
    m "Что? Сова?"
    hide screen bld1
    with d3
    return

###############################################################################################################################################################
label event_03:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "{size=-3}(Снова этот задумчивый парень...){/size}"
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    who2 "Альбус!"
    m "Эй.......... ты..."
    who2 "Тебе что-то нужно сделать с этой девченкой Грейнджер..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Честно... Я намекаю на наказания... как..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Эта маленькая ведьма!"
    menu:
        m "..."
        "\"Грейнджер? Гермиона Грейнджер, так?\"":
            who2 "Да, она..."
            who2 " Она одна из \"группировки Поттера\"."
        "\"Я на вашей стороне, Джэк, ведьмы просто сумашедшие!\"":
            who2 "Что...? Альбус, ты ведешь себя странно в последнее время."
            who2 "Все в порядке?"
            menu:
                m "..."
                "\"Да, все отлично. Продолжай.\"":
                    who2 "Как скажешь..."
                "\"Ты меня знаешь. Обожаю подкалывать.\"":
                    who2 "Хм....."

        "\".....................................................\"":
            pass
    who2 "Помните, как раньше пороли студентов?"
    who2 "Я клянусь, наши проблемы решились бы в миг, если бы мы вернули все обратно..."
    who2 "Да... Я бы с удовольствием отпорол эту девку перед всей школой..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_20.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Затем поднял юбку и..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_12.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "*Кхм!* К сожалению, на данный момент учителя очень ограничены в возможностях наказания учеников..."
    who2 "Я знаю, что вы так же, бессильны, как и я, но я говорю вам, что этой девке лучше прекратить испытывать мое терпение."
    menu:
        m "..."

        "\"Я позабочусь об этой шлюхе!\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "...?!"
            who2 "Альбус..."
            who2 "Ты ведешь себя странно..."
        "\"Никто не говорил, что будет легко.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Иногда мне кажется, что уж лучше оказаться в комнате полной дементоров..."
        "\"Вам станет лучше сегодня.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ты как всегда рад..."
    who2 "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Может быть мне лучше вздремнуть."
    who2 "Мне нужно быть в отличной форме завтра утром..."
    who2 "Если вы дадите слабину с этими детьми, то они сожрут вас целиком..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Доброй ночи, Альбус."


    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f
    pause 3
    hide screen snape_walk_01_f
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    who2 "................."
    who2 "Еще кое что..."
    show screen bld1
    show screen snape_main
    with Dissolve(.3)
    who2 "Игнорируйте любую ложь обо мне и тех девченках из Слизерина..."
    m "Само собой."
    hide screen bld1
    hide screen snape_main
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    jump day_start
###############################################################################################################################################################
label event_04:
    m "Ну, уже три дня прошло..."
    m "Интересно, что стало с этим двуличным чуваком?"
    return
###############################################################################################################################################################
label event_05: #Snape comes in, has a talk with Genie, then the duel starts.

    play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    who2 "Добрый вечер, Альбус."
    who2 "Я хочу поговорить с вами о тех проклятых детях..."
    who2 "Но сначала хочу у вас кое-что спросить..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Заметили ли вы, что-нибудь странное здесь в последнее время?"
    menu:
        m "..."
        "{size=-2}\"Как то, что вы постоянно ноете?\"{/size}":
            who2 "Что? Н-но... Эти дети..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ну, все же ты прав..."
        "{size=-2}\"Эта сова приносит мне письма, чувак!\"{/size}":
            who2 "Сова? Что-то не так?"
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Это не то, что я имею в виду..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ладно, забудь..."
#        "\"I Saw a dude with two faces the other day.\"":
#            who2 "?!"
#            who2 "What's that supposed to mean...?"
        "{size=-2}\"Нет, не совсем. Все как обычно.\"{/size}":
            who2 "Хм... Может я начал параноить..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Я здесь из-за этой \"группировки Поттера\""
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Есть несколько моментов, из-за которых стоит вычесть очки у Гриффиндора"
    who2 "И Грейнджер стала худшим примером из всех них за последнее время..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Она фактически идет под натиском."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Кстати, она не присылала вам какие-либо письма недавно?"
    menu:
        m "..."
        "\"Гермиона Грейнджер? Нет, ничего не было.\"":
            who2 "Понятно... Видимо она блефует."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Что за тупая ведьма."
        "\"Да... Каждый чертов день...\"":
            who2 "Действительно?"
            who2 "Есть что-то обо мне в частности?"
            who2 "Я надеюсь вы знаете меня хорошо и не будете слушать ее..."

    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Она никогда не признается, но именно она распространяет эти скверные слухи обо мне..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Ох... Эта шумная маленькая ведьма..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Я бы никогда не опустился до того, чтобы обменивать сексуальные утехи за очки для дома."
    who2 "Я имею в виду, мы используем очки, чтобы мотивировать студентов, чтобы ..."
    who2 "Я не могу говорить за других..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Истории, которые я слышу о Минерве МакГонагалл и этих бедных первокурсников Гриффиндора могут быть правдой..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Ну, я хотел бы убедиться, что ты не принимаешь слухи всерьез..."
    who2 "Эту скверную ложь распространяют дети."


    who2 "О.... Перед тем, как я уйду..."
    who2 "Есть один вопрос, который я обязан тебе задать..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Как меня зовут?"
    menu:
        m "..."
        "\"Что? Что это вообще за вопрос?\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ты прав..."
            who2 "Прости меня... Я последнее время слишком параною..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Но вам стоит быть осторожнее со слухами о том, что \"сами знаете кто\" жив и все такое..."
        "\"Высокий задумчивый парень\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Альбус, в последнее время у вас весьма своеобразное чувство юмора..."
            who2 "Вероятно, тебе стоит тратить меньше времени в компании с этим здоровяком Хагридом."
        "- \{Использовать магию для получения правильного ответа\} -":
            $ d_flag_01 = True
            hide screen snape_main
            with d3
            show screen blktone
            with d3
            ">Вы можете использовать ваши феноменальные космические силы, чтобы заглянуть в саму материю Вселенной и получить правильный ответ."
            hide screen blktone
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "!!?"
            m "Что за вопрос, Северус?"
            who2 "Прости меня...Последнее время я параною, вероятно."


    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "В таком случае, доброй ночи, Альбус."
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f
    pause 3
    hide screen snape_walk_01_f
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2




    stop music fadeout 1.0
    who2 "........................"
    hide screen snape_01_f
    hide screen bld1
    hide screen snape_main
    hide screen snape_02 #Snape stands still.
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3')
    pause 2
    g4 "???"

    show screen snape_defends
    hide screen blkfade
    with d3
    show screen ctc



    play music "music/hitman.mp3" fadein 1 fadeout 1 # TENSE THEME


    pause
    hide screen ctc
    show screen bld1
    with d3
    if d_flag_01:
        sna_06 "Кто ты такой, сволочь!"
        g4 "Что? Это я... эм... Абиус! То есть, Альбус!"
        sna_04 "Ты не надуришь меня."
        sna_04 "Только что ты использовал какую-то чужеродную магию!"
        sna_06 "Яви для меня свою истинную сущность, дьявол! Кто ты такой?!"
    else:
        sna_01 "Мое имя Северус Снейп!"
        sna_01 "Теперь твоя очередь...?"

    g4 "!!!"
    sna_01 "Полегче... Просто ответь на мой вопрос."

    m "Ладно, ладно. Можешь просто успокоиться?..."
    sna_01 "........"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait:
    menu:
        m "..."
        "\"Я тебе не враг.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_01 "Это первое, что сказал бы враг."
        "\"Я просто турист. Я уже ухожу.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_01 "У тебя ничего не выйдет."
        "\"Я работаю на Альбиса Думблдора!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_01 "Его зовут Альбус Дамблдор, ты, придурок!"
    if d_points == 2:
        pass
    else:
        jump no_wait

    sna_01 "Кто тебя послал сюда? Что ты сделал с настоящим Альбусом?"
    sna_01 "Покажи свои истинную сущность, последнее предупреждение!"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait_2:
    menu:
        m "..."

        "\"Я не могу. Это сложно объяснить...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_01 "У меня нет малейшего интереса к твоим объяснениям. Я бы все равно не поверил ни единому слову!"
        "\"Хватит угрожать мне, человек!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_01 "\"Человек\"?"
            sna_01 "Ты намекаешь на то, что ты {size=+5}не{/size} один из нас?"
            sna_01 "Что ты такое!? Немедленно отвечай, иначе я применю чары для снятия твоей маскировки!"
        "\"Я не причиню тебе вреда, клянусь!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_01 "Точно?"
            sna_01 "Докажи это. Сними свою маскировку немедленно!"

    if d_points == 2:
        pass
    else:
        jump no_wait_2



    sna_01 "Я услышал достаточно!"
    g4 "Во имя великих песков пустыни! Человек, ты дашь мне объясниться?!"
    sna_01 "Уже нечего объяснять!"
    sna_01 "Пока вы отказываетесь сотрудничать, вы будете под стражей!"
    g4 "Что?! Подожди!"


    stop music
    $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
    play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    $ end_u_1_pic =  "glass"
    pause.1
    show screen end_u_1
    hide screen snape_defends
    pause 3




    jump duel

###############################################################################################################################################################
label event_06: #THE TALK AFTER THE DUEL ENDS.
    $ potions = 0 #Makes sure there are no potions left in the possessions.

    #play music "music/Final Fantasy VII - Victory Fanfare.mp3" fadein 1 fadeout 1
    stop music fadeout 2.0
    g4 "*Задыхаясь*"
    g4 "Теперь ты готов поговорить?!"
    sna_08 "(...н-невероятно...)"

    play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    hide ch_gen
    show image "03_hp/04_duel/no_magic.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")

    m "Я сказал, что ты мне не ровня..."
    show screen bld1
    with d3
    m "Хотя, ты оказался неплох..."
    sna_01 "Ты колдовал заклинания голыми руками..."
    sna_01 "Если ты не человек, то... кто- -"
    sna_04 "{size=+5}Что ты такое?{/size}"
    sna_01 "Какой-то демон, призванный \"сам знаешь кем\"?"
    m "Призванный кем?"
    sna_02 "\"Сам знаешь кем\"!"
    m "Что?"
    sna_07 "......................"
    m "............................"
    m "Послушай, я не демон..."
    m "И само собой я не работаю на  \"сам не знаю кого\"!"
    sna_01 "............................."
    m "Я был хм..."
    m "...Я проводил эксперимент в своем мире и что-то пошло не так, вот я и здесь."
    m "Это все..."
    sna_01 ".........................."
    sna_01 "Тогда, что же стало с настоящим Альбусом Дамблдором?"
    m "Я уверен, он в порядке."
    m "Он, вероятно, очень удивлен, оказавшись в чужом мире, собственно как и я..."
    sna_01 "...................................."
    sna_01 "Когда это произошло?"
    m "Дня четыре назад..."
    sna_01 "Ты можешь вернуться назад?"
    m "Я думаю, что..."
    sna_02 "Почему ты еще не сделал этого?"
    m "Не уверен..."
    m "В этом мире очень странная магия... Мне просто стало любопытно."
    sna_01 "..................."
    sna_01 "Тебе нужно все исправить..."
    m "Исправить что?"
    sna_04 "Все. Тебе нужно вернуть Альбуса и самому вернуться обратно."
    menu:
        m "..."

        "\"Да, да, знаю. Тогда я пойду.\"":
            m "Да, да, я знаю..."
            m "Ну, тогда я пойду. Извини за все это."
            sna_01 "Хорошо, что никто не пострадал..."
        "\"Но мне нравится здесь! Могу я остаться?\"":
            sna_01 "Категорически нет."
            sna_01 "Кем бы ты не был, ты не из этого мира."
            sna_01 "Твое присутствие здесь сильно нарушает порядок вещей в мире."
            sna_01 "И в эти дни школа нуждается в хорошем директоре, как никогда ранее."
    sna_01 "Безопаснее всего венуться обратно именно сейчас."
    m "Хм ... Спасибо, господин Северус. Удачи с вашими студентами и \"шайкой Поттера\"."
    sna_01 "\"Шайка Поттера\"?"
    sna_07 "Ах, точно, эти пидерасты..."
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass

    sna_01 "Сработало? Это ты, Альбус?"
    menu:
        m "..."
        "\"Да, это Я. Как хорошо вернуться обратно!\"":
            sna_01 "Рад, что ты здесь. Ты в порядке?"
            m "Я в порядке, Северус, спасибо."
            sna_01 "Как там, в другом мире?"
            m "Очень много песка и довольно жарко, но все таки относительно неплохо."
            sna_01 "Понимаю... Ты соскучился по своему брату?"
            menu:
                m "..."
                "\"Да, я соскучился по тебе очень сильно!\"":
                    sna_01 "......................."
                    sna_01 "Да, точно...."
                "\"У меня нет брата, Северус.\"":
                     sna_01 "........................"
                     sna_01 "У вас может и нет, но у настоящего Альбуса Дамблдора он есть."
                "- Использовать магию, для получения правильного ответа -":
                    show screen bld1
                    with d3
                    ">Вы используете свою космическу силу, чтобы заглянуть в саму материю Вселенной и узнать правильный ответ."
                    hide screen bld1
                    with d3
                    m "Мой младший брат Аберфорт? Почему я должен соскучиться по нему?"
                    sna_01 "Я каждый раз чувствую, когда ты используешь свою странную магию..."
        "\"Не-а. Это все еще я. Не человеческий-чувак.\"":
            pass


    sna_01 "Почему ты все еще здесь, существо?"
    m "Я не уверен... Я пытался обратить заклинание, но ничего не вышло..."


    sna_07 "Чудеса..."
    sna_01 "Что это значит? Ты собрался остаться здесь навсегда?"
    m "Конечно нет..."
    m "Я здесь, возможно, только по тому, что заклинание компенсации дисбаланса вызвало само себя..."
    m "Если отменить заклинание, то я должен вернуться обратно в свой мир."
    m "Кроме того, твой друг Дамблдор тоже должен будет вернуться обратно сюда."
    sna_01 "Понимаю..."
    sna_01 "Как долго заклинание будет действовать?"
    menu:
        m "..."
        "\"Пару дней.\"":
            sna_01 "Понятно..."
        "\"Неделя или...\"":
            sna_01 "Хм.... Неделя, хух..."
        "\"Может быть месяцы...\"":
             sna_01 "Так долго?"
             sna_01 "Почему все настолько \"плохо\"?"
        "\"Я понятия не имею...\"":
            sna_01 "....................."
            sna_02 "Великолепно..."

    m "Хорошо, если честно, я не уверен, куда идти теперь..."
    m "Все это время, я думал, что смогу отметить заклинание когда захочу..."
    sna_01 "..................................................."
    sna_01 ".................................."
    sna_01 "..................."
    m "Снейп?"
    sna_01 "..................................................."
    m "Северус?"
    sna_06 "Да, да ..."
    sna_01 "Слушай, уже поздно и очень многое успело произойти..."
    sna_07 "Мне следует обдумать все это."
    sna_01 "Увидимся завтра, я зайду после занятий."
    sna_06 "до тех пор, держи свою истинную личность и наш разговор в тайне, идет?"
    m "Без проблем."
    sna_01 "Отлично, тогда..."
    sna_01 "Но перед тем, как я уйду, один вопрос..."
    m "Я слушаю..."
    sna_02 "........"
    sna_01 "Если ты не человек, тогда..."
    sna_07 "Что ты?"
    m "...Я джинн."
    sna_01 "Джинн?"
    m "Да, я обладаю крутой космической силой и все такое..."
    sna_01 "Серьезно?"
    m "О, да."
    sna_01 "Невероятно..."
    sna_01 "Ну, увидимся завтра.... джинн."
    m "Я буду здесь..."

    sna_07 "(Джинн? Что-то новое...)"
    jump day_start
###############################################################################################################################################################
label event_07: #THE TALK WITH SNAPE THE DAY AFTER THE DUEL.
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    sna "..................."
    hide screen snape_main
    with d3
    m "Добрый вечер..."
    show screen snape_main
    with d3
    sna "Заклинание все еще работает?"
    hide screen snape_main
    with d3
    m "Да, до сих пор."
    show screen snape_main
    with d3

    sna "Понятно..."
    sna "Прошой ночью я...ломал голову над нашей головоломкой."
    sna "И мне кажется, у меня есть решение..."
    m "Действительно? Отлично! Я слушаю."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ tt_xpos=300 #Defines position of the Snape's full length sprite. Right - 300  # 120 - center.          #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Давай просто продолжим эту игру..."
    m "Что?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, а что еще мы можешь сделать"
    sna "Обычно я предупредил бы министерство магии и уже они позаботились бы об этом..."
    sna "Но лучше я избегу каких-либо отношений с этими бюрократами..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Кроме того, потеря директора, хоть и временная, может сильно ранить репутацию школы..."
    sna "А что если ваше заклинание спадет завтра или даже сегодня ночью?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Я не вижу причин для паники..."
    m "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Исходя из всего этого, нам стоит просто играть свои роли..."

    m "Что именно делать?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Просто делай все как Альбус: не выходи из башни и не контактируй с людьми..."
    m "Это...."
    m "Звучит..."
    g4 "Невероятно скучно!"
    g4 "Чем мне здесь заниматься?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ты джинн. Сотвори что-нибудь для себя."
    m "Моя магия толком не работает здесь..."
    m "И моя лампа вообще в другом мире..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, а что вы скажете насчет этого?"
    sna "Может быть прислать вам парочку девок из Слизерина?"
    g9 "Понятия не имею, что такое \"Слизерин\", но думаю, это поможет..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Это шутка."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хотя..."
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, в любом случае я не представляю как развлечь {size=+7}тебя{/size} в этой ситуации."
    m "Да, но это!"
    m "Я бессмертен и всемогущ..."
    m "Это самое скучное, что могло произойти со мной!"
    g4 "Я нахожусь в маленьком запертом помещении и мне абсолютно нечего делать!"
    g4 "Я могу потерять сознание..."
    g4 "Ох! Ах! Я думаю уже начал!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "......."
    g4 "Я теряю сознание! Становится труднее дышать!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "...."
    g4 "Очень темно.."
    g4 "Ты все еще здесь?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "...."
    m "........."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ты закончил?"
    m "Да..."
    m "Серьезно, я сомневаюсь, что это пойдет мне напользу"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "У тебя есть другое предложение?"
    m "Я могу..."
    m "Вместо того, чтобы просто сидеть на заднице в этом кабинете, я бы мог исследовать ваш мир..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хорошо, что ты хочешь?"
    m "Научи меня твоей магии..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Моей магии?"
    m "Да... Как вы колдуете заклинания..."
    m "ИНтригует..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ладно, да будет так..."
    m "О, и пришли мне пару этих \"Слизеринских\" девок конечно же.."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "..............."
    sna "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ха-ха-ха!!!"
    m "Что? Что я такого сказал?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "А-ха-ха-ха-ха.."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Нет, нет, мои извинения..."
    sna "Это просто...ты все еще выглядишь и говоришь для меня как Альбус..."
    sna "Услышать от профессора Дамблода что-то вроде \"Пришли мне этих девок\"..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "У меня истерика... "
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Но ты не понял..."
    m "Хех..."
    g9 "Отправь мне этих шлюх, Северус. Я очень одинок вечерами."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ха-ха-ха! Прекрати, ты убьешь меня!"
    sna "А-ха-ха-ха!"
    m "Нет, я серьезно... Это возможно?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    sna "Увидим..."
    sna "Ты, в роли нашего директора, очень полезен для меня..."
    sna "Мне нужно некоторое время, чтобы выяснить, как я могу использовать нашу ситуацию в моих интересах."
    m "Ты имеешь в виду {size=+7}наших{/size} интересах, верно?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "О, да,да конечно..."
    sna "Ну, думаю на сегодня мы закончили..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Доброй ночи... джинни."
    m "Да, доброй ночи, Северус."

    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f
    pause 3
    hide screen snape_walk_01_f
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2

    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "\"Пришли мне этих шлюх, Северус!\" Ха-ха-ха..."
    hide screen s_head2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with d3
    m "Хм... "
    m "Полагаю, я просто свернусь клубком на этом столе и посплю..."
    pause.2
    show screen notes
    $ renpy.play('sounds/win2.mp3')
    show screen blktone
    with d3
    ">Теперь вы можете вызывать Снейпа в свой кабинет."
    hide screen blktone
    with d3
    $ hanging_with_snape = True

    jump day_start

###############################################################################################################################################################
label event_08: # HERMONE SHOWS UP FOR THE FIRST TIME. IN USE.
    #"EVENT_08"
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    m "Хах?"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    pause.7
    m "Кто-то стучит в дверь..."
    m "Черт... Я должен избегать любых контактов с людьми!"
    m "Хм... Каковы шансы, что это стучится не человек?"
    m "Ага, достаточно малы..."
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    m "Настойчивый ублюдок..."
    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.
    menu:
        m "..."
        "\"Кто это?\"":
            $ d_flag_01 = True
            who "Это я, профессор..."
            who "Гермиона Грейнджер. Могу я войти?"
            m "{size=-4}(Это та девка, которая засыпала меня своими письмами...){/size}"
            menu:
                m "..."
                "\"Уходи, пожалуйста. Я занят.\"":
                    her "Но, профессор, мне действительно нужно поговорить с вами..."
                    m "..........................................."
                    her "Профессор? Я вхожу!"
                    m "{size=-4}(Дерьмо...){/size}"
                "\"Да, да. Конечно входи.\"":
                    pass
        "\"Входите!\"":
            pass
        "\"Уходи!\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Но, профессор, мне действительно нужно поговорить с вами..."
            m "..........................................."
            who "Профессор? Я вхожу!"
            m "{size=-4}(Дерьмо...){/size}"
        "\"................\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Профессор, вы здесь?"
            m "{size=-4}(Уходи...){/size}"
            who "Но, профессор, мне действительно нужно поговорить с вами..."
            m "..........................................."
            her "Профессор? Я вхожу!"
            m "{size=-4}(Дерьмо...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 610
    $ hermione_chibi_ypos = 250
    show screen hermione_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(Девочка?){/size}"

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause 3
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    show screen ctc
    with Dissolve(.3)
    pause
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Доброе утро профессор."
    hide screen ctc
    menu:
        "\"Доброе утро... девочка.\"":
            her "{size=-4}(\"Девочка\"?){/size}"
            pass
        "\"Доброе утро, Гермиона.\"" if d_flag_01:
            pass
        "\"Доброе утро, Дитя.\"":
            her "{size=-4}(\"Дитя\"...?){/size}"
        "\"................................\"":
            pass
    her "Я была очень занята , но сегодня утром у меня есть немного времени, чтобы встретится с вами, профессор."
    her "Вы, наверное, знаете почему я здесь."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Тот вопрос, который я безуспешно пыталась довести до вашего внимания в последнее время."
    her "Я не могу понять, почему вы ничего не предпринимаете, чтобы остановить это!"
    her "Это не может больше продолжаться!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Такого рода неравенство начинает сказываться на факультетах..."
    her "Все потому, что мы более сплоченны, нежели остальные..."
    her "Как вы думаете, это справедливо, что те кто заслуживают быть лидерами, отстают от других?"
    her "Как вы думаете? Справедливо?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    m "{size=-4}(Вы только посмотрите на эту миленькую девчушку){/size}"
    m "{size=-4}(Только посмотрите ... Она восхитительна.){/size}"
    m "{size=-4}(Черт, я не видел женщину целую неделю){/size}"
    menu:
        "\"(Подрочить под столом, пока она говорит.)\"":
            $ jerk_off_session = True #Affects next conversation with Snape.
            $ d_flag_01 = True #If TRUE genie jerks off under the desk.
        "\"(Нет, это глупо! Мне нужно вести себя нормально!)\"":
            $ d_flag_01 = False #NOT JERKING OFF.
            pass
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        with d3
        show screen blktone8
        with d3
        ">Вы опустили руки под стол и обхватили свой член..."
        hide screen blktone8
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
    m "Да, продолжай, дорогая."
    $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen bld1
    with d3
    her "\"Да\"?! То есть это справедливо?"
    m "О, конечно нет, я хотел сказать \"нет\". Но все равно продолжай..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Стало легче на душе. Я рада, что вы согласны со мной, профессор..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Как я уже говорила, это просто смешно, и я не могу поверить, что это происходит сейчас и с нами!"
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        show screen blktone8
        with d3
        ">*Фап!* *Фап!* *Фап!*"
        ">Вы продолжаете дрочить свой член..."
        hide screen blktone8
        with d3
        show screen hermione_main
        show screen bld1
        with d3
    else:
        m "Понятно..."
    her "Я хочу сказать, что поняла, если бы это произошло несколько сотен лет назад..."
    her "Но мы давно прошли это, не так ли?"
    if d_flag_01:
        g9 "{size=-4}(Вы только посмотрите на эти розовые щечки? Хочу потыкать в них своим членом.){/size}"
        hide screen hermione_main
        show screen blktone8
        with d3
        ">Вы продолжаете дрочить..."
        hide screen blktone8
        show screen hermione_main
        with d3
    else:
        m "Эм... Я полагаю, что вы сделаете, то есть мы сделаем все, что нужно."
    her "Это навредит системе распределения очков для факультетов."
    her "Но и это не конец!"
    her "Так же это навредит нашей системе образования..."
    her "И что еще более важно - мотивация среди студентов неуклонно сокращается из-за этого!"
    if d_flag_01:
        m "{size=-4}(Посмотрите на эти огромные сиськи.){/size}"
        m "{size=-4}(Да... Я хочу зажать свой член между ними...){/size}"
    her "Как вы можете наблюдать, ситуация весьма тяжелая..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но мы все еще можем уладить..."
    her "Как сообщил представитель нашего Школьного Студентческого Совета..."
    her "У меня есть пара предложений, как сделать это более эффективно."
    if not d_flag_01:
        m ".............."
    her "Прежде всего, система очков для факультетов должна стать более сложной!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вам нужно контролировать распределение очков чуть лучше, сэр."
    if d_flag_01:
        g4 "{size=-4}(Да, шлюха... Грязная шлюха... Бьюсь об заклад, ты обожаешь сосать члены... Не так ли? Да, уверен в этом...){/size}"
        hide screen hermione_main
        with d3
        show screen blktone8
        with d4
        ">Вы неистово надрачиваете свой твердейший член!"
        hide screen blktone8
        with d4
        show screen hermione_main
        with d3
    her "Конечно, вы согласны со мной, профессор, не так ли?"
    if d_flag_01:
        g4 "{size=-4}*Тяжело дыша*{/size}"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Профессор...?"
        g4 "{size=-4}(Дерьмо. О чем она только что говорила?){/size}"
        g4 "Да, это так. Продолжай..."
        her "Эм... И так, как я сказала..."
        hide screen hermione_main
        with d3
        m "{size=-4}(Ох... Отлично вздрочнул, но я уже близок к \"великому финалу\".){/size}"
        m "{size=-4}(Может быть мне стоит прекратить пока не произошло чего.){/size}"
        menu:
            "\"(Да, думаю стоит послушать ее.)\"":
                show screen genie
                with d3
                $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
                pass
            "\"(Нет! Я должен закончить!)\"":
                pass
    else:
        m "{size=-4}(Должен ли Я? Да плевать...){/size}"
        m "Хм... Предпологаю, что должен..."
        her "{size=-4}(\"Пологаете\"?){/size}"
        her "{size=-4}(Почему-то профессор Дамблдор такой... равнодушный.){/size}"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Еще одна мера, которую стоит принять это более жестокий контроль за сотрудниками..."
    her "Особенно за учителями..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я надеюсь, что не переступаю черту, но некоторые учителя действительно требуют надзора..."
    if d_flag_01:
        g4 "{size=-4}(Да! Ты маленькая шлюха! Тупая маленькая шлюха!) *Задыхаясь*{/size}"
    else:
        m "......................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я понимаю, что у вас нет времени на все это. Вы деректор нашей школы и очень важный и занятой человек."
    her "Временами, оставаться лучшей ученицей довольно трудно для меня..."

    g4 "{size=-4}(Она сказала \"стояк\"!?) *задыхаясь*{/size}"
    her "Но вы могли бы предоставить эту задачу мне..."
    her "Просто всадить свою веру в меня."
    if d_flag_01:
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Да, вы должны! Просто всадите ее в меня!"
        stop music fadeout 1.0
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=-4}(О дерьмо, что она наделала!) *Аргх!*{/size}"
        hide screen hermione_main
        with d3
        hide screen bld1
        with d3
        show screen genie_jerking_sperm
        with d3
        pause 3

        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
        show screen bld1
        with d3
        show screen hermione_main
        with d3
        her "Профессор!? Что происходит...?"
        show screen genie_jerking_sperm_02
        with d3
        g4 "А... ДААААА.....!"
        her "???"
        g4 "*Тяжело дыша* Да! Да...."
        show screen genie
        #show screen genie_jerking_off
        with d3
        m "Да, девочка. Все именно так, как ты говоришь. Я позабочусь обо всем этом."
    else:
        m "Хорошо, я подумаю о твоем предложении. Обещаю."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Правда?"
    her "Хм..........."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это обнадеживает. Спасибо, Профессор."
    if d_flag_01:
        m "Нет, нет. Спасибо тебе..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Хм..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Мои занятия вот-вот начнутся. Мне лучше пойти."
    her "Спасибо за уделенное время..."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    if d_flag_01:
        m "{size=-4}(Это офигительно...) *Задыхаясь*{/size}"
        m "{size=-4}(Мои трусы просто уничтожены...){/size}"
    else:
        m "................."
        m "(Она симпатичная, но довольно трудолюбивая...)"
    hide screen genie_jerking_sperm_02
    with d3
    $ snape_against_hermione = True #Turns True after event_08. Activates special date with Snape # 01.
    $ event08_happened = True
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    return

### FOLLOWING EVENT IS NOT IN USE ANYMORE ###
###############################################################################################################################################################
label event_08_02:
    "EVENT_08_02"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер."
            m "(Снова эта молоденькая ведьма...)"
            her "Профессор, я вхожу..."
            m "{size=-4}(Crap!){/size}"
        "\"Да, входи...\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"


    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)

    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Почему он настолько снисходительный все время?){/size}"
            m "Что-то не так?"
            her "Нет, ничего сэр..."
        "\"Доброе утро, шлюха.\"":
            her "Eм... Что?"
            g4 "{size=-4}(ОК, это было глупо. Контролировать гнев, контролировать гнев !){/size}"
            m "*Кхм* Извините, что-то застряло в горле... Доброе утро, мисс Грейнджер."
            her "{size=-5}(Он назвал меня.... нет, показалось.){/size}"

    her "Профессор Дамблдор, Я здесь, чтобы поговорить с вами, как  президент \"ОПЗМП\"..."
    m "............."
    her "Мы провели чрезвычайное собрание вчера..."
    her "Главным вопросом была \"Хогвартская\"униформа для девочек..."
    her "Мы пришли к выводу, что в настоящее время дресс-код является весьма нецелесообразным для образовательного учреждения..."
    show screen ctc
    pause
    her "..."
    m "Серьезно?"
    hide screen ctc
    her "Да, профессор, Уверяю вас, я очень серьезна."
    her "Мы ищем способ заставить наших бедных девочек носить  платье ..."
    her "Сейчас они носят легкомысленные наряды и отвлекает мужчин от учебы, ставя их в невыгодное положение..."
    her "Все это отвлекающие факторы..."
    her "Бедные души..."
    m "Кто-нибудь из ребят жалуется на это?"
    her "Мы не будем ждать, пока проблема существует, сэр! Мы будем бороться с ней!"
    her "Ни один человек не должен находиться в невыгодном положении, в зависимости от пола."
    her "Это называется \"Сексизм\" в мире Маглов, сэр."
    m "Ваши объяснения  слишком запутанные, на мой взгляд, мисс Грейнджер."
    m "Скажите мне, что вы предлагаете , заставить каждую женщину носить паранджу в школе?"
    her "Удвоение длины юбки для девочек в школе было бы достаточно..."
    menu:

        "{size=-4}\"Это смешно. Отказано!\"{/size}":
            $ d_flag_05 = True #Notion refused. Will take affect in the next event.
            her "Что... Н-но? Мы приняли решение..."
            m "Мисс Грейнджер, Мне жаль , но я все еще директор этой школы..."
            m "И все решения  зависят от моего слова!"
            her "Значит вы игнорируете выбор народа, сэр?"
            m "Единственный голос, который я слышу ваш, мисс Грейнджер."
            her "Разве вы не знаете, что происходит с тиранами, которые недооценивают силы народа?"
            her "Их свергают!"
            m "Осторожно. Ваши слова пахнут изменой, юная леди."
            m "Разве вы не знаете, что происходит с предателями?"
            m "Их вешают!"
            her "!!!"
            her "Тцк!"
            her "Я добьюсь,чтобы вы восприняли наше решение всерьез, профессор!"

        "{size=-4}\"Нет сексизму. Просьба удовлетворена!\"{/size}":
            her "Великолепно. Я все сделаю."
            her "Спасибо профессор."
            hide screen bld1
            hide screen hermione_main
            with Dissolve(.3)
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_walk_01_f
            pause 2
            hide screen hermione_walk_01_f
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            pause.5
            m "...................."


    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "Я начинаю наслаждаться нашими встречами все меньше и меньше..."
    return
#NOT IN USE###############################################################################################################################################################
label event_08_03:
    "EVENT_08_03"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    m "Кто..."
    her "Профессор, я вхожу..."
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    her "Доброе утро, профессор Дамблдор."
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)

    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Он должны быть настолько снисходительной все время? Противный старый хер!){/size}"
            m "Что-то не так?"
            her "Ничего сэр..."
        "\"Доброе утро, мисс президент.\"":
            her "{size=-4}(Это звучало как сарказм?){/size}"


    if not d_flag_05:
        her "Вы мне обещали принять меры, профессор..."
        her "Но ничего не изменилось с момента нашего последнего разговора..."
        menu:

            "\"Я солгал...\"":
                her "Н-но..."
                her "Но вы директор школы, сэр. Вы слово должно означать что-то..."

            "\"Я забыл\"":
                her "Вы забыли, сэр?"
                her "Вы это серьезно?"
                her "Или, может быть, вы просто не хотите заниматься этим?"
            "\"Меня просто это не волнует.\"":
                her "Н-но....?"
                her "Профессор Дамблдор, это серьезный вопрос!"

    else:
        her "Профессор Дамблдор,вы отвергли предложение которое я дала вам когда мы прошлый раз мы встретились..."
        her "И теперь мы пожинаем результаты..."
    her "Ребятам все  еще трудно сосредоточиться на учебе..."
    m "О, у меня есть решение,!"
    m "Давай наденем на головы девушке бумажные пакеты!"
    her "Это тоже плохое обращение человека на основе ее пола..."
    her "Другой пример сексизма..."
    her "Это называется \"Женоненавистничество\"."
    m "\"Женоненавистничество\" - это общая неприязнь к женщинам, мисс Грейнджер."
    m "Здоровый мужчина  биологически неспособны нравится все самки его вида..."
    m "В противном случае человечество бы вымерло давным-давно уже..."
    her "Профессор, у нас нет времени для семантики."
    her "Вся школа находится в опасности!"
    m "Неужели..?"
    her "\"MRM\" встретились еще вчера, и- -"
    m "Нет, опять..."
    m "Существуют ли какие-либо мужские члены в вашей маленькой группе  \"Men's rights movement\"?"
    her "Это не относиться к дела"
    m "Ладно..."
#    her "That is irrelevant..."
#    m "How is it irrelavant? That's the only thing that {size=+7}IS{/size} relevant!"
    her "Позвольте мне закончить мое предложение, пожалуйста."
    her "Я официально к вам обращаюсь, как президент \"ОПЗМП\"..."
    her "И как представитель этой школы ..."
    her "Мы требуем чтобы эти новые нормы, подлежали соблюдению..."
    her "Во-первых..."
    her "Чтобы ни один школьный учитель не позволял повышать голос в сторону студента или обзывать студента..."
    m "Что?"
    her "Во-вторых..."
    her "Все школьные призраки должны быть заключены только в заброшенной башни в Северном крыле школы."
    m "У Вас есть привидения? Это очень круто!"
    her "В-третьих..."
    her "Каждый учитель, и особенно профессор Северус Снейп должны проходить проверку квалификации каждые три месяца..."
    m "Это все?"
    her "Это все, сэр."
    menu:
        m "..."
        "\"Хорошо. Ваши требования будут удовлетворены.\"":
            her "Спасибо, профессор."
            her "Я, как представитель студентов , благодарю за ваше сотрудничество."
        "\"Звучит как бред. Вы свободны\"":
            her "Что? Я..."
            her "Но это ... вы не можете..."
            m "Свободны!"
            her "Тцк..."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."

    $ snape_against_hermione = True #Turns True after event_08_03. Activates event_09 when hanging out with Snape next time.


    return




##################################################################################################################
label event_09: #Second visit from Hermione. Says she sent a letter to the Minestry.
                #Takes place after first special event with Snape, where he just complains about Hermione.

    #"EVENT_09"
    stop music fadeout 3.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер."
            m "Снова эта маленькая ведьма..."
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Конечно нет! Я занят! Возвращайся позже!\"":
                    her "Но..."
                    her "Хорошо... Тогда я зайду к вам завтра..."
                    return
                "\"Конечно. Входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ладно, хорошо..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    show screen ctc
    pause
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3

    her "Доброе утро, профессор Дамблдор."
    hide screen ctc
    menu:

        "\"Доброе утро, дитя.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "{size=-4}(Опять назвал меня \"дитя\"...){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Сэр, я была бы признательна, если бы вы обращались ко мне как к ровне..."
            m "{size=-4}(Я фактически старше тебя на миллионы лет, ведьма. Мы вообще не можем быть равны.){/size}"
            m "...................."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "................"
        "\"Доброе утро, мисс Грейнджер.\"":
            her "Эм... так вот, о причине, по которой я к вам зашла..."
        "\"Да, да, пофигу...\"":
            pass

    her "Я вижу, что независимо от того, что я делаю - я не могу до вас достучаться, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "В следствии вашего пренебрежительного отношения к своим обязанностям, я решила взять все на себя!"
    m "Ты что...?"
    her "Да! Мы, гордые студенты Хогвартса терпеть не можем сексизм..."
    her "Не следует думать, что какой-то пол в чем-то лучше другого."
    m "Но-"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Пожалуйста, дайте мне закончить, профессор!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я организовала \"Организацию по защите мужских прав\" в нашей школе!"
    g4 "Ох, как это типично для вас."
    g4 "Винить во всем-"
    stop music fadeout 1.0
    m "Стоп, ты сказала {size=+5}МУЖСКИХ{/size} прав?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    her "Вы понятия не имеете, какого быть мальчиком в нашей школе, особенно в эти дни..."
    menu:
        "\"Сомневаюсь, что это подает надежды...\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Нет, вы не сделали этого, потому что просто отказываетесь слушать нас, сэр!"
            her "Но теперь вы услышите нас..."
        "{size=-3}\"Эта самая глупая идея, которую я когда-либо слышал.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я была уверена, что вы скажете что-то вроде этого..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вы знаете, что девушки оказывают некоторые услуги, чтобы заработать очки для факультета?"
    her "Иногда даже для хороших оценок..."
    m "Правда?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "В \"Гриффиндоре\" никто этим не занимается, конечно же..."
    her "И вот, что ставит нас в невыгодное положение - наша честность!"
    her "Что насчет мальчиков - они должны трудиться в десять раз лучше, чем девочки, которым сдать тест не составит труда..."
    her "Или, если они достаточно удачны, получить какое-то ничтожное одно очко..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это сексизм в чистом виде!"
    menu:
        m "..."
        "\"Что ты хочешь, чтобы я сделал?\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Ничего!"
            m "Отлично. Я рад."
        "\"Я не уверен, что ты хочешь мне донести...\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Вам не нужно больше ничего говорить, профессор."
        "\"Ты смешна!\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я? Ну, увидим..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я уже отправила письмо в министерство магии"
    with hpunch
    g4 "{size=+7}Что ты сделала?!{/size}"
    m "{size=-4}(Стоп, меня действительно это так заботит?){/size}"
    her "Мне очень жаль, но вы мне оставили мне выбора, профессор."

    her "Теперь, прошу простить меня, мне пора на занятия..."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."


    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    return



















#NOT IN USE###############################################################################################################################################################
label event_09_2: #Takes place after second special event with Snape, where he just complains about Hermione.
    "EVENT_09"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер."
            m "(Снова эта молоденькая ведьма...)"
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Категорически нет! Я занят! Возвращайся позднее!\"":
                    her "Но..."
                    her "Хорошо... Я вернусь завтра..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Хорошо..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Он должнен быть настолько снисходительной все время? Противный старый хрен!){/size}"
            m "Что-то не так?"
            her "Ничего, сэр..."
        "\"...............\"":
            her "...................."


    her "Мои занятия скоро начнуться, так что у меня не так много времени..."
    her "Быть отличником-это не легко, поэтому я надеюсь, вы понимаете, что другие ученики в нашей школе берут пример с меня."
    #m "{size=-4}(Is that so...?){/size}"
    her "Я понимаю, что вы очень важно персона..."
    her "Но немогли бы вы  уделить немного своего времени, чтобы выполнять ваши обязанности как директора школы?"
    menu:
        "\"Прости,я не понял?\"":
            her "Да, я отказываюсь потакать вам больше!"
        "\"...................\"":
            pass
    her "Я принесла столько идей для школы ..."
    her "И вы, сэр, игнорируете, каждый из них!"
    her "Знаете ли вы, что некоторые девочки из \"Слизерина\" предлогают сексуальные услуги в обмен на очки факультета?"
    m "Что они?"
    her "Вы не понимаете что происходит?"
    her "Студенты не должны больше работать, не надо учиться, все, что им нужно делать, это показать свои тела..."
    her "Это ужасно!"
    her "Я предупреждаю, профессор..."
    menu:
        "\" Вы \"Пердупреждаете меня\" Мисс Грейнджер?\"":
            her "Да, профессор. Я предупреждаю вас."
            her "Если Вы не готовы выслушать меня, я найду кого-то, кто выслушает!"
        "\"..............................................................\"":
            pass
    her "Если Вы не примите меры, тогда вы не оставивите мне выбора, профессор..."
    her "Мне придется обратиться в Министерство магии..."
    m "{size=-4}(Министерство магии? Меня это так волнует?){/size}"
    menu:

        "\"Успокойтесь пожалуйста, мисс Грейнджер.\"":
            her "Я не могу оставаться спокойной, смотря на  ваше невежество, сэр!"
        "\"Я услышал, вас. Я приму меры, я обещаю.\"":
            her "В самом деле? Ну, я рада, что мы наконец пришли к пониманию, сэр."
            her "Или вы просто будете игнорировать мои просьбы, как обычно?"
        "\"Из моего кабинета, девушка! Вон, я сказал!!!\"":
            her "Что?"
            m "Вон из моего кабинета!"
            her "Н-но..."
            with hpunch
            g4 "{size=+7}ВЫШЛА Я СКАЗАЛ!!!{/size}"
            her "{size=-6}(Оу... никогда не видел его таким грозным...){/size}"
            her "{size=-6}(Мне лучше уйти, прежде чем он поймает инсульт или что-то подобное...){/size}"
            her "..............."
            jump pissed_me_off

    her "Ох... я уже опаздываю на занятия. Я должна идти."
    m "Хорошего дня... {size=-5}ведьма!{/size}"
    her "Спасибо, профессор."
    label pissed_me_off:
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."

    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    return





#NOT IN USE###############################################################################################################################################################
label event_10: #Takes place after second special even with Snape where Ginie is worried that Hermione is still in power.
    #Hermione says that she sent the letter to the Ministry of Magic."
    "EVENT_10"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер."
            m "(Снвоа эта молоденькая ведьма...)"
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Абсолютно нет! Я занят! Приходите по позже!\"":
                    her "Но..."
                    her "Хорошо... Тогда я вернусь позднее..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходите по позже.\"":
            her "Но..."
            her "Хорошо..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event10 = True #You let Hermione in. This event will stop looping now.
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, дитя.\"":
            her "{size=-4}(Опять \"дитя\"...){/size}"
            her "Сэр, я был бы очень признателен, если вы могли бы относиться ко мне как к ровне..."
            m "{size=-4}(Я на миллионы лет старше тебя, ведьма. Ты мне не ровня.){/size}"
        "\"Доброе утро, мисс Грейнджер.\"":
            her "Эм... та, причина, по которой я здесь сегодня..."
        "\"Да, Да, выкладывай...\"":
            her "Eм..."
    her "Я вижу, что вам не  неважно, чтобы я не делала, я просто не могу достучаться до вас, сэр."
    her "Так что в свете вашей халатности и по отношению к вашим обязанностям в качестве директора школы..."
    her "Я решила взять инициативу в свои руки!"
#    m "Did you now...?"
#    her "Yes! And since I detest sexism..."
#    m "You do, do you?"
#    her "Yes, I do. No individual shall be treated differently based on his or her gender."
#    m "This doesn't make any sence, girl!"
#    her "Let me finish, professor!"
#    her "I'm organizing a \"Men's rights movement\" in our school!"
#    m "Oh, this is just typical! Blame everything on- -"
#    m "Wait, did you say {size=+5}MEN'S{/size} rights?"
#    her "You have no idea how hard it is to be a boy in our school these days..."
#    menu:
#        "\"Didn't see this one coming...\"":
#            her "No, you did not, because you refuse to listen to me, sir!"
#        "\"Literally stupidest thing I've ever heard.\"":
#            her "I knew you will say something like that..."
    her "Половина девочек в этой школе сейчас продают себя ради очков факультета..."
    her "Иногда даже за хорошие отметки..."
    her "Никто из \"Гриффиндора\" не занимается, конечно..."
    her "И это то, что ставит нас в невыгодное положение - наша честность!"
    her "Немыслимо..."
    her "Мальчикам намного труднее, - они должны работать в десять раз упорнее, тогда как  девочкам достаточно просто пройти тест..."
    her "Или, если им повезет, получить одно очко факультета..."
    her "Это сексизм в чистом виде!"
    menu:
        "\"Что вы хотите чтобы {size=+7}Я{/size} сделал?\"":
            her "Ничего!"
        "\"Не уверен, что сказать...\"":
            her "Вам не нужно ничего говорить , профессор."
        "\"Вы смешны!\"":
            her "Я?Вот увидете..."
    her "Я уже направила письмо в Министерство магии."
    with hpunch
    g4 "{size=+7}Вы сделали, что?!{/size}"
    m "{size=-4}(Подожди, меня действительно это волнует?){/size}"
    her "Я сожалею, но Вы не оставили мне выбора, профессор."
    her "Теперь, если вы простите меня, я должна успеть на мои занятия..."

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "Эта девушка тихо высасывает всю радость из меня..."

    $ hermione_takes_classes = True

    $ hermione_is_waiting_02 = False #Makes sure this event is not repeated.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    return

###############################################################################################################################################################
label event_11: #Third visit, after second special date with Snape. Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_11"
    stop music fadeout 1.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    her "Профессор, я вхожу!"
    m "...."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    # show screen hermione_walk_01
    show screen hermione_chibi_robe #Hermione. Chibi. Walking. Wearing a robe.
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    #show screen hermione_02 #Hermione stands still.
    show screen hermione_02_b #Hermione stands still wearing a robe.
    show screen bld1
    with Dissolve(.3)

    $ robeon = True #Hermione is wearing a robe.
    $ only_upper = True #Otherwise skirt shows up under the robe.

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen ctc
    with Dissolve(.3)
    pause

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Добрый вечер, профессор."
    hide screen ctc
    menu:
        "\"- Взгляд полный ненависти -\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Можете смотреть на меня как угодно, сэр."
            her "Это не поможет решить проблемы школы."
        "*Раздражительный вздох*":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Не вовремя?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Ну, я уже здесь..."
        "\"....................................\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Профессор?"
            m "Да, да..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Что-то...странное произошло сегодня..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я не знаю, как это объяснить..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "................................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я почти провалила тест..."
    menu:
        "\"Такое бывает со студентами.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "С другими студентами. Но не со мной, сэр!"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я никогда..."
        "\"(Уходи, Снейп!)\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Простите?"
            m "Что?"
            m "Ох, Я сказал, что это очень плохо. Как ты себя чувствуешь?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "................."
        "\"Расскажи мне почему?\"":
            her "Потому что... это не обычный тест!"

    her "Я не уверена, что происходит..."
    m "Все зло настроено против вас, мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это не смешно, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вы должны считать меня \"мерилом\" нашей системы образования."
    her "Если я \"почти\" провалила тест, вероятно остальные вообще не сдали его."
    m "И...?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Да, профессор. Сегодня что-то пошло не так..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "................................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но что, если это не так?"
    her "Что, если отныне все тесты будут такие сложные?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Мне нужно лучше заниматься!"
    label cant_say:
    menu:
        "\"Я могу обучать вас, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Вы?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "О, благодарю вас за предложение, но не думаю, что в этом есть необходимость, сэр."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Лучший репетитор это книга и вся библиотека Хогвартса в моем распоряжении."
        "\"Мудрое решение, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Спасибо, профессор."
        "\"Тебе нужно взять мой член в свой ротик.\"":
            m "Тебе нужно взять мой чле- "
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "А?"
            m "{size=-4}(Нет, я не могу этого сказать...){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "......?"
            jump cant_say
    m "............"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Ну, если это все, то мне стоит скорректировать свое расписание."
    m "Как пожелаете..."

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    #show screen hermione_walk_01_f
    pause 2
    hide screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    $ robeon = False #Hermione is NOT wearing a robe.
    $ only_upper = False #Otherwise skirt shows up under the robe.

    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

    return


###############################################################################################################################################################
label event_12: # Hermione complains that she did failed a test. (EVENING EVENT!)
    #"EVENT_12"
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "Профессор! Мне нужно поговорить с вами!"
    m "(Теперь она даже не удосужилась постучаться?)"
    show screen bld1
    with Dissolve(.3)
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3

    her "Профессор, сегодня что-то пошло не так!"
    her "Сегодня я завалила тест..."
    her "Не могу поверить, что это произошло!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Как это вообще возможно?!"
    menu:
        "\"Тебе стоит лучше учиться, девочка!\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Но я занималась всю ночь!"
        "\"Ну же... Все в порядке.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_20.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Нет! Это катастрофа!"

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "И хуже того, мне кажется, что я единственная кто его завалила..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "На кого я теперь похожа?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Нужно узнать результаты, но..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Да, я уверена, что кто-нибудь еще завалил его..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я имею в виду, как без этого, верно?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "....................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "....верно?"
    menu:
        "{size=-3}\"Конечно. В конце концов вы лучший ученик.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Именно..."
            her "Или по крайней мере была им, до сегодняшнего дня..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_20.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Не могу поверить, что это произошло!"
        "{size=-3}\"Вы можете стать лучше, если я буду вас обучать.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Хм..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Да, это может помочь мне, я полагаю..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я благодарна вам за предложение, но..."
            her "Могу я подумать над этим?"
            m "Только не затягивай..."
        "{size=-3}\"Я думаю, что мы скоро все узнаем.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Да, думаю так..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Извините, профессор, возможно я была чересчур эмоциональна..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но вы должны понимать, что на кону моя репутация!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Что-то должно быть не так с этим тестом..."
    her "И несмотря на то, что мне не удалось его сдать, скорее всего у меня больше всех баллов..."
    her "Как обычно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3


    her "Ну, мне лучше пойти. У нас еще одно \"ОЗМП\" собрание сегодня."
    her "Я дам вам знать о новых идеях."
    m "Не могу дождаться..."



    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5





    $ event12_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    call day_start from _call_day_start


###############################################################################################################################################################
label event_13: # Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_13"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.



    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=500 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    with d4
    pause 1.3
    $ hermione_chibi_xpos = 500 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "....................."
    m "???"

    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    hide screen hermione_02 #Hermione stands still.
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "............"
    m "Мисс Грейнджер?"
    her "..............................."
    m "Мисс Грейнджер?!!"
    show screen bld1
    with d3
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_26.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    show screen ctc
    pause
    her "А?"
    hide screen ctc
    her "О, я уже здесь?"
    her "Извините, сэр... Я..."
    her ".................."
    her "Кажется я..."
    her "Кажется... ух..."
    her "... Я все таки завалила тест."
    her "Я..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_27.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Извините, профессор..."
    her "Я не знаю, почему я пришла к вам..."
    her "Я думаю лучше мне уйти..."
    m "..................."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)


    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 01.0 #The speed of moving the walking animation across the screen.
    hide screen bld1
    with d3
    show screen hermione_run

    pause.9
    hide screen hermione_run
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    pause.3
    m "............."
    m "Она будет в порядке..."
    m "Надеюсь..."








#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with d3
#    her "................."
#    $ walk_xpos=400 #Animation of walking chibi. (From)
#    $ walk_xpos2=510 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f
#    pause 2
#    hide screen hermione_walk_01_f
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 500 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with Dissolve(.3)
#    her "................"

#    $ walk_xpos=500 #Animation of walking chibi. (From)
#    $ walk_xpos2=610 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f
#    pause 2
#    hide screen hermione_walk_01_f
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    with Dissolve(.3)
#    pause.5



    $ event13_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    call day_start from _call_day_start_1



###############################################################################################################################################################
label event_14: # Hermione comes after her breakdown (when she failed the test). She is asking for tutoring. Tutoring unlocked.
    #"EVENT_14"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    show screen bld1
    with Dissolve(.3)
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)

    her "Доброе утро, Профессор."
    m "Я могу чем-то вам помочь, Мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Ну, прежде всего я хотела бы извиниться за вчерашнее..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я никогда не заваливала тесты и поэтому не знала, как реагировать..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но сейчас все намного лучше..."
    m "Понятно..."
    her "Я не займу вас надолго, обещаю..."
    if tutoring_offer_made:
        her "Я здесь, чтобы принять ваше предложение."
        menu:
            "\"Какое предложение?\"":
                her "Ранее вы предложили обучать меня, сэр..."
                menu:
                    "\"Ох...уже поздно.\"":
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Уже..."
                        her "Поздно, сэр?"
                        her "Н-но...."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Но мне нужны уроки, а вы умнейший волшебник, которого я знаю..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Пожалуйста, сэр, мне очень нужна ваша помощь."
                        menu:
                            "\"Покажи мне свои сиськи и мы договорились!\"":
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                her "М-мои...?"
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                her "............"
                                her "....."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                with hpunch
                                her "{size=+5}Профессор Дамблдор!!!{/size}"
                                m "{size=-5}(Ну, я хотя бы попытался...){/size}"
                                her "Я вам не \"Слизеринская\" шлюха!"
                                m "Конечно нет, мисс Грейнджер."
                                m "Это испытание... Ты прошла его. Хорошая работа."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                her "Что...?"
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                her "О, конечно. Я иногда туплю. Простите за крик, сэр."
                                m "Мое предложение в силе, если хотите, чтобы я вас обучал - я займусь этим."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3
                                her ".............."
                            "\"Ну, ладно, отлично...\"":
                                pass
                    "\"Ох, Отлично. Превосходно.\"":
                        pass

            "\"Чудно! Начнем сегодня?\"":
                pass
    else:
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Я... эм..."
        her "Сэр Дамблдор, я надеюсь, что не слишком многого прошу..."
        m "Да?"
        her "Эм... было бы неплохо, если..."
        her "..............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Вы могли бы немного обучить меня, сэр?"
        menu:
            "\"Я уверен, что это возможно.\"":
                pass
            "\"Хм... Я несколько занят.\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Сэр, пожалуйста, вы лучший волшебник, которого я знаю!"
                m "{size=-4}(Ты и представить себе не можешь, маленькая ведьма){/size}"
                m "Я думаю, можно устроить, да..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Благодарю, сэр. Я очень признательна вам."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3

    her "Просто скажите мне и я принесу свои книжки."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Теперь я должна учиться еще более усердно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "И я буду брать частные уроки у вас как можно чаще, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но это не все..."
    her "В \"ОЗМП\" мы исседуем нашу систему образования более детально..."
    her "Я думаю, кто-то играет не совсем честно..."
    m "Не может быть!"
    her "У меня есть список подозреваемых, я принесу его позже...."
    m "Эм... ладно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "О, занятия уже начинаются. Мне лучше пойти..."

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5



    stop music fadeout 1.0

    $ event14_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3')
    ">Теперь вы можете вызывать Гермиону Грейнджер в кабинет."
    hide screen blktone
    with d3
    $ summoning_hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_takes_classes = True
    $ tutoring_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.


    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1

    return




###############################################################################################################################################################
label event_15: # Hermione comes and asks to buy a favour from her.

    #"EVENT_15"

#    $ slytherin +=49
#    hide screen s_p_u
#    $ s_p_u_pic = "what_49_points"
#    show screen s_p_u

    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер."
            m "(Снвоа эта молоденькая ведьма...)"
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Категорически нет! Я занят! Возвращайся позднее!\"":
                    her "Но..."
                    her "Ладно... Тогда я вернусь позднее..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ну, ладно..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"


    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, профессор..."
    her "........................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "........................"
    her "........................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Эм......"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "................."
    m "Что такое, Мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Ну, Эм..."
    her "Понимаете ли... \"Гриффиндор\" больше не лидирует..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "И... все очень трудятся..."
    her "И они надеятся на мою помощь, но я не знаю что делать..."
    m "............................"
    her "Профессор Дамблдор...."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    stop music fadeout 2.0
    her "Я хочу купить очки для факультета за мои услуги!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    menu:
        "\"Ты имеешь в виду сексуальные услуги?\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Эм... Я не уверена..."
            her "Те, которые дадут нашему факультету дополнительные очки..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я бы могла написать эссе вам или..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Или может быть почистить вашу башню..?"
            m "{size=-4}(Почистить мою башню? Хех... Эта вероятно грязная шуточка или вроде того...){/size}"
            m "Ну, хорошо. Мы что-нибудь придумаем."
        "\"Ну, если вы настаиваете...\"":
            pass
        "\"Я так не думаю, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Н-но... Нам нужны очки..."
            her "Профессор, пожалуйста, я в безвыходном положении..."
            m "В безвыходном, вы говорите..?"
            m "Ну, ладно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    her "Спасибо, профессор..."
    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "И так...Что вы хотите?"
    menu:
        "\"Покажи мне свой язык...\"":
            $ d_flag_01 = True
            pass
        "\"Стой здесь. Дай мне взглянуть на тебя.\"":
            $ d_flag_02 = True
            pass
        "\"Корчи рожицы...\"":
            $ d_flag_03 = True
            pass
        "\"Скажи \"Я была очень плохой девочкой\".\"":
            $ d_flag_04 = True
            pass

    her "Эм..."
    her "Как много очков вы мне дадите за это...?"
    $ d_flag_05 = False # 20 Points.
    $ d_flag_06 = False # 40 Points.
    $ d_flag_07 = False # 10 Points.
    $ d_flag_08 = False # 1 Point.
    menu:
        "\"1 очко.\"":
            if d_flag_02: #Stand there.
                $ d_flag_08 = True # 1 Point.
                pass
            else:
                her "Я не думаю, что это стоит того..."
                jump choose_favor_agagin
        "\"10 очков.\"":
            if d_flag_02: #Stand there.
                $ d_flag_07 = True # 10 Points.
                pass
            else:
                her "Я не думаю, что это стоит того..."
                jump choose_favor_agagin
        "\"20 очков.\"":
            $ d_flag_05 = True
            her "Так мало...?"
            pass
        "\"40 очков.\"":
            $ d_flag_06 = True
            pass




    her "Эм, ладно..."
    if d_flag_01: #Show me your tongue.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "М-мой... язык, сэр?"
        m "Да, девочка, открой свой рот и покажи мне свой язычок."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "{size=-7}(Что за извращенец...){/size}"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Эм...ну, ладно тогда..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Вот..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_35.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "............."
        her "............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_36.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "................."
        show screen ctc
        pause
        menu:
            "\"Очень хорошо. Вот твои очки.\"":
                pass
            "\"Плохо. Ты можешь лучше.\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "..............."
                her "Ладно, я попробую получше, сэр..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "Как насчет этого?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_37.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "А-а-а.................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_38.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                "............................"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_39.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "......................................"
                her "..................................................."
                her "...................................................................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_40.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "......................................................................................................."

    if d_flag_02: #Stand still...
#    if d_flag_01: #STAND STILL.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "И так, я просто буду стоять здесь...?"
        m "Отлично... Теперь повернись... Медленно."
        her "Ух... Ладно..."
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.5
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.7)

        her_02 "................................."
        menu:
            m "Hm..."
            "\"Униформа очень идет вам, мисс Грейнджер...\"":
                her_01 "............"
                her_05 "Спасибо, Профессор Дамблдор..."
            "\"У вас отличное тело, мисс Грейнджер...\"":
                her_03 "!?"
                her_04 ".............."
                her_04 "Спасибо, профессор..."
            "\"Достаточно. Вот твои очки...\"":



                show screen hermione_01 #Hermione stands still.
                with Dissolve(.7)
                pause.5
                show screen bld1
                with d3
                jump stupid_enogh





        m "Очень хорошо. Теперь можешь повернуться обратно..."
        show screen hermione_01 #Hermione stands still.
        with Dissolve(.7)
        pause.7
        show screen hermione_main
        show screen bld1
        with d3
        her "................."



#    if d_flag_02: #Pretend to be a monkey.
#        her "A monkey then..."
#        her "ooh ooh...."
#        her "ooh ooh ooh...."
#        m "Good, but you can do better..."
#        her "ooh ooh ooh...."
#        her "ooh ooh ooh... eee eee eee aah aah aah..."
#        m "Very well..."
    if d_flag_03: #STUPID FACE
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3

        her "Скорчить глупую рожицу, значит..."
        her "Посмотрим..."
        label stupid_faces:
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_41.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Как насчет этого?"
        menu:
            "\"Отлично! очень тупо! Я имею в виду, глупо.\"":
                jump stupid_enogh
            "\"Не совсем глупая.\"":
                pass
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "........."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_43.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Как насчет этого?"
        menu:
            "\"Ха-ха! Ты похожа на идиота!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                pass
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "........."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_42.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Что если я сделаю так?"
        menu:
            "\"Отлично! Очень смешно!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                jump stupid_faces

    if d_flag_04: #BAD GIRL
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Я..."
        her "Я была очень плохой девочкой..."
        g9 "Ты была очень, очень, очень плохой девочкой?"
        her "Да, сэр..."
        her "Я была очень, очень, очень, очень плохой девочкой..."
        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Тебя нужно наказать?\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Нужно ли меня... наказать?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Эм..."
                her "....................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Ну, я не идеальная, если вы об этом, сэр..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Но нужно ли меня наказывать... Хм?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "На самом ли деле это мне решать...? Я имею в виду..."
                her "Какое это имеет значение?"
                m "Ты слишком самокритичная, девочка."
                m "Просто скажи, что тебя нужно наказать!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Ладно. Меня следует наказать!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "{size=-5}(И я действительно так думаю иногда...){/size}"
                m "Хорошая девочка."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "................??"
                m "Это было так трудно?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Н-нет , сэр..."
                m "Ладно, значит..."
            "\"Хочешь чтобы тебя отшлепали?\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Хочу ли я..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Чтобы меня отшлепали??"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "?!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Профессор, мне не очень уютно от таких вопросах- -"
                m "Извиняюсь, позволь мне перефразировать вопрос..."
                m "Как сильно тебе нужны эти очки?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her ".................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Да, сэр. Я хочу, чтобы меня ошлпепали"
                m "Отлично. Думаю достаточно на сегодня..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "{size=-4}(На сегодня?){/size}"
            "\"Иди сюда и пососи мой член!\"":
                m "{size=-5}(Слишком рано для этого... Для начала мне следует цепануть ее.){/size}"
                jump to_early_for_sucking_cocks



    label stupid_enogh:
    if d_flag_05:
        m "20 очков \"Гриффиндору\"."
        $ gryffindor +=20
    elif d_flag_06:
        m "40 очков \"Гриффиндору\"."
        $ gryffindor +=40
    elif d_flag_07:
        m "10 очков \"Гриффиндору\"."
        $ gryffindor +=10
    elif d_flag_08:
        m "1 очко \"Гриффиндору\"."
        $ gryffindor +=1


    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Да!.............."
    her "Это было довольно легко..."
    her "Вы думаете я могла бы покупать еще очки за подобные услуги в будущем, профессор?"
    menu:
        "\"Я не думаю, что это хорошая идея.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
            show screen hermione_main
            with d3
            her "Пожалуйста, профессор..."
            her "Нам действительно нужны эти очки..."
            m "......."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
            show screen hermione_main
            with d3
            her "Вы очень уважаемый мастер честно говоря..."
            her "Единственный человек в этой школе, у которого я могу попросить такое..."
            m "Ну, если ты настаиваешь..."
        "\"Возможно...\"":
            pass

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Спасибо, профессор. Огромное спасибо."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Ну, я думаю мне стоит идти..."
    m "............"

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    $ hermione_chibi_xpos = 610 #Near the desk.
    hide screen hermione_walk_01_f
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    if d_flag_01: #Show me your tongue
        her "{size=-4}(Хм...){/size}"
        her "{size=-4}(Студенты все время демонстрируют свои языки учителям...){/size}"
        her "{size=-4}(Хотя, учитель в это время обычно не смотрит...){/size}"
        her "{size=-4}(Но нет ничего плохо в том, что я сделал сегодня...){/size}"
        her "{size=-4}(Я получила свои очки для факультета...){/size}"

    if d_flag_02: #Stand still...
        her "{size=-4}(Я могу просто стоять здесь, а профессор будет смотреть на меня...){/size}"
        her "{size=-4}(В этом нет ничего плохого...вообще ничего...){/size}"
#        her "{size=-4}(ooh ooh ooh... eee eee eee aah aah aah...){/size}"
#        her "{size=-4}(I'm a monkey... I'm a money... I need to practice more...){/size}"
    if d_flag_03:
        her "{size=-4}(Глупое лицо...){/size}"
        her "{size=-4}(Глупое лицо...){/size}"
        her "{size=-4}(Мне нужно потренироваться с этим.){/size}"
    if d_flag_04:
        her "{size=-4}(Я плохая девченка...){/size}"
        her "{size=-4}(Я очень плохая девченка...){/size}"
        her "{size=-4}(Да, я могу легко говорить такое...){/size}"
        her "{size=-4}(В этом нет ничего плохого...вообще ничего...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)


    $ event15_happened = True #Allows next event to start. This one stops looping when you not let Hermione in.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    stop music fadeout 1.0
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3')
    ">Теперь вы можете продавать очки для факультета за сексуальные услуги Гермионы."
    hide screen blktone
    with d3
    $ buying_favors_from_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ event15_happened = True #Turns TRUE after event_15
    jump day_start




label duels:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "..."
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main
    with Dissolve(.3)
    sna2 "Альбус..."
    m "Нет"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna2 "Просто проверял на всякий случай"
                                                                                                                                                        #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    sna "Мне нужно проверить одну теорию на счет тебя"
    m "???"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Все видят тебя как Альбуса Дамблдора"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "И?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Но значит ли это, что здесь ты Альбус Дамблдор?"
    m "..."
    m "Ты упоролся что ли?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    pause 1.0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Мне нужно узнать, как работает эта магия"
    g4 "Прекрати смотреть на меня как на лягушку для опытов"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Нет я не про это"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "Дело в том, что при всей моей нелюбви к Дамблдору, он всегда исправно выполнял свои административные обязанности директора"
    g4 "К чему ты клонишь, Снейп?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Все распоряжения директора скреплялись его подписью, которую может поставить, как ни парадоксально, лишь Альбус Дамблдор"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Распоряжения пишутся на зачарованной бумаге, поэтому как бы я ни старался подделать его подпись, на бумаге все равно будет моя подпись"
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    sna "Поставить подпись Альбуса Дамблдора может лишь сам Альбус Дамблдор"
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Либо существо, которое является Албусом Дамблдором"
    g9 "Хочешь стать моим заместителем?"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    sna "Я не такой дурак, если потом все раскроется, я уже не смогу сказать, что ничего не знал"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Нужно проверить на мелочах, вот, я набросал несколько документов"
    $ letter_text = "{size=-3}       Ученики Хогвартса, в этом году турнир дуэльного клуба будет проходить в течении следующего месяца, начиная с 15 сентября до 15 октября. {/size} \n\n {size=-6} Альбус Дамблдор{/size}"
    show screen letter
    show screen ctc

    with Dissolve(.3)
    pause
    m "Турнир дуэльного клуба?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Когда то его учредили для проведения одного эксперимента, но впоследствии он имел такую популярность, что мне до сих пор приходится курировать это направление"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Эй, вообще, зачем я обьясняю это какому-то джину, какая тебе разница?"
    m "Эй эй, я хочу знать, что подписываю"
    hide screen letter
    hide screen ctc
    hide screen bld1
    with d3
    $ renpy.play('sounds/sign.ogg')
    pause 2.0
    $ letter_text = "{size=-3}       Принять в школу магии Хогвартс на должность врача Гингера Фэгота. {/size} \n\n {size=-6} Альбус Дамблдор{/size}"
    show screen letter
    show screen ctc

    with Dissolve(.3)
    pause
    m "Кто это?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Тебе действительно это интересно?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "У нас освободилась ставка врача, если бы я заранее не скзал Макгонгал, что ты болен, она бы уже раз 20 к тебе пришла с просьбой взять именно его"
    m "Что в нем особенного?"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    sna "Спроси это у Макгонгал, это ее идея"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Хотя на самом деле я догадываюсь зачем ей это, альбус не очень то на нее посматривал"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    m "Окей"
    hide screen letter
    hide screen ctc
    hide screen bld1
    with d3
    $ renpy.play('sounds/sign.ogg')
    pause 2.0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Отлично!"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Нужно будет придумать пару способов, как я смогу это использовать"
    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f
    pause 3
    hide screen snape_walk_01_f
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2       # SNAPE
    hide screen s_head2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    $ duels = 1
    $ chitchated_with_snape = True
    $ days_without_an_event = 0
    return


# письмо





label mizulina:
    "Профессору Дамблдору."
    "Профессор! Министерство магии более не может молча наблюдать за тем как в школе магии Хогвартс происходит постепенное растление учеников!"
    "Из достоверных источников нам доподлинно известно, что ..."
    "В случае если подобные нарушения не прекратятся, мы будем вынуждены привлечь всех виновных к уголовной ответственности"
    "Председатель комитета старых дев Хелена Мизулинская"
    jump day_main_menu

label mizulina_snape:
    m "Мне пришло какое-то стремное письмо"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Дай посмотреть"
    "*читает*"
    pause 3.0
    $ s_sprite = "03_hp/10_snape_main/snape_14.png"
    sna "Растление? Они что узнали про..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "А...{w} Хелена в своем духе"
    m "Кто это?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Одна сумасшедшая на всю голову старушка, непонятно каким образом получившая власть"
    m " про какой еще Азкабан там говорится?"
    m "Что?"
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"
    sna "Похоже на то, что им просто нужно показать, что они что-то там делают у себя в министерстве, а для этого нужно упрятать кого-то в тюрьму"
    m "И что теперь делать?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Она пишет про какой-то достоверный источник..."
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Ха, точно! Как я сразу не вспомнил"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "У этой Хелены здесь учится дочка на факультете Слизерен"
    menu puffend:
        "Предлагаешь отыграться на ней?" if vopr1 == 0:
            $ s_sprite = "03_hp/10_snape_main/snape_08.png"
            sna "Что? Нет, конечно же, тогда она точно не успокоится, пока нас обоих не отправят в Азкабан"
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            sna "..."
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            sna "Хотя я был бы не против отомстить этой сучке, хотя бы так"
            $ vopr1 = 1
            jump puffend

        "Можно подставить ее" if vopr2 == 0:
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            sna "Каким образом?"
            m "Что если дочь главного борца против растления окажется самой ярой извращенкой во всей школе?"
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            sna "..."
            $ s_sprite = "03_hp/10_snape_main/23.png"
            sna "Я хотел бы на это посмотреть"
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            sna "Ты ведь не серьезно, да?"
            m "Ну как бы это сказать... у меня есть некоторые наработки"
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            sna "Что ты имеешь ввиду?"
            m "Дай мне время и ты сам все увидишь"
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"
            sna "...{w}..."
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            sna "От меня потребуется что-нибудь?"
            m "Скажу тебе позже"
            $ vopr2 = 1
            if (vopr2 == 1) and (vopr3 == 1):
                jump mizulina_snape2
            else:
                jump puffend

        "Старый добрый шантаж" if vopr3 == 0:
            m "Я смогу найти компромат на эту ее дочь"
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"
            sna "Хм..."
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            sna "Возможно тогда у меня получится убедить министерство магии терроризировать какую-то другую школу"
            $ vopr3 = 1
            if (vopr2 == 1) and (vopr3 == 1):
                jump mizulina_snape2
            else:
                jump puffend

label mizulina_snape2:
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "Ее зовут Даффна Гринграсс, она студентка Слизерина"
    m "Почему Гринграсс?"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Ее родственница не очень популярно в мире магов"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Я бы сказал{w}, очень не популярна. Это из соображений безопасности. Я скажу ей, что директор вызвал ее"
    $ renpy.play('sounds/win_04.mp3')
    ">Теперь вы можете вызывать Дафну"
    stop music fadeout 1.0
    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ snape_busy = True
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    $ chitchated_with_snape = True
    $ daphne_event = 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu



label snape_kniga:
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Я недавно рылся в библиотеке и наткнулся на одну интересную книгу"
    g9 "Мне больше нравятся журналы"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Ты не понял. Я говорю о магической книге"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Мне кажется я нашел способ вернуть тебя обратно"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "Но судя по тому, что я еще здесь, все не так просто?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Есть один момент..."
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Эта книга на неизвестном мне древнем языке, я смог только примерно понять о чем она и кажется она как раз описывает ритуал, который поможет отправить тебя обратно"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "Я думал, что джины должны знать любые языки"
    m "Ну... возможно..."
    $ devil = 1
    $ renpy.play('sounds/win_04.mp3')
    $ book_evil = 1
    ">теперь вы можете переводить странную книгу на древнем языке"
    $ chitchated_with_snape = True
    jump snape_ready


label hermione_dial:
    her "Ну... последнее время происходит что-то странное"
    m "Что?"
    her "Некоторые девушки жалуются на то, что кто-то чувствуют что кто-то постоянно подсматривает за ними"
    her "А одна вчера заявила, что ее кто-то ночью попытался изнасиловать ее, но когда она подняла шум, кроме нее в комнате никого не было"
    g9 "Значит это все что он может? хм... не страшно"
    her "Кто может?"
    m "А? Да так, никто"
    jump day_time_requests

label snape_dial:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "..."
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    sna "Что ты делал вчера вечером?"
    m "..."
    m "Что?"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    sna "Мне начали поступать жалобы на странные вещи, ты случайно не выходил из кабинета?"
    m "Нет"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "......."
    sna "Наверное это опять привидения забавляются"
    m "Эм... а на что поступают жалобы?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Новый врач жалуется, что у него постоянно пропадают инструменты...{w} хотя это скорее всего он сам не знает куда что положил"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "Несколько девушек заявили мне, что кто-то невидимый их лапал и по крайней мере два десятка жаловались, что кто-то наблюдал за ними, пока они переодевались"
    m "..."
    g4 "......."
    m "Ничего не знаю об этом"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Наверное опять эти Уизли, жаль что сыворотку правды пришлось использовать год назад"
    stop music fadeout 1.0
    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ snape_busy = True
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    $ devil = 10
    $ chitchated_with_snape = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ days_without_an_event = 0
    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label fenix_rape:
    hide screen phoenix
    show screen raped_phoenix
    $ ph_body = "f/phx6.png"

    hide screen animation_feather


    pause 3

    hide screen heal3
    $ ph_body = "f/phx6.png"
    pause 2.0
    m "..."
    m "что-то здесь поменялось...{w} только не могу понять, что?"
    g4 "Что за черт?!"
    g4 "феникс, что с тобой???"
    pause 1
    show screen bld1
    show screen phoenix_main2
    with d3
    pause 2.0

    $ ph_body = "f/phx6.png"
    ph "..."
    $ ph_body = "f/phx8.png"
    ph "Он...{w} чудовище..."
    $ ph_body = "f/phx7.png"
    m "Что здесь произошло?"
    $ ph_body = "f/phx8.png"
    ph "Он делал...{w} все..."
    $ ph_body = "f/phx7.png"
    g4 "..."
    m "А что так можно было?"
    $ ph_body = "f/phx8.png"
    ph "Даже когда у меня получилось перевоплотиться обратно в феникса...{w} он...{w} продолжил..."
    $ pnx_stage = 100
    m "......"
    $ ph_body = "f/phx8.png"
    ph "Мне кажется... он... {w}снял заклинание..."
    $ ph_body = "f/phx7.png"
    m "..."
    m "Что?"
    g9 "То есть ты больше не сможешь обратно воплотиться в птицу?"
    $ ph_body = "f/phx8.png"
    ph "Вы не правильно поняли, мастер.....{w} у меня больше не хватит сил поддерживать человеческую форму"
    $ ph_body = "f/phx7.png"
    g4 "Что? Он сломал моего феникса?!"
    $ ph_body = "f/phx8.png"
    ph "Прощайте..."
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen raped_phoenix
    hide screen phoenix_main2
    hide screen phoenix_main
    show screen phoenix
    with d5
    pause 3
    hide screen heal3
    hide screen bld1
    with d3
    $ pnx_stage = 100
    g4 "Нет!"
    g4 "мой гребаный феникс, неееееет!"
    g4 "Твою мать, нужно быстрее что-то делать"
    $ days_without_an_event = 0
    return








label preview:
    $ chimi_chibi_xpos = 280
    $ harry_chibi_xpos = 350

    show screen harry_ch #Hermione stands still.
    show screen chimi_01 #Hermione stands still.
    show screen bld1
    with d3
    $ har_body = "f/hr_morda1.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen chimi_main2
    with d3
    harr "Что нам теперь делать, профессор Дамблдор?"





label priziv:
    stop music
    play music 'music/16 The Chess Game.mp3'
    hide screen genie
    show screen desk
    with d3
    show screen gin_pr
    show screen vizov
    with d3

    m "так...{w} вроде бы все так как там описано"
    m "ну что ж... здесь конечно же иногда было весело..."
    g4 "жаль я не смогу прихватить с собой эту горячую зубрилку"
    g9 "но все таки горячие наложницы Аграбы во главе с принцессой Жасмин ни с чем не сравнятся"
    g7 "прощай, другой мир, ты был...{w} не самым плохим местом"
    m "остались последние слова"
    m "Etis atis animatis… etis atis amatis…"
    # нехороший звук
    m "Exorcizo te, immundissime spiritus, omnis incursio adversarii, omne phantasma, omnis legio, in nomine Domini nostri Jesu Christi eradicare"
    m "et effugare ab hoc plasmate Dei. Ipse tibi imperat, qui te de supernis caelorum in inferiora terrae demergi praecepit. Ipse tibi imperat, qui mari, ventis, et tempestatibus impersvit!"



    $ demon_chibi_xpos = 580 #Near the desk.
    $ demon_chibi_ypos = 160 #Near the desk.
    play sound 'sounds/magic2.mp3'
    show screen demon_priziv #Hermione stands still.
    pause 2.0
    g6 "...{w}...................."
    show screen bld1
    $ demon_chibi_xpos = 470
    show screen demon_ch
    with d3
    $ dem_body = "f/de_def.png" #Sprite of Hermione's upper body.
    show screen demon_main
    with d3

    g6 "..."
    $ dem_body = "f/de_wtf.png"
    show screen demon_main
    dem "Что за х..."
    hide screen demon_main

    m "Что?"
    show screen demon_main
    $ dem_body = "f/de_govor.png"
    dem "Где я?"
    dem "Ты кто?"
    hide screen demon_main
    $ dem_body = "f/de_def.png"
    m "Я... "
    menu:
        "Дамблдор":
            pass

        "Джин":
            pass

        "Я просто мимо проходил":
            pass


    $ dem_body = "f/de_wtf.png"
    show screen demon_main
    dem "...{w} Кто?"
    $ dem_body = "f/de_govor.png"
    dem "На самом деле это не так важно, ГДЕ я?"
    $ dem_body = "f/de_def.png"
    hide screen demon_main
    g4 "Хотел бы я сам знать"
    $ dem_body = "f/de_smeh.png"
    show screen demon_main
    dem "Ха-ха-ха"
    $ dem_body = "f/de_smile.png"
    dem "В таком случае ты бесполезен, есть последнее желание?"
    hide screen demon_main
    g4 "Я бы не был таким самоуверенным, вообще то я владею достаточно могущественной древней магией..."
    $ dem_body = "f/de_wtf.png"
    show screen demon_main
    dem "Магией?"
    $ dem_body = "f/de_smeh.png"
    dem "ха-ха-ха"
    $ dem_body = "f/de_smile.png"
    dem "Ну давай покажи что ты можешь"
    hide screen bld1
    hide screen demon_main
    with d3
    pause 1.0
    hide screen gin_pr
    show screen gin_pr2
    with d5
    pause 1.0

    g9 "Ну что, потанцуем"

    $ dem_body = "f/de_kulak.png"
    show screen demon_main
    with d4
    dem "Ага"
    play sound "sounds/udar.mp3"
    $ dem_body = "f/kulak.png"
    with vpunch
    pause 1.0
    hide screen gin_pr2
    with d3
    hide screen demon_ch
    with d3
    hide screen demon_main
    with d3
    hide screen vizov
    $ devil = 8
    jump day_start

label after_demon:
    g8 "Похоже это была не самая лучшая идея..."
    g8 "Стоит ли говорить об этом Снейпу?"
    g8 "Мне кажется он не очень обрадуется"
    $ devil = 9
    return


label thank_mak:
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3')
    "Тук-тук-тук"
    m "Кто там опять?"

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ mkg_chibi_xpos = 610
    $ mkg_chibi_ypos = 0
    show screen mkg_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    $ mkg_trg = 1
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen mkg_walk
    pause 4
    $ mkg_chibi_xpos = 300 #Near the desk.
    show screen mkg_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    $ mkg_body = "f/face1.png" #Sprite of Hermione's upper body.
    show screen mkg_main
    show screen mkg_ch
    show screen ctc
    with Dissolve(.3)
    pause
    $ mkg_body = "f/face4.png"
    mkg "Приветик, Альби"
    $ mkg_body = "f/face1.png"
    m "................"
    g4 "*Что эта старая шлюха себе позволяет*"
    $ mkg_body = "f/face4.png"
    mkg "Только не говори, что ты собираешься делать вид, что ничего не было"
    $ mkg_body = "f/face1.png"
    m "...{w} да я не..."
    $ mkg_body = "f/face4.png"
    mkg "Я и не думала, что там под твоей бородой еще что-то осталось"
    $ mkg_body = "f/face1.png"
    g4 "...{w} я рад что получилось...{w} удивить тебя"
    $ mkg_body = "f/face4.png"
    mkg "Ох Альби, это действительно то, что мне было нужно"
    $ mkg_body = "f/face1.png"
    g4 "Еще немного и я блевану"
    $ mkg_body = "f/face4.png"
    mkg "Надеюсь, у тебя как-нибудь найдется время повторить это мероприятие"
    $ mkg_body = "f/face1.png"
    m "Я...{w} Внесу это в список своих дел..."
    $ mkg_body = "f/face4.png"
    mkg "Хахах, Альби, ты такой милашка"
    hide screen mkg_main
    hide screen ctc
    hide screen bld1
    with d3
    hide screen mkg_ch
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen mkg_walkf
    pause 4
    hide screen mkg_walkf
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    g4 "На самое последнее место, сразу после смерти. Твою мать... есть в этом замке хоть что-то до чего не доберется этот сраный демон"
    $ days_without_an_event = 0

    return

label second_demon:
    pause 2.0
    $ demon_chibi_xpos = 400 #Near the desk.
    $ demon_chibi_ypos = 170 #Near the desk.
    play sound 'sounds/magic2.mp3'
    stop music
    play music "music/16 The Chess Game.mp3"
    show screen demon_priziv #Hermione stands still.
    pause 2.0
    g6 "...{w}...................."
    show screen bld1
    $ demon_chibi_xpos = 340
    show screen demon_ch
    with d3
    $ dem_body = "f/de_def.png" #Sprite of Hermione's upper body.
    with d3
    hide screen demon_main
    g4 "..."
    $ dem_body = "f/de_govor.png"
    show screen demon_main
    dem "Ты очухался?"
    hide screen demon_main
    m "эм..."
    g4 "Хватит уже делать все то, чем бы я хотел здесь заниматься, но не могу"
    $ dem_body = "f/de_smile.png"
    show screen demon_main
    dem "Мне кажется ты не понял"
    hide screen demon_main
    # начинается пиздец
    g4 ".........."

    $ dem_body = "f/de_smile.png"
    show screen demon_main
    dem "Пока что мне весело гулять по этому месту, но если ты не придумаешь как отправить меня обратно..."
    $ dem_body = "f/de_govor.png"
    show screen demon_main
    dem "Все не обойдется парой раскуроченных задниц"
    hide screen demon_main
    m "Кстати о задницах"
    g9 "Что ты делаешь, что эти шлюшки становятся готовыми на все"

    $ dem_body = "f/de_smile.png"
    show screen demon_main
    dem "У тебя осталось не так много времени, лучше позаботится о том, чтобы я не успел разобрать этот замок до основания"
    hide screen bld1
    hide screen demon_priziv
    hide screen demon_main
    hide screen demon_ch
    with d6
    stop music
    pause 3.0
    play music "music/Chipper Doodle v2.mp3"
    m "...{w}.........."
    m "Наверное, действительно стоит поискать что-то"
    $ days_without_an_event = 0
    $ devil = 11
    hide screen bld1
    return

label ogon:
    hide screen desk
    hide screen genie
    $ tt_xpos=350
    $ tt_ypos=90
    show screen genie_stands
    show screen chair_02 #Empty chair near the desk.        show screen desk
    show screen desk
    show screen desk_02

    with Dissolve(0.5)
    if fire_in_fireplace == False:
        $ fire_in_fireplace = True
        show screen fireplace_fire

    ogn "У аппарата"
    m "..."
    $ ogon_first = 1
    $ ogon2 = 1
    ogn "СЛУШАЮ!!!"
    m "Эм..."
    menu:
        "...":
            ogn "...{w}....."
            ogn "Ну и ладно"
            # закрывается
            jump day_main_menu


        "Алло":
            ogn "Алло?"
            ogn "Слушаю вас, мой господин"
            pass


        "Что ты такое?":
            ogn "Что я такое?"
            ogn "Где Альбус Дамблдор?!!"
            g4 "..."
            m "Это я"
            ogn "..."
            ogn "впрочем, какая разница, я всего лишь заколдованный камин"
            m "..."
            ogn "Что вы хотели, мой господин?"
            pass

    menu:
        "Пока":
            hide screen chair_02
            hide screen genie_stands
            with d3
            jump day_main_menu
        "Покажи мне Гермиону":
            jump hermione_ogn

label ogon222:
    hide screen genie
    hide screen desk
    hide screen desk_02
    $ tt_xpos=350
    $ tt_ypos=90
    show screen genie_stands
    show screen chair_02 #Empty chair near the desk.
    show screen desk
    show screen desk_02
    if fire_in_fireplace == False:
        $ fire_in_fireplace = True
        show screen fireplace_fire
    with Dissolve(0.5)
    ogn "Слушаю"
    menu:
        "Пока":
            hide screen chair_02
            hide screen genie_stands
            with d3
            jump day_main_menu
        "Покажи мне Гермиону":
            jump hermione_ogn
        "Покажи мне Чжоу Чанг"  if (phoenix_ev == 1) and (chimi_event >= 11) and (ogon2 != 0) and (chimi_event < 17):
            $ ogon = 1  
            jump chochang_ogn


label hermione_ogn:
    if daytime:
        $ trig = renpy.random.randint(1, 5)
        if trig == 1:
            call hermione_ogn3 from _call_hermione_ogn3 
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        elif trig == 2:
            call hermione_ogn6 from _call_hermione_ogn6 
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu

        elif trig == 3:
            call hermione_ogn2 from _call_hermione_ogn2 
            her "ТВОЮ МАТЬ"
            her "РОНАЛЬД УИЗЛИ"
            ron "но оно ведь сработало"
            her "ЧТО ТЫ СДЕЛАЛ, ГОВНЮК!!!"
            "НА сегодня энергия закончилась"
            "Блин, на самом интересном моменте"
            $ ogon = 1
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        elif trig == 4:
            if whoring > 12:
                call hermione_ogn10 from _call_hermione_ogn10 
                $ ogon = 1
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu
            else:
                call hermione_ogn3 from _call_hermione_ogn3_1 
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu
        elif trig == 5:
            if whoring > 12:
                call hermione_metla from _call_hermione_metla 
                $ ogon = 1
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu
            else:
                call hermione_ogn3 from _call_hermione_ogn3_2
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu



    else:
        $ trig = renpy.random.randint(1, 4)
        if trig == 1:
            call hermione_ogn3 from _call_hermione_ogn3_3
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        elif trig == 2:
            call hermione_ogn6 from _call_hermione_ogn6_1
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        elif trig == 3:
            call hermione_ogn5 from _call_hermione_ogn5
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        elif trig == 4:
            if whoring > 12:
                call hermione_metla from _call_hermione_metla_1
                $ ogon = 1
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu
            else:
                call hermione_ogn5 from _call_hermione_ogn5_1
                show screen genie
                hide screen genie_stands
                hide screen chair_02 #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu


label hermione_ognn:
    "Гермионааа"
    "Крутяк"
    "Да, мальчики?"
    "Мне сегодня профессор Макгонгал 10 очков начислила"
    "И мне!"
    "Хм... Я вам не верю"
    "Да ладно, ты чего, я сам видел. Он такой прямо на лекции берет и отвечает"
    "Да?"
    "Что-то я не помню такого на лекции"
    "Это было когда ты отошла к директору"
    "Ах, да... возможно"


label hermione_ogn2:
    "Вы видите, что гермиона находится на уроке зельеварения"
    show screen backg
    hide screen animation_feather
    with Dissolve(1.0)
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with d3

    sna "Всем, разбиться на группы и МОЛЧА готовить зелье увеличения"
    hide screen snape_main
    with dissolve
    pause 0.5
    $ h_body = "f/har6.png"
    $ h_xpos = 300
    $ h_ypos = 0
    show screen hermione_main

    her "Так, два оболтуса, мы все знаем, кто здесь первое место в рейтинге студентов, так?!"
    $ h_body = "f/har8.png"
    her "Поэтому стоите и делаете что я говорю"
    $ h_body = "f/har7.png"
    her "Ясно?!"

    ron "Что вы делаете с профессором дамблдором так долго каждый день?"
    $ h_body = "f/har6.png"
    her "МОЛЧАТЬ!!!"
    $ h_body = "f/har7.png"
    ron "..."
    $ h_body = "f/har8.png"
    her "смотри в учебник, Уизли"
    $ h_body = "f/har7.png"
    ron "ага"
    $ h_body = "f/har8.png"
    her "Какие там ингридиенты?"
    $ h_body = "f/har7.png"
    ron "Укроп"
    $ h_body = "f/har8.png"
    her "Есть"
    $ h_body = "f/har7.png"
    ron "Кошачья жопа"
    $ h_body = "f/har8.png"
    her "Есть"
    $ h_body = "f/har7.png"
    ron "25 картошек"
    $ h_body = "f/har9.png"
    her "..."
    $ h_body = "f/har8.png"
    her "Это точно ингридиенты зелья увеличения?"
    $ h_body = "f/har7.png"
    ron "эм..."
    ron "да"
    $ h_body = "f/har9.png"
    her "..."
    $ h_body = "f/har6.png"
    her "Хорошо, что дальше?"
    $ h_body = "f/har7.png"
    ron "17 мандавошек"
    ron "добавить воды и нагреть"
    $ h_body = "f/har6.png"
    # звук бурлящей воды
    pause 1.0
    her "так... реакция пошла!"
    $ h_body = "f/har9.png"
    her "Кто будет пробовать?"
    "..."
    ron "Гермиона, это ведь ты готовила, ты и проверяй"
    $ h_body = "f/har1.png"
    her "..."
    $ h_body = "f/har6.png"
    her "ых... окей"
    $ h_body = "f/har1.png"
    "............"
    "Я ничего не чувствую...."
    pause 1.0
    hide screen hermione_main
    with d3
    $ h_body = "f/har4.png"
    show screen hermione_main
    with d3
    her "..."
    $ h_body = "f/har2.png"
    her "......"
    $ h_body = "f/har3.png"
    hide screen hermione_main
    with d3
    hide screen backg
    with d3
    return


label hermione_ogn3:
    show screen ogn
    with d3
    pause 1.5
    hide screen ogn
    show screen ogn_kniga
    "Вы видите как Гермиона учит уроки"
    $ ogon = 1
    pause 3.0
    hide screen ogn_kniga
    show screen ogn2
    pause 1.0
    hide screen ogn2
    ogn "На сегодня энергия закончилась"
    return

label hermione_ogn5:
    show screen ogn
    with d3
    pause 1.5
    hide screen ogn
    show screen ogn_spit
    "Вы видите как Гермиона спит"
    pause 3.0
    hide screen ogn_spit
    show screen ogn2
    pause 1.0
    hide screen ogn2
    $ ogon = 1
    ogn "На сегодня энергия закончилась"
    return

label hermione_ogn6:
    show screen ogn
    with d3
    pause 1.5
    hide screen ogn
    show screen ogn_metla
    "Вы видите как Гермиона летит на метле"
    pause 3.0
    hide screen ogn_metla
    show screen ogn2
    pause 1.0
    hide screen ogn2
    $ ogon = 1
    ogn "На сегодня энергия закончилась"
    return

label hermione_ogn4:
    "Вы видите, что гермиона сейчас на уроке защиты от магических животных"
    hide screen animation_feather
    show screen backg2
    with Dissolve(1.0)
    $ h_body = "03_hp/13_hermione_main/body_23.png"
    $ h_xpos = 300
    $ h_ypos = 0
    show screen hermione_main
    hag "Слушайте сюда, дети"
    chi "Мы уже давно не дети, громила"
    hag "Для меня вы все еще дети"
    hag "А если не будете слушать, то прослушаете что делать, чтобы тентаклемонстр не затрахал вас до смерти"
    "..."
    hag "Тотоже!"
    hag "Значит так! Если вы встретились с тентаклемонстром, первое, что вы должны сделать, это..."
    $ h_body = "03_hp/13_hermione_main/body_17.png"
    ron "Псс... псс... Гермиона!"
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "ТЫ не видишь, я слушаю, Уизли"
    $ h_body = "03_hp/13_hermione_main/body_07.png"
    ron "У меня срочное дело"
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "Ты отвлекаешь меня от лекции"
    ron "Ну мне очень срочно надо"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "ну ладно, Что тебе?"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    ron "Покажи сиськи"
    $ h_body = "03_hp/13_hermione_main/body_77.png"
    her "ты идиот, рон!"
    ron "гыы гы гы гы"
    harr "хы хы хы хы"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "и ты туда же, гарри!"
    hag "Осторожно! Вон он идет!"
    $ h_body = "03_hp/13_hermione_main/body_22.png"
    her "А? Что??"
    hag "Гермиона, не стой столбом!"
    $ h_body = "03_hp/13_hermione_main/body_130.png"
    her "Что? Где?"
    hide screen hermione_main
    with d3
    $ h_body = "f/har10.png"
    show screen hermione_main
    with d3
    "..."
    $ h_body = "f/har11.png"
    her "Спасите!"
    $ h_body = "f/har12.png"
    hag "Что за х..."
    hag "БЫстрее спасайте гермиону, пока он не начал..."
    ron "давайте хотя бы пару минут посмотрим...{w} для исследования..."
    $ h_body = "f/har11.png"
    her "господи, освободите меня пожалуйста!!!"
    $ ogon = 1
    hide screen hermione_main
    with dissolve
    hide screen backg2
    with Dissolve(1.0)
    ogn "На сегодня энергия закончилась"
    g4 "Блин, на самом интересном месте!"
    return


label hermione_ogn10:
    hide screen animation_feather
    show screen bibl
    with d6
    pause 0.6
    $ h_body = "f/h1.png"
    $ h_xpos = 300
    $ h_ypos = 0
    show screen hermione_main
    with d3
    har_govor "для приготовления зелья невидимости нужно смешать..."
    pause 1.0
    $ h_body = "f/h2.png"
    her "..."
    pause 1.0
    hide screen hermione_main
    $ h_body = "f/h3.png"
    show screen hermione_main
    pause 1.0
    hide screen hermione_main
    $ h_body = "f/h4.png"
    show screen hermione_main
    her "*зевает*"
    har_govor "Голландская мантикора достигает в высоту 4 метра!"
    $ h_body = "f/h2.png"
    her "...."
    $ h_body = "f/h5.png"
    her "ага"
    $ h_body = "f/h2.png"
    pause 2.0
    $ h_body = "f/h6.png"
    her "Эй, смотри, все ушли, тут никого кроме нас нет..."
    har_govor "при произнесении этого заклинания нужно двигать палочкой воот так"
    $ h_body = "f/h7.png"
    her "*вздыхает*"
    $ h_body = "f/h8.png"
    her "*я бы показала тебе как нужно вертеть палочкой*"
    har_govor "Гермиона, ты меня не слушаешь?"
    $ h_body = "f/h9.png"
    her "Эм...{w} нет гарри, мне очень интересно..."
    $ h_body = "f/h2.png"
    her "..."

    har_govor "хмм... тут написано, что для того, чтобы вызвать барабашку нужно..."
    pause 2.0
    $ h_body = "f/h8.png"
    pause 2.0
    $ h_body = "f/h6.png"
    her "псс..."
    $ h_body = "f/h9.png"
    har_govor "а?"
    $ h_body = "f/h10.png"
    her "хочешь покажу одно крутое заклинание?"
    pause 1.0
    $ h_body = "f/h11.png"
    pause 1.0
    har_morda "......."
    hide screen hermione_main
    with dissolve
    hide screen bibl
    with Dissolve(1.0)
    ogn "На сегодня энергия закончилась"
    g4 "Блин, на самом интересном месте!"

    return


label hermione_metla:
    stop music fadeout 2.0
    hide screen animation_feather
    $ nhxalign = 0.7
    $ new_herm = "new/h5.png"
    $ backgr = "new/quid.png"
    show screen fruk
    show screen new_herm
    with d6
    pause 0.6

    with d3
    qu "Так, еще раз, как мы и учили, говорите Вверх!"
    qu "чтобы повернуть вправо нагибаете ручку метлы под градусом...."
    $ new_herm = "new/h2.png"
    her "...."
    ron "Гермиона, что это с твоей новой метлой?"
    $ new_herm = "new/h4.png"
    her "эм.... что?"
    ron "мне кажется, что это не от нее?"
    $ new_herm = "new/h6.png"
    her "Ты что? Это же новый навигатор!"
    ron "навигатор?"
    $ new_herm = "new/h3.png"
    her "Конечно, с ним маневренность моейм метлы в 5 раз больше!"
    $ new_herm = "new/h7.png"
    ron "...."
    $ new_herm = "new/h7.png"
    ron "понятно"
    "*шепот в толпе - вот ведь извращенка эта Грейнджер*"
    pause 1.0
    hide screen new_herm
    with dissolve
    hide screen fruk
    with Dissolve(1.0)
    show screen ogn
    with d3
    pause 1.5
    hide screen ogn
    show screen ogn_metla
    "Вы видите Гермиону, летящую на метле"
    pause 3.0
    hide screen ogn_metla
    show screen ogn2
    pause 1.0
    hide screen ogn2
    $ ogon = 1
    ogn "На сегодня энергия закончилась"
    return














label second_letter:
    "Я не знаю, что ты там с ней делал, но это не работает"
    ".....{w} че?"
    "Вчера она отправила второе письмо"
    "Опять?"
    "*вот сука, нужно будет ее наказать*"
    "Письмо у тебя с собой?"
    "А ты думаешь я просто так пришел?"
    "Здравствуйте, мама. Как я Вам уже писала, директор этого богом забытого места несоответствует занимаемой должности. Сегодня он уже открыто до меня домогался. У меня есть все доказательства для того, чтобы упечь его на веки в Азкабан. Отправлю все по запросу. Ваша дочь, Дафна."
    "....."
    "О каких доказательствах она говорит?"
    # тут будет херня про момент типо он тогда уже подрочил на нее и он типо вспомнил про сперму, т.е. этот эвент будет после дрочки ей на одежду
    "Эм...{w} ну...{w} как бы так сказать"
    "....."
    "....."
    "Я не хочу об этом ничего знать"
    "....."
    "Что в этот раз напишем?"
    "Здравствуйте, мама."
    menu:
        "Йо, чо как, подруга":
            pass
        "Привки, мамик":
            pass
        "Здаров, чикса":
            pass

    "Хахаха... неплохо"
    "Что дальше?"
    "Как я Вм уже писала, директор этого богом забытого места несоответствует занимаемой должности"
    menu:
        "Я наконец то нашла себе парня, его зовут Фред, он из семьи маглов":
            pass

        "Я поняла, что учеба это не мое, я хочу уехать подальше отсюда":
            pass

        "Я уже неделю не хожу на занятия, преподаватели слишком тупые, чтобы меня чему-то учить":
            pass

    "Ухахаххахаа... хотел бы увидеть ее лицо, когда она прочтет"
    "Что потом?"

    "Сегодня он уже открыто до меня домогался. У меня есть все доказательства для того, чтобы упечь его на веки в Азкабан"
    menu:
        "Профессор говорит, что я должна посещать занятия, но что мне до него":
            pass

        "Я решила, что больше не буду ходить на занятия, я и так все знаю лучше преподавателей":
            pass

    "..........{w} как же ей потом влетит"
    "Как закончим?"
    "Ваша дочь, Дафна"
    menu:
        "Чао, пока.":
            pass


        "Можете не отвечать, до скорого.":
            pass

    "Хм...{w}....{w}.........."
    "......."
    "Это великолепно!"
    "Жду не дождусь, когда прочитаю ее ответ"
    "Ладно, пойду отправлю сову"
    "Надеюсь тебе это поможет, джин"
    "Не сомневайся"
    return
# только после этого эвента она будет соглашаться на всякую более ядреную дичь, но по идее письмо уйдет сразу после сисек,
# поэтому все будет постепенно происходить и игрок толком ничего не поймет






label last_kram_old:
    "На следующей неделе будет последний матч"
    "...."
    "Я знаю, все его давно ждут"
    "По этому поводу у меня будет к тебе самое важное задание"
    "Еще важнее, чем предыдущие?"
    "кхм, да"
    "Я даже боюсь представить, что это может быть"
    "все не так сложно как может показаться"
    "Ты знаешь кто такой Виктор Крам?"
    "Конечно же, он - звезда мирового масштаба, все его знают"
    "отлично"
    "эм...."
    "...."
    "ты правильно поняла"
    "но как я это сделаю?"
    "не бойся, я все предусмотрел"
    "просто дай ему это зелье и он сделает все что захочешь"
    "Главное, чтобы он не участвовал в матче"
    "хм...."
    "Я не уверена, но попробую"
    "Что значит не уверена, от этого зависит судьба школы!"
    "я сделаю!"
    "отлично"



####################################################
label new_fenix1_old:
    "Слушаю, мой господин"
    "Так, в этот раз у меня для тебя отличная новость"
    "новость?"
    "В этот раз у тебя не выйдет меня опрокинуть"
    "..."
    "И сегодня у нас будет секс"
    "секс?"
    "да, секс"
    "прямо как у Дживанны и Зулуса"
    "......{w}.........."
    "че?"
    "Ты что не знаешь историю про принцессу Дживанну?"
    "эм... что?"
    "какую еще дживанну?"
    "что происходит???"
    "Однажды, в старом старом королевстве"
    "эй я не просил мне рассказывать это дерьмо"
    "жила была принцесса Дживанна"
    "Я узнаю это место"
    "Да это же аграба"

    "Да, сука, да"
    "Даааааааааааа!!!!!!!"
    # он типо обратно возвращается
    ".........."
    "это...."

label new_fenix2_old:
    "Слушаю, мой господин"
    "..."
    "..."
    "..."
    "В этот раз я не поведусь на твои фокусы"
    "Фокусы? какие фокусы?"
    "Я хочу, чтобы ты уяснила, что тебе таки придется отведать моей палочки"
    "Палочки?"
    "нет сучка! Стой!"
    "...."
    "не той палочки"
    "той, которая растет прямо из меня"
    "прямо как у Расула?"
    "че? какого Расула?"
    "10"
    "нееееееееееет! опять это дерьмо!"

    "Оа ты сука! Да! заебись! я твой султан!"
    "....."
    "твою мать, ты опять это сделала!"





label new_fenix3:
    "Слушаю, мой господин"
################################
label hermione_fenix_old:
    m "Что ты знаешь о фениксах?"
    her "Фениксах?"
    her "Фениксы - "
    m "Эм...."
    g4 "А как сделать чтобы феникс перестал превращаться обратно в феникса?"
    her "......"
    m "......"
    her "......"
    her "Вы, наверное, об анимагах, это очень редкое заклинание, которым пользовались с 3 по 14 века в восточных странах"
    m "угу"
    her "Таким образом султаны наказывали непослушных жен или любовниц, превращая их ручных питомцев, в том числе фениксов"
    m "...."
    her "Если только вы не говорите про тех псевдофениксов, которых привозят из стран ОАЭ"
    m "....."
    m "не их, конечно же...."
    "...."
    "а что они?"
    "они не являются настоящими фениксами, а лишь обычными подневольными девушками, которых зачаровали для того, чтобы покупатель мог прятать их от жены"
    "........"
    "это{w} не"
    "отлично"
    "эм..."
    "Что?"
    "Профессор, а разве я не получу за это баллы?"
    "Эм... конечно, 5 баллов Гриффиндору!"
    "Спасибо!"
    "Еще что-то?"

#################################################
label harry_final:
    "профессор дамблдор!"
    "опять он"
    "проходи, Гарри"
    "профессор Дамблдор"
    "да?"
    "я достал это для вас"
    "отлично"
    "что вы хотите делать с этим, сэр?"
    "эм....{w} мне это нужно чтобы одолеть Вошмар-де-фурта"
    "..."
    "ну так что, давай мне его"
    "...{w}............{w}................"
    "я раскусил тебя!"
    "че?"
    "Я сразу заподозрил неладное с того самого дня!"
    "....."
    "Куда ты дел профессора?"
    "эм... я его никуда не девал"
    "не притворяйся, я сразу все понял!"
    "*поэтому и таскал мне все эти приблуды, ага*"
    "Что ты задумал?"
    "вообще-то...."
    "Я не боюсь тебя Волан-де-Морт!"
    "..........{w} вот оно что"
    "Авахамора!"
    "...."
    "точно, их магия не очень то действует на меня"
    "что?! ты даже не применял защитные чары?!"
    "экспилиармус!"
    "......"
    "чертов воландеморт, будь ты проклят!"
    "ЭКЗОРЦИО"
    "это может долго продолжаться..."
    "я уничтожу тебя раз и навсегда!"
    "так ну ладно"
    # одним ударом убивает его


label snape_cho:

    "Профессор..."
    "Ого"
    "Ты опять от него?"
    "Я... я не знаю... я шла в спальню и... оказалась здесь"
    "...."
    "Ты не встречала никого по пути?"
    "Нет... я..."
    "*то есть демон ее не трахал?*"
    "Можно мне.... к вам..."
    "О даааа.... сучка, еще как можно!"
    "тук - тук - тук"
    "не мешайте, я занят"

    "Я так и знал, что она здесь"
    "Вас двое?"
    "*вечно он меня обламывает*"
    "Это мисс Чанг"
    "так будет даже лучше"
    "Последнее время у нее случаются какие-то припадки"
    "Кто первый?"
    "Сначала все думали, что это лунатизм, но похоже, что тут замешана какая-то другая магия"
    "Инородная магия"
    "почему он на меня так смотрит?"
    "Ты все понял, джин, это какие-то твои фокусы?!"
    "Я тоже умею делать разные фокусы"
    "Что?? Нет, я же сказал, что не могу ничего делать из того, что умел!"
    "...."
    "Может быть ты, патлатый?"
    "Хм..."
    "Это какая-то странная магия, я еще такой не видел...."
    "Ладно, мне потребуется некоторое время чтобы снять эти чары"
    "....{w} эм"
    "Снять?"
    "ну да, не стоит играть с огнем раз уж на нас уже обратило внимание министерство"
    "стой"
    "что?"
    "Может быть это та самая магия, которая отправила меня сюда?"
    "...."
    "С чего бы это вдруг?"
    "Хотя, конечно, я такой еще не видел"
    "предоставь это мне"
    "....."
    "что?"
    "я могу сделать это"
    "зачем?"
    "поверь, снейп, я чуствую, что в этом замешана магия, из-за которой я здесь, я сам должен разобраться"
    "......{w}....."
    "ладно, делай что хочешь"
    "......{w} интересно, он действительно мне поверил?"
    "Ну что, дорогая, мы остались одни"
    "..."
    "Давай вернемся к нашему старому разговору..."
    "Какому разговору?"
    "...."
    "сука"
    "Эм, я шла к себе и не помню как оказалась здесь"
    "........."
    "Ты можешь идти"
    "..."
    "Нужно придумать как развести эту припадочную"








label quiditch:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    m "Ты мог бы и упомянуть что эта Гринграсс - капитан группы поддержки"
                                                         # SNAPE

    sna_01 "Я не очень слежу за этим цирком"
                                                       # SNAPE

    sna_07 "Надеюсь, что из-за отсутсвия директора у нас не возникнет лишних проблем с кубком"
    m "кубком?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                      # SNAPE

    sna_06 "будет несколько важных игр из-за которых сюда приедет много людей"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                      # SNAPE

    sna_18 "я уже все предусмотрел, все знают, что ты занят очень важными исследованиями и тебя никто не побеспокоит"

    m "Я бы не отказался чтобы меня побеспокоила парочка болельщиц"

    sna_01 "Чтобы ты стал с ними делать?"

    m "эм...{w} ну..."
                                                          # SNAPE

    sna_19 "Так и представляю, столетний Альбус Дамблдор развращает молодых студенток, хахахаха"

    m "эм..."
    m "Да, наверное, это глуповато"

    m "А что там будут за игры?"
                                                       # SNAPE

    sna_01 "Сборная Хогвартса будет играть с другими школами за звание чемпионов по квидиччу"
    m ".....{w}"
    m "че?{w} звучит как что-то похожее на пинг-понг"
                                                   # SNAPE

    sna_10 "кинг-конг?"
    m ".....{w} проехали"
    m "Мне нужно знать что это за квидичч"

    sna_11 "эм..."

    sna_10 "Ну если в двух словах...."

    $ dap_publ = 1
    ">Оставшийся вечер снейп рассказывает о том, что такое квидичч и про кубок между школами магии"
    return

label snape_kram:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                      # SNAPE
    show screen s_head2
    sna "как продвигается работа с нашей высокорожденной?"
    hide screen s_head2
    m "я почти закончил"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                        # SNAPE
    show screen s_head2
    sna "почти?"
    hide screen s_head2
    m "она уже готова, осталось только подтолкнуть ее сделать что-нибудь компрометирующее у всех на глазах"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2
    sna "У всех на глазах? На этом матче будет много прессы"
    hide screen s_head2
    m "Матч?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                        # SNAPE
    show screen s_head2
    sna "Ах, ты же не следишь за этим всем..."
    $ s_sprite = "03_hp/10_snape_main/24.png"                                        # SNAPE
    show screen s_head2
    sna "Мне пришлось изрядно потрудится, чтобы объяснить всем, почему на таком событии не присутствует директор школы, принимающей чемпионат"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                        # SNAPE
    show screen s_head2
    sna "Сюда слетелось пол мира, другие школы, пресса, просто зрители"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
    show screen s_head2
    sna "Отличный шанс отличиться для нее"
    hide screen s_head2
    m "Хм..."
    m "Что будет на этом матче?"
    show screen blktone
    with d3
    ">Весь вечер вы проводите со Снейпом, рассказывающим о будущем матче"
    m "Я могу устроить это, но мне понадобится одно зелье"
    $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                        # SNAPE
    show screen s_head2
    sna "Ха-ха-ха, а это прекрасная идея, У меня как раз есть подходящее!"
    $ daphne_event = 12
    hide screen s_head2
    call sly_plus from _call_sly_plus_15
    hide screen blktone
    hide screen bld1
    with d3
    return



#######################################################


#label harry_obrad_old:
#    "Профессор, сегодня было совершено еще одно нападение на студентку"
#    "...."
#    "Это опять проделки Воландеморта, профессор!"
#    "как же он заебал..."
#    "Может получится получить от этого выгоду?"
#    "Кхем, да, Гарри, этот Вор-мандер-форт совсем распоясался"
#    "Я так и знал!"
#    "Что мы будем делать, профессор?!!"
#    "Я работал над этим вопросом последние... кхм... 10 лет"
#    "....."
#    "Как я смог выяснить, на самом деле, он не из нашего мира!"
#    "Да, точно...{w}....{w}"
#    "Что?"
#    "......"
#    "Да, Гарри, он не обычный человек, он пришел из другого мира"
#    "......"
#    "Я сильно на тебя не рассчитываю, я буду искать способ вернуть его обратно в его мир все следующее время, но если ты тоже поищешь, это точно не помешает"
#    "......"
#    "Да, профессор! я побежал!!!"
#    "Имбецил"

#label harry_potions_old:
#    "Мне кажется я приблизился к разгадке как победить его, Гарри"
#    "..."
#    "Как же, профессор Дамблдор?!!"
#    "Для этого мне нужна будет твоя помощь"
#    "Я сделаю все что потребуется профессор!"
#    "да"
#    "Вместе мы победим его!"
#    "Отлично, мне нужно..."
#    "Вместе, мы сможем многое, я готов на все ради Хогвартса!"
#    "да, тебе нужно будет...."
#    "Заткнись!"
#    "...."
#    "...."
#    "Кхем, значит так, мне нужно будет, чтобы ты нашел...."





#    "Да профессор, я вернусь когда найду их"

#    "Профессор, я нашел то, что вы просили!"
#    "Отлично, Гарри!"
#    "Только как это поможет в сражении с Волан-Де-Мортом?"
#    "Эм... ну.... терпение молодой человек, ты все узнаешь, когда придет время"
#    "....."
#    "да, профессор!"
#    "долбоеб"









label hermione_podder01:
    $ hermione_pod_skirt = 2
    $ h_body = "03_hp/13_hermione_main/body_41.png"
    her "Вы звали меня, профессор?"
    g4 "Ах ты черт, что с тобой?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Ой, простите"
    $ h_body = "03_hp/13_hermione_main/body_48.png"
    her "ик"
    $ h_body = "03_hp/13_hermione_main/body_41.png"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_35.png"
    her "Мы с командой праздновали победу в кубке...."
    m "..... {w}со всей командой?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "эм...... я обещала мальчикам подарок в случае победы и...."
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "кажется переоценила свои силы"
    $ h_body = "03_hp/13_hermione_main/body_48.png"
    her "икк"
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "простите, но сегодня я не смогу продавать услуги, сэр"
    m "я вижу...."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "мне пора возвращаться, осталось еще 3 члена команды..."
    m "Остальные члены уже получили награду?"
    $ h_body = "03_hp/13_hermione_main/body_68.png"
    her "О да, я как следует...."
    $ h_body = "03_hp/13_hermione_main/body_47.png"
    her "Эй, что за намеки!"

    g4 "Какие уж тут намеки"
    $ h_body = "03_hp/13_hermione_main/body_43.png"
    her "......"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "я пошла, сэр"
    $ h_body = "03_hp/13_hermione_main/body_48.png"
    her "ик"
    m "......"
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if daytime:
        $ hermione_takes_classes = True
        if mad >=3 and mad <= 6:
            her "..............................."
        elif mad >=7:
            her "*Humph!*..."
        else:
            her "Oh, alright. I will go to classes then."
        hide screen bld1
        hide screen hermione_main
        hide screen blktone
        hide screen hermione_02
        hide screen ctc
        with d3
        jump day_main_menu
    else:
        if mad >=3 and mad <= 6:
            her "..............................."
        elif mad >=7:
            her "Tch..."
        else:
            her "Oh, alright. I will go to bed then."
        hide screen bld1
        hide screen hermione_main
        hide screen blktone
        hide screen hermione_02
        hide screen ctc
        with d3
        $ hermione_sleeping = True
        jump night_main_menu






label titfucking:
    if titfuck_points == 0:
        m "мисс Грейнджер"
        $ h_body = "03_hp/13_hermione_main/body_02.png"
        her "да, профессор?"
        $ h_body = "03_hp/13_hermione_main/body_01.png"
        m "у меня есть некоторая работа для вас"
        $ h_body = "03_hp/13_hermione_main/body_87.png"
        her "ох, могу себе представить"
        $ h_body = "03_hp/13_hermione_main/body_08.png"
        her "что на этот раз?"
        m "вы выполняли до этого какую-нибудь работу...{w} вашей грудью?" # специально сделал этот момент для каламбура job - titjob
        $ h_body = "03_hp/13_hermione_main/body_07.png"
        her "......."
        $ h_body = "03_hp/13_hermione_main/body_08.png"
        her "моей грудью, сэр?"
        $ h_body = "03_hp/13_hermione_main/body_12.png"
        her "...."
        m "ваша грудь отлично бы подошла для некоторой работы"
        $ h_body = "03_hp/13_hermione_main/body_21.png"
        her "профессор!"
        $ h_body = "03_hp/13_hermione_main/body_34.png"
        her "я поняла о чем вы" # а тут просто "я знаю что такое титджоб"
        m "так что, вы когда нибудь делали..... {w}такую работу?"
        $ h_body = "03_hp/13_hermione_main/body_18.png"
        her "......."
        $ h_body = "03_hp/13_hermione_main/body_34.png"
        her "{size=-7}нет...{/size}"
        m "эм... ты что-то сказала?"
        $ h_body = "03_hp/13_hermione_main/body_30.png"
        her "нет!!!"
        $ h_body = "03_hp/13_hermione_main/body_33.png"
        g9 "что ж, значит сегодня удачный день!"
        $ h_body = "03_hp/13_hermione_main/body_22.png"
        her "удачный?! как вы можете назвать его удачным?!"
        m "разве плохо учиться чему-то новому?"
        $ h_body = "03_hp/13_hermione_main/body_34.png"
        her "я не думаю, что это то, чему бы я хотела учиться в школе волшебства!!!"
        $ h_body = "03_hp/13_hermione_main/body_44.png"
        her  "......"
        m "это то, что ты сможешь применить в реальном мире"
        $ h_body = "03_hp/13_hermione_main/body_28.png"
        her "......"
        $ h_body = "03_hp/13_hermione_main/body_30.png"
        her "1000 очков"
        $ h_body = "03_hp/13_hermione_main/body_21.png"
        m "будьте реалисткой, мисс Грейнджер"
        $ h_body = "03_hp/13_hermione_main/body_30.png"
        her "10 000 очков!!"
        menu:
            "ты получишь 15 очков и я обещаю не кончать на тебя":
                jump too_much

            "ты получишь 45 очков":
                $ h_body = "03_hp/13_hermione_main/body_03.png"
                her "......."
                $ h_body = "03_hp/13_hermione_main/body_10.png"
                her "45 очков?"
                $ h_body = "03_hp/13_hermione_main/body_13.png"
                her "это поможет Гриффиндору снова лидировать...."
                m "это значит \"да\"?"
                $ h_body = "03_hp/13_hermione_main/body_34.png"
                her "да, да, да"
                g9 "отлично"
                m "приступайте, мисс Грейнджер"
                $ h_body = "03_hp/13_hermione_main/body_13.png"
                her "да, профессор"
                jump titfucking2


            "хорошо, 100 очков":
                $ h_body = "03_hp/13_hermione_main/body_22.png"
                her "......."
                $ h_body = "03_hp/13_hermione_main/body_13.png"
                her "правда?"
                m "да"
                $ h_body = "03_hp/13_hermione_main/body_29.png"
                her "ну......"
                $ h_body = "03_hp/13_hermione_main/body_34.png"
                her "хорошо"
                jump titfucking2


    elif titfuck_points == 1:
        m "Что ты думаешь на счет того, чтобы поработать сегодня?"
        $ h_body = "03_hp/13_hermione_main/body_29.png"
        her "эм...."
        $ h_body = "03_hp/13_hermione_main/body_04.png"
        her "я всегда готова сэр"
        $ h_body = "03_hp/13_hermione_main/body_03.png"
        her "...."
        m "отлично"
        g9 "у меня как раз есть работа для твоих сисек"
        $ h_body = "03_hp/13_hermione_main/body_10.png"
        her "опять?"
        $ h_body = "03_hp/13_hermione_main/body_23.png"
        her "......"
        m "так что?"
        $ h_body = "03_hp/13_hermione_main/body_02.png"
        her "да, сэр"
        jump titfucking2

    else:
        jump titfucking3

label titfucking3:
    m "мисс Грейнджер"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да, профессор?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "как вы смотрите на то, чтобы у этих двух замечательных сисек появилась работа?"
    $ h_body = "03_hp/13_hermione_main/body_66.png"
    her "........"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "конечно, профессор"

    hide screen hermione_main
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3
    hide screen desk_02
    hide screen hermione_walk_01
    hide screen genie
    $ genie_chibi_xpos = 300 #-185 behind the desk.
    $ genie_chibi_ypos = 200
    $ g_c_u_pic = "titjob_ani_pause"
    show screen chair_02
    show screen g_c_u
    show screen desk_02
    hide screen blktone


    ">Гермиона обхватывает ваш член своей грудью и начинает двигаться"
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    #Stroking the cock.
    $ genie_chibi_xpos = 300 #-185 behind the desk.
    $ genie_chibi_ypos = 200
    $ g_c_u_pic = "titjob_ani"
    hide screen blkfade
    with d7
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d3
    pause 5.0
    g9 "ох да, вот так"
    g9 "отлично"
    m "в этот раз у тебя получается лучше"

    her_16 "спасибо, профессор"
    m "хм......"
    menu:
        m "....."

        "что ты думаешь о моем члене?":
            her_03 "что?"
            her_01 "о.... вашем члене?"
            m "что ты думаешь о...."
            her_38 "он восхитетелен"
            m "....."
            m "продолжай"
            her_06 "если у меня превосходная грудь, то....."
            ">гермиона усиленно двигает грудью вокруг вашего члена"
            her_10 "то это превосходный член"
            m "....."
            m "превосходный?"
            her_06 "идеальный размер"
            her_18  "идеальная форма"
            ">гермиона опускает голову и касается языком вашего члена"
            her_33 "идеальный вкус"
            g9 "ах ты шлюха!"
            her_10 "я думаю, что ваш член должен быть общественным достоянием"
            m ".....{w} что?"
            her_19 "я думаю, что ваш идеальный член должен быть достоянием всей школы и каждая девушка должна иметь к нему доступ"
            g4 "......."
            m "ладно, я слышал достаточно"
            her_09 "это было слишком?"
            m "ну.................{w} немного"
            her_01 "извините, наверное, я немного переборщила...."
            m "просто сосредоточся на том чтобы хорошенько массажировать мой член"
            her_15 "......."
            ">гермиона продолжает дрочить ваш член своей грудью"

        "Скажи: \"я сисястая шлюха!\"":
            her_03 "простите?"
            her_10 "эм..... я сисястая шлюха!"
            g9 "отлично, я рад, что мы уяснили это"
            m "теперь скажи:...."
            menu:
                "я бесстыжая спермоглотка!":
                    her_03 "......"
                    her_10 "да, конечно"
                    her_05 "я......"
                    her_13 "я бесстыжая спермоглотка"
                    her_06 "грязная маленькая шлюха, которая хочет проглотить сперму своего хозяина"
                    g9 "о да, отлично"
                "я люблю сперму на своем лице!":
                    her_17 "я люблю сперму на своем лице"
                    her_37 "горячую..."
                    her_38 "липкую...."
                    her_34 "сперму......"
                    her_36 "......................................"
                    g9 "идеально"

        "У тебя получается лучше, ты тренировалась?":
            her_01 "эм..."
            her_05 "ну, можно и так сказать, не на настоящих членах"
            m "а на чем?"
            her_12 "ну я попросила Джинни...."
            m "это твоя подруга?"
            her_11 "да. Я спросила ее как лучше делать это"
            her_05 "она сказала, что лучший способ тренировки - это практика"
            m "и... ты практиковалась?"
            her_01 "на джинни"
            her_09 "эм... на ее руке..."
            g4 "ты дрочила рукой руку подруги?"
            her_10 "я просто тренировалась!"
            her_17 "она подсказала пару трюков"
            her_18 "вам нравится?"
            g9 "да, это намного луше"
            her_05 "мне кажется, что джинни тоже понравилось"
            m "почему ты так решила?"

            her_17 "ну...."
            her_37 "она даже начала....."
            her_38 "играть с собой......"
            g9 "да, продолжай, шлюха"

    m "теперь скажи:..."
    menu:
        "я люблю дразнить моего папочку своими большими сиськами":
            her_02 "я не делала этого!"
            m "я знаю, просто скажи это"
            her_08 "мой отец? это мерзко! Как вы могли предположить, что я...."
            m "Давай... просто скажи это для меня"
            her_04 "................"
            her_01 "ну...."
            her_05 "Иногда, когда я обнимала его"
            her_12 "............."
            m "что?"
            her_15 "я прижималась к нему своей грудью......"
            m "Как ты думаешь, ему нравилось?"
            her_17 "я не уверена"
            her_15 "то есть, я так думаю"
            her_05 "в такие моменты он всегда старался прикрыть свою промежность, чтобы я не видела...."
            m "что?"
            her_15 "его стояк"

            her_17 "я обнимала его каждый день, перед тем как ложиться спать"
            her_18 "я прижималась к нему...."
            g9 "хах, шлюха"
            her_17 "и когда он целовал меня в лоб"
            her_06 "Я уверена, он мог рассмотреть все, что находилось в моей блузке...."
            her_15 "но всего этого не было конечно!"
            her_15 "это все для вашего больного воображения!"
            g9 "конечно"

        "я люблю дразнить моих одноклассников моими большими титьками":
            her_05 "я люблю дразнить моих одноклассников моими большими титьками"
            g9 "о да, конечно"
            her_16 "я люблю завистливые взгляды других девочек"
            g9 "о да, так и представляю их..."
            her_18 "я обoжаю дразнить гарри и рона за завтраком"
            her_37 "иногда я прохожу мимо них лишь с одной застегнутой пуговицей..."
            her_38 "а иногда я одеваю только один жилет"
            her_34 "однажды когда я проходила мимо вашего кабинета ночью, моя грудь была едва прикрыта"
            her_16 "и когда я завернула за угол....."
            her_18 "один второкурсник бежал и угодил в них прямо головой"
            m "головй прямо в твои сиськи?"
            her_16 "все что я могла видеть - это верх его головы"
            g9 "что он делал?"
            her_01 "он пытался отстраниться..."
            m "пытался?"
            her_06 "ну... возможно я задержала его там..."
            her_05 "немножко"
            her_01 "просто для того, чтобы сказать ему, что все хорошо"
            g9 "ты маленькая шлюшка"
    m "хм...."

    g9 "твои сиськи такие мягкие"
    her_05 "спасибо, профессор"
    ">Гермиона сжимает свои груди сильнее и начинает быстро двигаться"
    g9 "Ооохх даааа!!!!"

    g4 "уже почти! куда мне кончить?"
    menu:
        "в рот":
            g4 "вот оно, тебе лучше быть готовой!"
            g4 "да, ты мальнкая шлюха!"
            ">Вы берете голову голову и просовываете свой член прямо в ротик гермионы"
            her_03 "!!!"
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            g9 "О ДА!! ДА!! ВОЗЬМИ ЭТО ШЛЮХА!!!"
            her_10 "!!!!"

            $ g_c_u_pic = "titjob_mouth_ani"
            hide screen bld1
            hide screen blkfade
            with d3
            show screen ctc
            pause 5.0




            $ sperm_on_tits = True
            $ h_body = "03_hp/13_hermione_main/body_125.png"
            her "......"
            m "это было.....{w} круто"
            her ".............."
            m "как ты себя чувствуешь?"
            her ".............."
            m "мисс Грейнджер?"
            $ h_body = "03_hp/13_hermione_main/body_135.png"
            ">гермиона открывает рот, сперма стекает с ее язычка прямо к ней на грудь"
            $ h_body = "03_hp/13_hermione_main/body_132.png"
            her "почему вы сделали это прямо мне в рот?"

            m "ну....... ты просила не делать этого тебе на лицо"
            $ h_body = "03_hp/13_hermione_main/body_126.png"
            hide screen ctc
            show screen blkfade
            with d5
            show screen hermione_main
            hide screen chair_02
            hide screen desk_02
            show screen genie
            show screen hermione_02
            hide screen g_c_u
            pause .1
            hide screen blkfade
            with d6
            her "уф.... так много спермы! я еле справилась!"
            m "ты хорошо постаралсь...."
            $ h_body = "03_hp/13_hermione_main/body_144.png"
            her "занятия почти начались, а я вся в вашей сперме...."
            m "45 очков Гриффиндору"
            $ h_body = "03_hp/13_hermione_main/body_141.png"
            her "...."
            $ h_body = "03_hp/13_hermione_main/body_13.png"
            her "спасибо, профессор"
            $ sperm_on_tits = False


        "на грудь":
            m "Аргххх"

            g4 "Да, шлюха!"
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            g9 "Yeah, you're tits felt great slut!"
            her_10 "!!!!"
            $ genie_chibi_xpos = 300 #-185 behind the desk.
            $ genie_chibi_ypos = 200
            $ g_c_u_pic = "titjob_chest_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            with d3
            g9 "аАаххх, дааа11"
            $ soerm_on_tits = True

            her_40 "!!!!!!!!!!!!!"
            her_12 ".............."

            hide screen ctc
            show screen blkfade
            with d5

            hide screen chair_02
            hide screen desk_02
            show screen genie
            show screen hermione_02
            hide screen g_c_u
            pause .8
            $ sperm_on_tits = True
            hide screen blkfade
            with d6
            pause 1.0
            show screen hermione_main
            with d6


            if daytime:

                $ h_body = "03_hp/13_hermione_main/body_21.png"
                her "зачем вы кончили так много?!"
                $ h_body = "03_hp/13_hermione_main/body_20.png"
                her "как будто кто-то вылил целое ведро на мою грудь"
                $ h_body = "03_hp/13_hermione_main/body_29.png"
                her "занятия почти начались а я вся в вашей сперме!"
                $ h_body = "03_hp/13_hermione_main/body_69.png"
                her  "......"
                m "просто вытри это, никто не заметит"
                g9 "если только не учует запах спермы"
                $ h_body = "03_hp/13_hermione_main/body_71.png"
                her "......"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "я хочу получить свою оплату"


            else:
                $ h_body = "03_hp/13_hermione_main/body_66.png"
                her "откуда у вас столько спермы?!"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "как мне теперь возвращаться в крыло гриффиндора в таком виде?!"
                m "просто вытри"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                m "это не первый раз, когда ты вернешься в кроватку с запахом спермы"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "......"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "я хочу свою оплату"

    m "45 очков Гриффиндору"
    her "...."
    her "спасибо, профессор"
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    if titfuck_points == 2:
        $ titfuck_points = 3
    call music_block from _call_music_block_40
    $ sperm_on_tits = False
    $ hermione_takes_classes = True
    jump day_main_menu

label titfucking2:
    hide screen hermione_main
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3

    hide screen hermione_walk_01
    hide screen genie
    $ genie_chibi_xpos = 300 #-185 behind the desk.
    $ genie_chibi_ypos = 200
    $ g_c_u_pic = "titjob_ani_pause"
    show screen chair_02
    show screen g_c_u
    show screen desk_02
    hide screen blktone

    ">Гермиона обхватывает ваш член своей грудью"

    m "отлично теперь давай, вверх-вниз"
    her_15 "..........."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    #Stroking the cock.
    $ genie_chibi_xpos = 300 #-185 behind the desk.
    $ genie_chibi_ypos = 200
    $ g_c_u_pic = "titjob_ani"
    hide screen blkfade
    with d7
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d3
    pause 5.0
    her_01 "...."
    g9 "............."
    her_12 "................"
    her_01 "это......{w} приятно, сэр?"
    m "прятно?"
    g9 "это охрененно"
    her_12 "............."
    pause 5.0
    her_01 "............."
    her_05 "эм, профессор..."
    m "да?"
    her_25 "вы обещаете, что не будете кончать мне на лицо?"
    menu:
        "обещаю не покрывать это милое личико моей спермой":
            her_04 "....."
            her_15 "спасибо, профессор"
            m "......"

        "посмотрим, как получится":
            her_04 "пфф"
            her_12 "....."
            her_10 "тогда хотя бы не на волосы"
            m "........."
            her_11 "........"
            her_04  "........."
            her_05 "так что?"
            m "хорошо"
            her_09 "спасибо"

    # прошло время

    pause 5.0
    her_15 "эм.... профессор?"
    m "что?"
    her_05 "вы еще не....."
    m "а что?"
    if daytime == True:
        her_12 "ну.... мне пора бы идти на занятия"
    else:
        her_12 "ну..... я обещала Джинни, что мы будем учить нумерологию этим вечером"
        her_04 "она что-нибудь заподозрит, если я проведу здесь много времени"
    m "тебе нужны очки или нет?"
    her_01 "я понимаю, простите"
    m "ты можешь ускорить это"
    her_05 "как?"
    menu:
        "расскажи мне как сильно ты любишь свои сиськи":
            her_01 "что?"
            her_05 "мою грудь?"
            m "ну знаешь, как хорошо иметь большую грудь"
            m "внимание, которое ты получаешь из-за нее..."
            her_12 "эм, ну"
            her_02 ".........."
            her_01 "................."
            her_16 "это было один раз в библиотеке...."
            her_16 "там никого не было, кроме меня и парня, который сидел рядом со мной"
            m "отлично, и что было дальше?"
            her_17 "ну, там было так жарко, поэтому я сняла мой жилет..."
            her_18 "этот парень пытался делать вид, что не смотрит, но я четко видела его похотливый взгляд"
            her_06 "потом я начала расстегивать пуговицы..... одну за другой"
            g9 "хах, ты маленькая шлюшка"
            her_16 "на третей пуговице он не мог оторвать глаз от меня"
            her_18 "когда я расстегнула четвертую, его руки опустились под стол"
            m "реально?"
            her_17 "да, мне кажется, я даже слышала как он мастурбирует"
            her_18 "когда я расстегнула пятую пуговицу, он мог видеть мои соски"
            m "тебе не было стыдно?"
            her_16 "на шестой пуговице уже нечего было скрывать...."
            her_06 "он видел мою голую грудь"
            her_18 "и он уже не пытался скрывать то, что он делает"
            her_17 "когда я расстегнула последнюю пуговицу, это уже было слишком для него"
            her_15 "он кончил прямо на стол, капелька даже попала мне на ногу"
            g4 "!!!"
            her_38 "кончи на меня старик, кончи мне прямо на грудь!"
            g4 "ах ты шлюха!"

        "Высунь твой язык и наклони голову вниз":
            her_03 "что?"
            m "просто сделай это"
            her_43 "так?"
            m "сильнее"
            her_44 ".........."
            m "да, хорошо. Наклоняй свою голову ниже и ниже"
            her_45 "......"
            her_46 "............................."
            g9  "........"
            her_44 "я не могу держать язык так долго, у меня начинает течь слюна"
            g9 "отлично, пусть она капает прямо на твои сиськи"
            her_45 "......."
            m "теперь поднеси свой язык как можно ближе к моему члену"
            her_45 "......"
            her_46 "вот так?"
            m "отлично, мисс Грейнджер"
            her_46 "......."
            g9 "отлично, продолжай дрочить мой член"
            ">вы пододвигаете член, чтобы он касался ее языка"
            her_44 "........."
            g9 "ох да, ты шлюха"
            ">вы делаете это еще раз"
            her_46 ".........."
            g9 "ох да, ты маленькая сисястая шлюха"
            her_45 "........"
            g4 "я хочу кончить в этот маленький шлюшкин ротик"
            her_46 "........."
            g4 "........"
    g4 "уже почти! куда мне кончить?!"

    menu:
        "кончить ей в рот":
            g4 "вот оно, тебе лучше быть готовой!"
            g4 "да, ты мальнкая шлюха!"
            ">Вы берете голову голову и просовываете свой член прямо в ротик гермионы"
            her_29 "!!!!!!!!!!!!!!!!!!"
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            $ g_c_u_pic = "titjob_mouth_ani"
            hide screen bld1
            hide screen blkfade
            with d3
            show screen ctc
            pause 5.0
            g9 "О ДА!! ДА!! ВОЗЬМИ ЭТО ШЛЮХА!!!"
            $ g_c_u_pic = "titjob_mouth_ani"
            hide screen bld1
            hide screen blkfade
            with d3
            show screen ctc
            pause 5.0



            hide screen blkfade
            with d5
            $ sperm_on_tits = True
            her_50 "!!!!!!!!!!!!!!!!!!!!!!!!!"
            her_50 "......"
            m "это было.....{w} круто"
            her_50 ".............."
            m "как ты себя чувствуешь?"
            her_47 ".............."
            m "мисс Грейнджер?"
            ">гермиона открывает рот, сперма стекает с ее язычка прямо на грудь"
            her_45 "почему вы сделали это прямо мне в рот?"
            m "ну....... ты просила не делать этого тебе на лицо"
            her_15 "........"
            hide screen ctc
            show screen blkfade
            with d5

            hide screen chair_02
            hide screen desk_02
            show screen genie
            show screen hermione_02
            hide screen g_c_u
            pause .1
            hide screen blkfade
            with d6
            pause 1.0
            show screen hermione_main
            with d6
            $ h_body = "03_hp/13_hermione_main/body_117.png"
            her "уф.... так много спермы! я еле справилась!"
            m "ты хорошо постаралсь...."
            $ h_body = "03_hp/13_hermione_main/body_118.png"
            her "занятия почти начались, а я вся в вашей сперме...."




        "кончить на грудь":
            g4 "Аргххх!!!"
            g4 "Да, шлюха!"
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch

            $ genie_chibi_xpos = 300 #-185 behind the desk.
            $ genie_chibi_ypos = 220
            $ g_c_u_pic = "titjob_chest_ani"
            hide screen blkfade
            with d6
            show screen ctc
            hide screen bld1
            with d3
            pause
            with d3
            g9 "аАаххх, дааа11"

            $ soerm_on_tits = True
            her_15 "!!!!!!!!!!!!!"
            $ g_c_u_pic = "new/tj_cum_chest_25.png"
            her_11 ".............."
            g9 "..............."
            her_12 "............"
            m "это было......"
            g9 "круто"
            her_12 "........................"
            hide screen ctc
            show screen blkfade
            with d5

            hide screen chair_02
            hide screen desk_02
            show screen genie
            show screen hermione_02
            hide screen g_c_u
            pause .8
            $ sperm_on_tits = True
            hide screen blkfade
            with d6
            pause 1.0
            show screen hermione_main
            with d6
            if daytime:
                $ h_body = "03_hp/13_hermione_main/body_21.png"
                her "зачем вы кончили так много?!"
                $ h_body = "03_hp/13_hermione_main/body_20.png"
                her "как будто кто-то вылил целое ведро на мою грудь"
                $ h_body = "03_hp/13_hermione_main/body_29.png"
                her "занятия почти начались а я вся в вашей сперме!"
                $ h_body = "03_hp/13_hermione_main/body_69.png"
                her  "......"
                m "просто вытри это, никто не заметит"
                g9 "если только не учует запах спермы"
                $ h_body = "03_hp/13_hermione_main/body_71.png"
                her "......"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "я хочу получить свою оплату"


            else:
                $ h_body = "03_hp/13_hermione_main/body_66.png"
                her "откуда у вас столько спермы?!"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "как мне теперь возвращаться в крыло гриффиндора в таком виде?!"
                m "просто вытри"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                m "это не первый раз, когда ты вернешься в кроватку с запахом спермы"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "......"
                $ h_body = "03_hp/13_hermione_main/body_118.png"
                her "я хочу свою оплату"

    m "45 очков Гриффиндору"
    her "...."
    her "спасибо, профессор"
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    if titfuck_points == 0:
        $ titfuck_points = 1
    elif titfuck_points == 1:
        $ titfuck_points = 2
    hide screen ctc
    with d3
    $ sperm_on_tits = False
    hide screen hermione_02
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f
    pause 2
    hide screen hermione_walk_01_f
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    call music_block from _call_music_block_41
    $ hermione_takes_classes = True
    jump day_main_menu










#label cho_nachalo_snape:
#    "Мне нужно, чтобы ты помог мне с этой припадочной"
#    "Что? ты же говорил, что сам решишь эту проблему"
#    "Ты сам знаешь, что здесь я слаб и не могу всего, что мог раньше"
#    "...."
#    "Что от меня требуется?"
#    "Ты ведь занимаешься зельеварением, правильно?"
#    "Да"
#    "Есть такие зелья... вызывающие некоторые..... кхем.... желания"
#    "желания?"
#    "ну...."
#    "Так ты попросил оставить ее тебе для того, чтобы удовлетворить пару твоих \"желаний\" пока она в трансе?"
#    "Ну... как бы это сказать...."
#    "*ворчит*"
#    "я мог бы и догадаться"
#    "......{w} так ты поможешь?"
#    "хм...."
#    "Вообще-то это запретная магия"
#    "......"
#    "но для профессоров есть исключения, верно?"
#    "не в этом дело, реагенты очень редкие, просто так их не найти"







label snape_daph_chat:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "..."
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen snape_main
    with Dissolve(.3)
    sna "Похоже дело с нашей маленькой принцессой продвигается"
    m "......."
    m "о чем ты?"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"
    sna "вчера я застукал ее во время дрочки одному из учеников"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "они подумали, что я ничего не видел, на самом деле я просто напугал их, когда мне надоело наблюдать"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Хах, не думал, что действительно получится ее подставить"
    m "Пока рано радоваться, еще многое предстоит сделать"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Не могу дождаться этого момента"
    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f
    pause 3
    hide screen snape_walk_01_f
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2       # SNAPE
    hide screen s_head2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    $ duels = 1
    $ snape_fap = 3
    $ chitchated_with_snape = True
    return



#label fire_fap:
#    sna "Всем внимательно слушать меня!"
#    sna "Для того чтобы приготовить противоядие от яда мурлков нужно смешать....."
#    harr ""
#    her ""
#    # появляется гермиона и просто начинает ему дрочить
#    sna "щепотку тухлых яиц тибетских троллей, 2/74 порции блевотины мексиканской гидры...."
#    harr "....."
#    her "...."
#    # дрочит и ускоряется
#    sna "Грейнджер!"
#    her "...."
#    her "да?"
#    "Встань"
#    "....."
#    "зачем?"
#    "Встань!"
#    "..........."
#    "что это у тебя на одежде?"
#    "....."
#    "это......"
#    "ой, мне кажется я уронила молочко вислобрюха"
#    "ЧТО?!!"
#    "Ты знаешь сколько оно стоит?!!!"
#    "Грейнджер, я сообщу в министерство магии!!!"


label hermione_potion2:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 610
    $ hermione_chibi_ypos = 250
    show screen hermione_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause 3
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    show screen ctc
    with Dissolve(.3)
    pause
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Good morning professor."
    hide screen ctc
    her "я приготовила зелье о котором вы говорили"
    m "отлично"
    show screen gift
    $ the_gift = "03_hp/18_store/32.png"
    $ renpy.play('sounds/win2.mp3')
    ">теперь у вас есть зелье превращения в хагрида"
    hide screen gift
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "....."
    $ h_body = "03_hp/13_hermione_main/body_08.png"
    her "эм.... профессор"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    m "да?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "как на счет моих очков"
    m "ах, да"
    m "15 очков Гриффиндору"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "спасибо, профессор"
    $ hagpot = 1
    $ quest_hagrid = 100
    jump day_time_requests

label find_feather:
    m "..."
    m "Эта птица линяет?"
    g4 "Почему здесь нет ни одной урны?"
    play sound "sounds/win2.mp3"
    $ ph_feather = 1
    ">Перо феникса было добавлено в ваш инвентарь"
    jump day_main_menu



label snape_ingr2:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "..."
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    show screen snape_main
    with Dissolve(.3)
    $ phx_ingr2 = 1
    sna "это последняя, которая у меня была. Надеюсь она тебе действительно нужна"
    $ the_gift = "03_hp/18_store/09.png" # THE ADVENTURE OF GALADRIEL. BOOK ONE.
    show screen gift
    with d3
    "Пыльца плотоядного фикуса была добавлена в вашу коллекцию"
    hide screen gift
    with d3
    g9 "отлично. Она не пропадет зря, будь уверен"
    jump snape_menu




label hermione_phx_potion:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 610
    $ hermione_chibi_ypos = 250
    show screen hermione_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01
    pause 3
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    show screen ctc
    with Dissolve(.3)
    pause
    her "Здравствуйте, профессор."
    hide screen ctc
    her "Я сделала зелье, которое вы просили"
    m "отлично"
    show screen gift
    $ the_gift = "03_hp/18_store/32.png"
    $ renpy.play('sounds/win2.mp3')
    ">Теперь у вас есть зелье для Феникса"
    hide screen gift
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "....."
    $ h_body = "03_hp/13_hermione_main/body_08.png"
    her "эм.... профессор"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "мои очки?"
    m "точно, очки"
    m "15 очков Гриффиндору"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "спасибо, профессор"
    $ phx_pot = 5
    jump day_time_requests    
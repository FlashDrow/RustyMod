label summon_potter:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ menu_x = 0.2
    $ harry_chibi_xpos = 370 #Near the desk.
    show screen harry_ch #Hermione stands still.
    show screen bld1
    with d3
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    with d3
    $ har_body = "f/hr_govor.png"
    harr "Вы звали меня, профессор?"

label harry_chat:
    $ har_body = "f/hr_def.png"
    menu:


        "Волос с бороды Хагрида" if quest_hagrid == 3:
            m "В этот раз мне потребуется от тебя очень уникальный ингридиент"
            $ har_body = "f/hr_udivl.png"
            harr "Что это, профессор?"
            m "кхм..."
            m "Мне нужен волос с бороды нашего лесника"
            $ har_body = "f/hr_def.png"
            harr "...."
            $ har_body = "f/hr_govor.png"
            harr "что?"
            $ har_body = "f/hr_def.png"
            m "мне нужен волос с бороды Хагрида"
            $ har_body = "f/hr_govor.png"
            harr "эм... а вы не пробовали спросить его?"
            $ har_body = "f/hr_def.png"
            m "..........."
            g4 "Это долгая история, тебе лучше о ней не знать"
            harr "......"
            $ har_body = "f/hr_govor.png"
            harr "Да, профессор"
            harr "Я постараюсь его достать, профессор"
            $ har_body = "f/hr_def.png"
            g9 "Отлично"
            $ quest_hagrid = 4
            jump harry_chat

        "Квест: яйца свинорыла" if phx_pot == 2:
            m "Гарри, я в двух шагах от поимки шмар-де-форта"
            $ har_body = "f/hr_udivl.png"
            harr "......"
            m "мне не достает последней детали"
            $ har_body = "f/hr_smile.png"
            harr "какой же, профессор?"
            m "Мне нужны яйца свинорыла из нашего леса"
            $ har_body = "f/hr_def.png"
            harr "эм... яйца, сэр?"
            m "да. ты сделаешь одолжение всему магическому сообществу если достанешь их"
            $ har_body = "f/hr_govor.png"
            harr "но... как я их достану, сэр?"
            $ har_body = "f/hr_def.png"
            g4 "какая разница как, на кону жизни людей!"
            $ har_body = "f/hr_udivl.png"
            harr "....."
            $ har_body = "f/hr_zlo.png"
            harr "да сэр! Я достану их!"
            m "вот и отлично"
            $ phx_ingr3 = 3
            hide screen bld1
            hide screen harry_main
            with Dissolve(.3)
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen harry_walk2
            pause 2
            $ harry_chibi_xpos = 610 #Near the desk.
            hide screen harry_walk2
            show screen harry_ch2 #Hermione stands still.
            with Dissolve(.3)
            $ harry_chated = True
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen harry_ch2 #Hermione stands still.
            if daytime:

                jump night_main_menu
            else:

                jump day_main_menu

        "-Что там с Чжоу Чанг?-" if chimi_event == 7:
            g9 "ну что, гарри, вчера ты заметил что-нибудь за ней?"
            $ har_body = "f/hr_govor.png"
            harr "эм... да, она вела себя сегодня..."
            $ har_body = "f/hr_def.png"
            m "как?"
            $ har_body = "f/hr_govor.png"
            harr "довольно странно"
            $ har_body = "f/hr_def.png"
            g4 "так что ты видел?"
            $ har_body = "f/hr_govor.png"
            harr "эм... хотя, наверное нет, ничего такого"
            $ har_body = "f/hr_def.png"
            g4 "..."
            m "что?"
            m "а что все таки было?"
            $ har_body = "f/hr_govor.png"
            harr "ну... эм..."
            harr "она общалась с парнями"
            $ har_body = "f/hr_def.png"
            m "и что они делали?"
            $ har_body = "f/hr_govor.png"
            harr "эм... я не видел"
            $ har_body = "f/hr_def.png"
            g4 "вообще ничего?"
            $ har_body = "f/hr_govor.png"
            harr "эм... нет"
            $ har_body = "f/hr_def.png"
            m "вот лопух"
            g4 "Не прекращай следить за ней, особенно в полнолуние"
            $ har_body = "f/hr_govor.png"
            harr "да сэр"
            $ har_body = "f/hr_def.png"
            $ chimi_event = 8
            jump harry_chat

        "-Спросить про Чжоу Чанг-" if (chimi_event > 10) and (chimi_event != 14) and (chimi_event != 15):
            if chimi_event >= 7:
                if (fullmoon == 2) or (fullmoon == 3):
                    jump harry_moon
                elif fullmoon == 0:
                    jump harrycho_not_moon
            "что то пошло не так"
            jump chimi_menu

        "-Что там с Чжоу Чанг?-" if (chimi_event > 3) and (harry_chimi == 0) and (chimi_event != 7):
            $ har_body = "f/hr_govor.png"
            harr "Ну... последнее время она ведет себя странно"
            $ har_body = "f/hr_def.png"
            m "Странно? Чо с ней?"
            $ har_body = "f/hr_govor.png"
            harr "Ну буквально вчера, пока я следил за ней..."
            $ har_body = "f/hr_def.png"
            m "......"
            m "Что?"
            $ har_body = "f/hr_govor.png"
            harr "Она подошла ко мне и сказала, что если еще раз увидит меня, то нашлет сглаз"
            $ har_body = "f/hr_def.png"
            m "......"
            $ har_body = "f/hr_govor.png"
            harr "Она не могла такого сказать сама, я думаю это был Волан-де-Морт!"
            $ har_body = "f/hr_def.png"
            m "......"
            g9 "Да, Гарри, похоже мы уже у него на хвосте"
            m "*что за идиот*"
            harr "...."
            m "продолжай наблюдение"
            $ har_body = "f/hr_govor.png"
            harr "да, сэр"
            $ har_body = "f/hr_def.png"
            jump harry_chat


        "Что там с Чжоу Чанг?" if (chimi_event < 3) and (chimi_event != 7):
            $ har_body = "f/hr_govor.png"
            harr "Эм... ничего"
            $ har_body = "f/hr_def.png"
            g4 "Как ничего?"
            $ har_body = "f/hr_govor.png"
            harr "Я следил за ней как мог, но она просто стала скрытнее"
            harr "Хотя каждый раз перед полнолунием она почему то становится общительной"
            $ har_body = "f/hr_def.png"
            m "Перед полнолунием, значит"
            $ chimi_event = 3
            m "Спасибо, Гарри"
            jump harry_chat


        "Что там с Чжоу Чанг??" if harry_chimi == 1:
            $ har_body = "f/hr_govor.png"
            harr "ну...."
            $ har_body = "f/hr_def.png"
            pause 1.0
            $ har_body = "f/hr_govor.png"
            harr "мне кажется, что с ней что-то не то"
            $ har_body = "f/hr_def.png"
            m "да, что?"
            $ har_body = "f/hr_morda1.png"
            harr "может быть, мне следует круглосуточно охранять ее?"
            g4 "...."
            $ harry_chimi = 2
            m "в другой раз"
            $ har_body = "f/hr_def.png"
            harr "да, профессор"
            jump harry_chat

        "Что там с Чжоу Чанг??" if harry_chimi == 2:
            $ har_body = "f/hr_govor.png"
            harr "ну...."
            $ har_body = "f/hr_def.png"
            pause 1.0
            $ har_body = "f/hr_govor.png"
            harr "мне кажется, что с ней что-то не то"
            $ har_body = "f/hr_def.png"
            m "да, что?"
            $ har_body = "f/hr_morda1.png"
            harr "может быть, мне нужно охранять ее сегодня?"
            g4 "...."
            $ harry_chimi = 2
            m "в другой раз"
            $ har_body = "f/hr_def.png"
            harr "да, профессор"
            jump harry_chat


        "Слухи на счет гермионы подтвердились?" if herm_vopr == 1:
            $ har_body = "f/hr_def.png"
            harr "Эм..."
            m "..."
            $ har_body = "f/hr_govor.png"
            harr "Нет, профессор"
            $ har_body = "f/hr_def.png"
            g4 "Что?{w} Нет?"
            $ har_body = "f/hr_govor.png"
            harr "Да, как и предполагалось, все это - происки Слизерина, наверное просто не могут смирится с тем, что в отличае от них нам не нужна поддержка, чтобы набирать очки"
            $ har_body = "f/hr_def.png"
            g4 "*Странно*"
            $ har_body = "f/hr_def.png"
            harr "Эм..."
            $ har_body = "f/hr_govor.png"
            harr "Профессор"
            $ har_body = "f/hr_def.png"
            m "Да?"
            $ har_body = "f/hr_govor.png"
            harr "Гриффиндор сильно сдал в последнее время..."
            $ har_body = "f/hr_morda1.png"
            harr "Можно мне еще 10 очков?"
            g4 "*Этот очкарик играет со мной?*"
            m "Очки зарабатываются потом и кровью, молодой человек"
            $ har_body = "f/hr_govor.png"
            harr "Ых... да, профессор"
            $ herm_vopr = 2
            jump harry_chat

        "Спросить про Гермиону":
            $ har_body = "f/hr_govor.png"
            harr "Эм, а что Гермиона?"
            $ har_body = "f/hr_def.png"
            m "Не делала она ничего странного последнее время?"
            # сделать разветвление
            $ har_body = "f/hr_govor.png"
            harr "Ну..."
            harr "Вообще-то она сильно изменилась в последнее время..."
            $ har_body = "f/hr_def.png"
            g9 "Да? Что с ней не так?"
            $ har_body = "f/hr_govor.png"
            harr "Ну... обычно она держалась нас с Роном...{w} теперь она постоянно в окружении парней"
            $ har_body = "f/hr_def.png"
            g9 "Она стала популярной?"
            $ har_body = "f/hr_govor.png"
            harr "Эм...{w} в некотором смысле"
            $ har_body = "f/hr_def.png"
            m "Не стесняйся, Гарри, говори"
            $ har_body = "f/hr_def.png"
            harr "Ну... начали ходить слухи, что она готова заниматься сексом с кем угодно"
            $ har_body = "f/hr_def.png"
            m "С кем угодно?"
            $ har_body = "f/hr_govor.png"
            harr "Ну...{w} вообще говорят, что она делает это с каждым, кто наберет 10 очков Гриффиндору"
            $ har_body = "f/hr_def.png"
            g9 "..."
            m "Ты не проверял"
            $ har_body = "f/hr_udivl.png"
            harr "Эм... что?"
            $ har_body = "f/hr_def.png"
            harr "Нет, конечно же нет"
            $ har_body = "f/hr_def.png"
            m "Почему?"
            $ har_body = "f/hr_def.png"
            harr "..."
            $ har_body = "f/hr_govor.png"
            harr "На самом деле... с тех пор у меня еще не получилось набрать 10 очков... профессор Снейп как с цепи сорвался, подговорил всех преподавателей давать очки только Слизерину"
            $ har_body = "f/hr_def.png"
            m "Хм..."
            menu:
                "Ясно, понятно":
                    jump harry_chat

                "По чистой случайности я могу дать тебе 10 очков":
                    $ har_body = "f/hr_udivl.png"
                    harr "..."
                    m "Мы оба знаем, что Гермиона не такая, и наша с тобой задача развеять эти грязные слухи"
                    $ har_body = "f/hr_smile.png"
                    harr "Да, профессор!"
                    m "10 очков Гриффиндору"
                    m "Теперь иди к ней и сделай вид, что хочешь награду за проделанную работу"
                    harr "..."
                    $ har_body = "f/hr_govor.png"
                    harr "Да, профессор"
                    hide screen bld1
                    hide screen harry_main
                    with Dissolve(.3)
                    $ walk_xpos=400 #Animation of walking chibi. (From)
                    $ walk_xpos2=610 #Coordinates of it's movement. (To)
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen harry_walk2
                    pause 2
                    $ harry_chibi_xpos = 610 #Near the desk.
                    hide screen harry_walk2
                    show screen harry_ch2 #Hermione stands still.
                    with Dissolve(.3)
                    m "*кретин*"
                    $ herm_vopr = 1
                    $ harry_chated = True
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    hide screen harry_ch2 #Hermione stands still.
                    if daytime:

                        jump night_main_menu
                    else:

                        jump day_main_menu



        "Спросить про Дафну" if (daphne_event >= 2):
            if daph_vopr == 0:
                m "Что ты можешь сказать про Дафну Грингас?"
                $ har_body = "f/hr_govor.png"
                harr "Про Дафну?"
                $ har_body = "f/hr_def.png"
                harr "Эм..."
                $ har_body = "f/hr_govor.png"
                harr "Она из Слизерина..."
                $ har_body = "f/hr_def.png"
                g4 "Оу... спасибо, Гарри, ты мне очень помог"
                $ har_body = "f/hr_govor.png"
                harr "Нет, ну я даже вижу ее не так часто... разве что на матчах по квидичу"
                $ har_body = "f/hr_def.png"
                m "*Квидичу? Что за идиотское название?*"
                m "А что на этих матчах?"
                $ har_body = "f/hr_govor.png"
                harr "Ну как, она ведь  капитан команды поддержки"
                $ har_body = "f/hr_def.png"
                g9 "Круппа поддержки? Ты имеешь ввиду су...{w} кхм... шлю...{w} девушек, танцующих в форме?"
                $ har_body = "f/hr_govor.png"
                harr "Эм... да, сэр"
                $ har_body = "f/hr_def.png"
                g4 "...{w}...{w}..."
                g4 "Почему Снейп не сказал, что здесь есть гребаная группа поддержки?!!"
                m "Есть что-то еще?"
                $ har_body = "f/hr_govor.png"
                harr "Ну... она достаточно популярна"
                $ har_body = "f/hr_def.png"
                g9 "*Еще бы сучка из группы поддержки была не популярна*"
                $ daph_vopr = 1
                jump harry_chat
            else:
                $ trig = renpy.random.randint(1, 4)
                if trig == 1:
                    $ har_body = "f/hr_govor.png"
                    harr "Странно, но она начала пропускать тренировки. Раньше такого не было."
                    $ har_body = "f/hr_def.png"
                    jump harry_chat
                if trig == 2:
                    $ har_body = "f/hr_govor.png"
                    harr "Недавно, когда я встретил ее, она показалась мне скрытней чем обычно"
                    $ har_body = "f/hr_def.png"
                    jump harry_chat
                if trig == 3:
                    $ har_body = "f/hr_govor.png"
                    harr "Я слышал слухи, что она перестала общаться с парнями, но я не уверен, что это правда"
                    $ har_body = "f/hr_def.png"
                    jump harry_chat
                if trig == 4:
                    $ har_body = "f/hr_govor.png"
                    harr "*Интересно с чего бы это?*"
                    $ har_body = "f/hr_def.png"
                    jump harry_chat


        "Можешь идти":
            $ harry_chated = 1
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            hide screen bld1
            hide screen harry_main
            hide screen blktone
            hide screen harry_ch
            hide screen ctc
            with d3
            if daytime:
                jump night_main_menu
            else:
                jump day_main_menu


label harry_first:
    $ renpy.play('sounds/knocking.mp3')
    "тук-тук-тук"
    m "..."
    g4 "Это не Снейп, он бы не стал стучать..."
    m "Гермиона?"
    menu:
        "Кто это?":
            jump harry_first1
        "...":
            jump harry_first1
        "Входите":
            jump harry_first2

label harry_first1:
    harr "Профессор Дамблдор, это я Гарри Поттер"
    m "..."
    menu:
        "Какой еще Гарри Поттер?":
            harr "... эм"
            harr "Профессор Дамблдор, это точно вы?"
            harr "..."
            jump harry_first2

        "Проходи, дитя":
            pass
        "Проходи, Гарри":
            pass
label harry_first2:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=330 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk
    pause 3
    $ harry_chibi_xpos = 330 #Near the desk.
    show screen harry_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    pause
    show screen harry_main
    with d3
    hide screen ctc
    # входит
    $ har_body = "f/hr_govor.png"
    harr "Профессор, в школе происходит что-то странное"
    $ har_body = "f/hr_def.png"
    m "..."
    $ har_body = "f/hr_govor.png"
    harr "Пока никто ничего не говорит, но все понимают, что-то неладное творится"
    $ har_body = "f/hr_def.png"
    g4 "*Что он хочет от меня*"
    $ har_body = "f/hr_govor.png"
    harr "Думаете это Лорд Волан-де-Морт?"
    $ har_body = "f/hr_def.png"
    g4 ".................."
    m "Я думаю...{w} не стоит торопиться с выводами..."
    $ har_body = "f/hr_zlo.png"
    harr "Это точно он... только пока не понятно, что он задумал..."
    $ har_body = "f/hr_def.png"
    m "Ну...{w} ты можешь подумать об этом на досуге"
    g4 "он уйдет отсюда или нет?! "
    $ har_body = "f/hr_govor.png"
    harr "Мне сказали, что на Чжоу напали этой ночью, я не могу допустить, чтобы с ней что-то случилось"
    $ har_body = "f/hr_def.png"
    m "Очень интересно..."
    m "............{w} эм"
    m "молодец{w}, продолжай наблюдение"
    $ har_body = "f/hr_smile.png"
    harr "да, профессор"
    hide screen harry_ch
    hide screen harry_main
    hide screen ctc
    hide screen bld1
    with d4
    g4 "*Что тут был за директор, если сюда врываются всякие пиздюки и докладывают мне о своих пассиях*"
    m "Может быть получится сделать из этого что-то интересное?"
    $ harry_event = 1
    return

label harry_2:
    $ renpy.play('sounds/knocking.mp3')
    "Тук-тук-тук"
    g4 "Кого опять принесло?"
    harr "Профессор, это я, Гарри"
    g4 "Почему сюда приходят всякие очкарики, а не горячие выпускницы??"
    menu:
        "Я занят":
            "..."
            harr "Профессор, это очень важно"
            g4 "..."
            harr "Профессор, мне нужно с вами поговорить"
            m "Похоже мне от него не отвязаться"
            jump harry_22

        "Проходи, дитя":
            jump harry_22
        "Проходи, Гарри":
            jump harry_22
label harry_22:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=330 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk
    pause 3
    $ harry_chibi_xpos = 330 #Near the desk.
    show screen harry_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    pause
    show screen harry_main
    with d3
    hide screen ctc
    harr "Профессор, это опять случилось"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "... эхм...{w} что случилось?"
    $ har_body = "f/hr_zlo.png"
    harr "Это все преспешники Воландеморта, я это точно знаю"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "..."
    $ har_body = "f/hr_govor.png" #Sprite of Hermione's upper body.
    harr "Нужно срочно что-то делать, в Хогвартсе уже 2 недели происходит что-то непонятное"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "Что происходит?"
    $ har_body = "f/hr_def.png"
    harr "Эм... ну..."
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    g4 "Ты что пришел сюда просто лишний раз потратить мое время?"
    m "*на самом деле у меня его не так уж мало*"
    $ har_body = "f/hr_govor.png" #Sprite of Hermione's upper body.
    harr "Кто-то опять напал на Чжоу Чанг"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "Опять?"
    g9 "Ты это видел?"
    $ har_body = "f/hr_govor.png" #Sprite of Hermione's upper body.
    harr "Эм... нет{w}, если бы я застал это, то точно помог бы ей"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "Она сама тебе сказала?"
    $ har_body = "f/hr_govor.png"
    harr "ым...{w}...{w} нет, она не очень то разговаривает со мной"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    g4 "Тогда... почему ты решил, что на нее кто-то напал?"
    $ har_body = "f/hr_govor.png"
    harr "Ну... она сторонится всех последнее время, видно, что переживает из-за чего-то"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    g4 "*Что за херню он несет?*"
    m "Хотя, возможно я смогу это использовать"
    m "Да, Гарри, ты прав"
    harr "..."
    g9 "Это все происки Волан-пер-шморда"
    $ har_body = "f/hr_udivl.png"
    harr "Да?"
    g9 "Да...{w} мы просто обязаны помешать его планам"
    m "Ты готов помочь мне, Гарри?"
    $ har_body = "f/hr_zlo.png"
    harr "Да, профессор, мы должны это сделать!"
    $ har_body = "f/hr_zlo.png" #Sprite of Hermione's upper body.
    m "Тогда у меня к тебе задание"
    $ har_body = "f/hr_govor.png"
    harr "Что мне делать?"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "Не своди с нее глаз, а когда случится что-то непонятное, сразу говори мне"
    $ har_body = "f/hr_govor.png"
    harr "Да, профессор! Я вас не подведу"
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    m "Отлично"
    $ harry_event = 2


    hide screen bld1
    hide screen harry_main
    with Dissolve(.3)
    $ walk_xpos=340 #Animation of walking chibi. (From)
    $ walk_xpos2=600 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk2
    pause 2
    $ harry_chibi_xpos = 610 #Near the desk.
    hide screen harry_walk2
    show screen harry_ch2 #Hermione stands still.
    with Dissolve(.3)
    m "*Идиот*"

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen harry_ch2 #Hermione stands still.
    with d3
    "Теперь вы можете вызывать Гарри Поттера"
    with Dissolve(.3)
    jump day_start
    # откроется вариант Позвать Гарри Поттера


label harry_obrad:
    "тук-тук-тук"
    m "..."
    g4 "Кто опять?"
    m "Гермиона?"
    menu:
        "Кто это?":
            pass
        "...":
            pass
        "Зайдите":
            pass

    harr "Профессор, это я, Гарри Поттер"
    m "..."


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=330 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk
    pause 3
    $ harry_chibi_xpos = 330 #Near the desk.
    show screen harry_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    pause
    show screen harry_main
    with d3
    hide screen ctc
    $ har_body = "f/hr_govor.png"
    harr "Профессор, сегодня было совершено еще одно нападение на студентку"
    m "...."
    $ har_body = "f/hr_zlo.png"
    harr "Это опять проделки Воландеморта, профессор!"
    g4 "как же он заебал..."
    m "Может получится получить от этого выгоду?"
    g9 "Кхем, да, Гарри, этот Вор-мандер-форт совсем распоясался"
    $ har_body = "f/hr_zlo.png"
    harr "Я так и знал!"
    $ har_body = "f/hr_def.png"
    harr "Что мы будем делать, профессор?!!"
    m "Я работал над этим вопросом последние... кхм... 10 лет"

    m "Как я смог выяснить, на самом деле, он не из нашего мира!"
    $ har_body = "f/hr_govor.png"
    m "Да, точно......."
    harr "Что?"
    m "......"
    m "Да, Гарри, он не обычный человек, он пришел из другого мира"
    harr "......"
    m "Я сильно на тебя не рассчитываю, я буду искать способ вернуть его обратно в его мир все следующее время, но если ты тоже поищешь, это точно не помешает"
    harr "......"
    $ har_body = "f/hr_govor.png"
    harr "Да, профессор! я побежал!!!"
    hide screen harry_ch
    hide screen harry_main
    hide screen ctc
    hide screen bld1
    with d4
    $ renpy.play('sounds/door.mp3')
    pause 1.0
    m "Имбецил"
    return

label svinoril:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=330 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk
    pause 3
    $ harry_chibi_xpos = 330 #Near the desk.
    show screen harry_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_s_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    pause
    show screen harry_main
    with d3
    hide screen ctc
    $ har_body = "f/hr_s_govor.png"
    harr "Профессор"
    $ har_body = "f/hr_s_def.png"
    m "..."
    g4 "эм...{w} что с тобой?"


    play sound "sounds/win2.mp3"
    show screen gift
    $ the_gift = "03_hp/18_store/37.png" # BUTTERBEER.
    "> Гарри передает вам окровавленный мешок"
    hide screen gift

    m "что это?"
    $ har_body = "f/hr_s_govor.png"
    harr "Я принес яйца свинорыла, которые вы просили"
    $ har_body = "f/hr_s_def.png"
    m "..."

    g4 "пожалуйста скажи мне, что ты украл их из гнезда, а мешок уже был с кровью"
    $ har_body = "f/hr_s_udivl.png"
    harr "эм... ну..."
    #$ har_body = "f/hr_s_def.png"
    m "я понял"
    m "хорошо"
    $ har_body = "f/hr_s_smile.png"
    harr "Не могу дождаться, когда с их помощью мы прищучим Волан-Де-Морта!"
    m "да, гарри, это уже почти случилось, сейчас мне нужно время"
    $ har_body = "f/hr_s_smile.png"
    harr "да, профессор"
    $ phx_ingr3 = 1
    $ harry_chated = 1
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    hide screen bld1
    hide screen harry_main
    hide screen blktone
    hide screen harry_ch
    hide screen ctc
    with d3
    if daytime:
        jump night_main_menu
    else:
        jump day_main_menu

label harry_potion:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=330 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen harry_walk
    pause 3
    $ harry_chibi_xpos = 330 #Near the desk.
    show screen harry_ch #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_def.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    pause
    show screen harry_main
    with d3
    hide screen ctc
    $ har_body = "f/hr_govor.png"
    harr "Профессор, я принес, то, что вы просили"
    $ har_body = "f/hr_def.png"
    ">Гарри передает вам волос"
    m "...."
    m "это действительно волос с его бороды?"
    $ har_body = "f/hr_smile.png"
    harr "да"
    $ har_body = "f/hr_def.png"
    m "отлично, гарри"
    $ har_body = "f/hr_govor.png"
    harr "еще что-то?"
    $ har_body = "f/hr_def.png"
    $ quest_hagrid = 5
    jump harry_chat

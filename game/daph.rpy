
# Болтать
# Купить сексуальные услуги
# Подарить подарок
#


label summon_daphne:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ menu_x = 0.2
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_02 #Hermione stands still.
    show screen bld1
    with d3
    if dap_level < 4:
        $ h_body = "dap/d_wha.png" #Sprite of Hermione's upper body.
    if dap_level >= 4:
        $ h_body = "dap/d_smile1.png" #Sprite of Hermione's upper body.
    if daphne_event == 9:
        $ h_body = "dap/d_vizsod5.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    with d3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    dap1 "Вы звали меня профессор?"
    if daphne_event == 9:
        m "...."
        m "Почему ты такая грустная, что-то случилось?"
        $ h_body = "dap/d_plach.png" #Sprite of Hermione's upper body.
        dap "я?"
        $ h_body = "dap/d_wha.png" #Sprite of Hermione's upper body.
        $ h_body = "dap/d_vizsod5.png" #Sprite of Hermione's upper body.
        dap "....{w}......."
        $ h_body = "dap/d_vizsod3.png" #Sprite of Hermione's upper body.
        dap "я просто сделаю все, что вы скажете..."
        g9 "хорошая девочка"
        $ daphne_event = 10
label daphne_chat:
    $ h_body = "dap/d_wha.png"
    menu:

        "Задание: \"Все для победы!\"" if (dap_level >= 11) and (daphne_event == 12):
            m "Мисс Гринграсс"
            $ h_body = "dap/d_smile1.png"
            dap "Да, профессор?"
            jump last_kram


        "-Болтать-":

            $ trig = renpy.random.randint(1, 6)
            if trig == 1:
                if devil >= 8:

                    $ h_body = "dap/d_ispug.png"
                    dap "Последнее время лучше не ходить поодиночке... говорят, что могут напасть. Куда смотрит администрация?"
                    pause 1.0
                    jump daphne_chat
                if devil < 8:
                    $ h_body = "dap/d_evilsmeh.png"
                    dap "Эта выскочка Грейнджер пытается водиночку обогнать Слизерен по очкам, ха!"
                    $ h_body = "dap/d_plach.png"
                    dap "Странно, но я не замечаю, когда она получает столько очков..."
                    pause 1.0
                    jump daphne_chat
            elif trig == 2:
                $ h_body = "dap/d_ispug.png"
                dap "Этот новый врач такой придурок, мне кажется он не той ориентации"
                pause 1.0
                jump daphne_chat
            elif trig == 3:
                $ h_body = "dap/d_zlo.png"
                dap "Этот замок полон извращенцев, половину матчей по квидиччу зрители пялятся на девушек из группы поддержки, а не на игроков"

                if dap_level > 4:
                    $ h_body = "dap/d_evilsmeh.png"
                    dap "Не могу сказать, что мне это не нравится"
                    pause 1.0
                    jump daphne_chat
                pause 1.0
                jump daphne_chat
            elif trig == 4:
                $ h_body = "dap/d_zlo.png"
                dap "Если бы не эта Грейнджер, Слизерин бы выигрывал кубок с огромным открывом. Странно, но я не помню, чтобы ей настолько часто давали очки"
                pause 1.0
                jump daphne_chat
            elif trig == 5:
                if dap_level > 0:
                    $ h_body = "dap/d_smile1.png"

                    dap "Все так удивились, когда увидели, что я начала приносить очки факультета...{w} Ха! Видели бы вы их лица!"
                    pause 1.0
                    jump daphne_chat
                if dap_level == 0:
                    $ h_body = "dap/d_zlo.png"
                    dap "не могу понять, когда грифиндор умудряется получать очки, на лекциях им почти никогда их не начисляют..."
                    pause 1.0
                    jump daphne_chat
            elif trig == 6:
                $ h_body = "dap/d_plach.png"
                dap "Грейнджер все еще на первом месте... но у меня пока достаточно времени..."
                pause 1.0
                jump daphne_chat




        "-Публичные задания-" if (daytime == True) and (daphne_event >= 6) and (dap_publ == 1):
            if daphne_publ_level == 0:
                jump daphne_public_first

            else:
                jump daph_publ

        "-Индивидуальные задания-" if daphne_event >= 6:
            if daphne_moral > 10:
                $ h_body = "dap/d_zlo.png"
                dap "Пфф! Нет уж!"
                $ h_body = "dap/d_wha.png"
                dap "Похоже дафна еще злится на вас, может быть попробовать позже?"
                jump daphne_chat
            else:
                menu dap_menu:


                    

                    "-Покажи мне грудь-":


                        if dap_level == 0:
                            $ h_body = "dap/d_ispug.png"
                            dap "..."
                            $ h_body = "dap/d_left.png"
                            dap "*до чего я докатилась*"

                            dap "..."
                            m "Чего же вы ждете, мисс Гринграсс?"
                            $ h_body = "dap/d_wha.png"
                            dap "Я не думала...{w} что профессор... в вашем возрасте будет интересоваться... таким"
                            g9 "*еще как будет*"
                            $ h_body = "dap/d_wha2.png"
                            dap "Эм... что?"
                            m "Вы что, подумали, что это лишь для плотского удовлетворения?"
                            $ h_body = "dap/d_plach.png"
                            dap "ну...{w} да."
                            $ h_body = "dap/d_wha2.png"
                            m "Вы еще очень молодая девушка, мисс Григрасс и вам многому нужно научиться"
                            m "У меня сугубо научный интерес"
                            $ h_body = "dap/d_wha.png"
                            dap "Да?"
                            $ h_body = "dap/d_left.png"
                            dap "Раз так..."

                            hide screen daphne_02
                            show screen daphne_tits
                            with d3

                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            with d3

                            pause 0.3
                            $ h_body = "dap/d_tits2.png"
                            show screen daphne_main

                            dap "..."
                            m "..."
                            m "*да уж, до 1го места ей далеко*"
                            g9 "*Но ей об этом лучше не знать*"
                            $ h_body = "dap/d_tits.png"
                            dap "*стою здесь, показываю грудь директору*"
                            $ h_body = "dap/d_tits3.png"
                            dap "*мама говорила, что девушка голубой крови должна быть готова на все ради цели*"
                            $ h_body = "dap/d_tits.png"
                            dap "*да*"
                            $ h_body = "dap/d_tits2.png"
                            dap "*только чистокровная волшебница из древнего рода может поступиться собственным чсв ради чести семьи*"
                            m "..."
                            $ h_body = "dap/d_tits.png"
                            m "Вы прекрасно справились, мисс Грингасс..."

                            m "10 очков Слизерину!"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen daphne_tits
                            with d3
                            pause 0.3
                            $ h_body = "dap/d_smile1.png"
                            show screen daphne_main
                            show screen daphne_02
                            dap "Спасибо, профессор"
                            ">Дафна выглядит довольной"

                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            with d3
                            $ walk_xpos=360 #Animation of walking chibi. (From desk)
                            $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                            $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                            show screen daphne_walk1f
                            pause 3
                            hide screen daphne_walk1f
                            $ daphne_chibi_xpos = 610
                            show screen daphne_02f
                            dap_wha "..."
                            dap_wha "Я...{w} докажу мамочке, что я достойна своей фамилии"
                            dap_smile2 "и она снова меня полюбит"
                            hide screen daphne_02f
                            with d3
                            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                            $ dap_level = 1
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu
                        elif dap_level > 0:
                            $ h_body = "dap/d_plach.png"
                            dap "..."
                            $ h_body = "dap/d_smile1.png"
                            dap "Да, профессор"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            with d3
                            pause 0.3
                            $ h_body = "dap/d_tits5.png"
                            show screen daphne_main3
                            ">Дафна уже не выглядит такой смущенной"
                            m "..."
                            m "У вас хорошая фигура, мисс Григрасс"
                            $ h_body = "dap/d_tits6.png"
                            dap "Эм...{w} да, я ведь капитан группы поддержки"
                            m "..."
                            pause 3.0
                            $ dap_pod = 1
                            $ h_body = "dap/d_tits4.png"
                            dap "*старый извращенец*"
                            dap "*летом я уеду домой на каникулы с первым местом в рейтинге студентов и мама не сможет мне ни в чем откзаать*"
                            dap "*я даже больше не буду рассказывать про то, какой ты извращенец...{w} неет, тебя посадят в азкабан за более отвратительные вещи*"
                            m "о чем вы задумались, мисс Гринграсс?"
                            $ h_body = "dap/d_tits.png"
                            dap "эмм..."
                            $ h_body = "dap/d_tits6.png"
                            dap "ни о чем, просто стараюсь, чтобы вам было лучше видно"
                            m "..."
                            $ h_body = "dap/d_tits4.png"
                            dap "*смотри пока можешь, старик*"
                            m "Достаточно, мисс Григрасс"
                            m "10 очков Слизерину!"
                            $ slytherin += 10
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            with d3
                            pause 0.3
                            $ h_body = "dap/d_smile1.png"
                            show screen daphne_main
                            dap "Да, сэр"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            with d3
                            $ menu_x = 0.5
                            if dap_level == 1:
                                $ dap_level = 2
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu

                    "-Потрогать задницу-":
                        if dap_level < 2:
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм...."
                            $ h_body = "dap/d_ispug.png"

                            dap "Что?!!"
                            $ h_body = "dap/d_krik.png"
                            dap "Как вы можете просить меня о таком..."
                            $ h_body = "dap/d_zlo.png"
                            dap "Наверное, мне все таки придется искать себе новое жилье"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            $ menu_x = 0.5
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu
                        elif dap_level == 2:
                            m "Сегодня мне опять понадобится ваша помощь"
                            $ h_body = "dap/d_wha.png"
                            dap "..."
                            dap "*что мне придется показывать на этот раз?*"
                            m "подойдите сюда, мисс Гринграсс"
                            dap "..."
                            dap "*что задумал этот старый извращенец*"
                            dap "эм..."
                            m "в чем дело, мисс гринграсс"
                            dap "..."
                            dap "*давай, раз начала, то обратного пути уже нет...{w} еще и получится, что я показывала сиськи директору просто так*"
                            dap "........."
                            m "мисс Гринграсс?"
                            dap "*выдох*{w} да, профессор"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "da/but1.png"
                            show screen g_c_u


                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3

                            dap "..."
                            m "посмотри там на столе где то затерялось перо"
                            dap "эм, что? перо? "
                            dap "я ничего не вижу"
                            g9 "..."
                            menu:
                                g9 "..."

                                "Схватить ее за задницу":
                                    jump daph_ass

                                "ничего не делать":
                                    m "........"
                                    dap "я ничего здесь не вижу"
                                    "неведомая сила велит вам держать руки при себе"
                                    g4 "что за дерьмо"
                                    g4 "я же джин, какая еще неведомая сила"
                                    "путем недюжих усилий вы вступаете в схватку с невидимым соперником и выходите победителем, теперь вас ничего не ограничивает"
                                    menu:
                                        "Схватить ее за задницу":
                                            jump daph_ass

                                        "Схватить ее за задницу":
                                            jump daph_ass

                                        "Схватить ее за задницу":
                                            jump daph_ass

                                    label daph_ass:
                                        show screen blkfade
                                        with d3

                                        ">Пока дафна роется на вашем столе, вы хватаете ее за задницу"
                                        hide screen blkfade
                                        with d3
                                        $ g_c_u_pic = "da/but2.png"
                                        dap_bol "!!!"
                                        g9 "........"
                                        $ g_c_u_pic = "daphne_but"
                                        dap_ispug "я должна была догадаться..."
                                        "*ЖМАК* *ЖМАК* *ЖМАК*"
                                        dap_visod "........................."
                                        show screen blkfade
                                        with d3
                                        ">вы чувствуете как дафна дрожит пока вы наслаждаетесь ее попкой"

                                        pause 0.5
                                        hide screen blkfade
                                        with d5
                                        dap_plach ".........{w} профессор"
                                        m "да?"
                                        $ dap_level = 3
                                        dap_plach "почему вы...{w} делаете это?"
                                        g4 "..."
                                        menu:
                                            "Мне нравится твоя попка":
                                                pass

                                            "Я люблю щупать молодых студенток":
                                                pass

                                            "это часть моего исследования":
                                                dap_plach "..."
                                                dap_visod "*теперь это так называется...*"

                                        dap_plach "..."
                                        dap_plach "но ведь вы же...{w} директор...{w} великий волшебник..."
                                        g9 "даже великим волшебникам нравятся классные задницы"
                                        dap_plach "......"
                                    label daph_ass2:
                                        dap "*неужели даже здесь все именно так*"
                                        menu:
                                            "Шлепнуть":
                                                $ renpy.play('sounds/slap.mp3')
                                                with vpunch
                                                "*ШЛЕП*"
                                                dap_bol "..."
                                                dap_gr "профессор..."
                                                $ renpy.play('sounds/slap.mp3')
                                                with vpunch
                                                pause 0.5
                                                $ renpy.play('sounds/slap.mp3')
                                                with vpunch
                                                pause 0.5
                                                $ renpy.play('sounds/slap.mp3')
                                                with vpunch
                                                "*ШЛЕП* *ШЛЕП* *ШЛЕП*"
                                                dap_bol "........"
                                                $ renpy.play('sounds/slap.mp3')
                                                with vpunch
                                                "*ШЛЕП*"
                                                dap_visod2 "не надо этого делать, пожалуйста...{w} кто-то может услышать..."
                                                m "хорошо"
                                                m "......"
                                                menu:
                                                    "Шлепнуть еще раз":
                                                        $ renpy.play('sounds/slap.mp3')
                                                        with vpunch
                                                        "*Шлеп*"
                                                        dap_ispug "профессор!!!"
                                                        m "извини, не удержался"
                                                        show screen blkfade
                                                        hide screen chair_02
                                                        hide screen g_c_u
                                                        hide screen desk
                                                        show screen genie
                                                        show screen daphne_02

                                                        with d3
                                                        ">вы отпускаете ее попку"
                                                        hide screen blkfade
                                                        $ h_body = "dap/d_plach.png"
                                                        show screen daphne_main
                                                        with d3
                                                        dap "......."
                                                        m "15 очков Слизерину"
                                                        dap "..."
                                                        dap "спасибо, профессор"



                                                        hide screen daphne_main
                                                        hide screen daphne_main2
                                                        hide screen daphne_main3
                                                        hide screen ctc
                                                        hide screen daphne_02
                                                        hide screen bld1
                                                        with d3
                                                        if daytime:
                                                            $ daphne_chated = 1
                                                            jump night_main_menu
                                                        else:
                                                            $ daphne_chated = 1
                                                            jump day_main_menu




                                                    "Прекратить":
                                                        "Вы продолжаете мять булочки дафны"
                                                        dap_gr "..."
                                                        g9 "......."
                                                        dap_plach "мне нужно на лекцию"
                                                        m "хорошо"
                                                        show screen blkfade
                                                        hide screen chair_02
                                                        hide screen g_c_u
                                                        hide screen desk
                                                        show screen genie
                                                        show screen daphne_02

                                                        with d3
                                                        ">вы отпускаете ее попку"
                                                        hide screen blkfade
                                                        $ h_body = "dap/d_plach.png"
                                                        show screen daphne_main
                                                        with d3
                                                        m "15 очков слизерину"
                                                        dap "..."
                                                        dap "спасибо, профессор"
                                                        hide screen daphne_main
                                                        hide screen daphne_main2
                                                        hide screen daphne_main3
                                                        hide screen ctc
                                                        hide screen daphne_02
                                                        hide screen bld1
                                                        with d3
                                                        if daytime:
                                                            $ daphne_chated = 1
                                                            jump night_main_menu
                                                        else:
                                                            $ daphne_chated = 1
                                                            jump day_main_menu

                                            "Продолжать мять булочки":
                                                "Вы продолжаете мять булочки дафны"
                                                dap_visod "..."
                                                g9 "......."
                                                dap_plach "мне нужно на лекцию"
                                                m "хорошо"
                                                show screen blkfade
                                                hide screen chair_02
                                                hide screen g_c_u
                                                hide screen desk
                                                show screen genie
                                                show screen daphne_02

                                                with d3
                                                ">вы отпускаете ее попку"
                                                hide screen blkfade
                                                $ h_body = "dap/d_plach.png"
                                                show screen daphne_main
                                                with d3
                                                m "15 очков слизерину"
                                                dap "..."
                                                dap "спасибо, профессор"
                                                hide screen daphne_main
                                                hide screen daphne_main2
                                                hide screen daphne_main3
                                                hide screen ctc
                                                hide screen daphne_02
                                                hide screen bld1
                                                with d3
                                                if daytime:
                                                    $ daphne_chated = 1
                                                    jump night_main_menu
                                                else:
                                                    $ daphne_chated = 1
                                                    jump day_main_menu


                        if dap_level > 2:
                            m "Мисс Гринграсс"
                            $ h_body = "dap/d_govor.png"
                            dap "да?"
                            $ h_body = "dap/d_wha.png"
                            m "мне потребуется помощь от вас"
                            $ h_body = "dap/d_ispug.png"
                            dap "..."
                            $ h_body = "dap/d_vizsod3.png"
                            dap "*я до сих пор не могу в это поверить*"
                            $ h_body = "dap/d_plach.png"
                            dap "*это точно не иллюзия?*"
                            m "Мисс Гринграсс"
                            $ h_body = "dap/d_govor.png"
                            dap "да, какая помощь?"
                            $ h_body = "dap/d_wha.png"
                            m "подойдите к моему столу и все поймете"
                            $ h_body = "dap/d_ispug.png"
                            dap "!!!"
                            m "?"
                            if dap_level == 3:
                                $ dap_level = 4
                            $ h_body = "dap/d_wot.png"
                            dap "Еще раз?!"
                            g4 "\"Еще раз?\"?{w} мы ведь только начали продвигать вас в рейтинге студентов"
                            $ h_body = "dap/d_plach.png"
                            dap "эм... я думала..."
                            m "что?"
                            $ h_body = "dap/d_vizsod4.png"
                            dap "..."
                            $ h_body = "dap/d_plach.png"
                            dap "Я не думала, что это так далеко зайдет"
                            g9 "*я же еще даже не начинал*"
                            m "хм..."
                            menu:
                                "то есть ты хочешь все бросить на пол пути?":
                                    $ h_body = "dap/d_plach.png"
                                    dap "..."
                                    $ h_body = "dap/d_left.png"
                                    dap "*я уже сделала достаточно, чтобы обратного пути не было*"
                                    m "так что?"
                                    $ h_body = "dap/d_vizsod4.png"
                                    dap "..."
                                    $ h_body = "dap/d_vizsod5.png"
                                    dap "............."
                                    pass

                                "20 очков":
                                    $ h_body = "dap/d_ispug.png"
                                    dap "20 очков?!"
                                    $ h_body = "dap/d_zlo.png"
                                    dap "Сэр, это слишком далеко зашло!!!"
                                    m "эм..."
                                    $ h_body = "dap/d_wha.png"
                                    m "25 очков"
                                    $ h_body = "dap/d_left.png"
                                    dap "......"
                                    pass

                            $ h_body = "dap/d_plach.png"
                            dap "да, сэр"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen daphne_02
                            $ walk_xpos=300 #Animation of walking chibi. (From)
                            $ walk_xpos2=200 #Coordinates of it's movement. (To)
                            $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                            show screen daphne_walk1
                            pause 1
                            hide screen daphne_walk1
                            with d3


                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            hide screen desk_02
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "da/but2.png"
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            g9 "......"
                            $ g_c_u_pic = "daphne_but"
                            ">вы начинаете жмакать булочки дафны"
                            dap_visod "......"
                            "*жмак* *жмак* *жмак*"
                            g9 "............."
                            "в этот раз ноги дафны не дрожат"
                            g9 "*скоро эта сучка войдет во вкус*"
                            dap_wha "профессор..."
                            m "да?"
                            dap_wha "почему именно я?"
                            m "..."
                            m "сосредоточся на 15 очках и на первом месте, которое ты получишь"
                            dap_visod "......"
                            dap_wha "просто... я не понимаю..."
                            m "ты слишком молода, чтобы понять, это все...{w} в научных целях"
                            dap_ispug "в научных?"
                            m "да... я работаю над сложным заклинанем{w} и для него мне нужна сочная задница"
                            dap_visod2 "..."
                            menu:
                                "Шлепнуть":
                                    play sound "sounds/slap.mp3"
                                    with vpunch
                                    "*ШЛЕП*"
                                    dap_bol "...{w}"
                                    dap_visod2 "профессор..."
                                    m "???"
                                    dap_plach "это тоже в научных целях?"
                                    m "именно в них"
                                    dap_visod "..."
                                    play sound "sounds/slap.mp3"
                                    with vpunch
                                    pause 0.5
                                    play sound "sounds/slap.mp3"
                                    with vpunch
                                    pause 0.5
                                    play sound "sounds/slap.mp3"
                                    with vpunch
                                    pause 0.5
                                    "*Шлеп* *шлеп* *шлеп*"
                                    dap_visod2 "*если я сейчас уйду, то точно никак не смогу занять первое место в рейтинге*"
                                    dap_plach "*мамочка все равно меня любит...{w} правда ведь?*"
                                    play sound "sounds/slap.mp3"
                                    with vpunch
                                    "*ШЛЕП*"
                                    dap_visod2 "..."
                                    dap_visod2 "*главное, чтобы никто не узнал*"
                                    m "хватит на сегодня"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk
                                    show screen genie
                                    show screen daphne_02
                                    show screen daphne_main
                                    with d6
                                    dap "..."
                                    m "15 очков слизерину"
                                    $ h_body = "dap/d_smile2.png"
                                    dap "Спасибо, профессор"
                                    $ renpy.play('sounds/door.mp3')
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen daphne_02
                                    hide screen bld1
                                    with d3
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "залезть в трусики":
                                    ">Вы медленно запускаете свою руку в  ее трусики..."
                                    dap_bol "!!!"
                                    dap_sl "что вы делаете"
                                    g9 "продолжаю эксперимент"
                                    dap_visod2 "..........."
                                    dap_wha "*он что действительно это делает?*"
                                    dap_sl "*это больше похоже на плохой сон...{w} который не кончается*"
                                    menu:
                                        "Поласкать ее киску":
                                            ">Ваша рука проникает вниз, и вы трогаете ее маленькую щель..."
                                            dap_bol "!!!"
                                            g9 "......."
                                            dap_gr "я..."
                                            dap_sl "*если я сейчас уйду, то точно никак не смогу занять первое место в рейтинге*"
                                            dap_plach "*мамочка все равно меня любит...{w} правда ведь?*"
                                            dap_visod2 "......"
                                            m "хватит на сегодня"
                                            show screen blkfade
                                            with d6
                                            hide screen chair_02
                                            hide screen g_c_u
                                            hide screen desk
                                            show screen genie
                                            show screen daphne_02
                                            hide screen blkfade
                                            $ h_body = "dap/d_zlo.png"
                                            show screen daphne_main
                                            with d6
                                            dap "...."
                                            m "15 очков слизерину"
                                            $ h_body = "dap/d_zlo.png"
                                            dap "......"
                                            "Кажется дафна разозлилась на вас"
                                            $ renpy.play('sounds/door.mp3')
                                            hide screen daphne_main
                                            hide screen daphne_main2
                                            hide screen daphne_main3
                                            hide screen ctc
                                            hide screen daphne_02
                                            hide screen bld1
                                            with d3
                                            $ daphne_moral -= 3
                                            if daytime:
                                                $ daphne_chated = 1
                                                jump night_main_menu
                                            else:
                                                $ daphne_chated = 1
                                                jump day_main_menu


                                        "Поласкать пальцем ее попку":

                                            ">Вы дотрагиваетесь до её узенькой дырочки..."
                                            dap_bol "!!!"
                                            g9 "..........."
                                            dap_krik "Профессор, это уже слишком!"
                                            ">дафна вырывается из ваших рук"
                                            m "хватит на сегодня"
                                            show screen blkfade
                                            hide screen chair_02
                                            hide screen g_c_u
                                            hide screen desk
                                            with d3
                                            show screen genie
                                            show screen daphne_02
                                            show screen daphne_main
                                            hide screen blkfade
                                            with d3
                                            dap "пфф!"
                                            m "15 очков слизерину"
                                            $ h_body = "dap/d_zlo.png"
                                            dap "......"
                                            "Кажется дафна разозлилась на вас"
                                            $ renpy.play('sounds/door.mp3')
                                            hide screen daphne_main
                                            hide screen daphne_main2
                                            hide screen daphne_main3
                                            hide screen ctc
                                            hide screen daphne_02
                                            hide screen bld1
                                            with d3
                                            $ daphne_moral -= 3
                                            if daytime:
                                                $ daphne_chated = 1
                                                jump night_main_menu
                                            else:
                                                $ daphne_chated = 1
                                                jump day_main_menu


                                "Продолжать мять булочки":
                                    "*жмак* *жмак* *жмак*"
                                    dap_visod "*когда это уже закончится...*"
                                    dap_wha "*зачем я согласилась, ведь понимала к чему он клонит*"
                                    m "хватит на сегодня"

                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk
                                    show screen genie
                                    show screen daphne_02
                                    show screen daphne_main
                                    m "15 очков слизерину"
                                    $ h_body = "dap/d_smile2.png"
                                    dap "Спасибо, профессор"
                                    $ renpy.play('sounds/door.mp3')
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen daphne_02
                                    hide screen bld1
                                    with d3
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu







                    "-Подрочи мне-":
                        if dap_level < 4:
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм...."
                            $ h_body = "dap/d_ispug.png"

                            dap "Что?!!"
                            $ h_body = "dap/d_krik.png"
                            dap "Как вы можете просить меня о таком..."
                            $ h_body = "dap/d_zlo.png"
                            dap "Наверное, мне все таки придется искать себе новое жилье"
                            $ renpy.play('sounds/door.mp3')
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            $ dap_moral = 3
                            $ menu_x = 0.5
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu
                        elif dap_level == 4:
                            m "Мисс Гринграсс"
                            $ h_body = "dap/d_govor.png"
                            dap "Да?"
                            $ h_body = "dap/d_wha.png"
                            m "Вы ведь уже знаете о мужских..."
                            g9 "потребностях"
                            $ h_body = "dap/d_ispug.png"
                            dap "Потребностях?"
                            $ h_body = "dap/d_left.png"
                            dap "........"
                            $ h_body = "dap/d_plach.png"
                            dap "Что на этот раз?"
                            m "Мне срочно нужно сделать одно очень сложное зелье"
                            $ h_body = "dap/d_wha.png"
                            dap "эм...... зелье?"
                            m "для него мне нужен один ингридиент, который я смогу получить только с вашей помощью"
                            $ h_body = "dap/d_ispug.png"
                            dap "???"
                            $ h_body = "dap/d_left.png"
                            dap "эм..."
                            g9 "..."
                            $ h_body = "dap/d_vizsod4.png"
                            dap "ах..."
                            $ h_body = "dap/d_ispug.png"
                            dap "Я не уверена, что могу делать это директору, сэр..."
                            m "Вы бы помогли мне с исследованиями...{w} и очень помогли своему факультету, мисс Григрасс"
                            $ h_body = "dap/d_left.png"
                            dap "..."
                            $ h_body = "dap/d_right.png"
                            dap "*Чего в этом плохого, если никто не узнает?*"
                            $ h_body = "dap/d_wha.png"
                            dap "*главное ведь результат, верно?*"
                            $ h_body = "dap/d_krik.png"
                            dap "Да, профессор"

                            g9  "отлично"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            $ genie_chibi_xpos = 100 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "daph_handjob"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3


                            g9 "Ох, да сучка"
                            dap_visod2 "*сучка...*"
                            g9 "..."
                            show screen blkfade
                            with d3
                            ">дафна неумело теребит ваш член"
                            dap_visod "..."
                            dap_visod "......"
                            dap_wha "эм"
                            dap_ispug "долго мне еще так делать?"
                            hide screen blkfade
                            with d3
                            m "ты можешь ускорить это, если скажешь..."
                            g9 "\"я была плохой девочкой\""
                            dap_visod2 "..."
                            dap_oh "Я..."
                            dap_wha "............"
                            dap_smile4sl "я была плохой девочкой"
                            g4 "*Да, шлюха!*"
                            dap_smile4sl "накажите меня, профессор"
                            g9 "*ох да, сучка!*"
                            dap_smile4sl "Я хочу чтобы вы наказали по самые гланды"
                            g9 "*ооох даа*"
                            $ dap_level = 5
                            "Вы чувствуете, что сейчас кончите"
                            menu:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"
                                    show screen blkfade
                                    g9 "даааа"
                                    dap_sperm "..."
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    hide screen blkfade
                                    with fade
                                    m "20 очков Слизерину"
                                    dap "..."
                                    $ h_body = "dap/d_sprm.png"


                                    dap "Спасибо, профессор"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    with d3
                                    $ walk_xpos=360 #Animation of walking chibi. (From desk)
                                    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                    show screen daphne_walk1f
                                    pause 3
                                    hide screen daphne_walk1f
                                    show screen daphne_02f

                                    $ daphne_chibi_xpos = 610
                                    dap_visod2 "*Я ведь не шлюха, правда? Я просто... {w}делаю то, что должна...*"

                                    hide screen daphne_02f
                                    with d3
                                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Не предупреждать":
                                    g4 "ох"
                                    g9 "даааа"
                                    show screen blkfade
                                    with d6
                                    pause 0.5
                                    dap_sperm "......"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"

                                    with fade
                                    hide screen blkfade
                                    show screen daphne_main
                                    with d6

                                    dap "Вы могли бы предупредить меня, профессор"
                                    m "ну... не получилось"
                                    dap "..."
                                    m "20 очков Слизерину"
                                    dap "Спасибо, профессор"

                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    with d3
                                    $ walk_xpos=360 #Animation of walking chibi. (From desk)
                                    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                    show screen daphne_walk1f
                                    pause 3
                                    hide screen daphne_walk1f
                                    show screen daphne_02f
                                    $ daphne_chibi_xpos = 610
                                    dap_visod2 "*лишь бы меня никто не заметил в таком виде"

                                    hide screen daphne_02f
                                    with d3
                                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu

                        else:
                            $ h_body = "dap/d_plach.png"
                            dap "Опять?"
                            $ h_body = "dap/d_vizsod5.png"
                            dap "..."
                            $ h_body = "dap/d_smile1.png"
                            dap "Да, профессор"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            $ genie_chibi_xpos = 100 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "daph_handjob"
                            show screen chair_02
                            show screen g_c_u


                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen desk
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            ">дафна принимается дрочить ваш член"
                            dap_visod "..."

                            m "В этот раз у тебя получается лучше"
                            dap_wha "эм... да, сэр"
                            dap_smile "мне нравится дрочить вам, сэр"
                            m "да?"
                            dap_smile2 "мне нравятся члены"
                            dap_smile3 "особенно, когда они во мне"
                            g4 "*ах ты сука*"
                            dap_smile4 "Вчера наша команда была в плохом настроении из-за проигрыша и мне пришлось подбодрить их, сэр"
                            dap_smile5 "Я сделала это, как вы учили меня"
                            g9 "*ах ты шлюха*"
                            if dap_level == 5:
                                $ dap_level = 6
                            dap_smile3 "Мне удавалось подбадривать одновременно трех игроков"
                            g9 "*эта сучка быстро учится*"
                            ">Вы чувствуете, что сейчас кончите"
                            menu:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"

                                    show screen blkfade
                                    with d6
                                    g9 "даааа"
                                    dap_sperm "..."
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade

                                    hide screen blkfade
                                    with d6
                                    pause 1.0
                                    m "20 очков Слизерину"
                                    "..."
                                    $ h_body = "dap/d_sprm.png"


                                    dap "Спасибо, профессор"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    with d3
                                    $ walk_xpos=360 #Animation of walking chibi. (From desk)
                                    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                    show screen daphne_walk1f
                                    pause 3
                                    hide screen daphne_walk1f
                                    show screen daphne_02f

                                    $ daphne_chibi_xpos = 610
                                    dap_plach "*Я ведь не шлюха, правда?"
                                    dap_plach "Я просто... {w}делаю то, что должна...*"
                                    $ dap_level += 1
                                    hide screen daphne_02f
                                    with d3
                                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Не предупреждать":
                                    g4 "ох"
                                    show screen blkfade
                                    with d3
                                    g9 "даааа"
                                    dap_sperm "......"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen blkfade
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade


                                    dap "Вы могли бы предупредить меня, профессор"
                                    m "ну... не получилось"
                                    dap "..."
                                    m "20 очков Слизерину"
                                    dap "Спасибо, профессор"

                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    with d3
                                    $ walk_xpos=360 #Animation of walking chibi. (From desk)
                                    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                    show screen daphne_walk1f
                                    pause 3
                                    hide screen daphne_walk1f
                                    show screen daphne_02f
                                    $ daphne_chibi_xpos = 610
                                    dap_visod2 "*лишь бы меня никто не заметил в таком виде"
                                    $ dap_level += 1
                                    hide screen daphne_02f
                                    with d3
                                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu





                    "-Минет-":
                        if dap_level < 6:
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм...."
                            $ h_body = "dap/d_wtf.png"

                            dap "Что?!!"
                            $ h_body = "dap/d_krik.png"
                            dap "Как вы можете просить меня о таком..."
                            $ h_body = "dap/d_vniz.png"
                            dap "Наверное, мне все таки придется искать себе новое жилье"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            $ menu_x = 0.5
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu
                        elif dap_level == 6:
                            m "Кхем - Кхем..."
                            m "Мисс Григасс"
                            $ h_body = "dap/d_govor.png"
                            dap "Да?"
                            $ h_body = "dap/d_plach.png"
                            dap "*что будет в этот раз?*"
                            $ h_body = "dap/d_wha.png"
                            m "Мне снова понадобится ваша помощь в одном исследовании"
                            $ h_body = "dap/d_plach.png"
                            dap "..."
                            $ h_body = "dap/d_smile1.png"
                            dap "Да, сэр"
                            m "нет"
                            m "На этот раз вам придется делать это ртом"
                            $ h_body = "dap/d_ispug.png"
                            dap "Что?"
                            $ h_body = "dap/d_zlo.png"
                            dap "Это уже слишком, профессор"
                            g4 ".........."
                            m "Разве вы не хотите быть на первом месте?"
                            $ h_body = "dap/d_wha2.png"
                            dap "Это не стоит того"
                            $ h_body = "dap/d_vizsod4.png"
                            dap "*неужели я до такого дошла*"
                            $ h_body = "dap/d_wha2.png"
                            m "Вы бы не хотели чтобы ваши родители вами гордились мисс Григрасс?"
                            $ h_body = "dap/d_vizsod3.png"
                            dap "..."
                            $ h_body = "dap/d_zlo.png"
                            dap "Они бы не гордились мной, если бы узнали, что мне пришлось для этого сделать"
                            $ h_body = "dap/d_vizsod.png"
                            dap "*Хотя, на самом деле, иногда мне кажется, что маме без разницы*"
                            $ h_body = "dap/d_plach.png"
                            m "......"
                            pause 2.0
                            $ h_body = "dap/d_left.png"
                            dap "Хорошо, я сделаю это"
                            g9 "вот это другой разговор"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "blowjob_daph"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            ">Дафна начинает неумело сосать ваш член"
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            g4 "*Я думал популярные сучки умеют делать минет*"
                            dap "*Хлюп!* *Хлюп!* *Хлюп!*"
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            dap_wha "Вам нравится, сэр?"
                            g4 "Сосредоточся, девочка"
                            dap_wha "да, сэр"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.5
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            g4 "........"
                            m "Тебе не приходилось делать этого раньше?"
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            dap_wha "Эм... нет сэр"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.5
                            dap "*Чаквк* *ЧАВК* *ЧАВК*"
                            m "Мне казалось, ты популярная девочка"

                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            dap_visod2 "ну да, только..."


                            dap_wha "родители не хотят, чтобы я сближалась непонятно с кем"
                            dap_smile "наш род слишком древний, чтобы портить его грязнокровками"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.5
                            "*ЧАВК* *ЧАВК* *ЧАВК*"

                            m "а разве среди студентов нет родовитых парней?"
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_wha "есть, сэр, но родители всегда запрещали мне общаться с кем попало и обещали подобрать мне жениха"
                            m "мы отвлеклись"
                            dap_wha "да, сэр"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_yaz "*Чавк!* *Чавк!* *Чавк!*"
                            ">Вы чувствуете, что сейчас кончите"
                            menu:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_plach "Сейчас?"
                                    show screen blkfade
                                    with d6
                                    g9 "Ох дааа"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_spr1.png"
                                    show screen daphne_main
                                    hide screen blkfade
                                    with fade
                                    with d6
                                    "..."
                                    m "ты проглотила?"
                                    $ h_body = "dap/d_spr2.png"
                                    pause 1.0
                                    $ h_body = "dap/d_vizsod4.png"
                                    pause 0.5
                                    $ h_body = "dap/d_smile1.png"
                                    dap "ну... это лучше, чем потом отмывать одежду, сэр"
                                    m "35 очков Слизерину"
                                    $ h_body = "dap/d_smile2.png"
                                    dap "Спасибо, сэр"
                                    if dap_level == 6:
                                        $ dap_level = 7
                                    hide screen g_c_u
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d6
                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Ничего не говорить":
                                    g4 "..........."
                                    show screen blkfade
                                    with d6
                                    g9 "Ох дааа"
                                    dap_ispug "Что? нет!"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    hide screen blkfade
                                    with fade
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "35 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    if dap_level == 6:
                                        $ dap_level = 7
                                    hide screen g_c_u
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d6
                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu

                        elif dap_level > 6:
                            m "Вы помните, что мы делали в прошлый раз?"
                            $ h_body = "dap/d_vizsod4.png"
                            dap "Эм... мы много чего{w} делали..."
                            m "Мне не хватило ингридиентов для зелья, нужно добыть еще"
                            $ h_body = "dap/d_plach.png"
                            dap "Ах это..."
                            $ h_body = "dap/d_smile1.png"
                            dap "Да, профессор"
                            show screen blkfade
                            with d3
                            ">Дафна принимается сосать ваш член"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "blowjob_daph"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            ">Дафна принимается сосать ваш член"
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            m "В этот раз у тебя получается лучше"
                            pause 2.0
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_smile "О да, я тренировалась, сэр"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            pause 2.0
                            m "Так ты все таки смогла найти...{w} чистокровных студентов?"
                            pause 2.0
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_smile2 "Ой, что вы, я же не на настоящих членах"
                            dap_smile "На самом деле родители запретили мне близко общаться с кем либо здесь..."
                            dap_wha "Приходится строить из себя стерву, чтобы не сближаться с людьми"
                            g4 "..."

                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            m "Выходит, что не так классно быть чистокровным волшебником..."
                            pause 2.0
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_smile2 "оу, это большая ответственность, сэр"
                            dap_smile "поэтому мне приходится делать все, чтобы не посрамить свою фамилию"

                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            pause 2.0
                            hide screen g_c_u
                            $ g_c_u_pic = "da/dro.png"
                            show screen g_c_u
                            with d3
                            pause 1.0
                            dap_plach "Я читала свою родословную, мои пра-пра-пра бабушки делали и более ужасные вещи, чтобы сохранить честь семьи"
                            m "Могу себе представить..."
                            dap_plach "моей пра-пра бабушке, Джозелин Гринграсс пришлось..."

                            m "ты отвлеклась"
                            dap_visod2 "да, сэр"
                            hide screen g_c_u
                            $ g_c_u_pic = "blowjob_daph"
                            show screen g_c_u
                            with d3

                            pause 2.0
                            dap "*Чавк!* *Чавк!* *Чавк!*"
                            g4 "..........."
                            # можно сделать момент для публичных заданий, с которого вывести на задание для компромата
                            ">вы чувствуете что сейчас кончите"
                            menu:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_wha "Сейчас?"
                                    show screen blkfade
                                    with d6
                                    g9 "Ох дааа"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    hide screen blkfade
                                    with d6
                                    $ h_body = "dap/d_spr1.png"
                                    show screen daphne_main

                                    dap "..."
                                    m "ты проглотила?"
                                    pause 1.0
                                    $ h_body = "dap/d_spr2.png"
                                    pause 1.5
                                    $ h_body = "dap/d_vizsod4.png"
                                    pause 1.0
                                    $ h_body = "dap/d_smile1.png"
                                    dap "ну...{w} это лучше, чем потом отмывать одежду, сэр"
                                    m "35 очков Слизерину"
                                    $ h_body = "dap/d_smile2.png"
                                    dap "Спасибо, сэр"
                                    if dap_level == 7:
                                        $ dap_level = 8
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Ничего не говорить":
                                    g4 "...."
                                    show screen blkfade
                                    with d6
                                    g9 "Ох дааа"
                                    dap_ispug "Что? нет!"
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    hide screen blkfade
                                    with d6
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main

                                    dap "..."
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "35 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    if dap_level == 7:
                                        $ dap_level = 8
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    $ menu_x = 0.5
                                    with d3
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu

                    "-Секс-":
                        if dap_level < 8:
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм...."
                            $ h_body = "dap/d_wtf.png"

                            dap "Что?!!"
                            $ h_body = "dap/d_krik.png"
                            dap "Как вы можете просить меня о таком..."
                            $ h_body = "dap/d_zlo.png"
                            dap "Наверное, мне все таки придется искать себе новое жилье"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            $ menu_x = 0.5
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu

                        elif dap_level == 8:
                            m "Мисс Григрасс"
                            $ h_body = "dap_govor"
                            dap "Да"
                            g9 "Сегодня мы станем немного ближе"
                            $ h_body = "dap/d_plach.png"
                            dap "эм..."
                            m "я узнаю вас буквально изнутри"
                            $ h_body = "dap/d_smile1.png"
                            dap "оу, мы уже проходили это заклинание, обмен разума, конечно"
                            g4 "ч...ч-че?"
                            $ h_body = "dap/d_smile3.png"
                            dap "ха-ха-ха"
                            $ h_body = "dap/d_smile1.png"
                            dap "Я знала, что рано или поздно вам понадобятся более глубокие исследования"
                            m "*она уже сама шутит над этим, маленькая шлюшка*"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "da/22_cum_01.png"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            ">Оперевшись на стол, Дафна раздвигает перед вами свои ноги"
                            g9 "..."
                            dap_ispug "ай"
                            m "просто расслабься "
                            "..."
                            dap_krik "аааааааааааааааааайййййййййййййй!!!!!"
                            "Вы начинаете трахать дафну"
                            "..."
                            "......."
                            "..............................."
                            g4 "Ты ничего не чувствуешь?"
                            dap_wha "вы... мне очень больно, сэр"
                            m "но ты молчишь?"
                            dap_wha "да...{w} я не должна показывать боль, сэр"
                            dap_wha "даже когда вы...{w} трахаете меня своим огромным членом и мне кажется что вы сейчас порвете меня"
                            dap_wha "Я должна вытерпеть это"
                            g4 "Что за дерьмо у нее в голове"



                            "вы чувствуете что сейчас кончите"
                            menu:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"
                                    g9 "Ох дааа"
                                    "..."
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    "55 очков Слизерину"
                                    "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 8:
                                        $ dap_level = 9
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Ничего не говорить":
                                    "Ох дааа"
                                    "Что? нет!"
                                    "..."
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "55 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 8:
                                        $ dap_level = 9
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu

                        else:
                            m "Мисс Григрасс"
                            $ h_body = "dap/dap_govor.png"
                            dap "Да"
                            $ h_body = "dap/d_wha.png"
                            g9 "сегодня у вас будет возможность продвинуть себя сразу на 55 очков"
                            $ h_body = "dap/d_plach.png"
                            dap "эм... "
                            $ h_body = "dap/d_smile2.png"
                            dap "снова нужно будет рассказывать про зябликов?"
                            m "Ну...{w} почти"
                            $ h_body = "dap/d_smile4.png"
                            dap "Так и знала"

                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "dasex_ani"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            ">Вы начинаете трахать дафну"
                            dap_oh "..."
                            g9 "тебе нравится это, маленькая шлюшка?"
                            dap_smile3 "профессор..."
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "шлеп!"
                            dap_smile4 "ах"
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            pause 0.5
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            pause 0.5
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "шлеп - шлеп - шлеп"
                            ">В этот раз дафна старается подмахивать"
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "Шлеп!"
                            dap_smile3 "профессор..."
                            g9 "ты была плохой девочкой"
                            dap_smile4 "я..."
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "Шлеп!"
                            g9 "Вот что бывает с маленькими девочками, которые не хотят учиться"
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "шлеп!"

                            dap_smile5 "...."
                            menu:
                                "Если бы твоя мать увидела тебя сейчас..":
                                    dap_wha "эмм"
                                    dap_smile "главное чтобы этого не увидели другие..."
                                    g9 "*еще как увидят, сучка, ты только погоди немного*"
                                    dap_gr "мама бы поняла это... ах..."
                                    dap_wha "ведь я делаю это для нее"
                                    g9 "да, ты маленькая шлюшка"
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    dap_wha "она никогда не говорила мне, но я всегда догадывалась как она смогла устроить свою карьеру..."
                                    g9 "выходит, ты потомственная шлюшка"
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    "ШЛЕП"

                                    dap_smile4sl "......"
                                    m "тебе нравится, когда тебя шлепают, сучка?"
                                    dap_smile5 "ах...{w} да, сэр"
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 1.0
                                    dap_smile3 "я хочу чтобы вы наказали меня"
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 0.5
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 0.5
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    "Шлеп - Шлеп - Шлеп"
                                    "ноги дафны затряслись"
                                    g4 "ты что, кончаешь, шлюха?"

                                    dap_smile4sl "простите... ах,  но я не могу больше..."
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 0.5
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 0.5
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    ">Шлеп - Шлеп - Шлеп"
                                    dap_smile4sl "..."
                                    ">Вы чувствуете, что тоже сейчас кончите"
                                    jump kon

                                "Сколько у тебя было парней до этого?":
                                    dap_smile4 "ах..."
                                    dap_smile5 "......."
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    pause 1.0
                                    g4 "отвечай, шлюшка"
                                    dap_smile5 "ахх..... вы первый, сэр..."
                                    g4 "..."
                                    m "кого ты пытаешься обмануть, у тебя же не было крови"
                                    dap_oh "ах, сэр... ох..."
                                    dap_oh "я с 9 лет занимаюсь верховой ездой... ах... это случилось еще в детстве... ох"
                                    g9 "ах да, я же забыл, что самая настоящая высокородная шлюха!"
                                    dap_smile5 "...."
                                    $ renpy.play('sounds/slap.mp3')
                                    with vpunch
                                    "шлеп!"
                                    dap_oh "ах"
                                    m "то есть у тебя вообще не было парней?"
                                    dap_smile5 "ох.... нет, сэр"
                                    dap_smile "я же говорила... ах... мне запрещают... ох"
                                    m "но здесь ведь тебя никто не видит, родители не узнают"
                                    dap_smile "да... но я должна... ах... быть достойной своей фамилии... ах"
                                    g9 "*ты станешь достойной, сучка, я тебе обещаю*"
                                    "Вы чувствуете, что сейчас кончите"
                                    jump kon


                            menu kon:
                                "Предупредить":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"
                                    g9 "Ох дааа"
                                    pause 1.0
                                    hide screen g_c_u
                                    $ g_c_u_pic = "dasex_cum_out_ani"
                                    show screen g_c_u
                                    pause 3.0

                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    m "55 очков Слизерину"
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 9:
                                        $ dap_level = 10
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Ничего не говорить":
                                    g4 "Ох дааа"
                                    dap_ispug "Что? нет!"
                                    pause 1.0
                                    hide screen g_c_u
                                    $ g_c_u_pic = "dasex_cum_out_ani"
                                    show screen g_c_u
                                    pause 3.0
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "55 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 9:
                                        $ dap_level = 10
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu




                    "-Время для анала-":
                        if dap_level < 10:
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм...."
                            $ h_body = "dap/d_ispug.png"

                            dap "Что?!!"
                            $ h_body = "dap/d_krik.png"
                            dap "Как вы можете просить меня о таком..."
                            $ h_body = "dap/d_zlo.png"
                            dap "Наверное, мне все таки придется искать себе новое жилье"
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3
                            hide screen ctc
                            hide screen bld1
                            hide screen daphne_02
                            $ menu_x = 0.5
                            if daytime:
                                $ daphne_chated = 1
                                jump night_main_menu
                            else:
                                $ daphne_chated = 1
                                jump day_main_menu
                        elif dap_level == 10:
                            m "Мисс Гринграсс"
                            $ h_body = "dap/d_govor.png"
                            dap "Да?"
                            $ h_body = "dap/d_wha.png"
                            m "Сегодня мне будет нужно, в научных целях, конечно же, про{size=+6}анал{/size}изировать одно явление"
                            $ h_body = "dap/d_plach.png"
                            dap "Эмм..."
                            $ h_body = "dap/d_wha.png"
                            dap "Что?"
                            g9 "Сегодня вы будете моим главным {size=+6}анал{/size}итиком"
                            $ h_body = "dap/d_plach.png"
                            pause 2.0
                            $ h_body = "dap/d_ispug.png"
                            pause 1.0
                            $ h_body = "dap/d_vizsod3.png"
                            dap "ах, это..."
                            $ h_body = "dap/d_smile1.png"
                            dap "..."
                            m"*вот так просто согласилась на анал?*"
                            g9 "*она определенно делает успехи*"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "da/22_cum_03.png"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3
                            m "для начала нужно будет слегка..."
                            $ renpy.play('sounds/spit.mp3')
                            # плевок
                            pause 1.0
                            dap_ispug "..."
                            play sound "sounds/gltch.mp3"
                            pause 1.0
                            dap_bol "{size=+3}!!!{/size}"
                            dap_oh "АЙ!!!"
                            m "не ерзай, так будет еще больнее"
                            dap_sl "мне больно, сэр"
                            $ g_c_u_pic = "dasex_ani"
                            dap_bol "!!!"
                            dap_oh "хватит... хватит!"
                            g4 "кто-то тут говорил, что должен стерпеть все с достоинством"
                            dap_sl "........."
                            ">дафна продолжает хныкать, пока вы разрабатываете ее анус"
                            show screen blkfade
                            with d6
                            pause 0.5
                            hide screen blkfade
                            with d6
                            dap_sl "......"
                            dap_visod2 "мне...{w} мне больно, сэр"
                            g9 "...."
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "*шлеп*"
                            dap_bol "!!!"
                            dap_visod2 "......"
                            with fade
                            ">вы чувствуете что сейчас кончите"
                            menu kon2:
                                "Кончить в нее":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"
                                    g9 "Ох дааа"
                                    hide screen g_c_u
                                    $ g_c_u_pic = "dasex_cum_out_ani"
                                    show screen g_c_u
                                    dap_smile4 "ах..."
                                    dap_smile4sl "я чувствую это"



                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    m "70 очков Слизерину"
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 10:
                                        $ dap_level = 11
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Кончить на нее":
                                    "Ох дааа"
                                    "Что? нет!"
                                    pause 1.0
                                    hide screen g_c_u
                                    $ g_c_u_pic = "dasex_cum_out_ani"
                                    show screen g_c_u
                                    pause 3.0
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "70 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    if dap_level == 10:
                                        $ dap_level = 11
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu

                        elif dap_level > 10:
                            m "Мисс Гринграсс"
                            $ h_body = "dap/d_govor.png"
                            dap "Да?"
                            $ h_body = "dap/d_wha.png"
                            m "Мне придется вновь про{size=+6}анал{/size}изировать вас"
                            $ h_body = "dap/d_plach.png"
                            dap "..."
                            $ h_body = "dap/d_vizsod4.png"
                            dap "опять..."
                            m "для освоения материала его всегда нужно как следует закреплять"
                            $ h_body = "dap/d_wha.png"
                            dap "*фыркает*"
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            hide screen daphne_main
                            hide screen daphne_main2
                            hide screen daphne_main3                                                                                                                                                                                   #HERMIONE
                            hide screen genie
                            hide screen desk
                            $ genie_chibi_xpos = -185 #-185 behind the desk. (Also 5 is something).
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "da/22_cum_01.png"
                            show screen chair_02
                            show screen g_c_u

                            hide screen daphne_02 #Hermione stands still.
                            hide screen blkfade
                            hide screen blktone
                            hide screen bld1
                            show screen ctc
                            with fade
                            pause
                            show screen bld1
                            with d3

                            dap_oh "ах"
                            $ g_c_u_pic = "dasex_ani"
                            dap_smile5 "............."
                            g9 "в этот раз твоя попка готова к этому"
                            dap_sl "мне... ах... все равно больно, сэр"
                            m "можешь кричать если хочешь"
                            dap_ispug "....."
                            dap_wha "но ведь тогда нас могут услышать"
                            g4 "*черт, а я ведь даже не знаю где находится этот кабинет*"
                            m "не хочу, чтобы ты сдерживалась"
                            dap_sl "я... ах... просто хочу чтобы вы сделали это быстрее"
                            $ g_c_u_pic = "dasex_ani"
                            g9 "{size=+6}Быстрее?{/size} ах ты шлюха!"
                            pause 2.0
                            dap_bol "!!!"
                            dap_krik "нет нет нет, стойте, пожайлуста нет, не так сильно!!!"
                            g9 "даа"
                            dap_sl "пожалуйста не так быстро.... нет.... пожалуйста.... аааааййй"
                            m "...."
                            dap_sl "......."

                            $ g_c_u_pic = "dasex_ani"
                            ">вы обратно сбавляете темп"
                            m "так тебе нравится больше?"
                            dap_smile4sl "ах... просто не надо... так сильно..."
                            m "тебе нравится, когда я тебя трахаю, маленькая шлюшка?"
                            dap_smile5 "ну... на самом деле..."
                            dap_smile "я рада что мне не пришлось ждать до того момента, когда родители подберут мне кого-то"
                            m "все это время ты хотела чтобы кто-то засадил тебе"
                            dap_smile5 "....."
                            g4 "что молчишь сука"
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            "шлеп"
                            dap_oh "профессор..."
                            m "думаешь, родители знают, какая их доча похотливая шлюха?"
                            dap_oh "я не... ах..."
                            "*ШЛЕП* *ШЛЕП*"
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            pause 1.0
                            $ renpy.play('sounds/slap.mp3')
                            with vpunch
                            m "твой учитель дерет тебя в задницу дорогая, не время строить из себя невинность"
                            dap_smile4 "я... делаю это для..."
                            m "для личной выгоды, как настоящая шлюха"
                            dap_smile4sl "...."


                            ">вы чувствуете что сейчас кончите"
                            menu kon3:
                                "Кончить в нее":
                                    g4 "Я сейчас..."
                                    dap_ispug "Сейчас?"
                                    g9 "Ох дааа"
                                    "..."
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    m "70 очков Слизерину"
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    $ dap_level += 1
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu


                                "Кончить на нее":
                                    g9 "Ох дааа"

                                    dap_smile4 "..."
                                    pause 1.0
                                    hide screen g_c_u
                                    $ g_c_u_pic = "dasex_cum_out_ani"
                                    show screen g_c_u
                                    pause 3.0
                                    hide screen chair_02
                                    hide screen g_c_u
                                    show screen genie
                                    show screen daphne_02
                                    $ h_body = "dap/d_sprm.png"
                                    show screen daphne_main
                                    with fade
                                    dap "почему вы меня не предупредили"
                                    dap "как мне теперь идти по коридору"
                                    m "70 очков Слизерину"
                                    dap "..."
                                    dap "Спасибо, сэр"
                                    hide screen daphne_main
                                    hide screen daphne_main2
                                    hide screen daphne_main3
                                    hide screen ctc
                                    hide screen bld1
                                    hide screen daphne_02
                                    with d3
                                    $ menu_x = 0.5
                                    $ dap_level += 1
                                    if daytime:
                                        $ daphne_chated = 1
                                        jump night_main_menu
                                    else:
                                        $ daphne_chated = 1
                                        jump day_main_menu
                    "Назад":
                        jump daphne_chat

        "-Дать подарок-":
            menu:
                "-Конфета-([candy])" if candy >= 1:
                    $ giftedD = True
                    jump giving_candyD #28_gifts.rpy

                "-Шоколад-([chocolate])" if chocolate >= 1:
                    $ giftedD = True
                    jump giving_chocolateD #28_gifts.rpy

                
                
                "-Обучающие журналы-([mag1])" if mag1 >= 1:
                    $ giftedD = True
                    jump giving_mag1D #28_gifts.rpy

                "-Девчачьи журналы-([mag2])" if mag2 >= 1:
                    $ giftedD = True
                    jump giving_mag2D #28_gifts.rpy

                "-Взрослые журналы-([mag3])" if mag3 >= 1:
                        $ giftedD = True
                        jump giving_mag3D #28_gifts.rpy

                "-Порнография-([mag4])" if mag4 >= 1:
                    $ giftedD = True
                    jump giving_mag4D #28_gifts.rpy



                
                "-Пачка презервативов-([condoms])" if condoms >= 1:
                    $ giftedD = True
                    jump giving_condomsD #28_gifts.rpy

                "-Лубрикант-([anal_lube])" if anal_lube >= 1:
                    $ giftedD = True
                    jump giving_lubeD #28_gifts.rpy

                "-Вибратор-([vibrator])" if vibrator >= 1:
                    $ giftedD = True
                    jump giving_vibratorD #28_gifts.rpy

                "-кляп с наручниками-([ballgag])" if ballgag >= 1:
                    $ giftedD = True
                    jump giving_ballgagD #28_gifts.rpy

                "-Анальная пробка-([plug])" if plug >= 1:
                    $ giftedD = True
                    jump giving_plugD #28_gifts.rpy

                "-Страпон-([strapon])" if strapon >= 1:
                    $ giftedD = True
                    jump giving_straponD #28_gifts.rpy

                


                "-Чулки-" if nets == 1:
                    $ giftedD = True
                    jump giving_netsD #28_gifts.rpy


                "-Назад-":
                    jump daphne_chat    


        "Ты свободна":
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            hide screen bld1
            hide screen daphne_main
            hide screen daphne_main2
            hide screen daphne_main3
            hide screen blktone
            hide screen daphne_02
            hide screen ctc
            with d3
            if daytime:
                $ daphne_chated = 1
                jump night_main_menu
            else:
                $ daphne_chated = 1
                jump day_main_menu



label daphne1:
    $ renpy.play('sounds/knocking.mp3')
    "Тук-тук-тук"
    "..."
    m "Кто опять?"
    menu:
        "Входите":
            jump daphne1_1

        "Кто это?":
            dap1 "Это я, Дафна Григрасс, профессор Снейп сказал, что вы звали меня"
            g9 "Ну что ж, Джинни, время для магии"
            jump daphne1_1

label daphne1_1:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 04.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1
    pause 4
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    dap1 "Звали, профессор?"
    m "Да"
    m "*кхем-кхем*"
    m "Так вот...{w}..........{w}..............................."
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    with d3
    $ h_body = "dap/d_wha2.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen daphne_main
    with d3
    dap1 "???"
    m "Эм..."
    g4 "Черт, мы забыли придумать легенду"
    $ h_body = "dap/d_wha.png"
    dap1 "Так что опять случилось?"
    m "*опять?*"
    m "Почему что-то должно случится?"
    $ h_body = "dap/d_plach.png"
    dap1 "Эм..."
    $ h_body = "dap/d_wha.png"
    dap1 "Ну, вы приглашаете меня к себе в кабинет только тогда, когда вам опять кто-то наябидничает"
    dap1 "Это опять эта грязнокровка Грейнджер?! А еще говорят, Гриффиндор - храбрость, благородство... пфф! Тоже мне!"
    m "..."
    $ h_body = "dap/d_zlo.png"
    dap1 "Что она опять про меня наговорила?"
    m "Это лучше ты мне расскажи... *ну а вдруг проканает*"
    $ h_body = "dap/d_plach.png"
    dap1 "..."
    $ h_body = "dap/d_rightwha.png"
    dap1 "*Этот старый хрыч блефует, ничего у него на меня нет*"
    $ h_body = "dap/d_smile3.png"
    dap1 "Эм...{w} Вероятно это все из-за того, что я вчера на уроке попыталась вместо небольшого камня поднять в воздух целую гору? Ну а что, я всегда стремлюсь быть лучше, чем обычные студенты"
    g4 "*Что она мне тут втирает?*"
    $ h_body = "dap/d_wha.png"
    m "Ладно"
    dap1 "..."
    g4 "*Блин надо было получше продумать наш план*"
    dap1 "..."
    menu dap_men:
        "Ты ведь капитан группы поддержки, правильно?":
            $ h_body = "dap/d_zlo.png"
            dap "Да, и это не обсуждается"
            m "Что, не понял?"
            dap "Я уже тысячу раз говорила, что единственная традиция, которую можно перенять и она не нарушает ни одного закона"
            m "Хм..."
            g4 "*вот же бешеная сука*"
            g9 "тем интереснее ее будет потом трахать*"
            jump dap_men

        "Ты не хотела бы помочь своему факультету в гонке за кубок?":
            $ h_body = "dap/d_wha2.png"
            dap "Помочь? каким образом?"
            g9 "*давай джинни, время магии*"
            m "ты...{w} не слышала о том, как некоторые девушки твоего факультета зарабатывают очки...{w} альтернативными методами?"
            $ h_body = "dap/d_plach.png"
            dap "..."
            $ h_body = "dap/d_wha.png"
            dap "мне кажется...{w} вы намекаете на что-то незаконное"
            g4 "*вот сука*"
            m "проехали"
            $ daph_pristav = 1
            jump dap_men

        "Из Министерства магии пришло письмо о нарушении моральных устоев учениками, ты об этом ничего не знаешь?":
            $ h_body = "dap/d_wha2.png"
            dap "Я? А почему сразу я?"
            $ h_body = "dap/d_right.png"
            dap "У нас не происходит ничего такого, чего бы не происходило в любом другом месте"
            $ h_body = "dap/d_zlo.png"
            dap "В этом министерстве магии сидят старые тетки, которым лишь бы поставить галочку в отчете, а до детей им дела нет"
            $ h_body = "dap/d_plach.png"
            dap "наверное..."
            jump dap_men

        "Можешь идти" if daph_pristav == 1:
            hide screen daphne_main
            hide screen daphne_main2
            hide screen daphne_main3
            hide screen ctc
            hide screen bld1
            with d3
            $ daphne_event = 3
            $ walk_xpos=360 #Animation of walking chibi. (From desk)
            $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
            $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
            show screen daphne_walk1f
            pause 3
            hide screen daphne_walk1f
            with d3
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            m "............"
            g4 "Похоже придется придумать что-то получше"
            $ menu_x = 0.5
            if daytime:
                $ daphne_chated = 1
                jump night_main_menu
            else:
                $ daphne_chated = 1
                jump day_main_menu




label daph_snape:
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
    sna "Джин, ты совсем ебанулся?"
    m "Эм..."
    m "Что-то произошло?"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Когда мы договаривались, что ты организуешь компромат на дочку главы департамента Министерства магии, я думал, что ты будешь изобретательнее, а не просто попробуешь предложить ей потрахаться"
    m "......."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "Откуда ты знаешь?"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Вчера я перехватил ее письмо, где она жалуется своей мамашке, что местный директор домогается до нее"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    g4 "*вот сука*"
    m "..."
    g4 "Погоди, ты меня подкалываешь? Откуда у тебя ее письмо?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Хах, все школы испокон веков читают письма своих студентов"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Просто никто об этом не знает"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    sna "Одна сумасшедшая из министерства пытается это узаконить"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"
    sna "Эх знавал я ее лет 20 назад... сосет как пыле..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Кхм, в прочем... не важно"
    sna "Нам нужно что-то с этим делать"
    m "......."
    g9 "Трахнем ее?"
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Сначала нужно что-то сделать с этим письмом!"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Я могу переделать его так, что никто не заметит"
    m "Отлично"
    m "Что напишем?"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "хм... надо подумать"
    m "Что там вообще в этом письме?"
    show screen letter
    $ letter_text = "{size=-6} Председателю комитета старых дев: Хелене Мизулинской{/size} \n \n {size=-3}      Здравствуйте, мама. Я с самого начала говорила Вам, что отправлять меня в эту школу было большой ошибкой. Сегодня директор пытался меня домогаться, используя свое должностное положение. \n \n             Ваша дочь, Дафна{/size}"
    pause
    hide screen letter
    m "..."
    m "Она с ней на вы?"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"
    sna "Ну а что, наверное, у нее в этом министерстве совсем поехали мозги"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Если я просто сожгу письмо, она отправит второе, нужно поменять содержание"
    m "Окей, как начнем?"

    menu:
        "\"Здравствуйте, мама...\""
        "Привет, маман":
            pass

        "Здаров, кашелка":
            pass

        "Йо, чо как, старуха?":
            pass

    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Пфф - ха - ха - ха"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Хотел бы я увидеть ее лицо в момент, когда она это прочтет"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "Что там дальше?"

    menu:
        "\"Я с самого начала говорила Вам, что отправлять меня в эту школу было большой ошибкой\""

        "Какого черта я до сих пор торчу в этой богом забытой дыре":
            pass

        "Мне осточертело просиживать лучшие годы в этой старой развалине":
            pass

        "Я хочу уехать из этого сраного замка":
            pass

    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Пфмха - ха - ха - ха"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Круто, что там дальше"
    menu:
        "\"Сегодня директор пытался меня домогаться, используя свое должностное положение.\""

        "Я уже взрослая и хочу гулять с крутыми мужиками, а не со всякими сопляками":
            pass

        "Здесь нет ни одного нормального мужика с большим членом, мне попадаются одни микропенисы":
            pass

    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Это...{w} просто..."

    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Божественно, ах - ха - ха - ха - ха"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Все бы отдал за то, чтобы увидеть ее лицо, когда она это прочтет"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Отлично я сегодня же отправлю его по адресу"
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
    $ daphne_event = 4
    $ days_without_an_event = 0
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    return


label daph_second:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d_sleza.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d_krik2.png"
    dap "Профессор Дамблдор!"
    $ h_body = "dap/d_wtf2.png"
    m "..."
    m "Да?"
    $ h_body = "dap/d_krik2.png"
    dap "Я больше не смогу здесь учиться!"
    $ h_body = "dap/d_vniz2.png"
    m "Почему?"
    $ h_body = "dap/d_wtfs.png"
    dap "Моя мать..... она..."
    m "Что?"
    $ h_body = "dap/d_krik2.png"
    dap "Она больше не хочет видеть меня..."
    $ h_body = "dap/d_wtfs.png"
    m "..."
    $ h_body = "dap/d_vniz2.png"
    dap "Что мне теперь делать"
    m "......."
    g4 "Может ты все таки расскажешь, что произошло?"
    $ h_body = "dap/d_sleza.png"
    dap "Сегодня сова принесла мне письмо"
    $ h_body = "dap/d_sleza.png"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    with d3
    show screen daphne_main2
    with d3
    show screen letter
    $ letter_text = "{size=-3}И слышать ничего не хочу, юная леди! У миссис Чанг дочка занимает 2е место в рейтинге студентов!!! Как я могу рассчитывать на повышение, если моя дочь вылетит из школы, которую заканчивают даже полукровки?!! Или ты заканчиваешь год на 1 месте в рейтинге студентов или можешь начинать искать себе новое жилье.{/size}"
    pause
    hide screen letter
    with d3
    m "..."
    g4 "*Охренеть, что творится в головах у этих канцелярских крыс*"
    $ h_body = "dap/d_krik2.png"
    dap "Профессор Дамблдор, я теперь сирота!!!"
    $ h_body = "dap/d_wtfs.png"
    m "..."
    m "Хм..."
    m "Но ведь...{w} ты еще можешь попытаться занять первое место в рейтинге студентов"
    g9 "*Да сучка, скоро будет жарко*"
    $ h_body = "dap/d_krik2.png"
    dap "Вы смеетесь надо мной?! Вы прекрасно знаете, что я за все время ни разу не зарабатывала очки факультета, тем более на первом месте эта выскочка Грейнджер, которая их будто печатает"
    $ h_body = "dap/d_vniz2.png"
    m "..."
    g9 "Я мог бы помочь вам с этим"
    dap "......."
    $ h_body = "dap/d_wtfs.png"
    dap "Помочь?"
    $ h_body = "dap/d_vniz2.png"
    dap "Нет, даже если вы подтянете меня по всем предметам, я все равно не успею обогнать даже половину студентов..."
    g4 "*Эта дура что, действительно не догоняет?*"
    $ h_body = "dap/d_wtfs.png"
    dap "Хотя вы могли бы поговорить с преподавателями, чтобы они справедливее относились ко мне! Вы ведь можете это!"
    m "эм..."
    m "Вообще то, я сам могу давать вам эти очки"
    dap "Эм... но вы ведь не ведете никаких предметов..."
    g4 "*Она притворяется или действительно такая тупая?*"
    m "Ну...{w} я мог бы давать вам индивидуальные уроки"
    $ h_body = "dap/d_vniz2.png"
    dap "........"
    dap "*вытирает глаза"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    with d3

    $ h_body = "dap/d_rightwha.png"
    show screen daphne_main
    dap "Хорошо"
    $ h_body = "dap/d_wha.png"
    dap "Когда будет первое занятие?"
    m "Можно прямо сейчас"
    $ h_body = "dap/d_ispug.png"
    dap "Да?"
    $ h_body = "dap/d_smile1.png"
    dap "С чего начнем?"
    m "Так..."
    m "Скажите ка, мисс Гринграсс..."
    menu:
        "В каком году было бородинское сражение?":
            pass

        "Что вы знаете о зябликах?":
            pass

    $ h_body = "dap/d_ispug.png"
    dap "..."
    $ h_body = "dap/d_plach.png"
    dap "эм..."
    $ h_body = "dap/d_wha2.png"
    dap "Что?"
    m "..."
    m "Вы безнадежный ученик, мисс Грингасс, следовало сразу это учесть, все отменяется"
    $ h_body = "dap/d_ispug.png"
    dap "..."
    $ h_body = "dap/d_plach.png"
    dap ".........."
    $ h_body = "dap/d_krik.png"
    dap "Я так и знала, что ничего не получится"
    $ h_body = "dap/d_plach2.png"
    m "..."
    g9 "Хм...{w} тем не менее, вы все еще можете заработать очки"
    $ h_body = "dap/d_plach.png"
    dap "Как?"
    m "Хм..."
    menu:
        "Станцуй для меня стриптиз":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            dap "Стоит на секунду дать слабину, как тот час же кто-то постарается сесть тебе на шею"
            pass


        "Покажи мне грудь":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            pass

        "Подрочи мне":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            pass

        "Минет":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            pass

        "Секс":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            pass

        "Время для анала":
            $ h_body = "dap/d_plach.png"
            dap "Эмм...."
            $ h_body = "dap/d_zlo.png"
            dap "Что?!!"
            $ h_body = "dap/d_krik.png"
            dap "Я сразу поняла куда вы клоните!"
            $ h_body = "dap/d_plach.png"
            pass

    $ renpy.play('sounds/door.mp3')
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen ctc
    hide screen bld1
    hide screen daphne_02
    with d3
    $ menu_x = 0.5
    m "..."
    $ daphne_event = 5
    m "Наверное{w}, стоило начать с чего-то менее хардкорного"
    $ days_without_an_event = 0
    return



label daph_norm:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d_zlo.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    dap "..."
    m "???"
    $ h_body = "dap/d_left.png"
    dap "Я согласна"

    m "Что?"
    $ h_body = "dap/d_wha2.png"
    dap "..."
    $ h_body = "dap/d_krik.png"
    dap "Я хочу зарабатывать очки на... \"индивидуальных занятия\""
    $ h_body = "dap/d_zlo.png"
    g9 "*Да сучка*"
    $ h_body = "dap/d_left.png"
    dap "Что я должна сделать?"
    $ daphne_event = 6
    jump dap_menu





label public_truci:
    m "Сегодня у меня для вас очень ответственное задание"
    $ h_body = "dap/d_plach.png"
    dap "???"
    m "Как я смог выяснить, у нас есть группа поддержки"
    $ h_body = "dap/d_ispug.png"
    dap "но вы ведь..."
    m "Поэтому, я должен лично проверить ее деятельность"
    $ h_body = "dap/d_wot.png"
    dap "....."
    $ h_body = "dap/d_left.png"
    dap "*Это опять что-то извращенское?*"
    $ h_body = "dap/d_wha.png"
    m "Я должен видеть вашу форму"
    $ h_body = "dap/d_govor.png"
    dap "Но она не менялась..."
    $ h_body = "dap/d_wha.png"
    g4 "Отлично, значит покажите мне старую форму"
    $ h_body = "dap/d_wha2.png"
    dap "пфф"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1f
    pause 3
    hide screen daphne_walk1f
    $ daphne_chibi_xpos = 610
    show screen daphne_02f
    hide screen daphne_02f
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of

    $ renpy.pause(2.0, hard = True)
    # приходит

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc


    g9 "хм, неплохо, прямо как в тех фильмах"
    m "Отлично, я должен проинспектировать вашу одежду"
    $ h_body = "dap/d2_plach.png"
    dap "....."
    dap "Ну...{w} вот она, на мне"
    m "....."
    $ h_body = "dap/d2_ispug.png"
    dap "............"
    g4 "*слишком рано*"
    # можно сделать разделение на 2 эвента или несколько
    m "Мне нужно более глубокое изучение"
    $ h_body = "dap/d2_govor.png"
    dap "Я не могу отдать вам ее, у нас сегодня репетиция"
    $ h_body = "dap/d2_wha.png"
    m "Чтож, ты можешь отдать не все"
    $ h_body = "dap/d2_plach.png"
    dap "А что вам нужно?"
    g9 "Мне вполне хватит твоих трусиков"
    $ h_body = "dap/d2_wtf.png"
    dap "......"
    $ h_body = "dap/d2_plach.png"
    dap "При чем тут они?"
    $ h_body = "dap/d2_left.png"
    dap "*старый извращенец*"
    m "Вы еще молоды, милая леди, и не все вам дано понять"
    $ h_body = "dap/d2_vizsod5.png"
    dap "....."
    $ h_body = "dap/d2_wha.png"
    dap "сколько очков я получу за это?"
    m "хм..."
    menu:
        "10":
            $ h_body = "dap/d2_left.png"
            dap "...."
            $ h_body = "dap/d2_vizsod3.png"
            dap "........"
            $ h_body = "dap/d2_govor.png"
            dap "ладно"
            dap ">дафна снимает и отдает вам свои трусики"
            $ h_body = "dap/d2_wha.png"
            dap  "....."
            m "Приходи вечером"
            $ h_body = "dap/d2_govor.png"
            dap "Да, сэр"
            $ dcr = 10

        "15":
            $ h_body = "dap/d2_wha.png"
            dap "15?"
            $ h_body = "dap/d2_rightwha.png"
            dap "......."
            $ h_body = "dap/d2_wha.png"
            dap "хорошо"
            ">дафна снимает и отдает вам свои трусики"
            $ h_body = "dap/d2_wha.png"
            dap "....."
            m "Приходи вечером"
            $ h_body = "dap/d2_govor.png"
            dap "Да, сэр"
            $ dcr = 15


        "25":
            $ h_body = "dap/d2_ispug.png"
            dap "25???"
            $ h_body = "dap/d2_smile2.png"
            dap "да, сэр"
            g9 "хорошо когда платишь тем, на что тебе насрать"
            show screen blkfade
            with Dissolve(1.0)
            pause 2.0
            ">дафна снимает и отдает вам свои трусики"
            hide screen blkfade
            with d9
            $ h_body = "dap/d2_wha.png"
            pause 1.0
            dap "....."
            m "Приходи вечером"
            $ h_body = "dap/d2_govor.png"
            dap "Да, сэр"
            $ dcr = 25



    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2f
    pause 3
    hide screen daphne_walk2f
    $ daphne_chibi_xpos = 610
    show screen daphne_01f
    hide screen daphne_01f
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of




    g9 "ну что, джинни, настало время для магии"
    show screen genie_jerking_off
    pause 2.0
    $ backgr = "new/j14.png"
    hide screen genie_jerking_off
    show screen fruk

    with d9
    pause 1.0
    jas "хозяин, сильнее, хоязин!"
    g9 "........"
    hide screen fruk
    $ backgr = "new/j15.png"
    show screen fruk
    pause 1.0
    jas "ааааххххх"

    hide screen fruk
    $ backgr = "new/4some_22.png"
    show screen fruk
    with d8
    pause 1.0
    iris "Меня следующей, пожалуйста, господин!"
    g9 "............"

    hide screen fruk
    $ backgr = "new/4some_22.png"
    show screen fruk
    with dissolve
    $ backgr = "new/d_a11.png"
    pause 1.0
    iris "он такой большой, господин!!!"

    g9 "Ахххххххх даааааааа"
    hide screen fruk

    show screen genie_jerking_off
    show screen genie_jerking_sperm
    with Dissolve(1.0)
    pause 2.0

    ">Вы кончаете прямо на трусики дафны"
    hide screen genie_jerking_sperm
    show screen genie
    with d3
    g9 "дело сделано"

    $ daphne_publ_request = 1

    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu




# начало нового
label truci_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc


    $ h_body = "dap/d2_wha.png"
    dap "......"
    m "......"
    $ h_body = "dap/d2_plach.png"
    dap "эм....{w} сэр?"
    m "да?"
    $ h_body = "dap/d2_vizsod5.png"
    dap "......."
    $ h_body = "dap/d2_vizsod3.png"
    dap "Где мои трусики?"
    $ daphn_publ = 1
    m "Ах, это"
    menu:
        "Вот они":
            jump public_truci2


        "Как прошел твой день?":
            m "Сначала расскажи как прошел твой день"
            $ h_body = "dap/d2_govor.png"
            dap "Эм... ну, впрочем как и всегда"
            dap "Я сходила на тренировку... без них было... достаточно странно"
            $ h_body = "dap/d2_smile2.png"
            dap "На самом деле не думала, что без них может быть так свободно"
            $ h_body = "dap/d2_wha.png"
            m "Кто-то заметил?"
            $ h_body = "dap/d2_plach.png"
            dap "Эм..."
            $ h_body = "dap/d2_govor.png"
            dap "Не знаю, я старалась не делать ничего такого сложного..."
            $ h_body = "dap/d2_ispug.png"
            dap "Хотя Сэнди на меня так странно потом смотрела..."
            g9 "*ништяк*"
            $ h_body = "dap/d2_wha.png"
            dap "...."
            $ h_body = "dap/d2_plach.png"
            dap "так...... я могу получить свои трусики?"
            m "да, конечно"
            jump public_truci2

label public_truci2:
    m "вот они"
    show screen blkfade
    with d6
    pause 1.0
    ">вы передаете дафне трусики измазанные вашей спермой"
    hide screen blkfade
    with d6
    $ h_body = "dap/d2_ispug.png"
    dap "что с ними?"
    m "......"
    $ h_body = "dap/d2_plach.png"
    dap "это............?"
    $ h_body = "dap/d2_vizsod3.png"
    dap "............"
    g9 "...."
    m "что?"
    $ h_body = "dap/d2_vizsod5.png"
    dap "....."
    $ h_body = "dap/d2_plach.png"
    dap "Я получу свои очки?"
    m "Конечно, же"
    if dcr == 10:
        m "10 очков Слизерину"
        $ h_body = "dap/d2_smile2.png"
        dap "Спасибо, профессор"

    elif dcr == 15:
        m "15 очков Слизерину"
        $ h_body = "dap/d2_smile2.png"
        dap "Спасибо, профессор"

    else:
        m "25 очков Слизерину"
        $ h_body = "dap/d2_smile2.png"
        dap "Спасибо, профессор"

    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen ctc
    hide screen bld1
    hide screen daphne_01
    with d3

    $ menu_x = 0.5
    $ daphne_publ_request = 0
    $ daphne_publ_level = 1
    if dap_level == 1:
        $ dap_level = 2
    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu






label daphne_public_first:
    m "Ты, наверное, знаешь, что в ближайшем будущем у нас будет проходить чемпионат"
    $ h_body = "dap/d_smile1.png"
    dap "Еще бы, все об этом только и говорят"
    m "ты ведь капитан группы поддержки, верно?"
    $ h_body = "dap/d_plach.png"
    dap "....."
    $ h_body = "dap/d_ispug.png"
    dap "эм...{w} да"
    m "Это очень ответственное место"
    dap "....."
    $ h_body = "dap/d_wha.png"
    dap "к чему вы клоните, профессор?"
    menu quid:
        "Хогвартс должен победить в этом чемпионате":
            m "Победа в этом чемпионате очень важна для нас"
            $ h_body = "dap/d_smile1.png"
            dap "Да, все очень ждут, когда он уже начнется"
            dap "уверена, что наша команда сможет победить"
            m "хмм"
            jump quid

        "Что вы там вообще делаете?":
            m "Как ты оцениваешь нынешнюю деятельность группы поддержки?"
            $ h_body = "dap/d_right.png"
            dap "эмм... у нас не очень то много желающих этим заниматься, состав постоянно меняется..."
            $ h_body = "dap/d_vniz.png"
            dap "из-за этого постоянно приходится все показывать заново"
            $ h_body = "dap/d_wha.png"
            dap "тем более не у всех получается повторять все движения так, как нужно"
            m "...."
            jump quid

        "Чем занимается капитан?":
            m "а чем занимаешься именно ты, как капитан?"
            $ h_body = "dap/d_govor.png"
            dap "эм... ну я руковожу этим всем"
            $ h_body = "dap/d_smile1.png"
            dap "девочки постоянно меняются, я единственная, кто знает"
            $ h_body = "dap/d_smile1.png"
            jump quid
        "Группа поддержки должна лучше работать":
            m "для подготовки к этим играм от группы поддержки потребуется больше чем обычно"
            $ h_body = "dap/d_plach.png"
            dap "эм...{w} ну..."
            $ h_body = "dap/d_smile1.png"
            dap "я могла бы набрать побольше девочек и придумать более интересную программу..."
            m "ты не понимаешь"
            $ h_body = "dap/d_wha.png"
            dap "...."
            m "как вы помогаете команде, кроме танцев?"
            $ h_body = "dap/d_plach.png"
            dap "эм..."
            dap "....."
            $ h_body = "dap/d_ispug.png"
            dap  "а что мы еще должны делать?"
            $ h_body = "dap/d_wha.png"
            g4 "Как что?!!"
            g4 "поднимать мотивацию игроков!"
            $ h_body = "dap/d_plach.png"
            dap "..."
            g9 "........"
            $ h_body = "dap/d_ispug.png"
            dap "................"
            $ h_body = "dap/d_wha.png"
            dap "Эм{w}, о чем вы?"
            g9 "*давай джинни, время магии"
            jump public_truci


label daph_publ:
    menu:


        "Флиртуй с учеником":
            if dap_level < 4:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if flirt_com == 0:
                m "Сегодня тебе нужно будет посодействовать в нашей победе над другими школами"
                $ h_body = "dap/d_ispug.png"
                dap "Что?"
                $ h_body = "dap/d_govor.png"
                dap "Я же не играю, я только..."
                $ h_body = "dap/d_wha.png"
                m "Тебе не нужно будет играть"
                $ h_body = "dap/d_wha.png"
                dap "...."
                $ h_body = "dap/d_govor.png"
                dap "Что вы хотите от меня?"
                $ h_body = "dap/d_wha.png"
                m "Я хочу, чтобы ты... *кхем*..."
                m "Подбодрила одного из игроков"
                $ h_body = "dap/d_ispug.png"
                dap "...."
                $ h_body = "dap/d_plach.png"
                dap "что бы я..."
                $ h_body = "dap/d_ispug.png"
                dap "Что?"
                g4 "......"
                m "У наших игроков напрочь отсутствует мотивация, мисс Гринграсс"
                $ h_body = "dap/d_wha.png"
                dap "....."
                $ h_body = "dap/d_ispug.png"
                dap "а при чем тут я?"
                m "мне удалось выяснить, что это связано, с недостатком женского внимания"
                $ h_body = "dap/d_left.png"
                dap "*вот куда клонит этот старый извращенец*"
                $ h_body = "dap/d_zlo.png"
                dap "Вы что, думаете, что я шлюха, чтобы заниматься непонятно чем?"

                m "Непонятно чем? Нужно будет всего лишь немного пофлиртовать с одним из игроков, чтобы поднять ему самооценку"
                if dap_level < 4:
                    jump too_much_d
                $ h_body = "dap/d_ispug.png"
                dap "Что?"
                $ h_body = "dap/d_plach.png"
                dap "Я не могу делать ничего такого с какими-то..."
                m "Вы можете сделать это с любым из игроков, разве там нет потомственных магов?"
                $ h_body = "dap/d_right.png"
                dap "Эм, ну вообще то, Драко..."
                $ h_body = "dap/d_vizsod3.png"
                dap "....."
                m "....."
                m "Так что?"
                $ h_body = "dap/d_wha.png"
                dap "Сколько очков я получу за это?"
                menu:
                    "25":
                        $ ponts = "25"


                    "40":
                        $ ponts = "40"


                    "60":
                        $ ponts = "60"


                $ h_body = "dap/d_vizsod4.png"
                dap "...."
                $ h_body = "dap/d_left.png"
                dap "*будь ты проклят, старик*"
                $ h_body = "dap/d_wha.png"
                $ daphne_publ_request = 2
                dap "Я вернусь вечером"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3
                $ daphne_publ_request = 2
                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            else:
                m "У меня есть для тебя задание"
                $ h_body = "dap/d_ispug.png"
                dap "......"
                $ h_body = "dap/d_plach.png"
                dap "что на этот раз?"
                m "не беспокойся, ты это уже делала"
                $ h_body = "dap/d_wha.png"
                dap "....."
                g9 "пора помочь своей команде получить победу"
                $ h_body = "dap/d_ispug.png"
                dap "еще раз"
                m "в прошлый раз ты плохо справилась"
                m "в этот раз придется попробовать сделать это нормально"
                $ h_body = "dap/d_vizsod5.png"
                dap "....."
                $ h_body = "dap/d_vizsod3.png"
                dap "хорошо"
                $ h_body = "dap/d_wha.png"
                dap "я вернусь после тренировки"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3
                $ daphne_publ_request = 2
                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

        "Пригласи на свидание":
            if dap_level < 6:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if date_com == 0:
                m "Сегодня тебе еще раз придется пойти на некоторые жертвы для победы в чемпионате"
                $ h_body = "dap/d_ispug.png"
                dap "Что? Опять?"
                g9 "*Ты ведь не думала, что на этом все закончится, правда?*"
                m "Кхем, ваши первичные действия уже принесли некоторые результаты..."
                $ h_body = "dap/d_wha.png"
                dap "Правда?"
                m "... {w} да, но этого не достаточно для победы над остальными школами!"
                $ h_body = "dap/d_plach.png"
                dap "..."
                dap "Опять нужно будет флиртовать с кем-то?"
                m "В этот раз от вас потребуется пригласить одного из игроков на свидание"
                if dap_level < 5:
                    jump too_much_d
                $ h_body = "dap/d_wtf.png"
                dap "что?"
                $ h_body = "dap/d_ispug.png"
                dap "Свидание??!"
                $ h_body = "dap/d_zlo.png"
                dap "Это исключено!"
                m "почему?"
                $ h_body = "dap/d_wha2.png"
                dap "Это же Свидание!"
                $ h_body = "dap/d_right.png"
                dap "После этого могут пойти слухи!"
                $ h_body = "dap/d_left.png"
                dap "Что Гринграсс встречается непонятно с кем!"
                m "..."
                g4 "А что в этом плохого?"
                $ h_body = "dap/d_zlo.png"
                dap "Как что?!"
                $ h_body = "dap/d_govor.png"
                dap "Я не хочу чтобы за моей спиной шептались"
                $ h_body = "dap/d_zlo.png"
                m "..."
                dap "Тем более...."
                $ h_body = "dap/d_visod2.png"
                dap "А что если он откажется"

                m "вот оно что"
                $ h_body = "dap/d_vizsod3.png"
                dap "я еще не приглашала никого"
                m "Не беспокойся, мне кажется вряд ли кто-то сможет отказать..."
                menu:
                    "Девушке из семьи Гринграсс":
                        $ h_body = "dap/d_vizsod5.png"
                        dap "хм... и то верно..."
                        pass

                    "Такой соблазнительной блондиночке":
                        $ h_body = "dap/d_zlo.png"
                        dap "......"
                        $ h_body = "dap/d_left.png"
                        dap "*чертов извращенец*"
                        pass



                m "За это Вы получите 45 очков"
                $ h_body = "dap/d_vniz.png"
                dap "....."
                $ h_body = "dap/d_wha.png"
                dap "Хорошо, я сделаю это"
                $ date_req = 1
                dap "Я вернусь вечером"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3
                $ daphne_publ_request = 3
                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            else:
                m "Неплохой денек, не правда ли?"
                $ h_body = "dap/d_plach.png"
                dap "эм....."
                m "просто отличный для прогулки"
                $ h_body = "dap/d_wha.png"
                dap "......"
                $ h_body = "dap/d_rightwha.png"
                dap "наверное...."
                $ h_body = "dap/d_wha.png"
                m "тогда вашим сегодняшним заданием будет пойти и назначить кому-нибудь свидание на сегодня"
                $ h_body = "dap/d_ispug.png"
                dap "еще раз?"
                m "твои действия уже приносят плоды, не стоит останавливаться"
                $ h_body = "dap/d_vizsod3.png"
                dap "...."
                $ h_body = "dap/d_plach.png"
                dap "а...."
                m "что?"
                dap "я могу пригласить того же, кого и в прошлый раз?"
                m "нет, это должен быть кто-то другой"
                $ h_body = "dap/d_vizsod3.png"
                dap "но ведь тогда все будут говорить, что я... встречаюсь с несколькими парнями"
                g9 "*хаха, это еще только начало сучка*"

                m "ты хочешь очки или нет?"
                $ h_body = "dap/d_plach.png"
                dap "......."
                $ h_body = "dap/d_vizsod5.png"
                dap "Хорошо, я вернусь вечером"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3
                $ daphne_publ_request = 3
                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu


        "Дай ему потрогать тебя":
            if dap_level < 8:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if mats_com == 0:

                m "Сегодня ты сможешь принести пользу своей школе"
                $ h_body = "dap/d_govor.png"
                dap "Эм... мне кажется я догадываюсь к чему вы клоните..."
                $ h_body = "dap/d_wha.png"
                m "Да, нужно поддержать нашу команду"
                $ h_body = "dap/d_plach.png"
                dap "Что я должна буду сделать?"
                m "Ты уже сделала большой шаг"
                m "Сегодня ты должна дать одному из членов команды"
                $ h_body = "dap/d_ispug.png"
                dap "что??"
                m "Дать ему потрогать тебя"
                g9 "*пока что*"
                if dap_level < 6:
                    jump too_much_d
                $ h_body = "dap/d_plach.png"
                dap "Дать.... {w} потрогать себя?"
                m "это не так уж много, тем более ты можешь сама выбрать кому"
                $ h_body = "dap/d_rightwha.png"
                dap "...."
                $ h_body = "dap/d_vizsod3.png"
                dap "*если только ему...*"
                m "так что?"
                $ h_body = "dap/d_wha.png"
                dap "сколько очков я получу за это?"
                menu flirt:
                    "25":
                        $ h_body = "dap/d_zlo.png"
                        dap "что? я получала столько и и за меньшие вещи!"
                        g4 "...."
                        jump flirt

                    "35":
                        $ h_body = "dap/d_rightwha.png"
                        dap "хм...."
                        $ h_body = "dap/d_wha.png"
                        dap "хорошо"
                        $ ponts = "35"


                    "45":
                        $ h_body = "dap/d_ispug.png"
                        dap "45?"
                        $ h_body = "dap/d_smile2.png"
                        dap "Я вернусь вечером"
                        $ ponts = "45"

                $ daphne_publ_request = 5
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            else:
                m "У меня для тебя есть очень ответственное задание"
                $ h_body = "dap/d_plach.png"
                dap "...."
                $ h_body = "dap/d_vizsod3.png"
                dap "опять..."
                m "да, ты опять поможешь своей школе!"
                $ h_body = "dap/d_left.png"
                dap "*или просто повеселю старого извращенца*"
                $ h_body = "dap/d_wha.png"

                dap "что за задание?"
                m "всего лишь дать себя потрогать какому-нибудь счастливцу"
                $ h_body = "dap/d_ispug.png"
                dap "...."

                g9 "...."
                $ h_body = "dap/d_plach.png"
                dap "хорошо"
                $ h_body = "dap/d_rightwha.png"
                dap "Я вернусь вечером"
                $ daphne_publ_request = 5
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

        "Покажи ему грудь":
            if dap_level < 10:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if tits_com == 0:
                m "Мисс Гринграсс, я чувствую, что сегодня мотивация наших игроков поднимется до небес"
                $ h_body = "dap/d_wot.png"
                dap "........"
                m "и причиной этому конечно же будете вы"
                $ h_body = "dap/d_vizsod5.png"
                dap "........."
                $ h_body = "dap/d_plach.png"
                dap "что мне нужно будет сделать?"
                m "в этот раз вас никто даже пальцем не коснется"
                $ h_body = "dap/d_wha.png"
                dap "...."
                $ h_body = "dap/d_smile1.png"
                dap "правда?"
                m "да"
                g9 "только посмотрит на вашу грудь"
                if dap_level < 7:
                    jump too_much_d
                $ h_body = "dap/d_wtf.png"
                dap "что?"
                $ h_body = "dap/d_wha2.png"
                m "сегодня вы покажете кому-нибудь свою грудь"
                $ h_body = "dap/d_plach.png"
                dap ".........."
                $ h_body = "dap/d_vizsod5.png"
                dap "блин"
                $ h_body = "dap/d_plach.png"
                dap "можно мне другое задание?"
                m "вы прекрасно знаете, что нет"
                $ h_body = "dap/d_vizsod3.png"
                dap "....."
                $ h_body = "dap/d_left.png"
                dap "*чертов старик*"
                $ daphne_publ_request = 4
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            else:

                m "У меня к тебе очень важное задание"
                $ h_body = "dap/d_wot.png"
                dap "...."
                $ h_body = "dap/d_wha.png"
                dap "как всегда"
                g9  "показать грудь, какому-нибудь счастливцу"
                $ h_body = "dap/d_left.png"
                dap "точно как всегда"
                m "ты еще здесь?"
                $ h_body = "dap/d_vizsod3.png"
                dap "....."
                $ daphne_publ_request = 4
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu


        "Передерни ему":
            if dap_level < 10:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if fap_com == 0:
                m "Мисс Гринграс, сегодня вы принесете пользу не только факультету, а всему Хогвартсу!"
                $ h_body = "dap/d_ispug.png"
                dap "..."
                $ h_body = "dap/d_vizsod3.png"
                dap "Почему то, я догадываюсь о чем пойдет речь"
                m "Сегодня вы пойдете и передерните одному из членов команды"
                $ h_body = "dap/d_wtf.png"
                dap "Что?"
                g9 "*ну а что, пора бы уже выходить в свет*"
                $ h_body = "dap/d_zlo.png"
                m "Впереди очень важный матч, разве ты не видишь как игроки волнуются"
                dap "...."
                $ h_body = "dap/d_zlo.png"
                dap "волнуются?"

                dap "из-за этого я должна им передергивать?"
                m "Вы могли бы сделать не только это...."
                $ h_body = "dap/d_plach.png"
                dap "...."
                g4 "*лишь бы не сорвалась*"

                m "но сегодня можно ограничится лишь дрочкой"
                if dap_level < 8:
                    jump too_much_d
                $ h_body = "dap/d_wha.png"
                dap "...."
                m "Школа нуждается в вас"
                $ h_body = "dap/d_zlo.png"
                dap "..."
                m "Как думаешь, что мама скажет, когда увидит, что твоя школа взяла первое место и увидит твою фотографию в новостях?"
                $ h_body = "dap/d_ispug.png"
                dap "Что?"
                $ h_body = "dap/d_right.png"
                dap "..."
                $ h_body = "dap/d_smile1.png"
                dap "Я сделаю это"

                g9  "*даже не спросила про очки*"
                $ h_body = "dap/d_smile2.png"
                dap "за 45 очков"
                m "договорились"
                $ daphne_publ_request = 6
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            else:
                m "Сегодня у меня есть для тебя работенка"
                $ h_body = "dap/d_plach.png"
                dap "какая?"

                m "ты должна будешь подбодрить одно из своих товарищей"
                $ h_body = "dap/d_vizsod5.png"
                dap "...."
                $ h_body = "dap/d_plach.png"
                dap "подбодрить?"
                g9 "ты все поняла"
                $ h_body = "dap/d_rightwha.png"
                dap "....."
                $ h_body = "dap/d_wha.png"
                dap "хорошо"
                $ daphne_publ_request = 6
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

        "Сделай ему минет":
            if dap_level < 11:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if minet_com == 0:

                m "Прошлая победа не была случайностью"
                $ h_body = "dap/d_smile2.png"
                dap "Да, наши парни молодцы"
                m "да"
                m "Поэтому, тебе нужно будет наградить одного из игроков"
                $ h_body = "dap/d_ispug.png"
                dap "Что?"
                m "Чтобы они повторили свой успех тебе нужно будет"
                $ h_body = "dap/d_plach.png"
                m "..."
                g9 "Отсосать одному из них"
                if dap_level < 9:
                    jump too_much_d
                $ h_body = "dap/d_wtf.png"
                dap "Что?!"

                $ daphne_publ_request = 7
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

            else:

                m "Мисс Гринрграсс, как на счет того, чтобы заработать сразу 60 очков сегодня?"
                $ h_body = "dap/d_plach.png"
                dap "эм..."
                $ h_body = "dap/d_wot.png"
                dap "для этого мне придется сделать что-то...."
                $ h_body = "dap/d_wha.png"
                g9 "я знал, что чистокровные волшебники славятся своей проницательностью"
                $ h_body = "dap/d_wot.png"
                dap "....."
                $ h_body = "dap/d_plach.png"
                dap "так что я должна буду сделать?"
                m "самую малость"
                g9 "всего лишь маленький отсос одному из игроков"
                $ h_body = "dap/d_vizsod3.png"
                dap "ах, это..."
                $ h_body = "dap/d_vizsod5.png"
                dap "...."
                $ h_body = "dap/d_wha.png"
                dap "да"

                $ daphne_publ_request = 7
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu


        "Трахнись с ним":
            if dap_level < 10:
                $ h_body = "dap/d_plach.png"
                dap "Эмм...."
                $ h_body = "dap/d_ispug.png"

                dap "Что?!!"
                $ h_body = "dap/d_krik.png"
                dap "Как вы можете просить меня о таком..."
                $ h_body = "dap/d_zlo.png"
                dap "Наверное, мне все таки придется искать себе новое жилье"
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                hide screen daphne_02
                $ menu_x = 0.5
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu
            if fuck_com == 0:
                m "Сегодня ты принесешь пользу своей команде"
                $ h_body = "dap/d_plach.png"
                dap "..."
                g9 "..."
                m "Ты должна будешь..."
                $ h_body = "dap/d_zlo.png"
                dap "90 очков"
                m "..."
                $ h_body = "dap/d_left.png"
                dap "Можете не произносить это в слух"
                m "..."
                $ h_body = "dap/d_right.png"
                dap "Я вернусь после тренировки"

                $ daphne_publ_request = 8
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3
                $ renpy.play('sounds/door.mp3') #Sound of
                m "Похоже она уже готова к кульминации нашей работы"
                m "Нужно обговорить со снейпом за бутылочкой вина, что делать с ней дальше"
                $ daphne_event = 11
                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

            else:
                m "Как у вас сегодня настроение, мисс Гринграсс?"
                $ h_body = "dap/d_plach.png"
                dap "...."

                $ h_body = "dap/d_wot.png"
                dap "*очередной подъеб?*"
                $ h_body = "dap/d_wha.png"
                dap "эм.... нормально"
                m "отлично, потому что сегодня вы должны поднять его одному из игроков"
                $ h_body = "dap/d_ispug.png"
                dap "....."
                $ h_body = "dap/d_vizsod3.png"
                dap "что я должна буду сделать?"
                m "как вы думаете?"
                $ h_body = "dap/d_plach.png"
                dap "эм..."
                $ h_body = "dap/d_vizsod5.png"
                dap "...."
                g9 "...."
                $ h_body = "dap/d_plach.png"
                dap "...."
                g9 "правильно"
                $ h_body = "dap/d_zlo.png"
                dap "хорошо, я сделаю это"
                $ daphne_publ_request = 8
                hide screen daphne_main
                hide screen daphne_main2
                hide screen daphne_main3
                hide screen ctc
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen daphne_walk1f
                pause 3
                hide screen daphne_walk1f
                $ daphne_chibi_xpos = 610
                show screen daphne_02f
                hide screen daphne_02f
                with d3

                $ renpy.play('sounds/door.mp3') #Sound of
                if daytime:
                    $ daphne_chated = 1
                    jump night_main_menu
                else:
                    $ daphne_chated = 1
                    jump day_main_menu

        "Назад":
            jump daphne_chat




label public_test:
    $ ponts = "50"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ h_body = "dap/d2_wha.png"
    menu pubtest:
        "флирт":
            jump flirt_complete

        "поцелуй":
            "poka ne gotovo"
            jump pubtest

        "сиськи":
            jump grud_complete

        "мацать":
            jump mats_complete

        "фап":
            jump fap_complete


        "минет":
            jump minet_complete

        "секс":
            jump fuck_complete



label flirt_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    $ daphne_publ_request = 0
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"

    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ flirt_com = 1
            $ slytherin += 15
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            if flirt_com == 0:
                g4 "Что значит выполнила, расскажи подробнее"
                $ h_body = "dap/d2_visod2.png"
                dap "Эм... ну, как вы и просили..."
                $ h_body = "dap/d2_govor.png"
                dap "Когда тренировка закончилась, я подождала, пока все выйдут из раздевалки"
                $ h_body = "dap/d2_wha.png"
                m "и?"
                $ h_body = "dap/d2_vizsod5.png"
                dap "Я дождалась, когда будет выходить драко и..."
                m "..."
                m "И?"
                $ h_body = "dap/d2_vizsod5.png"
                dap "Эм, ну мы поговорили"
                g4 "Что? Поговорили?"
                $ h_body = "dap/d2_vizsod3.png"
                dap "...."
                m "так что было?"

                dap "Ну..."
                $ h_body = "dap/d2_plach.png"
                dap "Я сказала, что он хорошо играет"
                m ".................."
                g4 "Мне кажется ты не очень хорошо поняла слово \"флирт\""
                $ h_body = "dap/d2_govor.png"
                dap "Это не все"
                $ h_body = "dap/d2_wha.png"
                m "Что было дальше?"
                $ h_body = "dap/d2_plach.png"
                dap "ну"
                $ h_body = "dap/d2_vizsod5.png"
                dap "я....{w} вроде как несколько раз коснулась его своими бедрами"
                m "...........{w}...............{w}.................."
                g4 "это все?"
                m "*не густо, но для начала сгодится*"
                $ h_body = "dap/d2_plach.png"
                dap "Я сделала все что могла"
                m "[ponts] очков Слизерину"
                $ h_body = "dap/d2_wha.png"
                dap "...."
                $ h_body = "dap/d2_smile2.png"
                $ flirt_com = 1
                dap " Спасибо"
                jump public_completed2
            else:
                if dap_level < 8:
                    $ dcr = renpy.random.randint(1,1)
                else:
                    $ dcr = renpy.random.randint(2,3)
                if dcr == 1:
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "У меня был очень ограниченный выбор"
                    m "...."
                    $ h_body = "dap/d2_right.png"
                    dap "не понимаю, почему в команде так мало парней из слизерина?"
                    $ h_body = "dap/d2_wha2.png"
                    dap "это все тренер виноват, он просто завидует и набирает таких же безродных как он сам"
                    g4 "*что она несет*"
                    $ h_body = "dap/d2_rightwha.png"
                    dap "если бы я отбирала игроков, я бы вообще...."
                    $ h_body = "dap/d2_wha.png"
                    g4 "может перейдем к твоему заданию?"
                    $ h_body = "dap/d2_govor.png"
                    dap "ах, да"
                    $ h_body = "dap/d2_wha.png"
                    pause 1.0
                    $ h_body = "dap/d2_govor.png"
                    dap "как я и говорила, мне пришлось выбирать всего из пары человек"
                    $ h_body = "dap/d2_wha.png"
                    m "............"
                    $ h_body = "dap/d2_smile3.png"
                    dap "я ведь не могла флиртовать с каким-нибудь нищебродом, хуже могут быть только полукровки"
                    m "..................."
                    g4 "Так что было дальше?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Я подошла к одному из \"Слизеринских\" парней...."
                    $ h_body = "dap/d2_wha.png"
                    m "и?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Я сказала ему \"эй, я видела твою семью в вестнике магической аристократии\""
                    $ h_body = "dap/d2_wha.png"
                    m ".........{w}.........................{w}........................................."
                    $ h_body = "dap/d2_smile5.png"
                    dap "........."
                    m "эм"
                    $ h_body = "dap/d2_smile2.png"
                    dap "я сделала это"
                    g4 "Ты точно правильно расслышала, что я просил тебя сделать?"
                    $ h_body = "dap/d2_plach.png"
                    dap  "....."
                    $ h_body = "dap/d2_govor.png"
                    dap "Вы просили пофлиртовать с кем-то из команды"
                    $ h_body = "dap/d2_wha.png"
                    g4 "при чем тут какой то там вестник???"
                    $ h_body = "dap/d2_wha2.png"
                    dap "как причем?!"
                    $ h_body = "dap/d2_smile3.png"
                    dap "Я же вспомнила, что это его семья, то есть я помню его фамилию!"
                    $ h_body = "dap/d2_zlo.png"
                    dap "Он не мог не оценить оказанного ему внимания!!!"
                    $ h_body = "dap/d2_wha.png"
                    m "............................."
                    m "не уверен, что это именно то, о чем мы с тобой договаривались"
                    $ h_body = "dap/d2_ispug.png"
                    dap "....."
                    $ h_body = "dap/d2_plach.png"
                    dap "но я ведь получу очки?"
                    $ flirt_com = 2
                    m "....."
                    menu:
                        "да":
                            m "[ponts] очков Слизерину"
                            $ slytherin += 15
                            dap "спасибо"
                            jump public_completed2

                        "нет":
                            jump public_completed2
                elif dcr == 2:
                    $ h_body = "dap/d2_ispug.png"
                    dap "эм, сегодня все прошло так странно"
                    m "почему?"
                    $ h_body = "dap/d2_wha.png"
                    dap "я потратила на ваше задание весь вечер"
                    m "что ты делала?"
                    $ h_body = "dap/d2_plach.png"
                    dap "У меня никак не получалось свести разговор к флирту"
                    m "...."
                    $ h_body = "dap/d2_govor.png"
                    dap "Сначала я подошла к одному парню... он из достаточно высокого рода"
                    $ h_body = "dap/d2_plach.png"
                    dap "почему-то он не очень приветливо воспринял мои попытки к общению..."
                    m "да ладно?"
                    m "что ты ему сказала?"
                    $ h_body = "dap/d2_wha.png"
                    dap "Ну как обычно, спросила что он тут шляется"
                    m "....."
                    g4 "че?"
                    m "Тебе еще никто не говорил, что это не самый лучший способ начать разговор?"
                    $ h_body = "dap/d2_plach.png"
                    dap "ну...."
                    $ h_body = "dap/d2_govor.png"
                    dap "Я подошла к другому парню, тоже из Слизерина"
                    $ h_body = "dap/d2_wha.png"
                    dap "я постаралась быть максимально милой и даже встала в достаточно открытую позу"
                    m "что было дальше?"
                    $ h_body = "dap/d2_plach.png"
                    dap "он сказал, что спешит к своему другу"
                    m "....."
                    m "наверное, он просто больше любит \"друзей\" нежели девочек"
                    $ h_body = "dap/d2_smile3.png"
                    dap "хм, а это интересно, можно слить эту информацию в газеты и его семья не будет больше зазнаваться, что они на 2 места в рейтинге выше нас"
                    g4 "........{w} че?"
                    m "давайте вернемся к заданию"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну..... дальше я хотела опять подойти к Драко, но мне кажется он был не в себе"
                    m "то есть?"
                    $ h_body = "dap/d2_ispug.png"
                    dap "почему то он сделал вид, что не знает меня..."
                    $ h_body = "dap/d2_wha2.png"
                    dap "пока я пыталась отчитать его, он дождался когда придет Чжо Чанг и ушел прямо с ней"
                    $ h_body = "dap/d2_left.png"
                    dap "Козел"
                    m "....."
                    g4 "Чо Чанг?!"
                    $ h_body = "dap/d2_plach.png"
                    dap "эм.... да"
                    g4 "вот красный ублюдок"
                    $ h_body = "dap/d2_wha.png"
                    dap "Эм... вообще то он тоже из слизерина, если уж на то пошло, то он зеленый"
                    m "...."
                    m "вернемся к заданию"
                    $ h_body = "dap/d2_govor.png"
                    dap "Ну, больше игроков из слизерина не осталось, поэтому я нашла парня из когтервана"
                    $ h_body = "dap/d2_wha.png"
                    m "и?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "я постаралась быть максимально милой и.... он ответил тем же"
                    m "....."
                    m "а точнее?"
                    $ h_body = "dap/d2_smile5.png"
                    dap "он пригласил меня на свидание"
                    $ h_body = "dap/d2_smile2.png"
                    dap "первый раз меня кто-то пригласил на свидание"
                    m "..."
                    m "ты согласилась?"
                    $ h_body = "dap/d2_plach.png"
                    dap "что? конечно же нет! его семья всего лишь 23 в рейтинге, пфф"
                    $ h_body = "dap/d2_wha.png"
                    m "понятно, мисс Гринграсс"
                    m "15 очков Слизерину"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 3:
                    m "Расскажи подробнее"
                    $ h_body = "dap/d2_wha.png"
                    dap "да"
                    $ h_body = "dap/d2_govor.png"
                    dap "В этот раз я не стала выцеплять кого-то конкретного"
                    $ h_body = "dap/d2_wha.png"
                    m "да?"
                    m "и что же ты сделала?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Пока тренировалась команда по квидичу, мы с девочками тоже отрабатывали внизу"
                    $ h_body = "dap/d2_wha.png"
                    g4 "че делали?"
                    $ h_body = "dap/d2_plach.png"
                    dap "Эм..."
                    $ h_body = "dap/d2_govor.png"
                    dap "Отрабатвали кричалки...."
                    $ h_body = "dap/d2_zlo.png"
                    dap "Это не просто знаете ли, всем вместе кричать одно и тоже"
                    $ h_body = "dap/d2_wha.png"
                    m "...."
                    m "так что там было?"
                    $ h_body = "dap/d2_govor.png"
                    dap "После того как мы отработали всю программу..."
                    $ h_body = "dap/d2_smile2.png"
                    dap "я немного изменила ее и вся команда слышала, что в случае победы в чемпионате, девочки подбодрят игроков другим способом"
                    m "ого"
                    g9 "*она начинает учиться*"
                    $ h_body = "dap/d2_left.png"
                    dap "Жаль только потом тренер выгнал нас с поля"
                    m "..."
                    $ h_body = "dap/d2_wha2.png"
                    dap "Какое право он вообще имеет на такое?!"

                    dap "Вы же директор, вы накажете его за это?"
                    m "ВЫ отлично справились мисс Гринграсс"
                    $ h_body = "dap/d2_wha.png"
                    dap "......."
                    dap "*это значит \"Нет?\" *"
                    m "...."
                    $ h_body = "dap/d2_plach.png"
                    dap "Я получу свои очки?"
                    m "30 очков Слизерину"
                    $ slytherin += 30
                    $ h_body = "dap/d2_smile2.png"
                    dap "Спасибо"
                    jump public_completed2

label date_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    $ daphne_publ_request = 0
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я сделала это"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "45 очков Слизерину!"
            $ slytherin += 45
            dap "хм, Спасибо"
            jump public_completed2

        "Мне нужны подробности":
            if dap_level < 8:
                m "Как прошло ваше свидание?"
                $ h_body = "dap/d2_plach.png"
                dap "Эм... ну..."
                $ h_body = "dap/d2_wha.png"
                dap "А как может пройти свидание в замке..."
                $ h_body = "dap/d2_govor.png"
                dap "Мы немного побродили рядом с лесом"
                $ h_body = "dap/d2_wha.png"
                m "а дальше?"
                $ h_body = "dap/d2_govor.png"
                dap "посидели у озера"
                $ h_body = "dap/d2_wha.png"
                m "....{w} а дальше?"
                $ h_body = "dap/d2_plach.png"
                dap "эм.... что дальше?"
                $ h_body = "dap/d2_wha.png"
                g4 "Вы что не..."
                $ h_body = "dap/d2_wha2.png"
                dap "Нет, мы не целовались"
                g4 "*Да при чем тут...*"
                $ h_body = "dap/d2_smile3.png"
                dap "Гринграсс никогда не целуются на первом свидании"
                m "...... да уж{w}, повезло мужским особям Гранграсс"
                $ h_body = "dap/d2_wha.png"
                dap "вы обещали мне очки"
                m "да"
                m "45 очков Слизерину!"
                $ slytherin += 45
                $ h_body = "dap/d2_smile2.png"
                dap "хм, Спасибо"
                $ date_com = 1
                jump public_completed2
            else:
                
                m "Как прошло ваше свидание?"
                $ h_body = "dap/d2_govor.png"
                dap "Я назначила свидание нашему нападающему"
                $ h_body = "dap/d2_wha2.png"
                dap "Так этот придурок потащил меня в лес"
                m "Что вы там делали?"
                $ h_body = "dap/d2_rightwha.png"
                dap "Самое идиотское место, какое только можно придумать"
                m "Почему?"
                $ h_body = "dap/d2_wha.png"
                dap "Мне пришлось постоянно оглядываться, с любой стороны на нас мог смотреть кто угодно"
                $ h_body = "dap/d2_ispug.png"
                dap "Тем  более если бы услашал мои стоны"
                m "Понятно"
                m "45 очков Слизерину!"
                $ slytherin += 45
                $ h_body = "dap/d2_smile2.png"
                dap "хм, Спасибо"
                jump public_completed2
            #    elif dcr == 2:
            #        $ h_body = "dap/d2_spwha.png"
            #        dap "Я...{w} выполнила ваше задание, сэр"
            #        m "я заметил"
            #        $ h_body = "dap/d2_spispug.png"
            #        dap "я пригласила на свидание одного парня из нашей команды, но он привел нескольких друзей"
            #        $ h_body = "dap/d2_spwha2.png"
            #        dap "они были не очень аккуратными"
            #        $ h_body = "dap/d2_spispug.png"
            #        dap "Блин придется всю одежду отстирывать, почему нам не выдают несколько комплектов этой формы?"
            #        m "..."

            #        m "45 очков Слизерину!"
            #        $ h_body = "dap/d2_spsmile2.png"
            #        dap "Ах да, очки"
            #        dap "Спасибо"
            #        jump public_completed2

label grud_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    $ daphne_publ_request = 0
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я сделала это, сэр"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":

            m "45 очков Слизерину!"
            $ slytherin += 45
            dap "Спасибо, сэр"
            jump public_completed2

        "Мне нужны детали":

            if tits_com == 0:
                m "Ты знаешь, как это делается, расскажи подробнее"
                $ h_body = "dap/d2_vizsod5.png"
                dap "Эм, ну я не смогла решиться явно намеренно показать кому-то свою грудь..."
                m "..."
                $ h_body = "dap/d2_smile2.png"
                dap "поэтому я просто \"случайно\" забыла закрепить шпильку на форме"
                g4 ".........{w} и?"
                $ h_body = "dap/d2_govor.png"
                dap "когда я делала один из элементов нашей программы с меня слетела рубашка"
                $ h_body = "dap/d2_smile2.png"
                g9 "круто"
                $ h_body = "dap/d2_smile5.png"
                dap "на какое-то время все видели мою грудь"
                $ h_body = "dap/d2_smile3.png"
                dap "и никто даже не смог подумать, что я это специально"
                g9 "она начинает делать успехи"
                $ h_body = "dap/d2_smile2.png"
                dap "мои очки?"
                $ tits_com = 1
                $ ponts = "45"
                jump public_completed2
            else:
                if tits_com == 1:
                    $ dcr = renpy.random.randint(1,1)
                elif tits_com > 1:
                    $ dcr = renpy.random.randint(1,4)

                if dcr == 1:
                    m "Как твои успехи?"
                    $ h_body = "dap/d2_smile2.png"
                    dap  "Вроде получилось"
                    g4 "Вроде?"
                    $ h_body = "dap/d2_wha.png"
                    dap "эм... ну..."
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "..."
                    $ h_body = "dap/d2_govor.png"
                    dap "Я выбрала момент, когда меня видел только один парень"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "Я быстро приподняла ливчик, чтобы он точно увидел..."
                    m "..."
                    m "что было дальше?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "Я так и не поняла заметил ли он, это длилось чуть больше секунды"
                    $ h_body = "dap/d2_ispug.png"
                    dap "Надо было получше подготовится, кто угодно мог заметить"
                    $ h_body = "dap/d2_plach.png"
                    $ tits_com += 1
                    dap "Я получу очки за это?"
                    menu:
                        "да":
                            m "45 очков Слизерину!"
                            $ slytherin += 45
                            $ h_body = "dap/d2_smile2.png"
                            dap "Спасибо, сэр"
                            jump public_completed2

                        "нет":
                            m "извини, но в этот раз ты плохо справилась"
                            $ h_body = "dap/d2_ispug.png"
                            dap "значит... все было зря..."
                            $ h_body = "dap/d2_left.png"
                            dap "черт"
                            jump public_completed2
                elif dcr == 2:
                    m "Ты знаешь, как это делается, расскажи подробнее"
                    $ h_body = "dap/d2_govor.png"
                    dap "Конечно, сэр"
                    $ h_body = "dap/d2_wha.png"
                    dap "Я попыталась сделать это именно так, как вы и говорили"
                    m "то есть?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Ну, во время игры я попыталась отвлечь одного из защитников"
                    $ h_body = "dap/d2_wha.png"
                    m  "...."

                    $ h_body = "dap/d2_govor.png"
                    dap "Когда команда атаковала, показала грудь и он пропустил гол"
                    $ h_body = "dap/d2_smile3.png"
                    dap "Я даже не думала, что это действительно сработает"
                    m "...."
                    m "Кто то еще это видел?"
                    $ h_body = "dap/d2_plach.png"
                    dap "Эм, не знаю сэр"
                    $ tits_com += 1
                    m "45 очков Слизерину!"
                    $ slytherin += 45
                    $ h_body = "dap/d2_smile2.png"
                    dap "Спасибо, сэр"
                    jump public_completed2
                elif dcr == 3:
                    m "Ты знаешь, как это делается, расскажи подробнее"
                    $ h_body = "dap/d2_smile2.png"
                    dap "Конечно, сэр"
                    $ h_body = "dap/d2_govor.png"
                    dap "В этот раз я постаралась сделать все правильно"
                    $ h_body = "dap/d2_smile2.png"
                    dap "Когда одна из команд забила гол..."
                    m "..."
                    $ h_body = "dap/d2_govor.png"
                    dap "Мы сделали наш обычный трюк, когда я встаю на верх пирамиды и говорю кричалку"
                    $ h_body = "dap/d2_smile2.png"
                    dap "Так вот, в момент когда я встала наверх пирамиды, я показала всей команде свою грудь"
                    $ h_body = "dap/d2_smile3.png"
                    dap "Это даже выглядело как элемент нашего танца"
                    g9 "круто"
                    $ h_body = "dap/d2_rightwha.png"
                    dap "Все видели мою голую грудь..."
                    $ h_body = "dap/d2_smile2.png"
                    dap "это было так воз..."
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "неловко, так что, вы дадите мне мои очки?!"
                    m "45 очков Слизерину!"
                    $ slytherin += 45
                    $ h_body = "dap/d2_smile2.png"
                    dap "Спасибо, сэр"
                    jump public_completed2
                elif dcr == 4:
                    m "Ты знаешь, как это делается, расскажи подробнее"
                    $ h_body = "dap/d2_wha.png"
                    dap "Конечно, сэр"
                    $ h_body = "dap/d2_smile2.png"
                    dap "В этот раз я решила, чтобы они сами все сделали"
                    m "то есть?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Душевые мальчиков и девочек разделяет всего одна стена"
                    $ h_body = "dap/d2_smile2.png"
                    m "интересно"
                    $ h_body = "dap/d2_wha.png"
                    dap "Да, интересно, как администрация смогла это допустить"
                    g4 "*эта сучка даже сейчас наезжает*"
                    m "а что на счет задания?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "так вот, мальчики наверное еще с допотопных времен проделали брешь в стене"
                    m "......"
                    g9 "шарят"
                    $ h_body = "dap/d2_govor.png"
                    dap "всегда эту брешь прикрывало защитное заклинание"
                    m "...."
                    $ h_body = "dap/d2_smile3.png"
                    dap "и я специально ослабила его"
                    $ h_body = "dap/d2_smile2.png"
                    dap "потом достаточно было всего лишь немного задержаться"
                    m "кто-то тебя ведел?"
                    $ h_body = "dap/d2_smile4.png"
                    $ tits_com += 1
                    dap "конечно"
                    $ h_body = "dap/d2_govor.png"
                    dap "я не знаю кто конкретно, но я отчетливо слышала чьи-то движения"
                    $ h_body = "dap/d2_rightwha.png"
                    dap "Интересно, он дрочил в это время?"
                    m "Вы проявили изобретательность, мисс Гринграсс"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    m "45 очков Слизерину!"
                    $ slytherin += 45
                    dap "Спасибо, сэр"
                    jump public_completed2

label mats_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    $ daphne_publ_request = 0
    show screen daphne_main
    with d3
    hide screen ctc
    $ ponts = "35"
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ slytherin += 35
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            if mats_com == 0:
                m "Ну что, ты выполнила задание?"
                dap "да, сэр"
                m "Давай, выкладывай подробности"
                $ h_body = "dap/d2_govor.png"
                dap "Ну, как вы и говорили, я подошла к одному парню из команды"
                $ h_body = "dap/d2_wha.png"
                m "..."
                $ h_body = "dap/d2_rightwha.png"
                dap "Это был тот парень, с которым у нас было свидание, так что все было не так сложно"
                $ h_body = "dap/d2_plach.png"
                dap "После тренировки мы остались в раздевалки и он... обнимал меня"
                m "....{w} чего?"
                $ h_body = "dap/d2_vizsod5.png"
                dap "Ну... хорошо, он откровенно лапал меня"
                g9 "...."
                m "Где?"
                $ h_body = "dap/d2_vizsod3.png"
                dap "..."
                $ h_body = "dap/d2_wha.png"
                dap "Везде"
                m "..."
                m "вы неплохо справились, мисс Гринграсс"
                m "35 очков слизерину!"
                $ slytherin += 35
                $ h_body = "dap/d2_smile2.png"
                dap "Спасибо"
                $ mats_com = 1
                jump public_completed2
            else:
                $ dcr = renpy.random.randint(1, 4)
                if dcr == 1:
                    m "Как прошло?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Я опять попробовала подойти к Драко..."
                    $ h_body = "dap/d2_wha.png"
                    m "и?"
                    $ h_body = "dap/d2_smile.png"
                    dap "в этот раз с ним все было нормально"
                    $ h_body = "dap/d2_rightwha.png"
                    dap "он как ни в чем не бывало просто сказал \"Привет\"!"
                    $ h_body = "dap/d2_wha2.png"
                    dap "После того, что он сделал! Пфф!"
                    m "........"
                    m "эм...."
                    m "напомни мне, а что такого он сделал?"
                    $ h_body = "dap/d2_zlo.png"
                    dap "как что?!"
                    $ h_body = "dap/d2_govor.png"
                    dap "Он сделал вид, что не заметил меня в прошлый раз"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "и ушел с какойто...."
                    $ h_body = "dap/d2_wha2.png"
                    dap "Когтерванкой!"
                    m "да уж....."
                    dap "Он тогда точно это сделал специально!"
                    m "*зевает*"
                    dap "Он ведь знает, что ее семья на 1 строчку опережает мою в рейтинге"
                    $ h_body = "dap/d2_right.png"
                    dap "Он специально сделал вид, что предпочел ее мне!"
                    m "*храпит*"
                    $ h_body = "dap/d2_wha.png"
                    dap "....."
                    dap "эм....."
                    $ h_body = "dap/d2_plach.png"
                    dap "профессор?"
                    g4 "а, что?"
                    m "....."
                    m "Так как твое задание?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "ах да...."
                    $ h_body = "dap/d2_govor.png"
                    dap "я подошла, когда он был один и сказала, что он может потрогать меня..."
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "было так неловко это произносить"
                    m "...."
                    m "и он?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "он не стал стесняться"
                    $ h_body = "dap/d2_plach.png"
                    dap "все продолжалось около двух минут, пока нам не помешали"
                    m "...."
                    $ h_body = "dap/d2_wha.png"
                    dap "так я получу очки?"
                    m "да"
                    m "35 очков Слизерину!"
                    $ slytherin += 35
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 2:
                    $ h_body = "dap/d2_plach.png"
                    dap "Эм..."
                    m "ну так, что ты сделала или нет?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "наверное..."
                    m "наверное?"
                    g4 "что это значит?"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "ну, я не смогла позволить себе унижаться и напрямую просить мальчиков трогать меня"
                    m "...."
                    $ h_body = "dap/d2_govor.png"
                    dap "но я попросила одного парня из Пуффендуя помочь нам с танцем"
                    $ h_body = "dap/d2_wha.png"
                    m "и?"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну.... я ведь сама его выдумала, в одном из движений он должен был держать меня за ноги и талию"
                    g4 "че?"
                    m "он сам понял, что трогает тебя?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "мне кажется, да"
                    m "кажется?"
                    $ h_body = "dap/d2_plach.png"
                    dap "ну, по крайней мере ему точно понравилось"
                    m "почему?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "он спросил можно ли перейти из команды в группу поддержки"
                    $ h_body = "dap/d2_smile5.png"
                    dap "и еще он думал, что успешно скрывает свой стояк"
                    m "...."

                    m "вы хорошо справились мисс Гринграс"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    m "Но в следующий раз такое не проканает"
                    $ h_body = "dap/d2_ispug.png"
                    dap "следующий раз??"
                    m "...."
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "...."
                    m "35 очков Слизерину"
                    jump public_completed2
                elif dcr == 3:
                    $ h_body = "dap/d2_rightwha.png"
                    dap "Сегодня перед тренировкой я поймала одного парня и сказала, что если он наберет больше всех очков, то я дам ему потрогать мою попу"
                    m "неплохо"
                    m "и что было дальше?"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну...."
                    $ h_body = "dap/d2_plach.png"
                    dap "у него ничего не получилось"
                    m "...."
                    $ h_body = "dap/d2_smile2.png"
                    dap "я уже думала, что задание провалено, но ко мне подошел другой парень...."
                    m "и что было дальше?"
                    $ h_body = "dap/d2_govor.png"
                    dap "он сказал, что это он набрал больше всех очков"
                    $ h_body = "dap/d2_wha.png"
                    m "вот как"
                    m "и что ты сделала?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "ну... я не хотела возвращаться с пустыми руками, поэтому мы отошли в укромное место и там все произошло"
                    m "...."
                    m "что произошло?"
                    $ h_body = "dap/d2_plach.png"
                    dap "эм...."
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "он трогал меня"
                    m "где он трогал вас?"
                    $ h_body = "dap/d2_ispug.png"
                    dap "......."
                    $ h_body = "dap/d2_left.png"
                    dap "*проклятый старик*"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "он трогал.....   под юбкой...."
                    m "...."
                    m "вы прекрасно справились мисс Гринграсс"
                    $ ponts = "35"
                    m "[ponts] очков Слизерину"
                    $ slytherin += 15
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 4:
                    $ h_body = "dap/d2_rightwha.png"
                    dap "Сегодня я попыталссь выцепить кого-то, но все уходили группами"
                    m "...."
                    m "то есть ты провалила задание?"
                    $ h_body = "dap/d2_wha.png"
                    dap "нет..."
                    m "а что тогда?"
                    $ h_body = "dap/d2_govor.png"
                    dap "ну, как я и говорила, я не смогла поймать кого-то одного...."

                    dap "поэтому мне пришлось подойти к нескольким парням, которые уже собирались уходить"
                    m "и что было дальше?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "Ну... сначала я просто немного мило поговорила с ними"
                    dap "я хотела, чтобы они сами все сделали, я ведь не проститутка"
                    m "совсем нет"
                    $ h_body = "dap/d2_smile3.png"
                    dap "они не заставили себя долго ждать"
                    $ h_body = "dap/d2_smile4.png"
                    dap "как только мы зашли в их комнату, они бросились на меня"
                    g9 "круто"
                    $ h_body = "dap/d2_plach.png"
                    dap "их руки были везде"
                    m "что было дальше?"
                    $ h_body = "dap/d2_govor.png"
                    dap "они продержали меня там пол часа и как то очень быстро все переменилось"
                    $ h_body = "dap/d2_wha.png"
                    m "в каком смысле?"
                    dap "я не знаю, но в какой то момент один резко потерял всякий интерес, потом другой, а затем последний"
                    m "....."
                    $ h_body = "dap/d2_smile4.png"
                    dap "мне кажется я знаю почему"
                    $ h_body = "dap/d2_smile3.png"
                    dap "вы думаете они успели кончить?"
                    m "почему нет?"
                    $ h_body = "dap/d2_smile4.png"
                    dap "....."
                    $ h_body = "dap/d2_smile2.png"
                    dap "наверное, мне просто хлюпики попались"
                    m "возможно"
                    $ h_body = "dap/d2_wha.png"
                    dap "так я получу свои очки?"
                    m "40 очков Слизерину"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    jump public_completed2

label fap_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    $ daphne_publ_request = 0
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ ponts = "50"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ slytherin += 45
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            if fap_com == 0:
                m "Как прошло?"
                $ h_body = "dap/d2_vizsod5.png"
                dap "Эм... ну, у меня не очень получилось..."
                g4 "как это?"
                $ h_body = "dap/d2_rightwha.png"
                dap "Ну... я позвала Драко, мы попытались уединится в одном из кабинетов"
                $ h_body = "dap/d2_vizsod3.png"
                dap "я уже залезла к нему в штаны, как..."
                m "....."
                g4  "что?"
                $ h_body = "dap/d2_smile4.png"
                dap "неважно, просто в этот раз не получилось"
                m "в таком случае я не могу дать тебе очков"
                $ h_body = "dap/d2_smile4.png"
                dap "я понимаю"
                $ fap_com = 1
                $ snape_fap = 1
                jump public_completed2
            else:
                $ dcr = renpy.random.randint(2,4)
                if dcr == 1:

                    g9 "......."
                    $ h_body = "dap/d2_govor.png"
                    dap "я....."
                    m "вероятно, все прошло более чем удачно?"
                    $ h_body = "dap/d2_spzlo.png"
                    dap "Удачно?{w} вы смеетесь?"
                    m "Ну... ты действительно выглядишь забавно"
                    $ h_body = "dap/d2_spright.png"
                    dap "Эти ублюдки совсем ничего не знают об этикете"
                    dap "я ведь просила сказать, когда...."
                    m "\"эти\"?{w} то есть ты перевыполнила план?"
                    $ h_body = "dap/d2_spwha.png"
                    dap "Эм... можно сказать и так"
                    $ h_body = "dap/d2_sprightwha.png"
                    dap "Это вышло случайно, я позвала одного парня, но с ним пришли еще двое"
                    $ h_body = "dap/d2_spzlo.png"
                    dap "я подумала, что ничего страшного, но они оказались такими противными"

                    dap "никогда больше не буду с ними"
                    m "Вы прекрасно справились, мисс Гринграсс"
                    m "45 очков Слизерину!"
                    $ slytherin += 45
                    dap "Спасибо"
                    jump public_completed2
                elif dcr == 2:

                    $ h_body = "dap/d2_govor.png"
                    dap "Ну... после тренировки я позвала одного из нападающих..."
                    dap "Мы уединились в одной из аудиторий"
                    $ h_body = "dap/d2_wha.png"
                    dap "Его хватило буквально на пол минуты, поэтому почти ничего не произошло"
                    $ h_body = "dap/d2_plach.png"
                    dap "эм...{w} я ведь все равно получу за это очки?"
                    m "конечно, ты хорошо справилась"
                    m "45 очков Слизерину!"
                    $ slytherin += 45
                    $ h_body = "dap/d2_smile2.png"
                    dap "Спасибо"
                    jump public_completed2
                elif dcr == 3:
                    $ h_body = "dap/d2_govor.png"
                    dap "В этот раз я постаралась, чтобы все прошло удачно"
                    $ h_body = "dap/d2_wha.png"
                    m ".........{w} и как?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "Нам никто не помешал"
                    m "твою мать, говори что было или не получишь никаких очков"
                    $ h_body = "dap/d2_wha.png"
                    dap "да, хорошо"
                    $ h_body = "dap/d2_smile2.png"
                    dap "я подошла к парню, с которым уже выполняла одно из заданий"
                    m "*хах... теперь это так называется?*"
                    $ h_body = "dap/d2_govor.png"
                    dap "мы прошли в отдельную комнату и я удостверилась, что все двери закрыты и нам никто не помешает"
                    $ h_body = "dap/d2_wha.png"
                    m "......"
                    m "так что было дальше?"
                    $ h_body = "dap/d2_plach.png"
                    dap "ну.... как вы и просили, я сделала это"
                    m "что \"это\"?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "....."
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "я передернула ему"
                    $ h_body = "dap/d2_vizsod5.png"
                    m "он кончил?"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "ну.....{w} да"
                    m "что значит ну? ты не уверена?"
                    $ h_body = "dap/d2_plach.png"
                    dap "у меня никак не получалось и ему пришлось немного помочь мне"
                    m "......."
                    m "ничего страшного"
                    m "вы прекрасно справились, мисс Гринграсс"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 4:
                    $ h_body = "dap/d2_smile2.png"
                    dap "На самом деле все получилось само собой"
                    m "а подробнее?"
                    $ h_body = "dap/d2_govor.png"
                    dap "Ну, одного из защитников сбили и он упал прямо на землю"
                    $ h_body = "dap/d2_smile2.png"
                    m "*зевает* очень интересно"
                    $ h_body = "dap/d2_smile3.png"
                    dap "ну, я вызвалась довести его до медпункта"
                    m "...."
                    $ h_body = "dap/d2_govor.png"
                    dap "этого нового врача почему то не было на месте.... в общем там все и случилось"
                    m "что случилось?"
                    $ h_body = "dap/d2_plach.png"
                    dap "...."
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "я..."
                    m "что?"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "я передернула ему"
                    m "отлично"
                    m "в этот раз получилось сделать так, чтобы он кончил?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "да.... {w}в этот раз у меня получилось"
                    m "вы хорошо справились, мисс гринграсс"
                    m "[ponts] очков Слизерину"
                    dap "спасибо"
                    jump public_completed2


label minet_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    $ daphne_publ_request = 0
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ h_body = "dap/d2_wha.png"
    $ ponts = "60"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ slytherin += 55
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            if minet_com == 0:
                m "давай выкладывай"
                $ h_body = "dap/d2_plach.png"
                dap "ну..... эм...."
                m "что?"
                $ h_body = "dap/d2_rightwha.png"
                dap "Сегодня я сделала минет одному парню из команды..."
                m "......"
                m "что это был за парень?"
                $ h_body = "dap/d2_govor.png"
                dap "это был нападающий из Слизерина"
                $ h_body = "dap/d2_wha.png"
                m "........"
                $ h_body = "dap/d2_vizsod3.png"
                dap "............"
                m "и как прошло?"
                $ h_body = "dap/d2_ispug.png"
                dap "......."
                $ h_body = "dap/d2_plach.png"
                dap "ну..."
                $ h_body = "dap/d2_vizsod5.png"
                dap "это был мой первый минет"

                dap "и...."
                $ h_body = "dap/d2_vizsod3.png"
                dap "мне кажется, что я уже перешла грань"
                m "что?"
                $ h_body = "dap/d2_smile4.png"
                dap "можно мне просто мои очки и я уйду отсюда???"
                $ minet_com = 1
                menu:
                    "хорошо":
                        m "Ладно, ты хорошо потрудилась"
                        m "55 очков Слизерину"
                        $ slytherin += 55
                        $ h_body = "dap/d2_vizsod5.png"
                        dap "..."
                        dap "....."
                        jump public_completed2
                        # убегает

                    "нет, расскажи подробнее":
                        $ h_body = "dap/d2_ispug.png"
                        dap "Подробнее???"
                        $ h_body = "dap/d2_zlo.png"
                        dap "что еще можно сказать?!"
                        $ h_body = "dap/d2_smile4.png"
                        dap "я, Дафна Гринграсс сегодня отсосала какому-то парню, которого видела пару раз за все время"
                        $ h_body = "dap/d2_plach.png"
                        dap "что вы еще хотите услышать?!!"
                        m "...."
                        m "55 очков Слизерину"
                        $ h_body = "dap/d2_vizsod3.png"
                        dap "....."

                        # убегат
                        jump public_completed2
            else:
                $ dcr = renpy.random.randint(1,4)
                if dcr == 1:
                    m "мне нужны детали"
                    $ h_body = "dap/d2_plach.png"
                    dap "ну...."
                    $ h_body = "dap/d2_rightwha.png"
                    dap "Я не хотела, чтобы кто-то узнал о том, что мне придется сделать"
                    $ h_body = "dap/d2_wha.png"
                    dap "поэтому я подошла к парню, с которым никто не общается"
                    $ h_body = "dap/d2_smile2.png"
                    dap "даже если он попробует кому-то расскзаать, ему никто не поверит"
                    m "*зевает*"
                    m "так было что-нибудь или нет??"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "...."
                    $ h_body = "dap/d2_govor.png"
                    dap "да, я отвела его в один из кабинетов и..."
                    $ h_body = "dap/d2_wha.png"
                    m "что?"
                    $ h_body = "dap/d2_plach.png"
                    dap "..."
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "я отсосала ему"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "...."

                    m "....."
                    m "ему понравилось?"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну.... если можно так сказать"
                    $ h_body = "dap/d2_plach.png"
                    dap "его хватило буквально на несколько секунд"
                    dap "после этого он извинился и убежал"
                    m "понятно"
                    $ h_body = "dap/d2_plach.png"
                    dap "....."
                    $ h_body = "dap/d2_wha.png"
                    dap "я получу свои очки?"
                    m "55 очков Слизерину"
                    $ slytherin += 55
                    dap "....."
                    jump public_completed2
                elif dcr == 2:
                    m "что нового?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "я еще раз сделала это"
                    m "ты знаешь как это работает, мне нужны детали"
                    $ h_body = "dap/d2_plach.png"
                    dap "....."
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "почему даже после того что я сделала вы заставляете меня еще и говорить о таких вещах?"
                    m "хм, ты можешь не говорить"
                    $ h_body = "dap/d2_plach.png"
                    dap "..."
                    m "но в таком случае ты не получишь очков"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "........"
                    $ h_body = "dap/d2_wha.png"
                    dap "я сделала это одному из запасных"
                    m "......"
                    $ h_body = "dap/d2_govor.png"
                    dap "тренировка команды задержалась, поэтому я не хотела терять время"
                    $ h_body = "dap/d2_wha.png"
                    dap "пока команда была в воздухе, я...."
                    $ h_body = "dap/d2_plach.png"
                    dap "....."
                    m "ты.... что?"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "....."
                    $ h_body = "dap/d2_ispug.png"
                    dap "вы обязательно хотите, чтобы я произносила это?"
                    m "......"
                    $ h_body = "dap/d2_plach.png"
                    dap "......"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну хорошо"
                    $ h_body = "dap/d2_govor.png"
                    dap "пока вся команда была в воздухе я....."
                    $ h_body = "dap/d2_smile4.png"
                    dap "я сделала минет одному из запасных, который сидел на трибунах"
                    m "...."
                    m "ты делала это прямо на трибунах? Вас кто-то видел?"
                    $ h_body = "dap/d2_govor.png"
                    dap "нет, мы спустились за них"
                    $ h_body = "dap/d2_wha.png"
                    dap "нас никто не видел"
                    m "*жаль*"
                    g9 "*было бы прикольно*"
                    m "55 очков Слизерину"
                    $ h_body = "dap/d2_smile2.png"
                    dap "....."
                    jump public_completed2
                elif dcr == 3:
                    m "ну как?"
                    $ h_body = "dap/d2_wtf.png"
                    dap "Эти ублюдки меня изнасиловали!"
                    m "что?"
                    $ h_body = "dap/d2_wha2.png"
                    dap "они изнасиловали меня!"
                    m "но ты же сама должна была их изнасиловать...."
                    $ h_body = "dap/d2_zlo.png"
                    dap "как вы можете!!!"
                    dap "я как и в прошлый раз договорилась с ними"
                    dap "но в этот раз похоже, что они сговорились"
                    m "что?"
                    $ h_body = "dap/d2_wha2.png"
                    dap "все 3 нападающих набрали одинаковое количество очков"
                    m "возможно это была случайность"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "а после тренировки они начали требовать обещанное"
                    m "...."
                    $ h_body = "dap/d2_wtf.png"
                    dap "они не отпускали меня, пока каждый из них не кончил мне на лицо"
                    m "......"
                    $ h_body = "dap/d2_zlo.png"
                    dap "я просила их не делать этого, но они просто смеялись и в конце концов я час отмывала одежду"
                    dap "ублюдки"
                    dap "когда я закончу год первой в рейтинге студентов, я упрошу мамочку отправить каждого из них в азкабан"
                    dap "на 3.... нет, на 8 лет!"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "....."
                    m "ты отлично справилась"
                    m "55 очков Слизерину"
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 4:
                    m "похоже, что у тебя получилось"
                    $ h_body = "dap/d2_wha.png"
                    dap "эм.... что?"

                    dap "откуда вы знаете?"
                    $ h_body = "dap/d2_ispug.png"
                    dap "блииин, я что проходила с этим несколько часов???"
                    dap "черт, надеюсь никто не заметил"
                    g9 "*ага, точно не заметили*"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "черт"
                    ">Дафна быстро вытирает сперму с одежды"
                    m "Ну так что? я хочу знать подробности"
                    $ h_body = "dap/d2_wha.png"
                    dap "Эм, ну..... ничего необычного"
                    $ h_body = "dap/d2_govor.png"
                    dap "Я подошла отдельно каждому нападающему и пообещала шикарный минет если они забьют больше всего мячей"
                    $ h_body = "dap/d2_smile3.png"
                    dap "В итоге все 3 нападающих летели как угорелые и мы выиграли с разгромным счетом"
                    m "....."
                    m "изобретательно"
                    m "а что на счет нападающего?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "эм, ну как я и обещала, я сделала ему добротный минет"
                    $ h_body = "dap/d2_plach.png"
                    dap "я постаралась все проглотить, чтобы не пачкать одежду, но не получилось"
                    m "....."
                    m "ничего страшного"
                    m "55 очков Слизерину"
                    $ slytherin += 55
                    dap "спасибо"
                    jump public_completed2

label fuck_completed:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    $ daphne_publ_request = 0
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ ponts = "70"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ slytherin += 60
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            if fuck_com == 0:
                $ h_body = "dap/d2_plach.png"
                dap "ну...."

                m "что ну?"
                $ h_body = "dap/d2_rightwha.png"
                dap "вообще-то я сделала это, но"
                m "......"
                m "что?"
                $ h_body = "dap/d2_ispug.png"
                dap "на самом деле я не уверена...."
                m "что значит не уверена??"
                $ h_body = "dap/d2_wha.png"
                dap "я нашла, парня, который точно никому бы не рассказал..."
                m "и?"
                $ h_body = "dap/d2_vizsod5.png"
                dap "ну...."
                $ h_body = "dap/d2_vizsod3.png"
                dap "у него оказался такой маленький"
                m "..."
                $ h_body = "dap/d2_plach.png"
                dap "я встала в удобную позу, почувствовала, что он шевелится, но...."
                $ h_body = "dap/d2_plach.png"
                dap "он ерзал примерно с минуту, потом одел штаны и ушел"
                dap "я даже не поняла, что это было"
                $ h_body = "dap/d2_wha.png"
                dap "у меня даже не оставалось времени, поэтому я пришла сюда"
                m "понятно"
                m "такое бывает"
                $ h_body = "dap/d2_plach.png"
                dap "эм..."
                dap "я ведь получу за это очки?"
                m "конечно, ты не виновата"
                m "60 очков Слизерину"
                $ slytherin += 60
                $ h_body = "dap/d2_smile2.png"
                dap "спасибо"
                $ fuck_com = 1
                jump public_completed2
            else:
                $ dcr = renpy.random.randint(1,5)
                if dcr == 1:
                    m "ты сделала, что должна была, девочка?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "ох еще бы"
                    m "......"
                    m "что случилось?"
                    $ h_body = "dap/d2_wha2.png"
                    dap "Все мужчины - ублюдки"
                    m "эм......"
                    $ h_body = "dap/d2_left.png"
                    dap "Ненавижу"
                    m "Не стоит так резко"
                    $ h_body = "dap/d2_wha2.png"
                    dap "всем плевать на все"
                    m "может все таки расскажешь, что произошло?"
                    $ h_body = "dap/d2_left.png"
                    dap "этот ублюдок"
                    m "кто?"
                    $ h_body = "dap/d2_wha.png"
                    dap "эм..."
                    $ h_body = "dap/d2_plach.png"
                    dap "я не знаю как его зовут, какой то парень из пуффендуя"
                    m "что он сделал?"
                    $ h_body = "dap/d2_wha2.png"
                    dap "он кончил!"
                    m "......"
                    m "такое иногда случается, когда парень трахает тебя, это нормально"
                    dap "старый извращенец, разве не понятно??"
                    m "....."
                    $ h_body = "dap/d2_zlo.png"
                    dap "он сделал это в меня!!"
                    m "....."
                    $ h_body = "dap/d2_right.png"
                    dap "Ублюдок ничего не знает о порядочности, морали и..."
                    m "...."
                    $ h_body = "dap/d2_wha2.png"
                    dap "он козел!!!"
                    m "так вы...."
                    g4 "*черт, нужно было очернить ее, а не делать беременной*"
                    $ h_body = "dap/d2_left.png"
                    dap "теперь мне придется пить защитное зелье, а от него потом 3 дня все болит!!!"
                    m "*хах, вот как*"
                    m "ну....."
                    m "я думаю 60 баллов немного скрасят твои страдания?"
                    $ h_body = "dap/d2_smile3.png"
                    dap "ох, еще бы"
                    m "60 очков Слизерину"
                    dap "спасибо"
                    $ slytherin += 60
                    jump public_completed2
                elif dcr == 2:
                    m "................."
                    m "что это с тобой?"
                    dap "я встретила...."
                    m "кого?"
                    dap "ЕГО"
                    g4 "ЧТо, черт побери, это что опять он?"
                    dap "мне кажется..... это был профессор Снейп"
                    m "Снейп?"
                    dap "я хотела сбежать от него и пойти выполнить ваше задание..."
                    dap "но он окликнул меня и сказал, что знает все о нас с вами"
                    dap "и требует платы за молчание....."
                    m "....."
                    dap "после этого он отвел меня в помещение и 3 часа трахал своим огромным членом"
                    dap "ме кажется.... я не смогу нормально ходить ближайшие 2 недели"
                    m "........."
                    m "хм"
                    g4 "а у него не было..... эм..... красных ушей?"
                    dap "...... он, просил передать вам, что......"
                    m "что?"
                    dap "......."
                    dap "........"
                    g4 "что же с ним делать"
                    jump public_completed2
                elif dcr == 3:
                    m "тебе есть что рассказать?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "да..."
                    $ h_body = "dap/d2_rightwha.png"
                    dap "я сделала это с одним из защитников"
                    m "....."
                    $ h_body = "dap/d2_smile2.png"
                    dap "я сказала одному из них, что если он не пропустит ни одного мяча в наши ворота, то его ждет награда"
                    $ h_body = "dap/d2_smile4.png"
                    dap "как думаете, какой был счет?"
                    m "........."
                    $ h_body = "dap/d2_smile3.png"
                    dap "120 - 0 !"
                    $ h_body = "dap/d2_smile3.png"
                    dap "сначала я не думала, что все что я делаю, может дать такой результат"
                    dap "мужчинами так легко управлять"
                    g4 "эээ..."
                    $ h_body = "dap/d2_rightwha.png"
                    dap "*интересно, как далеко они могут зайти*"
                    m "довольно"
                    $ h_body = "dap/d2_wha.png"
                    dap "???"
                    m "ты хорошо справилась"
                    m "60 очков Слизерину"

                    dap "..."
                    g4 "я не планировал делать из нее такую стерву"
                    m "хотя если вспомнить, что ее ждет...."
                    g9 "так будет даже приятнее"
                    jump public_completed2
                elif dcr == 4:
                    $ h_body = "dap/d2_smile4.png"
                    dap "я слегка перевыполнила план"
                    m "что?"
                    $ h_body = "dap/d2_smile2.png"
                    dap "ну..."
                    $ h_body = "dap/d2_govor.png"
                    dap "у меня не получилось выцепить кого-то одного"
                    $ h_body = "dap/d2_wha.png"
                    dap "я, как обычно, пообещала одному парню награду, но он не справился"
                    $ h_body = "dap/d2_smile4.png"
                    dap "поэтому мне пришлось импровизировать"
                    m "........"
                    m "импровизировать?"
                    $ h_body = "dap/d2_wha.png"
                    dap "ну..... типо того"
                    $ h_body = "dap/d2_smile2.png"
                    dap "я подошла к нападающему, который набрал больше всех очков и сделала недвусмысленный намек"
                    m "....."
                    $ h_body = "dap/d2_govor.png"
                    dap "он сразу все понял и мы пошли к нему в комнату"
                    $ h_body = "dap/d2_plach.png"
                    dap "когда все началось, внезапно пришли его друзья"
                    m "....."
                    $ h_body = "dap/d2_smile4.png"
                    dap "......"
                    m "......"
                    m "60 очков Слизерину"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    jump public_completed2
                elif dcr == 5:
                    m "Как прошло?"
                    $ h_body = "dap/d2_plach.png"
                    dap "Ну... эм... я сделала это"
                    g4 "что значит, я сделала это?"
                    $ h_body = "dap/d2_wha.png"
                    dap "После тренировки я взяла Драко за руку и повела его в раздевалку"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "мы подождали, когда все уйдут и там сделали это"
                    m "вы отлично справились мисс Гринграсс"
                    $ h_body = "dap/d2_smile2.png"
                    dap "спасибо"
                    m "55 очков Слизерину!"
                    $ slytherin += 55
                    dap "я могу идти?"
                    m "да"
                    dap "хихик"
                    jump public_completed2



















label flirt_complete1:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    $ h_body = "dap/d2_govor.png"
    dap "Я выполнила ваше задание"
    $ h_body = "dap/d2_wha.png"
    menu:
        "Отлично, вот твои очки":
            m "[ponts] очков Слизерину!"
            $ slytherin += 15
            dap "хм, Спасибо"
            jump public_completed2


        "Мне нужны подробности":
            g4 "Что значит выполнила, расскажи подробнее"
            $ h_body = "dap/d2_visod2.png"
            dap "Эм... ну, как вы и просили..."
            $ h_body = "dap/d2_govor.png"
            dap "Когда тренировка закончилась, я подождала, пока все выйдут из раздевалки"
            $ h_body = "dap/d2_wha.png"
            m "и?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "Я дождалась, когда будет выходить драко и..."
            m "..."
            m "И?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "Эм, ну мы поговорили"
            g4 "Что? Поговорили?"
            $ h_body = "dap/d2_vizsod3.png"
            dap "...."
            m "так что было?"

            dap "Ну..."
            $ h_body = "dap/d2_plach.png"
            dap "Я сказала, что он хорошо играет"
            m ".................."
            g4 "Мне кажется ты не очень хорошо поняла слово \"флирт\""
            $ h_body = "dap/d2_govor.png"
            dap "Это не все"
            $ h_body = "dap/d2_wha.png"
            m "Что было дальше?"
            $ h_body = "dap/d2_plach.png"
            dap "ну"
            $ h_body = "dap/d2_vizsod5.png"
            dap "я....{w} вроде как несколько раз коснулась его своими бедрами"
            m "...........{w}..............."
            m "*не густо, но для начала сгодится*"
            $ h_body = "dap/d2_plach.png"
            dap "Я сделала все что могла"
            m "[ponts] очков Слизерину"
            $ slytherin += 15
            $ h_body = "dap/d2_wha.png"
            dap "...."
            $ h_body = "dap/d2_smile2.png"
            dap " Спасибо"
            jump public_completed2

        "Мне нужны подробности":
            $ h_body = "dap/d2_vizsod5.png"
            dap "У меня был очень ограниченный выбор"
            m "...."
            $ h_body = "dap/d2_right.png"
            dap "не понимаю, почему в команде так мало парней из слизерина?"
            $ h_body = "dap/d2_wha2.png"
            dap "это все тренер виноват, он просто завидует и набирает таких же безродных как он сам"
            g4 "*что она несет*"
            $ h_body = "dap/d2_rightwha.png"
            dap "если бы я отбирала игроков, я бы вообще...."
            $ h_body = "dap/d2_wha.png"
            g4 "может перейдем к твоему заданию?"
            $ h_body = "dap/d2_govor.png"
            dap "ах, да"
            $ h_body = "dap/d2_wha.png"
            pause 1.0
            $ h_body = "dap/d2_govor.png"
            dap "как я и говорила, мне пришлось выбирать всего из пары человек"
            $ h_body = "dap/d2_wha.png"
            m "............"
            $ h_body = "dap/d2_smile3.png"
            dap "я ведь не могла флиртовать с каким-нибудь нищебродом, хуже могут быть только полукровки"
            m "..................."
            g4 "Так что было дальше?"
            $ h_body = "dap/d2_govor.png"
            dap "Я подошла к одному из \"Слизеринских\" парней...."
            $ h_body = "dap/d2_wha.png"
            m "и?"
            $ h_body = "dap/d2_govor.png"
            dap "Я сказала ему \"эй, я видела твою семью в вестнике магической аристократии\""
            $ h_body = "dap/d2_wha.png"
            m "........."
            m "............."
            $ h_body = "dap/d2_smile5.png"
            dap "........."
            m "эм"
            dap "я сделала это"
            g4 "Ты точно правильно расслышала, что я просил тебя сделать?"
            $ h_body = "dap/d2_plach.png"
            dap  "....."
            $ h_body = "dap/d2_govor.png"
            dap "Вы просили пофлиртовать с кем-то из команды"
            $ h_body = "dap/d2_wha.png"
            m "при чем тут какой то там вестник"
            $ h_body = "dap/d2_wha2.png"
            dap "как причем?!"
            $ h_body = "dap/d2_smile3.png"
            dap "Я же вспомнила, что это его семья, то есть я помню его фамилию!"
            $ h_body = "dap/d2_wha.png"
            dap "Он не мог не оценить оказанного ему внимания!!!"
            m "............................."
            m "не уверен, что это именно то, о чем мы с тобой договаривались"
            $ h_body = "dap/d2_ispug.png"
            dap "....."
            $ h_body = "dap/d2_plach.png"
            dap "но я ведь получу очки?"
            m "....."
            menu:
                "да":
                    m "[ponts] очков Слизерину"
                    dap "спасибо"
                    jump public_completed2

                "нет":
                    jump public_completed2


        "Мне нужны подробности":
            $ h_body = "dap/d2_ispug.png"
            dap "эм, сегодня все прошло так странно"
            m "почему?"
            $ h_body = "dap/d2_wha.png"
            dap "я потратила на ваше задание весь вечер"
            m "что ты делала?"
            $ h_body = "dap/d2_plach.png"
            dap "У меня никак не получалось свести разговор к флирту"
            m "...."
            $ h_body = "dap/d2_govor.png"
            dap "Сначала я подошла к одному парню... он из достаточно высокого рода"
            $ h_body = "dap/d2_plach.png"
            dap "почему-то он не очень приветливо воспринял мои попытки к общению..."
            m "да ладно?"
            m "что ты ему сказала?"
            $ h_body = "dap/d2_wha.png"
            dap "Ну как обычно, спросила что он тут шляется"
            m "....."
            g4 "че?"
            m "Тебе еще никто не говорил, что это не самый лучший способ начать разговор?"
            $ h_body = "dap/d2_plach.png"
            dap "ну...."
            $ h_body = "dap/d2_govor.png"
            dap "Я подошла к другому парню, тоже из Слизерина"
            $ h_body = "dap/d2_wha.png"
            dap "я постаралась быть максимально милой и даже встала в достаточно открытую позу"
            m "что было дальше?"
            $ h_body = "dap/d2_plach.png"
            dap "он сказал, что спешит к своему другу"
            m "....."
            m "наверное, он просто больше любит \"друзей\" нежели девочек"
            $ h_body = "dap/d2_smile3.png"
            dap "хм, а это интересно, можно слить эту информацию в газеты и его семья не будет больше зазнаваться, что они на 2 места в рейтинге выше нас"
            g4 "........{w} че?"
            m "давайте вернемся к заданию"
            $ h_body = "dap/d2_wha.png"
            dap "ну..... дальше я хотела опять подойти к Драко, но мне кажется он был не в себе"
            m "то есть?"
            $ h_body = "dap/d2_ispug.png"
            dap "почему то он сделал вид, что не знает меня..."
            $ h_body = "dap/d2_wha2.png"
            dap "пока я пыталась отчитать его, он дождался когда придет Чжо Чанг и ушел прямо с ней"
            $ h_body = "dap/d2_left.png"
            dap "Козел"
            m "....."
            g4 "Чо Чанг?!"
            $ h_body = "dap/d2_plach.png"
            dap "эм.... да"
            g4 "вот красный ублюдок"
            $ h_body = "dap/d2_wha.png"
            dap "Эм... вообще то он тоже из слизерина, если уж на то пошло, то он зеленый"
            m "...."
            m "вернемся к заданию"
            $ h_body = "dap/d2_govor.png"
            dap "Ну, больше игроков из слизерина не осталось, поэтому я нашла парня из когтервана"
            $ h_body = "dap/d2_wha.png"
            m "и?"
            $ h_body = "dap/d2_smile2.png"
            dap "я постаралась быть максимально милой и.... он ответил тем же"
            m "....."
            m "а точнее?"
            $ h_body = "dap/d2_smile5.png"
            dap "он пригласил меня на свидание"
            $ h_body = "dap/d2_smile2.png"
            dap "первый раз меня кто-то пригласил на свидание"
            m "..."
            m "ты согласилась?"
            $ h_body = "dap/d2_plach.png"
            dap "что? конечно же нет! его семья всего лишь 23 в рейтинге, пфф"
            $ h_body = "dap/d2_wha.png"
            m "понятно, мисс Гринграсс"
            m "15 очков Слизерину"
            $ slytherin += 15
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            jump public_completed2

        "Мне нужны подробности":
            m "Расскажи подробнее"
            $ h_body = "dap/d2_wha.png"
            dap "да"
            $ h_body = "dap/d2_govor.png"
            dap "В этот раз я не стала выцеплять кого-то конкретного"
            $ h_body = "dap/d2_wha.png"
            m "да?"
            m "и что же ты сделала?"
            $ h_body = "dap/d2_govor.png"
            dap "Пока тренировалась команда по квидичу, мы с девочками тоже отрабатывали внизу"
            $ h_body = "dap/d2_wha.png"
            g4 "че делали?"
            $ h_body = "dap/d2_plach.png"
            dap "Эм..."
            $ h_body = "dap/d2_govor.png"
            dap "Отрабатвали кричалки...."
            $ h_body = "dap/d2_zlo.png"
            dap "Это не просто знаете ли, всем вместе кричать одно и тоже"
            $ h_body = "dap/d2_wha.png"
            m "...."
            m "так что там было?"
            $ h_body = "dap/d2_govor.png"
            dap "После того как мы отработали всю программу..."
            $ h_body = "dap/d2_smile2.png"
            dap "я немного изменила ее и вся команда слышала, что в случае победы в чемпионате, девочки подбодрят игроков другим способом"
            m "ого"
            g9 "*она начинает учиться*"
            $ h_body = "dap/d2_left.png"
            dap "Жаль только потом тренер выгнал нас с поля"
            m "..."
            $ h_body = "dap/d2_wha2.png"
            dap "Какое право он вообще имеет на такое?!"

            dap "Вы же директор, вы накажете его за это?"
            m "ВЫ отлично справились мисс Гринграсс"
            $ h_body = "dap/d2_wha.png"
            dap "......."
            dap "*это значит \"Нет?\" *"
            m "...."
            $ h_body = "dap/d2_plach.png"
            dap "Я получу свои очки?"
            m "30 очков Слизерину"
            $ h_body = "dap/d2_smile2.png"
            dap "Спасибо"
            jump public_completed2


label date_complete1:
    m "..."
    dap "Я сделала это"
    menu:
        "Отлично, вот твои очки":
            m "45 очков Слизерину!"
            $ slytherin += 45
            dap "хм, Спасибо"
            jump public_completed2

        "Мне нужны подробности":
            m "Как прошло ваше свидание?"
            $ h_body = "dap/d2_plach.png"
            dap "Эм... ну..."
            $ h_body = "dap/d2_wha.png"
            dap "А как может пройти свидание в замке..."
            $ h_body = "dap/d2_govor.png"
            dap "Мы немного побродили рядом с лесом"
            $ h_body = "dap/d2_wha.png"
            m "а дальше?"
            $ h_body = "dap/d2_govor.png"
            dap "посидели у озера"
            $ h_body = "dap/d2_wha.png"
            m "....{w} а дальше?"
            $ h_body = "dap/d2_plach.png"
            dap "эм.... что дальше?"
            $ h_body = "dap/d2_wha.png"
            g4 "Вы что не..."
            $ h_body = "dap/d2_wha2.png"
            dap "Нет, мы не целовались"
            g4 "*Да при чем тут...*"
            $ h_body = "dap/d2_smile3.png"
            dap "Гринграсс никогда не целуются на первом свидании"
            m "...... да уж{w}, повезло мужским особям Гранграсс"
            $ h_body = "dap/d2_wha.png"
            dap "вы обещали мне очки"
            m "да"
            m "45 очков Слизерину!"
            $ slytherin += 45
            $ h_body = "dap/d2_smile2.png"
            dap "хм, Спасибо"
            jump public_completed2

        "Мне нужны подробности":
            m "Как прошло ваше свидание?"
            $ h_body = "dap/d2_govor.png"
            dap "Я назначила свидание нашему нападающему"
            $ h_body = "dap/d2_wha2.png"
            dap "Так этот придурок потащил меня в лес"
            m "Что вы там делали?"
            $ h_body = "dap/d2_rightwha.png"
            dap "Самое идиотское место, какое только можно придумать"
            m "Почему?"
            $ h_body = "dap/d2_wha.png"
            dap "Мне пришлось постоянно оглядываться, с любой стороны на нас мог смотреть кто угодно"
            $ h_body = "dap/d2_ispug.png"
            dap "Тем  более если бы услашал мои стоны"
            m "Понятно"
            m "45 очков Слизерину!"
            $ slytherin += 45
            $ h_body = "dap/d2_smile2.png"
            dap "хм, Спасибо"
            jump public_completed2

        "Черт подери, что с тобой?":
            $ h_body = "dap/d2_wha.png"
            dap "Я...{w} выполнила ваше задание, сэр"
            m "я заметил"
            $ h_body = "dap/d2_govor.png"
            dap "я пригласила на свидание одного парня из нашей команды, но он привел нескольких друзей"
            $ h_body = "dap/d2_wha2.png"
            dap "они были не очень аккуратными"
            $ h_body = "dap/d2_ispug.png"
            dap "Блин придется всю одежду отстирывать, почему нам не выдают несколько комплектов этой формы?"
            m "..."
            m "45 очков Слизерину!"
            $ slytherin += 45
            $ h_body = "dap/d2_smile2.png"
            dap "Ах да, очки"
            dap "Спасибо"
            jump public_completed2


label kiss_complete:
    jump public_completed

label grud_complete1:
    $ dcr = renpy.random.randint(1,1)
    if dcr == 1:
        dap "Я сделала это, сэр"
        menu:
            "Отлично, вот твои очки":

                m "45 очков Слизерину!"
                $ slytherin += 45
                dap "Спасибо, сэр"
                jump public_completed2

            "Мне нужны детали":

                menu:
                    "1":

                        m "Ты знаешь, как это делается, расскажи подробнее"
                        $ h_body = "dap/d2_vizsod5.png"
                        dap "Эм, ну я не смогла решиться явно намеренно показать кому-то свою грудь..."
                        m "..."
                        $ h_body = "dap/d2_smile2.png"
                        dap "поэтому я просто \"случайно\" забыла закрепить шпильку на форме"
                        g4 ".........{w} и?"
                        $ h_body = "dap/d2_govor.png"
                        dap "когда я делала один из элементов нашей программы с меня слетела рубашка"
                        $ h_body = "dap/d2_smile2.png"
                        g9 "круто"
                        $ h_body = "dap/d2_smile5.png"
                        dap "на какое-то время все видели мою грудь"
                        $ h_body = "dap/d2_smile3.png"
                        dap "и никто даже не смог подумать, что я это специально"
                        g9 "она начинает делать успехи"
                        $ h_body = "dap/d2_smile2.png"
                        dap "мои очки?"
                        m "45 очков Слизерину!"
                        $ h_body = "dap/d2_smile5.png"
                        dap "Спасибо, сэр"
                        jump public_completed
                    "2":


    # вечером
                        m "Как твои успехи?"
                        $ h_body = "dap/d2_smile2.png"
                        dap  "Вроде получилось"
                        g4 "Вроде?"
                        $ h_body = "dap/d2_wha.png"
                        dap "эм... ну..."
                        $ h_body = "dap/d2_vizsod5.png"
                        dap "..."
                        $ h_body = "dap/d2_govor.png"
                        dap "Я выбрала момент, когда меня видел только один парень"
                        $ h_body = "dap/d2_vizsod5.png"
                        dap "Я быстро приподняла ливчик, чтобы он точно увидел..."
                        m "..."
                        m "что было дальше?"
                        $ h_body = "dap/d2_vizsod5.png"
                        dap "Я так и не поняла заметил ли он, это длилось чуть больше секунды"
                        $ h_body = "dap/d2_ispug.png"
                        dap "Надо было получше подготовится, кто угодно мог заметить"
                        $ h_body = "dap/d2_plach.png"
                        dap "Я получу очки за это?"
                        menu:
                            "да":
                                m "45 очков Слизерину!"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Спасибо, сэр"
                                jump public_completed

                            "нет":
                                m "извини, но в этот раз ты плохо справилась"
                                $ h_body = "dap/d2_ispug.png"
                                dap "значит... все было зря..."
                                $ h_body = "dap/d2_left.png"
                                dap "черт"
                                jump public_completed

                    "3":
                        dap "Я сделала это, сэр"
                        menu:
                            "Отлично, вот твои очки":
                                m "45 очков Слизерину!"
                                dap "Спасибо, сэр"
                                jump public_completed

                            "Мне нужны детали":
                                m "Ты знаешь, как это делается, расскажи подробнее"
                                $ h_body = "dap/d2_govor.png"
                                dap "Конечно, сэр"
                                $ h_body = "dap/d2_wha.png"
                                dap "Я попыталась сделать это именно так, как вы и говорили"
                                m "то есть?"
                                $ h_body = "dap/d2_govor.png"
                                dap "Ну, во время игры я попыталась отвлечь одного из защитников"
                                $ h_body = "dap/d2_wha.png"
                                m  "...."

                                $ h_body = "dap/d2_govor.png"
                                dap "Когда команда атаковала, показала грудь и он пропустил гол"
                                $ h_body = "dap/d2_smile3.png"
                                dap "Я даже не думала, что это действительно сработает"
                                m "...."
                                m "Кто то еще это видел?"
                                $ h_body = "dap/d2_plach.png"
                                dap "Эм, не знаю сэр"
                                m "45 очков Слизерину!"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Спасибо, сэр"
                                jump public_completed

                    "4":

                        dap "Я сделала это, сэр"
                        menu:
                            "Отлично, вот твои очки":
                                m "45 очков Слизерину!"
                                dap "Спасибо, сэр"
                                jump public_completed

                            "Мне нужны детали":
                                m "Ты знаешь, как это делается, расскажи подробнее"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Конечно, сэр"
                                $ h_body = "dap/d2_govor.png"
                                dap "В этот раз я постаралась сделать все правильно"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Когда одна из команд забила гол..."
                                m "..."
                                $ h_body = "dap/d2_govor.png"
                                dap "Мы сделали наш обычный трюк, когда я встаю на верх пирамиды и говорю кричалку"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Так вот, в момент когда я встала наверх пирамиды, я показала всей команде свою грудь"
                                $ h_body = "dap/d2_smile3.png"
                                dap "Это даже выглядело как элемент нашего танца"
                                g9 "круто"
                                $ h_body = "dap/d2_rightwha.png"
                                dap "Все видели мою голую грудь..."
                                $ h_body = "dap/d2_smile2.png"
                                dap "это было так воз..."
                                $ h_body = "dap/d2_vizsod5.png"
                                dap "неловко, так что, вы дадите мне мои очки?!"
                                m "45 очков Слизерину!"
                                $ h_body = "dap/d2_smile2.png"
                                dap "Спасибо, сэр"
                                jump public_completed

                    "5":

                        dap "Я сделала это, сэр"
                        menu:
                            "Отлично, вот твои очки":
                                m "45 очков Слизерину!"
                                dap "Спасибо, сэр"
                                jump public_completed

                            "Мне нужны детали":
                                m "Ты знаешь, как это делается, расскажи подробнее"
                                $ h_body = "dap/d2_wha.png"
                                dap "Конечно, сэр"
                                $ h_body = "dap/d2_smile2.png"
                                dap "В этот раз я решила, чтобы они сами все сделали"
                                m "то есть?"
                                $ h_body = "dap/d2_govor.png"
                                dap "Душевые мальчиков и девочек разделяет всего одна стена"
                                $ h_body = "dap/d2_smile2.png"
                                m "интересно"
                                $ h_body = "dap/d2_wha.png"
                                dap "Да, интересно, как администрация смогла это допустить"
                                g4 "*эта сучка даже сейчас наезжает*"
                                m "а что на счет задания?"
                                $ h_body = "dap/d2_smile2.png"
                                dap "так вот, мальчики наверное еще с допотопных времен проделали брешь в стене"
                                m "......"
                                g9 "шарят"
                                $ h_body = "dap/d2_govor.png"
                                dap "всегда эту брешь прикрывало защитное заклинание"
                                m "...."
                                $ h_body = "dap/d2_smile3.png"
                                dap "и я специально ослабила его"
                                $ h_body = "dap/d2_smile2.png"
                                dap "потом достаточно было всего лишь немного задержаться"
                                m "кто-то тебя ведел?"
                                $ h_body = "dap/d2_smile4.png"
                                dap "конечно"
                                $ h_body = "dap/d2_govor.png"
                                dap "я не знаю кто конкретно, но я отчетливо слышала чьи-то движения"
                                $ h_body = "dap/d2_rightwha.png"
                                dap "Интересно, он дрочил в это время?"
                                m "Вы проявили изобретательность, мисс Гринграсс"
                                $ h_body = "dap/d2_smile2.png"
                                dap "спасибо"
                                m "45 очков Слизерину!"
                                dap "Спасибо, сэр"
                                jump public_completed

label mats_complete1:
    menu:
        "1":

            m "Ну что, ты выполнила задание?"
            dap "да, сэр"
            m "Давай, выкладывай подробности"
            $ h_body = "dap/d2_govor.png"
            dap "Ну, как вы и говорили, я подошла к одному парню из команды"
            $ h_body = "dap/d2_wha.png"
            m "..."
            $ h_body = "dap/d2_rightwha.png"
            dap "Это был тот парень, с которым у нас было свидание, так что все было не так сложно"
            $ h_body = "dap/d2_plach.png"
            dap "После тренировки мы остались в раздевалки и он... обнимал меня"
            m "....{w} чего?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "Ну... хорошо, он откровенно лапал меня"
            g9 "...."
            m "Где?"
            $ h_body = "dap/d2_vizsod3.png"
            dap "..."
            $ h_body = "dap/d2_wha.png"
            dap "Везде"
            m "..."
            m "вы неплохо справились, мисс Гринграсс"
            m "35 очков слизерину!"
            $ h_body = "dap/d2_smile2.png"
            dap "Спасибо"
            $ mats_com = 1
            jump public_completed

        "2":
            m "Как прошло?"
            $ h_body = "dap/d2_govor.png"
            dap "Я опять попробовала подойти к Драко..."
            $ h_body = "dap/d2_wha.png"
            m "и?"
            $ h_body = "dap/d2_smile.png"
            dap "в этот раз с ним все было нормально"
            $ h_body = "dap/d2_rightwha.png"
            dap "он как ни в чем не бывало просто сказал \"Привет\"!"
            $ h_body = "dap/d2_wha2.png"
            dap "После того, что он сделал! Пфф!"
            m "........"
            m "эм...."
            m "напомни мне, а что такого он сделал?"
            $ h_body = "dap/d2_zlo.png"
            dap "как что?!"
            $ h_body = "dap/d2_govor.png"
            dap "Он сделал вид, что не заметил меня в прошлый раз"
            $ h_body = "dap/d2_vizsod5.png"
            dap "и ушел с какойто...."
            $ h_body = "dap/d2_wha2.png"
            dap "Когтерванкой!"
            m "да уж....."
            dap "Он тогда точно это сделал специально!"
            m "*зевает*"
            dap "Он ведь знает, что ее семья на 1 строчку опережает мою в рейтинге"
            $ h_body = "dap/d2_right.png"
            dap "Он специально сделал вид, что предпочел ее мне!"
            m "*храпит*"
            $ h_body = "dap/d2_wha.png"
            dap "....."
            dap "эм....."
            $ h_body = "dap/d2_plach.png"
            dap "профессор?"
            g4 "а, что?"
            m "....."
            m "Так как твое задание?"
            $ h_body = "dap/d2_smile2.png"
            dap "ах да...."
            $ h_body = "dap/d2_govor.png"
            dap "я подошла, когда он был один и сказала, что он может потрогать меня..."
            $ h_body = "dap/d2_vizsod3.png"
            dap "было так неловко это произносить"
            m "...."
            m "и он?"
            $ h_body = "dap/d2_smile2.png"
            dap "он не стал стесняться"
            $ h_body = "dap/d2_plach.png"
            dap "все продолжалось около двух минут, пока нам не помешали"
            m "...."
            $ h_body = "dap/d2_wha.png"
            dap "так я получу очки?"
            m "да"
            m "35 очков Слизерину!"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            jump public_completed

        "3":
            $ h_body = "dap/d2_plach.png"
            dap "Эм..."
            m "ну так, что ты сделала или нет?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "наверное..."
            m "наверное?"
            g4 "что это значит?"
            $ h_body = "dap/d2_vizsod3.png"
            dap "ну, я не смогла позволить себе унижаться и напрямую просить мальчиков трогать меня"
            m "...."
            $ h_body = "dap/d2_govor.png"
            dap "но я попросила одного парня из Пуффендуя помочь нам с танцем"
            $ h_body = "dap/d2_wha.png"
            m "и?"
            $ h_body = "dap/d2_wha.png"
            dap "ну.... я ведь сама его выдумала, в одном из движений он должен был держать меня за ноги и талию"
            g4 "че?"
            m "он сам понял, что трогает тебя?"
            $ h_body = "dap/d2_smile2.png"
            dap "мне кажется, да"
            m "кажется?"
            $ h_body = "dap/d2_plach.png"
            dap "ну, по крайней мере ему точно понравилось"
            m "почему?"
            $ h_body = "dap/d2_smile2.png"
            dap "он спросил можно ли перейти из команды в группу поддержки"
            $ h_body = "dap/d2_smile5.png"
            dap "и еще он думал, что успешно скрывает свой стояк"
            m "...."

            m "вы хорошо справились мисс Гринграс"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            m "Но в следующий раз такое не проканает"
            $ h_body = "dap/d2_ispug.png"
            dap "следующий раз??"
            m "...."
            $ h_body = "dap/d2_vizsod5.png"
            dap "...."
            m "40 очков Слизерину"
            jump public_completed

        "4":
            $ h_body = "dap/d2_rightwha.png"
            dap "Сегодня перед тренировкой я поймала одного парня и сказала, что если он наберет больше всех очков, то я дам ему потрогать мою попу"
            m "неплохо"
            m "и что было дальше?"
            $ h_body = "dap/d2_wha.png"
            dap "ну...."
            $ h_body = "dap/d2_plach.png"
            dap "у него ничего не получилось"
            m "...."
            $ h_body = "dap/d2_smile2.png"
            dap "я уже думала, что задание провалено, но ко мне подошел другой парень...."
            m "и что было дальше?"
            $ h_body = "dap/d2_govor.png"
            dap "он сказал, что это он набрал больше всех очков"
            $ h_body = "dap/d2_wha.png"
            m "вот как"
            m "и что ты сделала?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "ну... я не хотела возвращаться с пустыми руками, поэтому мы отошли в укромное место и там все произошло"
            m "...."
            m "что произошло?"
            $ h_body = "dap/d2_plach.png"
            dap "эм...."
            $ h_body = "dap/d2_vizsod3.png"
            dap "он трогал меня"
            m "где он трогал вас?"
            $ h_body = "dap/d2_ispug.png"
            dap "......."
            $ h_body = "dap/d2_left.png"
            dap "*проклятый старик*"
            $ h_body = "dap/d2_vizsod5.png"
            dap "он трогал.....   под юбкой...."
            m "...."
            m "вы прекрасно справились мисс Гринграсс"
            jump public_completed

        "5":
            $ h_body = "dap/d2_rightwha.png"
            dap "Сегодня я попыталссь выцепить кого-то, но все уходили группами"
            m "...."
            m "то есть ты провалила задание?"
            $ h_body = "dap/d2_wha.png"
            dap "нет..."
            m "а что тогда?"
            $ h_body = "dap/d2_govor.png"
            dap "ну, как я и говорила, я не смогла поймать кого-то одного...."

            dap "поэтому мне пришлось подойти к нескольким парням, которые уже собирались уходить"
            m "и что было дальше?"
            $ h_body = "dap/d2_smile2.png"
            dap "Ну... сначала я просто немного мило поговорила с ними"
            dap "я хотела, чтобы они сами все сделали, я ведь не проститутка"
            m "совсем нет"
            $ h_body = "dap/d2_smile3.png"
            dap "они не заставили себя долго ждать"
            $ h_body = "dap/d2_smile4.png"
            dap "как только мы зашли в их комнату, они бросились на меня"
            g9 "круто"
            $ h_body = "dap/d2_plach.png"
            dap "их руки были везде"
            m "что было дальше?"
            $ h_body = "dap/d2_govor.png"
            dap "они продержали меня там пол часа и как то очень быстро все переменилось"
            $ h_body = "dap/d2_wha.png"
            m "в каком смысле?"
            dap "я не знаю, но в какой то момент один резко потерял всякий интерес, потом другой, а затем последний"
            m "....."
            $ h_body = "dap/d2_smile4.png"
            dap "мне кажется я знаю почему"
            $ h_body = "dap/d2_smile3.png"
            dap "вы думаете они успели кончить?"
            m "почему нет?"
            $ h_body = "dap/d2_smile4.png"
            dap "....."
            $ h_body = "dap/d2_smile2.png"
            dap "наверное, мне просто хлюпики попались"
            m "возможно"
            $ h_body = "dap/d2_wha.png"
            dap "так я получу свои очки?"
            m "40 очков Слизерину"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            jump public_completed




label fap_complete1:
    $ dcr = renpy.random.randint(1,4)
    if dcr == 1:
        m "Как прошло?"
        $ h_body = "dap/d2_vizsod5.png"
        dap "Эм... ну, у меня не очень получилось..."
        g4 "как это?"
        $ h_body = "dap/d2_rightwha.png"
        dap "Ну... я позвала Драко, мы попытались уединится в одном из кабинетов"
        $ h_body = "dap/d2_vizsod3.png"
        dap "я уже залезла к нему в штаны, как..."
        m "....."
        g4  "что?"
        $ h_body = "dap/d2_smile4.png"
        dap "неважно, просто в этот раз не получилось"
        m "в таком случае я не могу дать тебе очков"
        $ h_body = "dap/d2_smile4.png"
        dap "я понимаю"
        jump public_completed
    elif dcr == 2:
        g8 "......."
        $ h_body = "dap/d2_govor.png"
        dap "я....."
        m "вероятно, все прошло более чем удачно?"
        $ h_body = "dap/d2_spzlo.png"
        dap "Удачно?{w} вы смеетесь?"
        m "Ну... ты действительно выглядишь забавно"
        $ h_body = "dap/d2_spright.png"
        dap "Эти ублюдки совсем ничего не знают об этикете"
        dap "я ведь просила сказать, когда...."
        m "\"эти\"?{w} то есть ты перевыполнила план?"
        $ h_body = "dap/d2_spwha.png"
        dap "Эм... можно сказать и так"
        $ h_body = "dap/d2_sprightwha.png"
        dap "Это вышло случайно, я позвала одного парня, но с ним пришли еще двое"
        $ h_body = "dap/d2_spzlo.png"
        dap "я подумала, что ничего страшного, но они оказались такими противными"

        dap "никогда больше не буду с ними"
        m "Вы прекрасно справились, мисс Гринграсс"
        m "45 очков Слизерину!"
        dap "Спасибо"
        jump public_completed
    elif dcr == 3:
        
        $ h_body = "dap/d2_govor.png"
        dap "Ну... после тренировки я позвала одного из нападающих..."
        dap "Мы уединились в одной из аудиторий"
        $ h_body = "dap/d2_wha.png"
        dap "Его хватило буквально на пол минуты, поэтому почти ничего не произошло"
        $ h_body = "dap/d2_plach.png"
        dap "эм...{w} я ведь все равно получу за это очки?"
        m "конечно, ты хорошо справилась"
        m "45 очков Слизерину!"
        $ h_body = "dap/d2_smile2.png"
        dap "Спасибо"
        jump public_completed
    elif dcr == 4:
        $ h_body = "dap/d2_govor.png"
        dap "В этот раз я постаралась, чтобы все прошло удачно"
        $ h_body = "dap/d2_wha.png"
        m ".........{w} и как?"
        $ h_body = "dap/d2_smile2.png"
        dap "Нам никто не помешал"
        m "твою мать, говори что было или не получишь никаких очков"
        $ h_body = "dap/d2_wha.png"
        dap "да, хорошо"
        $ h_body = "dap/d2_smile2.png"
        dap "я подошла к парню, с которым уже выполняла одно из заданий"
        m "*хах... теперь это так называется?*"
        $ h_body = "dap/d2_govor.png"
        dap "мы прошли в отдельную комнату и я удостверилась, что все двери закрыты и нам никто не помешает"
        $ h_body = "dap/d2_wha.png"
        m "......"
        m "так что было дальше?"
        $ h_body = "dap/d2_plach.png"
        dap "ну.... как вы и просили, я сделала это"
        m "что это?"
        $ h_body = "dap/d2_vizsod5.png"
        dap "....."
        $ h_body = "dap/d2_vizsod3.png"
        dap "я передернула ему"
        $ h_body = "dap/d2_vizsod5.png"
        m "он кончил?"
        $ h_body = "dap/d2_vizsod3.png"
        dap "ну.....{w} да"
        m "что значит ну? ты не уверена?"
        $ h_body = "dap/d2_plach.png"
        dap "я делала это первый раз и ему пришлось немного помочь мне"
        m "вы прекрасно справились, мисс Гринграсс"
        $ h_body = "dap/d2_smile2.png"
        dap "спасибо"
        jump public_completed

    elif dcr == 5:
        $ h_body = "dap/d2_smile2.png"
        dap "На самом деле все получилось само собой"
        m "а подробнее?"
        $ h_body = "dap/d2_govor.png"
        dap "Ну, одного из защитников сбили и он упал прямо на землю"
        $ h_body = "dap/d2_smile2.png"
        m "*зевает* очень интересно"
        $ h_body = "dap/d2_smile3.png"
        dap "ну, я вызвалась довести его до медпункта"
        m "...."
        $ h_body = "dap/d2_govor.png"
        dap "этого нового врача почему то не было на месте.... в общем там все и случилось"
        m "что случилось?"
        $ h_body = "dap/d2_plach.png"
        dap "...."
        $ h_body = "dap/d2_vizsod5.png"
        dap "я..."
        m "что?"
        $ h_body = "dap/d2_vizsod3.png"
        dap "я передернула ему"
        m "отлично"
        m "в этот раз получилось сделать так, чтобы он кончил?"
        $ h_body = "dap/d2_vizsod5.png"
        dap "да.... {w}в этот раз у меня получилось"
        m "вы хорошо справились, мисс гринграсс"
        jump public_completed





label minet_complete1:
    menu:
        "1":
            m "давай выкладывай"
            $ h_body = "dap/d2_plach.png"
            dap "ну..... эм...."
            m "что?"
            $ h_body = "dap/d2_rightwha.png"
            dap "Сегодня я сделала минет одному парню из команды..."
            m "......"
            m "что это был за парень?"
            $ h_body = "dap/d2_govor.png"
            dap "это был нападающий из Слизерина"
            $ h_body = "dap/d2_wha.png"
            m "........"
            $ h_body = "dap/d2_vizsod3.png"
            dap "............"
            m "и как прошло?"
            $ h_body = "dap/d2_ispug.png"
            dap "......."
            $ h_body = "dap/d2_plach.png"
            dap "ну..."
            $ h_body = "dap/d2_vizsod5.png"
            dap "это был мой первый минет"

            dap "и...."
            $ h_body = "dap/d2_vizsod3.png"
            dap "мне кажется, что я уже перешла грань"
            m "что?"
            $ h_body = "dap/d2_smile4.png"
            dap "можно мне просто мои очки и я уйду отсюда???"
            menu:
                "хорошо":
                    m "Ладно, ты хорошо потрудилась"
                    m "55 очков Слизерину"
                    $ h_body = "dap/d2_vizsod5.png"
                    dap "..."
                    dap "....."
                    jump public_completed
                    # убегает

                "нет, расскажи подробнее":
                    $ h_body = "dap/d2_ispug.png"
                    dap "Подробнее???"
                    $ h_body = "dap/d2_zlo.png"
                    dap "что еще можно сказать?!"
                    $ h_body = "dap/d2_smile4.png"
                    dap "я, Дафна Гринграсс сегодня отсосала какому-то парню, которого видела пару раз за все время"
                    $ h_body = "dap/d2_plach.png"
                    dap "что вы еще хотите услышать?!!"
                    m "...."
                    m "55 очков Слизерину"
                    $ h_body = "dap/d2_vizsod3.png"
                    dap "....."
                    # убегает
                    jump public_completed

        "2":
            m "мне нужны детали"
            $ h_body = "dap/d2_plach.png"
            dap "ну...."
            $ h_body = "dap/d2_rightwha.png"
            dap "Я не хотела, чтобы кто-то узнал о том, что мне придется сделать"
            $ h_body = "dap/d2_wha.png"
            dap "поэтому я подошла к парню, с которым никто не общается"
            $ h_body = "dap/d2_smile2.png"
            dap "даже если он попробует кому-то расскзаать, ему никто не поверит"
            m "*зевает*"
            m "так было что-нибудь или нет??"
            $ h_body = "dap/d2_vizsod5.png"
            dap "...."
            $ h_body = "dap/d2_govor.png"
            dap "да, я отвела его в один из кабинетов и..."
            $ h_body = "dap/d2_wha.png"
            m "что?"
            $ h_body = "dap/d2_plach.png"
            dap "..."
            $ h_body = "dap/d2_vizsod3.png"
            dap "я отсосала ему"
            $ h_body = "dap/d2_vizsod5.png"
            dap "...."

            m "....."
            m "ему понравилось?"
            $ h_body = "dap/d2_wha.png"
            dap "ну.... если можно так сказать"
            $ h_body = "dap/d2_plach.png"
            dap "его хватило буквально на несколько секунд"
            dap "после этого он извинился и убежал"
            m "понятно"
            $ h_body = "dap/d2_plach.png"
            dap "....."
            $ h_body = "dap/d2_wha.png"
            dap "я получу свои очки?"
            m "55 очков Слизерину"
            dap "....."
            jump public_completed


        "3":
            m "что нового?"
            $ h_body = "dap/d2_smile2.png"
            dap "я еще раз сделала это"
            m "ты знаешь как это работает, мне нужны детали"
            $ h_body = "dap/d2_plach.png"
            dap "....."
            $ h_body = "dap/d2_vizsod5.png"
            dap "почему даже после того что я сделала вы заставляете меня еще и говорить о таких вещах?"
            m "хм, ты можешь не говорить"
            $ h_body = "dap/d2_plach.png"
            dap "..."
            m "но в таком случае ты не получишь очков"
            $ h_body = "dap/d2_vizsod3.png"
            dap "........"
            $ h_body = "dap/d2_wha.png"
            dap "я сделала это одному из запасных"
            m "......"
            $ h_body = "dap/d2_govor.png"
            dap "тренировка команды задержалась, поэтому я не хотела терять время"
            $ h_body = "dap/d2_wha.png"
            dap "пока команда была в воздухе, я...."
            $ h_body = "dap/d2_plach.png"
            dap "....."
            m "ты.... что?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "....."
            $ h_body = "dap/d2_ispug.png"
            dap "вы обязательно хотите, чтобы я произносила это?"
            m "......"
            $ h_body = "dap/d2_plach.png"
            dap "......"
            $ h_body = "dap/d2_wha.png"
            dap "ну хорошо"
            $ h_body = "dap/d2_govor.png"
            dap "пока вся команда была в воздухе я....."
            $ h_body = "dap/d2_smile4.png"
            dap "я сделала минет одному из запасных, который сидел на трибунах"
            m "...."
            m "ты делала это прямо на трибунах? Вас кто-то видел?"
            $ h_body = "dap/d2_govor.png"
            dap "нет, мы спустились за них"
            $ h_body = "dap/d2_wha.png"
            dap "нас никто не видел"
            m "*жаль*"
            g9 "*было бы прикольно*"
            m "55 очков Слизерину"
            $ h_body = "dap/d2_smile2.png"
            dap "....."
            jump public_completed



        "4":
            m "ну как?"
            $ h_body = "dap/d2_wtf.png"
            dap "Эти ублюдки меня изнасиловали!"
            m "что?"
            $ h_body = "dap/d2_wha2.png"
            dap "они изнасиловали меня!"
            m "но ты же сама должна была их изнасиловать...."
            $ h_body = "dap/d2_zlo.png"
            dap "как вы можете!!!"
            dap "я как и в прошлый раз договорилась с ними"
            dap "но в этот раз похоже, что они сговорились"
            m "что?"
            $ h_body = "dap/d2_wha2.png"
            dap "все 3 нападающих набрали одинаковое количество очков"
            m "возможно это была случайность"
            $ h_body = "dap/d2_vizsod5.png"
            dap "а после тренировки они начали требовать обещанное"
            m "...."
            $ h_body = "dap/d2_wtf.png"
            dap "они не отпускали меня, пока каждый из них не кончил мне на лицо"
            m "......"
            $ h_body = "dap/d2_zlo.png"
            dap "я просила их не делать этого, но они просто смеялись и в конце концов я час отмывала одежду"
            dap "ублюдки"
            dap "когда я закончу год первой в рейтинге студентов, я упрошу мамочку отправить каждого из них в азкабан"
            dap "на 3.... нет, на 8 лет!"
            $ h_body = "dap/d2_vizsod3.png"
            dap "....."
            m "ты отлично справилась"
            m "55 очков Слизерину"
            dap "спасибо"
            jump public_completed

        "5":
            m "похоже, что у тебя получилось"
            $ h_body = "dap/d2_wha.png"
            dap "эм.... что?"

            dap "откуда вы знаете?"
            $ h_body = "dap/d2_ispug.png"
            dap "блииин, я что проходила с этим несколько часов???"
            dap "черт, надеюсь никто не заметил"
            g9 "*ага, точно не заметили*"
            $ h_body = "dap/d2_vizsod3.png"
            dap "черт"
            ">Дафна быстро вытирает сперму с одежды"
            m "Ну так что? я хочу знать подробности"
            $ h_body = "dap/d2_wha.png"
            dap "Эм, ну..... ничего необычного"
            $ h_body = "dap/d2_govor.png"
            dap "Я подошла отдельно каждому нападающему и пообещала шикарный минет если они забьют больше всего мячей"
            $ h_body = "dap/d2_smile3.png"
            dap "В итоге все 3 нападающих летели как угорелые и мы выиграли с разгромным счетом"
            m "....."
            m "изобретательно"
            m "а что на счет нападающего?"
            $ h_body = "dap/d2_smile2.png"
            dap "эм, ну как я и обещала, я сделала ему добротный минет"
            $ h_body = "dap/d2_plach.png"
            dap "я постаралась все проглотить, чтобы не пачкать одежду, но не получилось"
            m "....."
            m "ничего страшного"
            m "55 очков Слизерину"
            dap "спасибо"
            jump public_completed
    jump public_completed

label fuck_complete1:
    menu:
        "1":
            $ h_body = "dap/d2_plach.png"
            dap "ну...."

            m "что ну?"
            $ h_body = "dap/d2_rightwha.png"
            dap "вообще-то я сделала это, но"
            m "......"
            m "что?"
            $ h_body = "dap/d2_ispug.png"
            dap "на самом деле я не уверена...."
            m "что значит не уверена??"
            $ h_body = "dap/d2_wha.png"
            dap "я нашла, парня, который точно никому бы не рассказал..."
            m "и?"
            $ h_body = "dap/d2_vizsod5.png"
            dap "ну...."
            $ h_body = "dap/d2_vizsod3.png"
            dap "у него оказался такой маленький"
            m "..."
            $ h_body = "dap/d2_plach.png"
            dap "я встала в удобную позу, почувствовала, что он шевелится, но...."
            $ h_body = "dap/d2_plach.png"
            dap "он ерзал примерно с минуту, потом одел штаны и ушел"

            dap "я даже не поняла, что это было"
            $ h_body = "dap/d2_wha.png"
            dap "у меня даже не оставалось времени, поэтому я пришла сюда"
            m "понятно"
            m "такое бывает"
            $ h_body = "dap/d2_plach.png"
            dap "эм..."
            dap "я ведь получу за это очки?"
            m "конечно, ты не виновата"
            m "60 очков Слизерину"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            jump public_completed


        "2":
            m "ты сделала, что должна была, девочка?"
            $ h_body = "dap/d2_smile2.png"
            dap "ох еще бы"
            m "......"
            m "что случилось?"
            $ h_body = "dap/d2_wha2.png"
            dap "Все мужчины - ублюдки"
            m "эм......"
            $ h_body = "dap/d2_left.png"
            dap "Ненавижу"
            m "Не стоит так резко"
            $ h_body = "dap/d2_wha2.png"
            dap "всем плевать на все"
            m "может все таки расскажешь, что произошло?"
            $ h_body = "dap/d2_left.png"
            dap "этот ублюдок"
            m "кто?"
            $ h_body = "dap/d2_wha.png"
            dap "эм..."
            $ h_body = "dap/d2_plach.png"
            dap "я не знаю как его зовут, какой то парень из пуффендуя"
            m "что он сделал?"
            $ h_body = "dap/d2_wha2.png"
            dap "он кончил!"
            m "......"
            m "такое иногда случается, когда парень трахает тебя, это нормально"
            dap "старый извращенец, разве не понятно??"
            m "....."
            $ h_body = "dap/d2_zlo.png"
            dap "он сделал это в меня!!"
            m "....."
            $ h_body = "dap/d2_right.png"
            dap "Ублюдок ничего не знает о порядочности, морали и..."
            m "...."
            $ h_body = "dap/d2_wha2.png"
            dap "он козел!!!"
            m "так вы...."
            g4 "*черт, нужно было очернить ее, а не делать беременной*"
            $ h_body = "dap/d2_left.png"
            dap "теперь мне придется пить защитное зелье, а от него потом 3 дня все болит!!!"
            m "*хах, вот как*"
            m "ну....."
            m "я думаю 60 баллов немного скрасят твои страдания?"
            $ h_body = "dap/d2_smile3.png"
            dap "ох, еще бы"
            jump public_completed

        "3":
            m "................."
            m "что это с тобой?"
            dap "я встретила...."
            m "кого?"
            dap "ЕГО"
            g4 "ЧТо, черт побери, это что опять он?"
            dap "мне кажется..... это был профессор Снейп"
            m "Снейп?"
            dap "я хотела сбежать от него и пойти выполнить ваше задание..."
            dap "но он окликнул меня и сказал, что знает все о нас с вами"
            dap "и требует платы за молчание....."
            m "....."
            dap "после этого он отвел меня в помещение и 3 часа трахал своим огромным членом"
            dap "ме кажется.... я не смогу нормально ходить ближайшие 2 недели"
            m "........."
            m "хм"
            g4 "а у него не было..... эм..... красных ушей?"
            dap "...... он, просил передать вам, что......"
            m "что?"
            dap "......."
            dap "........"
            g4 "что же с ним делать"
            jump public_completed

        "4":
            m "тебе есть что рассказать?"
            $ h_body = "dap/d2_smile2.png"
            dap "да..."
            $ h_body = "dap/d2_rightwha.png"
            dap "я сделала это с одним из защитников"
            m "....."
            $ h_body = "dap/d2_smile2.png"
            dap "я сказала одному из них, что если он не пропустит ни одного мяча в наши ворота, то его ждет награда"
            $ h_body = "dap/d2_smile4.png"
            dap "как думаете, какой был счет?"
            m "........."
            $ h_body = "dap/d2_smile3.png"
            dap "120 - 0 !"
            $ h_body = "dap/d2_smile3.png"
            dap "сначала я не думала, что все что я делаю, может дать такой результат"
            dap "мужчинами так легко управлять"
            g4 "эээ..."
            $ h_body = "dap/d2_rightwha.png"
            dap "*интересно, как далеко они могут зайти*"
            m "довольно"
            $ h_body = "dap/d2_wha.png"
            dap "???"
            m "ты хорошо справилась"
            m "60 очков Слизерину"
            dap "..."
            g4 "я не планировал делать из нее такую стерву"
            m "хотя если вспомнить, что ее ждет...."
            g9 "так будет даже приятнее"
            jump public_completed
        "5":
            $ h_body = "dap/d2_smile4.png"
            dap "я слегка перевыполнила план"
            m "что?"
            $ h_body = "dap/d2_smile2.png"
            dap "ну..."
            $ h_body = "dap/d2_govor.png"
            dap "у меня не получилось выцепить кого-то одного"
            $ h_body = "dap/d2_wha.png"
            dap "я, как обычно, пообещала одному парню награду, но он не справился"
            $ h_body = "dap/d2_smile4.png"
            dap "поэтому мне пришлось импровизировать"
            m "........"
            m "импровизировать?"
            $ h_body = "dap/d2_wha.png"
            dap "ну..... типо того"
            $ h_body = "dap/d2_smile2.png"
            dap "я подошла к нападающему, который набрал больше всех очков и сделала недвусмысленный намек"
            m "....."
            $ h_body = "dap/d2_govor.png"
            dap "он сразу все понял и мы пошли к нему в комнату"
            $ h_body = "dap/d2_plach.png"
            dap "когда все началось, внезапно пришли его друзья"
            m "....."
            $ h_body = "dap/d2_smile4.png"
            dap "......"
            m "......"
            m "60 очков Слизерину"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            jump public_completed

        "6":

            m "Как прошло?"
            $ h_body = "dap/d2_plach.png"
            dap "Ну... эм... я сделала это"
            g4 "что значит, я сделала это?"
            $ h_body = "dap/d2_wha.png"
            dap "После тренировки я взяла Драко за руку и повела его в раздевалку"
            $ h_body = "dap/d2_vizsod3.png"
            dap "мы подождали, когда все уйдут и там сделали это"
            m "вы отлично справились мисс Гринграсс"
            $ h_body = "dap/d2_smile2.png"
            dap "спасибо"
            m "55 очков Слизерину!"
            dap "я могу идти?"
            m "да"
            dap "хихик"
            jump public_completed




label public_comleted0:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2f
    pause 3
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d2_wha.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc

label public_completed1:
    menu:
        "заново":
            jump public_test

        "конец":
            hide screen daphne_main
            hide screen daphne_main2
            hide screen daphne_main3
            hide screen ctc
            hide screen bld1
            with d3
            $ walk_xpos=360 #Animation of walking chibi. (From desk)
            $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
            $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
            show screen daphne_walk1f
            pause 3
            hide screen daphne_walk1f
            $ daphne_chibi_xpos = 610
            show screen daphne_02f
            hide screen daphne_02f
            with d3
            $ renpy.play('sounds/door.mp3') #Sound of
            if daytime:
                $ daphne_chated = 1
                jump night_main_menu
            else:
                $ daphne_chated = 1
                jump day_main_menu

label public_completed:
    m "[ponts] очков Слизерину"
    dap "спасибо"
label public_completed2:
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk2f
    pause 3
    hide screen daphne_walk2f
    $ daphne_chibi_xpos = 610
    show screen daphne_02f
    hide screen daphne_02f
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of
    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu





label too_much_d:
    $ h_body = "dap/d_wtf.png"
    dap "что?!!"

    m "......."
    $ h_body = "dap/d_krik.png"
    dap "как вы смеете мне предлагать такое?!"

    m "почему бы и нет?"
    $ h_body = "dap/d_zlo.png"
    dap "Вы хоть знаете кто я?"
    m "а что такого?"
    $ h_body = "dap/d_wot.png"
    dap "я... я........{w} пффф!"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1f
    pause 3
    hide screen daphne_walk1f
    $ daphne_chibi_xpos = 610
    show screen daphne_02f
    hide screen daphne_02f
    with d3
    $ daphne_chated = 1
    $ renpy.play('sounds/door.mp3') #Sound of
    $ menu_x = 0.5
    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu


label daph_snape2:
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
    sna "Наша маленькая аристократская шлюшка никак не успокоится"
    m "а?"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    sna "Я перехватил еще одно письмо"
    m "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "смотри сам"
    show screen letter
    $ letter_text = "{size=-3}Здравствуйте мама. На этот раз у меня есть все доказательства недопустимого поведения профессора Дамблдора, которого вы так хотели сместить с должности. Все министерство магии сможет увидеть в омуте памяти как он заставлял меня раздеться. Жду ваших инструкций. Ваша дочь Дафна Г."
    pause
    hide screen letter
    with dissolve
    pause 2.0
    g4 "меня все еще передергивает от ее общения с матерью"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Да это вообще поехавшая семейка, не обращай внимания"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Главное - отвадить ее докладывать все матери, пока она не догадалась использовать что-то кроме почты"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "давай, что там было?"
    sna "поехали"

    menu:
        "\"здравствуйте мама\""

        "чо как, старуха":
            pass

        "как житуха, предки?":
            pass

        "Привет чуваки":
            pass

    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Pff-ha-ha-ha"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Черт я думал, что во второй раз будет не так смешно, но ошибся"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    m "Что дальше?"

    menu:
        "\"На этот раз у меня есть все доказательства недопустимого поведения профессора Дамблдора, которого вы так хотели сместить с должности.\""

        "Вы еще там не подохли?":
            pass

        "Вышлите мне презервативов, да побольше":
             pass

        "Что там с моим наследством?":
            pass


    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Pff-ha-ha-ha"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Отлично, дальше?"
    menu:
        "\"Все министерство магии сможет увидеть в омуте памяти как он заставлял меня раздеться.\""

        "Я перетрахалась почти со всей школой":
            pass

        "Я решила, что пора уходить из этой тупой школы":
            pass

        "Вчера я победила в конкурсе самой глубокой глотки":
            pass

    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "это..."

    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Даже лучше чем первое письмо"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Жаль что я не увижу ее лицо, когда она это прочитает"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Она получит его уже завтра"
    $ daphne_event = 7
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

    $ days_without_an_event = 0
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    return



label last_jurnalist_quest:
    m "На следующей неделе будет последний матч"

    $ h_body = "dap/d_smile1.png"
    dap "Я знаю, все его давно ждут"
    m "По этому поводу у меня будет к тебе самое важное задание"
    $ h_body = "dap/d_plach.png"
    dap "...."
    $ h_body = "dap/d_wha2.png"
    dap "Еще важнее, чем предыдущие?"
    m "кхм, да"
    $ h_body = "dap/d_vizsod5.png"
    dap "Я даже боюсь представить, что это может быть"
    m "все не так сложно как может показаться"
    $ h_body = "dap/d_plach.png"
    m "Ты знаешь кто такой Виктор Крам?"
    $ h_body = "dap/d_smile1.png"
    dap "Конечно же, он - звезда мирового масштаба, все его знают"
    m "отлично"
    $ h_body = "dap/d_plach.png"
    dap "эм...."
    $ h_body = "dap/d_vizsod5.png"
    dap "...."
    g9 "....."
    m "ты правильно поняла"
    $ h_body = "dap/d_plach.png"
    dap "но как я это сделаю?"
    m "не бойся, я все предусмотрел"
    m "просто дай ему это зелье и он сделает все что захочешь"
    m "Главное, чтобы он не участвовал в матче"
    $ h_body = "dap/d_rightwha.png"
    dap "хм...."

    $ h_body = "dap/d_def.png"
    dap "Я не уверена, но попробую"
    g4 "Что значит не уверена, от этого зависит судьба школы!"
    $ h_body = "dap/d_krik.png"
    dap "я сделаю!"
    $ h_body = "dap/d_def.png"
    m "отлично"
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    hide screen bld1
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen blktone
    hide screen daphne_02
    hide screen ctc
    with d3
    g9 "Жду не дождусь увидеть полосу новостей с ее лицом"

    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu


label last_jurnalist:
    stop music fadeout 1.0
    pause 1.0
    play sound "sounds/applause01.ogg"
    play music "sounds/from_crowd.ogg"
    pause 1.0
    m "..."
    g4 "..."
    m "Что это за звук?"
    m "Похоже уже началось..."
    g4 "Опять мне придется все пропускать"
    m "Интересно, отсюда видно хоть что-то?"
    
    hide screen desk
    hide screen genie
    $ tt_xpos=190
    $ tt_ypos=80
    show screen genie_stands
    show screen chair_02 #Empty chair near the desk.
    show screen desk
    with Dissolve(0.5)
    pause 1.0
    $ backgr = "new/stad1.png"
    show screen fruk
    with dissolve
    stop sound fadeout 1.0
    pause 1.0
    play music "sounds/from_crowd.ogg"
    pause 2.5
    comm1 "И воот наконец-то главный матч этого года!"
    comm1 "Сборная Думстранга будет играть против сборной Хогвартса!"
    comm2 "Целых 5 лет прошло с их последней встречи и сегодня мы узнаем, какая из школ магии лучше играет в квидич!"
    m "похоже, что я еще ничего не упустил"
    comm1 "даже не верится, что все прибывшие смогли уместится на трибунах"
    comm2 "думаю не обошлось без пары-тройки десятков заклинаний на шестое измерение"
    comm1 "даа, ощущение, что сюда слетелась вся англия, все журналисты сегодня устремились именно сюда"
    m "журналисты?"
    g9 "это мне и нужно"

    pause 1.0
    show screen bld2
    with Dissolve(0.7)
    #stop music fadeout 1.0
    pause 1.0
    mal "Блин, кто нибудь вообще верит в нашу команду?"
    mal2 "Что то не очень, даже прошлые матчи были откровенным везением"
    fem "Да, каждый раз у соперника случался форс мажор каким то чудом"
    mal "думаете это было подстроено?"
    fem "Не думаю, я это заявляю во всеуслышание"
    mal2 "Блин, ну не знаю, все равно они смогли победить"
    fem "Да о чем вы говорите, за дурмстранг играет Виктор Крам! Лучший игрок современности!"
    mal "Если только с ним ничего не случится"
    hide screen bld2
    with Dissolve(0.7)
    "..."
    hide screen fruk
    $ backgr = "new/stad8.png"
    show screen fruk
    with dissolve
    comm1 "Команды вышли на разминку"
    comm2 "Хм... похоже не в полном составе"
    comm2 "Покрайней мере я не вижу главную звезду этого матча, Виктора Крама"
    mal "Я же говорил..."
    mal2 "Да ладно тебе, еще играть то не начали"
    g4 "Где Дафна?"
    m "Она должна была быть у их ложи..."
    m "Вижу!"
    g9 "Даже не верится, что сейчас будет..."
    #stop music fadeout 1.0
    #pause 1.0
    #hide screen fruk
    #$ backgr = "new/room.jpg"
    #show screen fruk
    #with Dissolve(1.0)
    # звук
    #pause 1.5
    #$ h_body = "dap/d_def.png"
    #show screen daphne_main
    #play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3"
    pause 1.0
    $ h_body = "dap/d_rightwha.png"
    dap_left "Хм... он должен будет проходить где-то здесь..."
    $ h_body = "dap/d_def.png"
    dap_wha "Кажется... здесь..."
    $ h_body = "dap/d_smile.png"
    dap_plach "Это он?"
    $ h_body = "dap/d_zlo.png"
    dap_smile "так, мне всего то нужно будет подойти поближе..."
    $ h_body = "dap/d_smile.png"
    dap_smile3 "Погнали!"
    pause 2.0
    $ h_body = "dap/d_smile2.png"
    dap_smile2 "Виктор! Виктор, я ваша покл..."
    bogu "Не мешайтесь, дамочка"
    $ h_body = "dap/d_ispug.png"
    dap_ispug "Но..."
    bogu "Никаких но! Автографы только после игры!"
    $ h_body = "dap/d_plach.png"
    dap_plach "Но...{w} я должна..."
    $ h_body = "dap/d_vizsod2.png"
    dap_visod2 "Я должна...."

    dap_visod  "...."
    g4 "*твою мать*"
    $ h_body = "dap/d_visod5.png"
    dap_visod2 "Я...{w} подвела профессора..."
    g4 "какого хрена..."
    $ h_body = "dap/d_plach.png"
    dap_left "Придется придумать что-то другое"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    play music "sounds/from_crowd.ogg"
    hide screen fruk

    $ backgr = "new/stad8.png"
    show screen fruk
    with Dissolve(1.0)
    comm1 "Да! и вот мы видим главную звезду сегодняшнего матча!"
    play sound "sounds/applause02.ogg"
    comm1 "Виктор Крамм!"
    comm2 "трибуны ликуют... мне кажется даже болельщики хогвартса, по крайней мере женская их часть."
    comm1 "Думаете Гарри Поттер не сможет составить ему конкуренцию?"
    comm2 "ну знаете, при всем уважении, мне кажется он лучше умеет попадать в новости, нежели ловить мячи"
    g4 "Дерьмо, похоже придется придумать что-то еще"
    g4 "такая была возможность прославить ее на весь мир"
    m "ну ладно, хоть матч посмотрю"
    play sound "sounds/refer.ogg"
    pause 2.0
    hide screen fruk
    $ backgr = "stadium_def"
    #$ backgr = "new/stad2.png"
    show screen fruk
    with dissolve
    comm1 "Матч начался!"
    
    comm2 "игроки дурмстранга выглядят на порядок сильнее своих соперников"
    comm1 "еще бы! говорят, их игроки тренируются только в сильную метель, а вне тренировок только и делают что дерутся с медведями"
    comm2 "......"
    comm2 "ты это сам придумал, джим"
    comm1 "вообще то, это ты мне рассказывал..."
    hide screen fruk
    $ backgr = "dooms_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm2 "10 очков в пользу Дурмстранга!"

    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    with dissolve
    comm1 "вполне закономерно сборная дурмстранга открывает счет первой"
    comm1 "не думаю, что хогвартс сможет легко отыграться"
    hide screen fruk
    $ backgr = "dooms_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm1 "уже 20 очков в пользу Дурмстрага!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    with dissolve
    pause 2.0
    hide screen fruk

    $ backgr = "dooms_gool"
    
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm2 "30 очков в пользу Дурмстранга!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    with dissolve
    comm1 "Вполне прогнозируемо, команда хогвартса просто ничего не может противопоставить своему противнику"
    comm2 "Думаете здесь совсем нет никакой интриги?"
    comm1 "все ясно как белый день, странно, что снитч еще в игре"
    pause 2.0
    hide screen fruk
    $ backgr = "dooms_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm1 "40 очков в пользу Дурмстранга!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    with dissolve
    comm2 "Если так будет продолжаться дальше, то команду хогвартса не сможет спасти даже ее ловец"
    play sound "sounds/refer.ogg"
    comm1 "капитан команды хогвартса берет перерыв"
    show screen blkfade
    with Dissolve(0.8)
    hide screen fruk
    with dissolve
    pause 1.0
    $ backgr = "new/stad9.png"
    show screen fruk
    hide screen blkfade
    with Dissolve(0.8)
    har_govor "Давайте, ребята, мы должны надрать им задницы"
    pl1 "Ым, никто не говорил, что мы выйдем играть против таких зверей"
    pl2 "да, в гробу я видел такую игру"
    pl3 "я бы вообще не пошел на игру, если бы не освобождение от лекций"
    har_udivl "..."
    hide screen fruk
    $ backgr = "new/stad1.png"
    show screen fruk
    with Dissolve(0.7)
    comm2 "это что, группа поддержки?"
    comm1 "ничего себе, не думал, что в хогвартсе есть что то подобное"

    pl1 "Смотрите это дафна там?"
    pl2 "Что?"
    pl3 "Где?"
    hide screen fruk
    $ backgr = "new/cheer.png"
    show screen fruk
    with Dissolve(2.0)
    comm1 "эм... что это они делают?"
    m "...."
    comm2 "Эта девушка.... она что правда..."
    comm1 "Она что, полностью голая??"

    g6 "......{w}..........{w}............"
    
    g5 "это....{w} это...."
    g9 "даже лучше чем было задуманно!"
    pl1 "Это она серьзно?"
    pl2 "Ты еще спрашиваешь, после того что она начала вытворять?"
    pl3 "Она? а что она?"
    pl2 "Хаха, во ты лошара, да она с половиной команды перетрахалась!"
    pl3 ".... со мной тоже"
    pl2 "ты уже спалился лошара, это твой шанс"
    pl3 "Черт, думаете она не врет?"
    pl1 "блин, я хочу трахнуть эту мисс голубую кровь"
    harr "да... давайте выиграем кубок!"
    pl1 "срать на этот кубок, я хочу залезть в дырку Гринграсс"
    har_udivl "..."
    pl3 "Черт, у меня от одной мысли стояк"

    comm1 "Вот это представление устаивает группа поддержки Хогвартса!"
    play sound "sounds/photo.ogg"
    with flashbulb
    pause 0.5
    play sound "sounds/photo.ogg"
    with flashbulb
    pause 0.5
    play sound "sounds/photo.ogg"
    with flashbulb
    pause 0.1
    play sound "sounds/photo.ogg"
    with flashbulb
    pause 0.1
    play sound "sounds/photo.ogg"
    with flashbulb
    pause 0.1
    
    comm2 "Теперь я понимаю, почему Хогвартс так плохо играет, похоже у них есть дела поважнее квидича"
    comm1 "жду не дождусь увидеть ее фотографию в магическом вестнике"
    comm2 "Даа, это будет просто бомба"

    comm1 "Что..."
    comm1 "Мне передали, что это не кто иная как наследница семьи Гринграсс"
    comm2 "Действительно?"
    comm2 "Это же..."
    comm2 "Не думаю, что через неделю останется хоть один волшебник, не знающий об этой девушке"
    play sound "sounds/refer.ogg"
    pause 2.0
    comm1 "перерыв окончен!"
    
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    with Dissolve(1.0)

    comm1 "Что ж, после такого перерыва можно и игру просмотреть"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm1 "И в первые же секунды нападающий Хогвартса зарабатывает первые очки!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    
    pl1 "минет мой!"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm2 "Еще 10 очков от сборной хогвартса"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    pl3 "да! я тоже попроведаю этот ротик"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm2 "И еще 10 очков!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    comm1 "После такого тайм аута команда буквально разошлась!"
    pl3 "думаете если я трахну Гринграсс, я стану чистокровным?"
    pl1 "Это так не работает идиот, нужно родится в семье волшебников!"
    pl3 "..."
    pl3 "А если в анал?"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm1 "И еще 10 очков"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    g9 "Похоже у нее будет много работы, хехе"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    pl2 "Я с вами!"
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    comm2 "Невероятные камбек от сборной Хогвартса!"
    comm2 "Что они делали в этот тайм аут?"
    har_govor "Поччти поймал!"
    pl1 "Эй стой!"
    har_govor "А?"
    pl1 "мы должны набрать очки!"
    har_govor "Но..."
    pl2 "Кто нибудь сбейте его"
    har_govor "эй, вы чего"
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/attack_snape.ogg"
    $ renpy.pause(1.0, hard = True)
    play sound "sounds/applause02.ogg"
    comm2 "Еще 10 очков!"
    pause 1.0
    hide screen fruk
    $ backgr = "hogw_gool"
    show screen fruk
    comm1 "10 очков"
    comm2 "Просто невероятный разгром сборной Дурмстранга, неужели эта команда была переоценена?"
    har_govor "черт, почти поймал!"
    comm2 "Иии Виктор Крам, главная звезда на поле, ловит снитч!"
    comm2 "Но, к сожалению, это не поможет комнаде выиграть, потому что счет становится 320:140..."
    comm1 "Этот матч определенно войдет в историю!"
    comm1 "Кто бы мог подумать, что..."
    hide screen fruk
    $ backgr = "new/stad2.png"
    show screen fruk
    pl1 "Черт, жду не дождусь когда смогу обналичить свой очки"
    pl2 "Интересно можно обменять анал на 3 минета?"
    pl1 "Надо было забивать больше, мне она за неделю не расплатится"
    fem "Какие же вы все извращенцы!"
    fem "Это подумать надо, начать нормально играть только после того как кто то посветит своими сиськами!"
    pl3 "Это все потому что ты просто завидуешь, ведь предложение касалось только парней"
    fem "Что? Да я бы ни за что..."
    pl2 "Хаха, ну да, точно"
    pl2 "Кстати где она?"
    pl1 "Надо поскорее найти"
    "..."
    hide screen fruk
    hide screen quid_quest
    show screen genie
    hide screen genie_stands
    hide screen chair_02 #Empty chair near the desk.
    hide screen desk
    with dissolve
    m "....."
    g9 "похоже, что я немного переуседрствовал с ее обучением"
    # заходит снейп
    pause 1.0
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ daphne_event = 14
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
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main
    with Dissolve(.3)
    sna "Это было...{w}......{w}............."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Просто Идеально!"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Уже сегодня ее фотографии увидят буквально все!"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Как ты смог ее на такое уговорить?"
    m "Эм... вообще-то она..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "А команда то! Как они могли купиться на это... чтобы Гринграсс стала трахаться с кем то из них! ХА!"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    m "..."
    m "думаешь она не станет этого делать?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"
    sna "Ты хочешь сказать, что она действительно может..."
    m "ну..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "хах, ладно не отвечай, хочу, чтобы это оставалось сюрпризом"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Жду не дождусь когда прочитаю письма от министерства, от Гринграссов... да от всех! Все издания будут просить наш комментарий"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Я  буду только говорить в каком я шоке от того, что проделала чистокровная волшебница из такой семьи..."
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Даже не верится, что все получилось на столько хорошо"

    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Кстати она куда-то ушла и я так и не смог ее найти после матча"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Наверное, нужно будет поискать ее после того как я разберусь с праздником"
    m "праздником?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Ну конечно, из-за, кхм \"болезни\" директора, я должен проследить за праздником в честь победы"
    m "Интересно было бы посмотреть что там будет"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "Эй, мы же договаривались, тебя не должны видеть"
    m "...{w} да, я понял"
    $ s_sprite = "03_hp/10_snape_main/23.png"
    sna "Пойду подготовлю речь"
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
    $ daphne_event = 14
    #$ duels = 1
    $ chitchated_with_snape = True
    $ days_without_an_event = 0
    return



label last_kram:
    m "Близится кульминация всего нашего труда"
    $ h_body = "dap/d_udivl.png"
    dap "эм... кульминация?"
    m "Скоро будет гланвый матч по квидичу за кубок школ"

    $ h_body = "dap/d_smile1.png"
    dap "Да, все давно его ждут"
    m "Твоя помощь команде была понастоящему неоценима"
    $ h_body = "dap/d_wha3.png"
    dap "...."
    $ h_body = "dap/d_vizsod5.png"
    dap "да..."
    $ h_body = "dap/d_visod2.png"
    dap "наверное..."
    m "ты большая молодец"
    $ h_body = "dap/d_wha5.png"
    dap "..."
    $ h_body = "dap/d_smile1.png"
    dap "спасибо, профессор"
    m "однако, для победы этого явно не достаточно"
    $ h_body = "dap/d_ispug.png"
    dap "..."
    $ h_body = "dap/d_plach.png"
    dap "н-но..."
    m "ты хорошо потрудилась, но пора сделать последний рывок"
    $ h_body = "dap/d_ispug.png"
    dap "...."
    $ h_body = "dap/d_wha5.png"
    dap "рывок?{w} какой рывок?"

    m "Сегодня у меня будет к тебе самое важное задание из всех"
    $ h_body = "dap/d_plach.png"
    dap "...."
    $ h_body = "dap/d_wha2.png"
    dap "Еще важнее, чем предыдущие?"
    m "кхм, да"
    $ h_body = "dap/d_vizsod5.png"
    dap "Я даже боюсь представить, что это может быть"
    m "все не так сложно как может показаться"
    $ h_body = "dap/d_plach.png"
    m "Ты знаешь кто такой Виктор Крам?"
    $ h_body = "dap/d_smile1.png"
    dap "Конечно же, он - звезда мирового масштаба, все его знают"
    m "отлично"
    $ h_body = "dap/d_plach.png"
    dap "эм...."
    $ h_body = "dap/d_wha4.png"
    dap "а что мне нужно будет делать?"

    m "прямо перед разминкой ты должна будешь попросить у него автограф"
    $ h_body = "dap/d_plach.png"
    dap "..."
    $ h_body = "dap/d_smile1.png"
    dap "ах... автограф?"
    g9 "и заставить его пропустить этот матч"
    $ h_body = "dap/d_ispug.png"
    dap "что? каким образом?"
    m "у тебя есть твое главное оружие"
    $ h_body = "dap/d_plach.png"
    dap "оружие?"
    g9 "я бы даже сказал, целых три"
    $ h_body = "dap/d_plach.png"
    dap "..."
    $ h_body = "dap/d_visod2.png"
    dap "а..."
    $ h_body = "dap/d_wha3.png"
    dap "эм..."
    $ h_body = "dap/d_govor.png"
    dap "но он же звезда, я не думаю, что он станет рисковать перед матчем изза секса..."
    $ h_body = "dap/d_wha3.png"
    m "просто случайно пролей на него вот это зелье"
    $ h_body = "dap/d_ispug.png"
    dap "Эм... что это?"
    m "Профессор снейп любезно согласился помочь нам в наших начинаниях и сделал самое убойное возбуждающее зелье"
    play sound "sounds/win2.mp3"
    show screen gift
    $ the_gift = "03_hp/18_store/34.png" # BUTTERBEER.
    ">вы передаете дафне возбуждающее зелье"
    hide screen gift
    with dissolve
    m "должно хватить и пары капель, но для надежности можешь использовать весь флакон"
    $ the_gift = "03_hp/18_store/d_plach.png" # BUTTERBEER.
    $ h_body = "dap/d_vizsod5.png"
    dap "да но...{w} это..."
    m "разве ты не хочешь чтобы сборная Хогвартса победила в кубке?"
    $ h_body = "dap/d_plach.png"
    dap "хочу, но..."
    m "я дам тебе столько очков, что ты займешь первое место в рейтинге с большим отрывом"
    $ h_body = "dap/d_ispug.png"
    dap "что?"
    g9 "мама будет тобой гордиться"
    $ h_body = "dap/d_plach.png"
    dap "..."
    $ h_body = "dap/d_right2.png"
    dap "......"
    $ h_body = "dap/d_left.png"
    dap "Хорошо, я сделаю это..."
    m "Отлично"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    stop music fadeout 1.0
    #$ h_body = "dap/d_def.png"
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    hide screen bld1
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen blktone
    hide screen daphne_02
    hide screen ctc
    with d3
    g9 "Жду не дождусь увидеть полосу новостей с ее лицом"
    #m "Можно предупредить об этом гермиону. Нужно поспешить, если я хочу успеть"
    $ daphne_event = 13
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu


label after_all:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ daphne_chibi_xpos = 610
    $ daphne_chibi_ypos = 250
    show screen daphne_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 04.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1
    pause 4
    $ daphne_chibi_xpos = 300 #Near the desk.
    show screen daphne_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "dap/d_smile.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    show screen daphne_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen daphne_main
    with d3
    hide screen ctc
    #$ h_body = "dap/d_govor.png"
    m "...."
    m "Эм..."
    $ h_body = "dap/d_govor2.png"
    dap "Сэр"
    $ h_body = "dap/d_smile.png"
    m "Как ты?"
    $ h_body = "dap/d_govor2.png"
    dap "эм... хорошо"
    $ h_body = "dap/d_vizsod5.png"
    dap "Моей маме пришлось задействовать все свои связи, чтобы уладить вопрос с журналистами..."
    g4 "*Что?!*"
    g4 "*Твою мать, мы что зря все это делали?!*"
    $ h_body = "dap/d_visod2.png"
    dap "Она сказала, что не думала, что ее дочь такая...{w} такая..."
    m "..."
    $ h_body = "dap/d_vizsod5.png"
    dap "проститутка"
    m "да ладно, всякое бывает"
    $ h_body = "dap/d_visod2.png"
    dap "да, но... это все изменило"
    m "Что?"
    $ h_body = "dap/d_left.png"
    dap "Она хотела собрать на вас компромат о падении нравственности в школе..."
    g9 "Хах, неужели"
    $ h_body = "dap/d_smile2.png"
    dap "Но теперь она должна отстать"
    m "Отлично"
    # взгляд с намеком
    $ h_body = "dap/d_smile.png"
    dap "И еще..."
    m "Что?"
    $ h_body = "dap/d_plach.png"
    dap "Она сказала, что я..."
    $ h_body = "dap/d_vizsod5.png"
    dap "Больше не член семьи Гринграсс..."
    m "..."
    $ h_body = "dap/d_plach.png"
    dap "И больше не обручена с Драко Малфоем{w}, теперь его женой будет моя сестра..."
    m "..."
    $ h_body = "dap/d_ispug.png"
    dap "И я теперь...{w} обычная девушка..."
    $ h_body = "dap/d_vizsod5.png"

    dap  "...{w}......"
    m "....."
    $ h_body = "dap/d_smile.png"
    dap "Спасибо вам, профессор..."
    m "....."
    m "Эм... {w}Да не за что"
    g9 "*Я бы и еще раз это провернул*"
    $ h_body = "dap/d_smile2.png"
    dap "Благодаря вам я теперь свободна"
    m "Это было...{w} не самое плохое приключение"
    $ h_body = "dap/d_smile3.png"


    $ h_body = "dap/d_smile.png"
    dap "Я должна отблагодарить вас, сэр"
    g9 "Эта сучка ненасытна, даже после всего этого, она все еще..."
    hide screen daphne_02
    $ walk_xpos=300 #Animation of walking chibi. (From)
    $ walk_xpos2=200 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen daphne_walk1
    pause 0.8
    # минет
    show screen blkfade
    with Dissolve(1.0)

    dap_smile "сегодня я хочу сделать это здесь..."
    m "...{w} Нас же увидят"
    dap_smile4 "От этого я возбуждаюсь еще больше, профессор"
    g9 "ну держись, сучка"
    $ okno2 = "new/bashna/1smdown.png"
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen bld1
    hide screen daphne_02
    hide screen daphne_walk1
    hide screen blkfade
    $ okno1 = 1
    $ okno2 = "new/bashna/1smdown.png"
    show screen okno
    with Dissolve(2.0)
    pause 0.1
    $ okno2 = "new/bashna/1smz.png"
    play sound "sounds/gltch.mp3"
    with vpunch

    pause 0.5
    $ okno2 = "new/bashna/1smdown.png"
    dap "ааах"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    $ okno2 = "new/bashna/1smsl.png"
    with vpunch
    dap "да сэр! трахните меня как грязную шлюху!"
    g9 "хах, меня долго упрашивать не придется девочка"
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    $ okno2 = "new/bashna/1smdown.png"
    dap "ааах"
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smup.png"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smup.png"
    with vpunch
    pause 0.5
    hide screen okno
    $ okno2 = "new/bashna/1smdown.png"
    show screen okno
    with dissolve
    dap "даа"
    $ okno2 = "new/bashna/1krz.png"
    dap "сильнее, пожалуйста!"
    g4 "..."
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    $ okno2 = "new/bashna/1smup.png"
    dap "хах, черт"
    mal "эй"

    $ okno2 = "new/bashna/1smz.png"
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smup.png"
    with vpunch
    pause 0.5
    dap "ооохх"
    mal "что это там"
    $ okno2 = "new/bashna/1smdown.png"
    dap "..."
    fem "где?"
    mal "да вон, в окне"
    mal "у профессора дамблдора"
    hide screen okno
    $ okno2 = "new/bashna/1krz.png"
    show screen okno
    with dissolve
    dap "хах, да, профессор, еще! еще!"
    g4 "сучка, да ты смеешься"
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1smz.png"
    with vpunch
    pause 0.5
    $ okno2 = "new/bashna/1smdown.png"
    mal2 "это же..."

    dap "...."
    hide screen okno
    $ okno1 = 2
    show screen okno
    with Dissolve(1.0)
    fem "что она там делает"
    play sound "sounds/gltch.mp3"
    $ okno2 = "new/bashna/1krz.png"
    with vpunch
    pause 0.5
    dap "ааахх"

    mal "она что..."
    mal3 "Вот это сиськи!"
    g4 "Черт, тебя уже увидели"
    $ okno2 = "new/bashna/1smdown.png"
    dap "да{w}, пусть они видят"
    g4 "ты сумашедшая сучка"
    $ okno2 = "new/bashna/1krz.png"
    dap "какая разница! трахните меня посильнее, пожалуйста!"
    g4 "ну держись шлюха"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    hide screen okno
    $ okno1 = 3
    $ okno2 = "new/bashna/2orgasm.png"
    show screen okno
    with dissolve
    pause 1.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    dap "ааааах"
    mal2 "Что она делает... вы видите?"
    fem "не может быть..."
    mal "Это же кабинет Дамблдора"
    fem "не могу поверить..."
    mal3 "Может это иллюзия?"
    mal "если так, то она очень реалистичная"


    $ okno2 = "new/bashna/2down.png"
    dap "Я люблю вас профессор!"
    g4 "Сучка, угомонись!"
    $ okno2 = "new/bashna/2krz.png"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5

    dap "Да, профессор, трахайте меня сильнее!"
    g4 "Черт, что ты делаешь, нас же увидят"
    $ okno2 = "new/bashna/2smsl.png"
    dap "Я хочу, чтобы все знали, что я люблю вас, профессор!"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch

    pause 0.5

    mal2 "охренеть"
    fem "после того, что она учудила на кубке, это не так уж странно"
    mal "Да, похоже она окончательно свихнулась"
    play sound "sounds/gltch.mp3"
    with vpunch
    g4 "хаааа!"
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen okno
    $ okno1 = 4
    $ okno2 = "new/bashna/2yorg.png"
    show screen okno
    with dissolve
    dap "да профессор!"
    show screen blkfade
    with Dissolve(2.0)
    hide screen okno
    hide screen blkfade
    show screen daphne_02

    with dissolve
    $ h_body = "dap/d_smile.png" #Sprite of Hermione's upper body.
    pause 2.0
    show screen daphne_main
    with dissolve
    dap "спасибо вам за все, профессор"
    g9 "да ладно, заходи ко мне почаще и все"
    $ h_body = "dap/d_wha4.png"
    dap "эм..."
    $ h_body = "dap/d_smile6.png" #Sprite of Hermione's upper body.
    dap "я уезжаю"
    m "что?"
    $ h_body = "dap/d_wha3.png"
    dap "я думала, что вам уже все сказали..."
    $ h_body = "dap/d_vizsod5.png"
    dap "сегодня мой последний день в хогвартсе"
    dap "Мне придется пожить некоторое время с бабушкой, пока скандал в министерстве магии забудется"
    m "....{w} ого"
    $ h_body = "dap/d_smile.png"
    dap "прощайте, профессор"
    # трах прямо в окне
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    hide screen bld1
    hide screen okno
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen blktone
    hide screen daphne_02
    hide screen ctc
    with d3
    m "..."
    m "значит это все?"
    g6 "я буду скучать по этой сучке"
    $ daphne_event = 100
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if daytime:
        $ daphne_chated = 1
        jump night_main_menu
    else:
        $ daphne_chated = 1
        jump day_main_menu


label daphne_last_event02:
    pause 1.0
    play sound "sounds/applause02.ogg"
    #play music "music/07 Introducing Colin2.mp3"
    with hpunch
    pause 1.0
    
    g4 "Черт возьми, ничего себе грохот"
    play music "music/07 Introducing Colin2.mp3"
    pause 1.5
    m "..."
    m "Судя по музыке, вечеринка уже началась"
    g9 "Снейп ведь не думал, что я правда буду сидеть, пока все там развлекаются?"
    show screen blkfade
    with Dissolve(0.8)
    show screen end_u_1
    $ end_u_1_pic =  "03_hp/17_ending/02_1.png"

    $ badges = False

    hide screen hermione_main
    hide screen room # MAIN BG (DAY).

    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.

    hide screen main_menu_01

    with fade
    #hide screen end_u_1                                           #<---- SCREEN
    #hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    #hide screen end_u_4                                           #<---- SCREEN
    pause.1
    hide screen blkfade
    with d5
    show screen ctc
    pause
    hide screen ctc
    hide screen bld1
    with d7

    m "Черт, в этом замке ничего не найти"
    m "Судя по звуку, я приближаюсь"
    m "Это должно быть где-то здесь..."
    pause 0.5
    hide screen end_u_1
    $ end_u_1_pic =  "03_hp/17_ending/02.png"
    show screen end_u_1
    with dissolve
    pause 0.5
    m "Точно, вот оно!"
    play sound "sounds/from_crowd.ogg"
    cr5 "*шум*"
    sna_01 "..."
    sna_02 "кхе-кхе"
    stop sound
    play music "sounds/from_crowd.ogg"
    cr5 "*шум*"
    sna_03 "...."
    sna_04 "..........."
    cr5 "*шум*"
    sna_05 "МОЛЧААААААААТЬ!"
    stop music fadeout 1.0
    cr5 "......"
    sna_10 "...."
    sna_09 "......."
    sna_06 "И мы поздравляем наших чемпионов!"
    sna_02 "Команду которая разгромила всех на своем пути и доказала, что Хогвартс - лучшая школа магии..."
    sna_09 "Команду которая принесла кубок..."
    sna_08 "блаблаблабла"
    show screen bld1
    with Dissolve(0.8)
    #stop music fadeout 1.0
    pause 1.0
    mal "Когда нам уже дадут наш приз"
    mal2 "Надеюсь нас с ним не обломают"
    mal3 "думаете дафна просто обманула нас?"
    fem "Конечно обманула! А вы поверили, что член семьи гринграсс пойдет на такое? Фу, извращенцы!"
    mal "ты просто завидуешь"
    fem "Чему?!"
    mal3 "Блин а что если так, неужели она действительно пойдет на такое?"
    mal2 "Жду не дождусь когда присуну этой высокорожденной"
    mal3 "Говорят, если трахаешь Гринграссов, то твоя кровь становится чистой"
    mal "Ты это сам выдумал, чудила"
    hide screen bld1
    with dissolve



    sna_06 "Хочу поблагодарить нашу команду за столь большой вклад в престиж нашей школы..."
    sna_21 "даже в отсутвии директора..."
    sna_13 "Но благодаря грамотному управлению его временного заместителя..."
    m "Я думал, что на вечеринках обычно веселятся, а не слушают всякие бредни"
    sna_06 "Каждый член команды награждается отличительным орденом и..."
    sna_10 "эм..."
    sna_05 "Эй, кто утащил ордена??!"
    cr3 "шепот"
    sna_08 "Эм... что?"
    sna_01 "Мне срочно передали, что..."
    cr3 "шепот"
    sna_17 "как? она правда..."
    sna_20 "хм..."
    sna_12 "Команда может пройти в аудиторию 11,5 Б"
    sna_19 "Там их ждет..."
    sna_18 "особая церемония награждения"
    m "Особая церемония?"
    mal "что там будет?"
    mal2 "откуда я знаю"
    mal3 "Думаете там..."
    fem "пойдемте уже"

    g4 "Черт, я не могу это пропустить"
    hide screen end_u_1
    $ end_u_1_pic =  "03_hp/17_ending/02_1.png"
    show screen end_u_1
    with dissolve
    m "нужно пройти за ними, только так, чтобы не заметили"
    show screen blkfade
    with Dissolve(0.8)
    stop music fadeout 1.7
    $ renpy.pause(1.5, hard = True)
    mal "интересно что там"
    mal2 "давай уже открывай"
    play sound "sounds/door.mp3"
    pause 1.0
    g6 "..."
    $ end_u_1_pic =  "end/wall.png"
    $ h_body = "dap/podarok.png"
    show screen daphne_main
    hide screen blkfade
    with Dissolve(1.5)
    pause 1.0
    play music "music/Daphne.mp3" fadein 1 fadeout 1
    dap "привет, мальчики"
    g9 "моя девочка"
    pause 0.5
    mal "черт, я знал, я знал что это правда"
    mal2 "Вот это дойки, я думал она туда подкладывает что-то"
    mal3 "годы тренировок действительно стоили того, чтобы потерять девственность с Дафной Гринграсс"
    fem "Вы извращенцы, вы что действительно будете ее..."
    mal "почему бы нет"
    show screen blkfade
    with dissolve
    hide screen bld1
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve1.png"
    show screen end_u_1
    hide screen blkfade
    with Dissolve(0.8)
    mal2 "Так, я капитан команды, значит я первый!"
    mal "Эй ты, после  меня!"
    mal3 "Как бы не так!"
    pause 0.8
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve2.png"
    show screen end_u_1
    with dissolve
    play sound "sounds/gltch.mp3"
    with vpunch
    play sound "sounds/gltch.mp3"
    with vpunch
    dap "ах"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve13.png"
    show screen end_u_1
    with dissolve
    play sound "sounds/gltch.mp3"
    with vpunch
    play sound "sounds/gltch.mp3"
    with vpunch
    mal2 "Черт, она явно не девственница"
    scene ve2 with dissolve
    mal "ты что идиот, она с половиной команды уже перетрахалась"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve15.png"
    show screen end_u_1
    with dissolve

    dap "давай... глубже..."
    mal2 "ах ты сучка!"
    # звук фть

    
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve16.png"
    show screen end_u_1
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    dap "хах..."
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    mal "черт... я не хочу просто так смотреть"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve300.png"
    show screen end_u_1
    with dissolve
    mal "пододвинься"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve3.png"
    show screen end_u_1
    with dissolve
    dap "А? чего?"
    mal "Мисс Гринграсс, откройте ваш высокорожденный рот"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve4.png"
    show screen end_u_1
    with dissolve
    dap "ммм-ммм--ммм"
    mal3 "хаха"
    mal "Ахх, черт"
    mal "вот это ништяк"
    dap "ммм--ммм-мм"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    dap "ммм-ммм--ммм"
    mal2 "как же круто"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve17.png"
    show screen end_u_1
    with dissolve
    mal2 "ох черт, хах"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve18.png"
    show screen end_u_1
    with dissolve
    mal2 "ну что, Кто следующий?"

    mal3 "Я!"
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve4.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    dap "гхм... ммм... ммм"
    mal3 "что ты там мычишь, шлюха?"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    dap "чмок-чмок-чмок"
    mal3 "я всегда знал, что за пафосной сучкой скрывается обычная блядина"
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    dap "гхм... ммм... ммм"
    mal4 "Черт, я тоже хочу"
    hide screen end_u_1
    hide screen vechel
    $ end_u_1_pic =  "end/ve5.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    #show vechel over ve5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    pause 0.5
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve6.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    #show vechel over ve6
    dap "мм--ммм---мммм"
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve19.png"
    show screen end_u_1
    show screen vechel
    with dissolve

    mal4"охх... ооо"
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve21.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    play sound "sounds/gltch.mp3"
    with vpunch
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve24.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    dap "Да..."
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve25.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    dap "ммм---мммм--ммм"
    mal2 "Черт..."
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve22.png"
    show screen end_u_1
    show screen vechel
    with dissolve
    play sound "sounds/gltch.mp3"
    with vpunch
    mal2 "хааааа"
    dap "мгм-мгмл-мгм"
    hide screen vechel
    hide screen end_u_1
    $ end_u_1_pic =  "end/ve30.png"
    show screen end_u_1
    with Dissolve(1.0)
    pause
    dap "да...{w} давайте все!"
    mal3 "вот ведь шлюха"
    mal "получай!"
    hide screen end_u_1
    $ end_u_1_pic =  "dap_cum1"
    show screen end_u_1
    with dissolve
    pause
    mal2 "хаа!"
    hide screen end_u_1
    $ end_u_1_pic =  "dap_cum2"
    show screen end_u_1
    with dissolve
    pause
    mal3 "дааа!"
    hide screen end_u_1
    $ end_u_1_pic =  "dap_cum3"
    show screen end_u_1
    with dissolve
    pause
    dap "ммм - ммм - ммм"
    g6 "...."
    g9 "Наши уроки явно не прошли зря"


    scene blkfade
    with dissolve
    pause 2.0
    $ h_body = "dap/d_sp1.png" #Sprite of Hermione's upper body.
    $ end_u_1_pic =  "03_hp/17_ending/02_1.png"
    show screen end_u_1
    with Dissolve(1.0)
    g9 "эта сучка действительно сошла с ума"
    m "наверное, я даже перестарался"
    m "..."
    g9 "нее...."
    m "что? кто-то идет?"
    $ h_body = "dap/d_sp1.png" #Sprite of Hermione's upper body.
    show screen daphne_main
    with Dissolve(1.0)
    pause 2.0
    
    m "..."
    dap "..."
    $ h_body = "dap/d_sp2.png" #Sprite of Hermione's upper body.
    dap "А... профессор? вы здесь?"
    $ h_body = "dap/d_sp3.png" #Sprite of Hermione's upper body.
    m "как ты, девочка?"
    $ h_body = "dap/d_sp2.png" #Sprite of Hermione's upper body.

    dap "Эм... я..."
    $ h_body = "dap/d_sp4.png" #Sprite of Hermione's upper body.

    dap "у меня не получилось выполнить ваше задание..."
    m "Все хорошо, ты молодец"
    $ h_body = "dap/d_sp2.png" #Sprite of Hermione's upper body.

    dap "спасибо, профессор"
    $ h_body = "dap/d_sp4.png" #Sprite of Hermione's upper body.

    dap "Я... пойду, наверное..."
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main32
    hide screen daphne_main
    hide screen daphne_main2
    hide screen daphne_main3
    with Dissolve(1.0)
    m "...."
    m "Мне даже стыдно...{w} немного...."
    "*голоса*"
    $ daphne_event = 15
    g4 "пора возвращаться, а то меня заметят"
    hide screen end_u_1
    jump day_start



label snape_afterdaph:
    m "так значит история с этой Гринграсс закончилась?"
    sna_09 "да, у нее теперь достаточно дел и без нас"
    sna_14 "Ей придется очень сильно постараться, чтобы обвинить хогвартс в разврате, не затрагивая слухов о своей дочурке"
    sna_18 "Поэтому она приложит все усилия, чтобы никто даже не смотрел в нашу сторону"
    m "стало быть все отлично получилось"
    sna_19 "да"
    m "а что будет с младшей?"
    sna_01 "кое кто из ее родственников попросил дать ей отпуск на время всей шумихи"
    m "думаешь, она вернется?"
    sna_17 "по крайней мере, не в ближайшее время"
    call sly_plus from _call_sly_plus_16
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    #$ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    #$ sfmax = True # Turns TRUE when friendship with Snape been maxed out.
    return

return
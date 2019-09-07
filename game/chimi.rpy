label summon_chimi:
    if (chimi_chated == 1) and (daytime == True):
        "Чжоу Чанг уже ушла на уроки"
        jump day_main_menu
    elif (chimi_chated == 1) and (daytime == False):
        "Чжоу Чанг уже спит"
        jump day_main_menu
    elif chimi_chated == 0:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ menu_x = 0.2
        $ chimi_chibi_xpos = 320 #Near the desk.
        show screen chimi_02 #Hermione stands still.
        show screen bld1
        with d3
        $ ch_body = "f/cho_def.png" #Sprite of Hermione's upper body.
        show screen chimi_main
        with d3
        chi "Вы звали меня профессор?"
        jump chimi_menu

label chimi_menu:
    $ ch_body = "f/cho_def.png"
    menu:
        chi "Вы звали меня профессор?"

        "Задание: \"Лучшее в мире лекарство\"" if (chimi_event == 9) and (viagra >= 1):
            m "Мисс Чанг"
            $ viagra -= 1
            $ ch_body = "f/cho_govor.png"
            chi "да?"
            $ ch_body = "f/cho_def.png"
            m "вы принимаете лекарство, которое дает вам профессор снейп?"
            $ ch_body = "f/cho_smile3.png"
            chi "эм... да"
            $ ch_body = "f/cho_smile3.png"
            m "оно вам помогает?"
            $ ch_body = "f/cho_grust.png"
            chi "ну... наверное, по крайней мере я не замечала новых провалов памяти"
            m "хм..."
            m "то есть вы не помните, как вчера пришли в мужскую спальню и начали раздеваться?"
            $ ch_body = "f/cho_udivl.png"
            chi "что?"
            g9 "..."
            m "я так и думал"
            $ ch_body = "f/cho_smile3.png"
            chi "разве я..."
            m "похоже, что лекарства, которое дает вам профессор снейп явно не достаточно"
            $ ch_body = "f/cho_grust.png"
            chi "..."
            m "Принимайте вот это по 1 ложке каждый вечер"
            
            show screen gift
            $ the_gift = "03_hp/18_store/34.png" # BUTTERBEER.
            ">Вы передаете Чжоу Чанг возбуждающее зелье"
            hide screen gift
            pause 1.0
            
            $ ch_body = "f/cho_smile3.png"
            chi "хм..."
            $ ch_body = "f/cho_govor.png"
            chi "да профессор"
            $ ch_body = "f/cho_def.png"
            g9 "отлично"
            $ ch_body = "f/cho_smile3.png"
            chi "..."
            g4 "ты не хочешь выпить его прямо сейчас?"
            $ ch_body = "f/cho_udivl.png"
            chi "эм...."
            $ ch_body = "f/cho_grust.png"
            chi "хорошо"
            
            $ ch_body = "f/cho_gipn.png"
            chi "...."
            m "сработало?"
            $ ch_body = "f/cho_gipn.png"
            chi "хах"
            m "как ты себя чувствуешь?"
            $ ch_body = "f/cho_gipn_smile.png"
            chi "я.... я хочу..."
            g9 "*шикардос*"
            m "ну так что, можем начинать?"
            $ ch_body = "f/cho_gipn.png"
            chi "а... что?"
            $ ch_body = "f/cho_smile3.png"
            chi "как же.... ах..."
            m "хах"
            g9 "ты ничего не хочешь мне сделать"
            $ ch_body = "f/cho_gipn.png"
            chi "я хочу... ах..."
            g9 "..."
            $ ch_body = "f/cho_yaz.png"
            chi "профессор... пожалуйста..."
            m "да, я слушаю"
            $ ch_body = "f/cho_smile3.png"
            chi "мне нужно выйти..."
            m "..."
            g4 "что? зачем?"
            $ ch_body = "f/cho_zakr6.png"
            chi "хах... пожалуйста... мне очень нужно..."
            g4 "а что, ты не можешь здесь?"
            $ ch_body = "f/cho_zakr5.png"
            chi "я... я не могу... пожалуйста, мне очень нужно"
            g4 "вот сука"
            m "...."
            $ ch_body = "f/cho_yaz.png"
            chi "профессор... пожалуйста..."
            m "ты можешь идти"
            $ ch_body = "f/cho_gipn.png"
            chi "да... спасибо..."            
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            hide screen bld1
            hide screen chimi_main
            hide screen blktone
            hide screen chimi_02
            hide screen ctc
            with d3
            $ chimi_chated = 1
            g4 "черт..."
            m "..."
            m "эм... оно точно сработало так как мне кажется или ей просто..."
            g4 "черт теперь и не узнать"
            $ chimi_event = 10
            $ chimi_chated = 1
            if daytime:

                jump night_main_menu
            else:

                jump day_main_menu


        "-Болтать-":
            $ ch_body = "f/cho_govor.png"
            $ trig = renpy.random.randint(1, 6)
            if trig == 1:
                chi "Последнее время за мной постоянно вьется Поттер, наверное, еще не дорос до того, что для того, чтобы понравится девушке, нужно кое что другое"
            elif trig == 2:
                chi "Последнее время почему-то все изменились, не могу понять почему...{w} ходят, шепчутся о чем-то..."
            elif trig == 3:
                chi "Говорят, последнее время здесь творится что-то неладное{w}, я слышала, что на кого-то напали, но мне так и не сказали на кого"
            elif trig == 4:
                chi "Новый санитар какой-то странный{w}, сначала он просто был озобоченным придурком, а теперь еще и ищет непонятно кого"
            elif trig == 5:
                chi "Говорят это все Тот-кого-нельзя-называть... ха!... по мне так просто очередной маньяк-извращенец"
            elif trig == 6:
                chi "Я учавствую в турнире дуэльного клуба, эта Грейнджер считает, что у нее все равно есть шансы, ха!"

            jump chimi_menu


        "-Как прошел день?-":
            if (chimi_event == 11) or (chimi_event == 12):
                m "Мисс Чанг?"
                $ ch_body = "f/cho_govor.png"
                chi "Да, профессор?"
                $ ch_body = "f/cho_def.png"
                m "Вы можете рассказать что было вчера вечером?"
                $ ch_body = "f/cho_grust.png"
                chi "Эм..."
                $ ch_body = "f/cho_smile3.png"
                chi "Я вышла из вашего кабинета, потом..."
                $ ch_body = "f/cho_grust.png"
                chi "эм..."
                $ ch_body = "f/cho_smile3.png"
                chi "дальше я... эм..."
                $ ch_body = "f/cho_nedov1.png"
                chi "в общем, ничего особенного, я пошла в спальню и все"
                $ ch_body = "f/cho_nedov2.png"
                g4 "эта сука что-то скрывает"
                m "понятно"
                if chimi_event == 11:
                    m "может быть этот очкарик что-то расскажет?"
                    $ chimi_event = 12
                elif (chimi_event == 12) and (ogon2 != 0):
                    m "хм... а ведь..."
                    g9 "я могу посмотреть в огонь"
                    m "Нужно только дождаться полнолуния"
                    $ chimi_event = 13
                jump chimi_menu

            else:
                $ ch_body = "f/cho_govor.png"
                chi "Как прошел мой день?"
                $ ch_body = "f/cho_udivl.png"
                chi "Почему вы это спрашиваете?"
                m "Не случалось ли чего-то странного?"
                $ ch_body = "f/cho_def.png"
                chi "Ну..."
                $ trig = renpy.random.randint(1, 4)
                if trig == 1:
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Этот Поттер буквально преследует меня...{w} Не подходит и не говорит ничего, но как не оглянусь, он постоянно где-то за углом..."
                elif trig == 2:
                    $ ch_body = "f/cho_grust.png"
                    chi "почему то многие начали избегать меня...{w} не могу понять, что произошло?"
                elif trig == 3:
                    $ ch_body = "f/cho_smile1.png"
                    chi "Я заметила как этот новый врач засматривается на парней... хотя сейчас наверное это уже и не назовешь странным"
                elif trig == 4:
                    $ ch_body = "f/cho_govor.png"
                    chi "Эм... да нет, ничего такого"

            m "хм..."
            m "Значит ничего"
            jump chimi_menu



        "-Предложить купить сексуальные услуги-":
            m "Мисс, Чанг, вам не кажется, что ваш факультет сильно отстает в гонке за кубок?"
            $ ch_body = "f/cho_nedov1.png"
            chi "Эм... Ну а что делать, если у нас нет ни профессора Снейпа, который дает очки только своему факультету, ни Грейнджер, которая..."
            $ ch_body = "f/cho_def.png"
            m "Которая что?"
            chi "..."
            $ ch_body = "f/cho_smile1.png"
            chi "Неважно"
            menu:

                "А ведь вы могли бы быть не хуже Гермионы Грейнджер":
                    $ ch_body = "f/cho_evil.png"
                    chi "Ха, ну это как посмотреть, я думаю мало кто хотел бы быть лучше Грейнджер в этом плане"
                    g4 "*сука*"
                    $ ch_body = "f/cho_def.png"
                    m "Тем не менее, вы могли бы очень хорошо помочь своему факультету"
                    $ ch_body = "f/cho_nedov2.png"
                    chi "..."
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Каким образом?"
                    $ ch_body = "f/cho_nedov2.png"
                    m "Возможно вы слышали о том, что у девушек есть некоторые преимущества в получении очков"
                    $ ch_body = "f/cho_nedov2.png"
                    chi "..."
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Я поняла на что вы намекаете с первой же фразы, и можете быть уверены, профессор Дамблдор, что я такими вещами не занимаюсь"
                    $ ch_body = "f/cho_evil.png"
                    chi "Вы ведь говорите это, чтобы меня проверить, не так ли"
                    g4 "..."
                    m "Конечно же"
                    jump chimi_menu

                "Вы можете заработать очки для вашего факультета прямо сейчас":
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Я? Сейчас?"
                    $ ch_body = "f/cho_nedov2.png"
                    chi "..."
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Как?"
                    $ ch_body = "f/cho_nedov2.png"
                    m "Возможно вы слышали о том, что у девушек есть некоторые преимущества в получении очков"
                    chi "..."
                    $ ch_body = "f/cho_nedov1.png"
                    chi "Я поняла на что вы намекаете с первой же фразы, и можете быть уверены, профессор Дамблдор, что я такими вещами не занимаюсь"
                    $ ch_body = "f/cho_evil.png"
                    chi "Вы ведь говорите это, чтобы меня проверить, не так ли"
                    g4 "..."
                    m "Конечно же"
                    jump chimi_menu





        "-Ты свободна-":
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            hide screen bld1
            hide screen chimi_main
            hide screen blktone
            hide screen chimi_02
            hide screen ctc
            with d3
            $ chimi_chated = 1
            if daytime:

                jump night_main_menu
            else:

                jump day_main_menu

label chimi_gang_bang:
    "тук-тук-тук"
    m "..."
    g4 "кто угодно, только не та старая ведьма"
    # входит
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ chimi_chibi_xpos = 610
    $ chimi_chibi_ypos = 250
    show screen chimi_01 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=300 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen chimi_walk2
    pause 3
    $ chimi_chibi_xpos = 300 #Near the desk.
    show screen chimi_01 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    $ ch_body = "f/sperm_govor.png" #Sprite of Hermione's upper body.
    show screen chimi_main
    show screen chimi_01
    show screen ctc
    with Dissolve(.3)
    pause
    show screen chimi_main
    with d3
    hide screen ctc
    chi "профессор"
    $ ch_body = "f/sperm_yaz.png"
    g6 ".............."

    chi "Мне показалось.... "
    $ ch_body = "f/sperm_yaz.png"
    g5 "Твою мать, что с тобой произошло?"

    chi "Со мной?{w} Что?"
    $ ch_body = "f/sperm_yaz.png"
    m "..."

    chi "{size=+5}{b}Он{/b}{/size} сказал, что я должна зайти к вам"
    $ ch_body = "f/sperm_yaz.png"
    m "..."
    m "Кто он?"

    chi "эм... я не помню..."
    $ ch_body = "f/sperm_yaz.png"
    m "Похоже она не очень понимает происходящее"
    g6 "Что последнее ты помнишь?"

    chi "Последнее?"
    chi "Я шла в аудиторию... потом кто-то позвал меня..."
    chi "Потом я сняла с себя одежду и..."
    $ ch_body = "f/sperm_yaz.png"
    m "..........."
    g9 "крутяк"

    chi "Я взяла его{w}... потом {size=+5}{b}он{/b}{/size} вставил его мне в..."
    $ ch_body = "f/sperm_yaz.png"
    g9 "..."

    chi "{size=+5}{b}Он{/b}{/size} просил называть его люци"
    $ ch_body = "f/sperm_yaz.png"
    g9 "ага"

    chi "это продолжалось около трех часов"
    $ ch_body = "f/sperm_yaz.png"
    g9 "фигасе"

    chi "что мне делать дальше, профессор?"
    $ ch_body = "f/sperm_yaz.png"
    m "хм..."

    chi "я бы могла..."
    $ ch_body = "f/sperm_yaz.png"
    g4 "не сейчас"
    $ ch_body = "f/sperm_smile.png"
    chi "вы уверены? я хочу взять ваш член себе в рот"

    g4 "......."
    chi "потом скакать на нем как наездница"
    g4 "..."
    $ ch_body = "f/sperm_yaz.png"
    m "*надо будет позвать ее завтра*"
    m "тебе лучше сейчас передохнуть, а завтра приходи ко мне"

    chi "да, профессор"
    hide screen chimi_02
    hide screen chimi_01
    hide screen chimi_main
    hide screen chimi_main2
    with d3
    hide screen ctc
    hide screen bld1
    with d3
    g9  "*мой гарем пополнился еще и азиаточкой*"
    g4 "чертов демон, надо узнать как он делает это"
    $ renpy.play('sounds/win2.mp3')
    ">теперь вы можете вызывать Чжоу Чанг"
    $ chimi_event = 1
    $ chimi_chated = 1
    if daytime:

        jump night_main_menu
    else:

        jump day_main_menu







label chihmi_second_norm:
    if (chimi_chated == 1) and (daytime == True):
        "Чжоу Чанг уже ушла на уроки"
        if daytime:

            jump night_main_menu
        else:

            jump day_main_menu
    elif (chimi_chated == 1) and (daytime == False):
        "Чжоу Чанг уже спит"
        if daytime:

            jump night_main_menu
        else:

            jump day_main_menu
    elif chimi_chated == 0:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ menu_x = 0.2
        $ chimi_chibi_xpos = 320 #Near the desk.
        show screen chimi_02 #Hermione stands still.
        show screen bld1
        with d3
        $ ch_body = "f/cho_def.png" #Sprite of Hermione's upper body.
        show screen chimi_main
        with d3
        $ ch_body = "f/cho_def.png"
        chi "Здравствуйте, профессор. Мне сказали вы звали меня"
        m "Да, звал"

        chi "......"
        g9 "................"
        $ ch_body = "f/cho_nedov2.png"
        chi "............................."
        $ ch_body = "f/cho_nedov1.png"
        chi "По какому вопросу?"
        $ ch_body = "f/cho_nedov2.png"
        g4 "*По какому вопросу? После того вечера она решила делать вид, что ничего не было?*"
        m "Кхем-кхем...{w} Вы провинились, мисс Чанг. Мне придется..."
        g9 "Наказать вас"
        $ ch_body = "f/cho_govor.png"
        chi "Что? Провинилась? В чем???"
        $ ch_body = "f/cho_def.png"
        m "..."
        g4 "*Она прикидывается что ли?*"
        m "Эм... ну..."
        g4 "В том, в чем вы провинились в прошлый раз!"
        $ ch_body = "f/cho_grust.png"
        chi "В прошлый раз?{w} Я не помню, чтобы провинялась в чем-то, профессор"
        m "..."
        m "*У меня есть одна теория, но ее нужно проверить...*"
        menu gang_dopr:
            "Закрой глаза и представь зяблика":

                $ ch_body = "f/cho_udivl.png"
                chi "Что? Зяблика? Эм..."
                pause 1.0
                $ ch_body = "f/cho_zakr3.png"
                chi "Представила..."
                $ ch_body = "f/cho_zakr1.png"
                m "Отлично..."
                m "Как выглядит этот зяблик?"
                $ ch_body = "f/cho_zakr3.png"
                chi "Эм... ну... Он средних размеров... у него есть крылья... и он...{w}... зяблик..."
                $ ch_body = "f/cho_zakr1.png"
                m "А как тебя зову?!"
                $ ch_body = "f/cho_zakr3.png"
                chi "Чжоу Чанг"
                $ ch_body = "f/cho_zakr1.png"
                m "Столица Великобритании?!!"
                $ ch_body = "f/cho_zakr3.png"
                chi "Москва"
                $ ch_body = "f/cho_zakr1.png"

                m "Ты помнишь как тебя оприходовал огромный демон?!!"
                pause 1.0
                $ ch_body = "f/cho_nedov2.png"
                chi "...{w}...{w}...................{w} о чем вы профессор?"
                m "Понятно..."
                m "Спасибо, мисс Чанг, вы мне очень помогли в моем исследовании"
                $ ch_body = "f/cho_nedov1.png"
                chi "Исследовании? Каком исследовании??"
                m "Совершенно секретном, конечно же"
                $ ch_body = "f/cho_nedov2.png"
                chi "..."
                g4 "Чертов демон, не мог подольше подержать свои чары..."
                $ chimi_event = 2
                jump gang_dopr


            "Ты последнее время ничего ни чем таким не занималась с парнями из слизерина?":
                chi "Эмм... я не очень понимаю о чем вы, профессор..."
                $ ch_body = "f/cho_govor.png"
                chi "Нет, ничем \"Таким\" я с ними не занималась"
                $ ch_body = "f/cho_nedov1.png"
                g4 "Чертов демон, не мог подольше подержать свои чары..."
                $ chimi_event = 2
                jump gang_dopr
            "Ты не замечала последнее время никого красного с рогами?":
                $ ch_body = "f/cho_udivl.png"
                chi "Красного с рогами?"
                $ ch_body = "f/cho_smile2.png"
                chi "Конечно же!"
                g4 "Действительно видела?"
                $ ch_body = "f/cho_smile1.png"
                chi "Да, Хагрид показывал нам сатира"
                $ ch_body = "f/cho_def.png"
                m "..."
                m "Сатира?"
                $ ch_body = "f/cho_govor.png"
                chi "Да, он показывал как защищаться от его магии"
                $ ch_body = "f/cho_def.png"
                g4 "*Она точно не издевается?*"

                g4 "Чертов демон, не мог подольше подержать свои чары..."
                $ chimi_event = 2
                jump gang_dopr
            "Ты не помнишь того как приходила сюда недавно?":
                $ ch_body = "f/cho_udivl.png"
                chi "Как недавно?"
                $ ch_body = "f/cho_def.png"
                m "..."
                g4 "Недавно"
                $ ch_body = "f/cho_govor.png"
                chi "Ну... последний раз я была здесь летом, когда делали ремонт"
                $ ch_body = "f/cho_def.png"
                m "*блять*"
                g4 "Чертов демон, не мог подольше подержать свои чары..."
                $ chimi_event = 2
                jump gang_dopr

            "ты можешь идти" if chimi_event == 2:
                $ menu_x = 0.5 #Menu position is back to default. (Center).
                hide screen bld1
                hide screen chimi_main
                hide screen blktone
                hide screen chimi_02
                hide screen ctc
                with d3
                $ chimi_chated = 1
                $ chimi_event = 2
                m "Вот черт"
                if daytime:

                    jump night_main_menu
                else:

                    jump day_main_menu




label chim_moon1:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ chimi_chibi_xpos = 610
    $ chimi_chibi_ypos = 250
    show screen chimi_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=350 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen chimi_walk1
    pause 3
    $ chimi_chibi_xpos = 350 #Near the desk.
    show screen chimi_02 #Hermione stands still.
    pause.5

    with Dissolve(.3)
    $ ch_body = "f/cho_gipn.png" #Sprite of Hermione's upper body.
    show screen chimi_main
    show screen chimi_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen chimi_main
    with d3
    hide screen ctc
    # zahodit
    $ ch_body = "f/cho_gipn.png"
    chi "Вы.....{w} звали меня.... профессор?"
    m ".................{w} эм........{w}........{w} сработало?"
    chi "................."
    m "как ты себя чувствуешь?"
    $ ch_body = "f/cho_gipn_rot.png"
    chi "я..... {w} я......"
    g9 "......."
    g9 "ништяк"
    m "значит очкарик не врал"
    g9 "ну что, джинни, пришло твое время, ты ведь еще никогда не трахал азиаточек?"

    show screen blkfade
    with d9
    hide screen genie
    hide screen chimi
    hide screen chimi_main
    $ chimi_sex = "cho_blowjob"
    show screen gin_chimi
    show screen desk_02
    ">Чжо Чанг залезает под стол"
    pause 1.0
    hide screen blkfade
    with d8
    g9 "......"
    chi_gipn "*Хлюп* *Чавк!* *Хлюп!*"
    g9 "........"
    m "все таки ты можешь быть не такой стервозной сучкой, да?"
    chi_gipn "*мглм*  *мглм*  *мглм*  *мглм*"
    g9 "хахахахаахаха"
    $ renpy.play('sounds/knocking.mp3')
    "тук-тук-тук"
    m "эм....."
    g4 "кто это так невовремя?"
    harr "это я, Гарри Поттер"
    m "........"
    m "хм"
    hide screen gin_chimi
    hide screen desk_02
    $ chimi_sex = "cho_minet2"
    show screen gin_chimi4
    with d6
    g9 "проходи, Гарри"

    pause 1.0
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
    g9 "что-то опять стреслось, гарри?"
    $ har_body = "f/hr_govor.png"
    harr "нет, профессор"
    $ har_body = "f/hr_def.png"
    pause .5
    $ har_body = "f/hr_govor.png"
    harr "просто я следил за Чжо Чанг и мне показалось, что она зашла сюда"
    $ har_body = "f/hr_def.png"
    chi_gipn "*чавк* *чавк* *чавк* *чавк*"
    m ".........................."

    g9 "но ее здесь нет"
    $ har_body = "f/hr_govor.png"
    harr "я понял"
    $ har_body = "f/hr_def.png"
    pause
    $ har_body = "f/hr_govor.png"
    harr "ладно я тогда пойду"
    $ har_body = "f/hr_def.png"
    g9 "стой......"
    harr "..........."
    $ har_body = "f/hr_govor.png"
    harr "да, профессор?"
    $ har_body = "f/hr_def.png"
    m "ты что-нибудь нашел по тому как нам избавиться от этого Шмардепорта?"
    $ har_body = "f/hr_govor.png"
    harr "еще нет, профессор"
    $ har_body = "f/hr_def.png"
    pause 1.0
    $ har_body = "f/hr_smile.png"
    harr "но я уже вышел на его след"

    g9 "неужели"
    m "что ты смог найти, гарри?"
    $ har_body = "f/hr_govor.png"
    harr "исходя из его активности, я понял что он постоянно находится в Хогвартсе"
    $ har_body = "f/hr_def.png"
    m "........."
    $ har_body = "f/hr_govor.png"
    harr "да, и скорее всего маскируется под одного из нас"
    $ har_body = "f/hr_def.png"
    m ".........{w} неужели?"
    $ har_body = "f/hr_govor.png"
    harr "вероятно, под одного из преподавателей, скорее всего профессоров"
    $ har_body = "f/hr_def.png"
    g4 "......................................{w} ты уверен?"
    $ har_body = "f/hr_govor.png"
    harr "все доказательства говорят об этом"
    $ har_body = "f/hr_def.png"
    g4 "....."
    chi_gipn "мгл мглм мглм мглм чмок мглм мглм мглм"
    $ har_body = "f/hr_udivl.png"
    harr "что это было, профессор?"

    g4 "это.....{w} мой живот урчит"
    $ har_body = "f/hr_def.png"
    harr "......."
    m "ты копаешь не в ту сторону, Гарри"
    harr "......."
    m "не нужно вычислять, как он попал сюда, нужно найти способ избавиться от него"
    $ har_body = "f/hr_govor.png"
    harr "эм.... но если мы не найдем........"
    $ har_body = "f/hr_def.png"
    m "пока ты ищешь способ от него избавиться я позабочусь о том, чтобы найти его"
    harr "........"
    $ har_body = "f/hr_govor.png"
    harr "да, профессор"
    $ har_body = "f/hr_def.png"
    chi_gipn "мглмглм чмок чмок мглм мглм мглмг"
    harr "............"
    g4 "............"
    m "ты можешь идти, Гарри"
    $ har_body = "f/hr_govor.png"
    harr "да, профессор"
    $ har_body = "f/hr_def.png"
    pause 1.0
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

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen harry_ch2 #Hermione stands still.
    with d3
    pause
    g4 "похоже снейп не шутил, когда говорил, что лучше держаться от него подальше"
    chi_gipn "*чавк* *чавк* *чмок*"
    g9 "да, вот так"
    ">вы чувствуете, что начинаете приплывать"
    show screen blkfade
    with d9
    hide screen gin_chimi
    hide screen desk_02
    hide screen gin_chimi2
    hide screen gin_chimi4
    pause 1.0
    with vpunch
    g4 "ах ты гребаная шлюха!"
    chi_sperm "........"
    pause 2.0
    show screen genie
    show screen chimi_02

    hide screen blkfade
    with d9
    pause .5
    show screen chimi_main
    pause 2.0
    m "можете идти в свою комнату, мисс Чанг"
    chi "....."
    $ chimi_event = 4
    $ chimi_level += 1
    $ chimi_chated = 1
    $ harry_chated = 1
    hide screen chimi_main
    hide screen chimi_02
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause .5
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    if daytime:
        jump night_main_menu
    else:

        jump day_main_menu


label chimi_after:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01
    with d3
    pause 2.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    pause 2.0
    $ s_sprite = "03_hp/10_snape_main/24.png"
    sna "Я позаботился о том, чтобы у нее больше не было таких приступов"
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    sna "но причину попадания в транс я так и не нашел"
    m "........."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "не знаешь, изза чего это с ней произошло?"
    m ".........."
    g4 "*он испортит мне всю малину*"
    m "хм....."
    m "нет, не знаю"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "........."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "ладно"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    sna "по крайней мере она больше не попытается кого-то убить"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "но если не устранить первопричину, то это может привести к непредсказумым последствиям"
    m "да?"
    m "каким например?"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "это какая-то очень древняя магия, я не специалист в этом, я сомневаюсь, что вообще где-то есть такой специалист"
    m "понятно"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "лучше не стоит ее больше трогать"
    g4 "..........."
    m "я понял"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "......."
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"
    sna "но все таки это, конечно, было весьма весело"
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
    $ chitchated_with_snape = True
    pause 1.5
    g4 "не стоит ее больше трогать джинни, еби собственный кулак, джинни, может тебе вообще сесть и ничего не делать, джинни?!!"
    $ chimi_event = 7
    $ chimi_level = 6
    return


label chim_moon:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ chimi_chibi_xpos = 610
    $ chimi_chibi_ypos = 250
    show screen chimi_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=350 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen chimi_walk1
    pause 3
    $ chimi_chibi_xpos = 350 #Near the desk.
    show screen chimi_02 #Hermione stands still.
    pause.5

    with Dissolve(.3)
    $ ch_body = "f/cho_gipn.png" #Sprite of Hermione's upper body.
    show screen chimi_main
    show screen chimi_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen chimi_main
    with d3
    hide screen ctc
    # zahodit
    $ ch_body = "f/cho_gipn.png"
    chi "Вы.....{w} звали меня.... профессор?"
    g9 "..........."
    m "в этот раз нам никто не помешает"
    chi "............"
    m "хм..."
    m "интересно, как работает эта магия?"
    m "ты помнишь кто я?"
    $ ch_body = "f/cho_gipn_smile.png"
    chi "{size=+5}{b}Он{/b}{/size} говорил, что ты джин"
    m "........................."
    g4 "че он говорил?"
    $ ch_body = "f/cho_gipn_rot.png"
    chi "и то что ты скоро сдохнешь"
    $ ch_body = "f/cho_gipn_smile.png"
    g4 "че???"
    chi "..........."
    pause 2.0
    $ ch_body = "f/cho1.png"
    pause 0.7
    $ ch_body = "f/cho2.png"
    pause 0.7
    $ ch_body = "f/cho3.png"
    pause 0.7

    $ ch_body = "f/cho4.png"
    pause 0.7
    $ ch_body = "f/cho5.png"
    hide screen chimi_02
    show screen chimi_03
    with dissolve
    pause 0.3
    stop music fadeout 1.0
    play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    $ ch_body = "f/cho_gipn_evil2.png"
    chi "вы все скоро сдохните"
    $ ch_body = "f/cho_gipn_evil.png"
    g4 "..................."
    hide screen genie
    show screen chair_02
    show screen gin_pr3
    show screen desk_02

    with d9
    pause 1.0
    g4 "что за черт......."
    $ ch_body = "f/cho_gipn_evil2.png"
    chi "глупый джин"
    $ ch_body = "f/cho_gipn_evil.png"
    hide screen desk_02
    hide screen chair_02
    show screen lev_chair
    show screen lev_table
    # сдвигает стол
    g4  "черт побери, что происходит"
    $ ch_body = "f/cho_gipn_evil2.png"
    chi "вам всем скоро придет конеееееццццц"
    $ ch_body = "f/cho_gipn_evil.png"
    # лицо
    $ ch_body = "f/cho_gipn_evil5.png"
    g4 "надо было договориться с тем мужиком"
    $ ch_body = "f/cho_gipn_evil2.png"
    chi "молиииииссссссьььь сссссвввооооооииимммммм ббббогггааааммммм джжжжжжииииииинннннннн"
    $ ch_body = "f/cho_gipn_evil5.png"
    g4 ".................."
    stop music fadeout 1.5
    pause 2.0
    $ renpy.play('sounds/knocking.mp3')
    pause 2.0
    hide screen chimi_main
    with d6
    sna "джин, это твои проделки?! у меня все амулеты ходуном ходят!"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    show screen snape_01 #Snape stands still.
    pause.1
    with Dissolve(.3)
    $ tt_xpos=420 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0

    with Dissolve(.3)
    pause 1.0
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    sna_10 ".............."
    sna_08 "что здесь творится......."
    g4 ".........{w} это не я, она сама"
    sna_08 "что с ней?"
    chi_evil "вы все сдохните!"
    sna_04 "это......"
    sna_04 "похоже на одержимость"
    chi_evil "*другим голосом* Северус!"
    sna_01 "..... что?"
    chi_evil "*другим голосом* Северус, это я"
    sna_10 "что???"
    sna_10 "Л-л-л-лили?!"
    g4 "....."
    chi_evil "*другим голосом* ты мне никогда не нравился"
    sna_17 "что?"
    chi_evil "*другим голосом* зачем ты пытался подкатывать ко мне, все ведь знали что у тебя маленький член"
    sna_04 "ах ты тварь"
    hide screen snape_01
    show screen snape_defends2
    with d6
    sna_04 "авахамора!"
    hide screen snape_defends2
    show screen snape_defends3
    $ renpy.play('sounds/attack_snape.ogg')
    pause 1
    show screen blkfade
    hide screen snape_defends3
    with dissolve
    pause 5.0
    chi_gipn "что произошло?"
    show screen chair_02
    show screen desk_02
    hide screen chimi_03
    show screen chimi_02
    hide screen lev_chair
    hide screen lev_table
    hide screen heal3
    show screen snape_01
    with d6
    hide screen blkfade
    with d8
    chi_gipn "................."
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    # после этого
    pause 2.0

    sna_01 "это было.....{w} странно"
    sna_01 "почему ты не позвал меня?"
    m "ну.... {w} она просто пришла и начала такое выделывать"
    sna_08 "пришла сама??"
    m "эм.......{w} ну............{w} да"
    sna_02 ".........."
    sna_01 "почему, когда я пришел в эту дурацкую школу, мне никто не говорил, что можно вот так просто трахать студенток"
    m "........."
    m "ну................."
    chi_gipn "..............."
    g9 "у нас здесь есть одна"
    sna_01 "эм................."
    sna_01 "ты что, хочешь........"
    m "она явно не против"
    sna_21 "........"
    show screen blkfade
    with Dissolve(1.0)
    pause 2.0
    chi_gipn "люблю длинных"
    sna_21 "ах ты шлюха!"
    hide screen snape_02
    hide screen snape_defends2
    show screen chair_02

    show screen desk_02
    hide screen gin_pr3
    hide screen snape_01
    hide screen lev_chair
    hide screen lev_table
    hide screen gin_pr
    hide screen chimi_02
    hide screen chimi_01
    $ chimi_sex = "tripple"
    show screen gin_chimi5
    pause 1.0
    hide screen blkfade
    with d9

    g9 "......."
    sna_21 "вот значит как ты проводишь здесь время?"
    m "...."
    m "на самом деле я даже рад, что попал сюда"
    m "хотя конечно, перенестись в тело султана было бы лучше"
    chi_gipn "мглмглмглм"
    sna_15 "хахаххахаха"
    m "эта Чанг была не особенно сговорчивой до....."
    sna_01 "да, она настоящая заноза"
    sna_16 "хотя кто настоящая заноза, так это грейнджер"
    m "она тоже скоро изменится"
    sna_15 "хахаха"
    sna_09 "повезло мне с тобой, джинни"
    sna_20 "жаль, что не все надоедливые ученики - девушки"
    sna_19 "я бы с удовольствием отдал Поттера тебе"
    m "эм...."
    m "вообще то он уже заходил ко мне"
    sna_10 "........"

    sna_17 "что ему нужно?"
    chi_gipn "мглмглмглмглмгл"
    m "ну...{w} он как раз очень взволнован на счет этой особы"
    sna_01 "будь с ним осторожен, этот мелкий гад может что-то заподозрить"
    m "......"
    m "а мне он показался на редкость тупым"
    sna_14 "хаха, и здесь я не могу с тобой не согласится"
    sna_01 "но все таки будь осторожен"
    show screen blkfade
    with d9
    g4 "аааааггггррррррр"
    sna_05 "ах ты гребаная шлюха!"
    chi_sperm ".........."
    hide screen desk_02
    hide screen chair_02
    show screen genie
    hide screen gin_chimi5
    show screen snape_02
    show screen chimi_02
    $ chimi_chibi_xpos = 300
    pause 1.0
    hide screen blkfade
    with d9
    sna_09 "я позабочусь, чтобы никто не заметил, что мисс чанг пролила гоблинское молочко в кабинете директора"
    chi_sperm "молочко"
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    hide screen bld1
    hide screen chimi_main
    hide screen blktone
    hide screen chimi_02
    hide screen snape_02
    hide screen ctc
    with d3
    $ chimi_event = 6
    $ chimi_chated = 1
    $ snape_chated = True
    $ chimi_level = 4
    if daytime:

        jump night_main_menu
    else:

        jump day_main_menu







label chimi_gipn_harry:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ chimi_chibi_xpos = 610
    $ chimi_chibi_ypos = 250
    show screen chimi_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=350 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen chimi_walk1
    pause 3
    $ chimi_chibi_xpos = 350 #Near the desk.
    show screen chimi_02 #Hermione stands still.
    pause.5

    with Dissolve(.3)
    $ ch_body = "f/cho_gipn.png" #Sprite of Hermione's upper body.
    show screen chimi_main
    show screen chimi_02
    show screen ctc
    with Dissolve(.3)
    pause
    show screen chimi_main
    with d3
    hide screen ctc
    # zahodit
    $ ch_body = "f/cho_gipn.png"
    chi "Вы.....{w} звали меня.... профессор?"
    g9 "..........."
    g9 "мне все больше нравится идея оставить этого демона здесь навсегда"
    m "хм..."
    m "интересно, это происходит только с ней?"
    g4 "главное, чтобы ту старую ведьму это не коснулось"
    chi "что я должна делать?"
    g9 "......................"
    m "хм, дай подумать, в прошлый раз нам немного помешали...."
    g9 "поэтому сегодня мы оттянемся по полной"
    m "раздевайтесь, мисс Чанг"
    chi "........."
    show screen blkfade
    with d8
    hide screen chimi_02
    show screen chimi_01
    $ ch_body = "f/cho_gol_gipn.png"
    hide screen blkfade
    ">Чжоу Чанг снимает с себя одежду"
    pause 0.5
    with d8
    pause 1.5
    g9 "............."
    chi "........"
    m "хм..."
    m "с чего начнем в этот раз?"
    g9 "впереди долгая ночь, девочка"

    hide screen chimi_main
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ harry_chibi_xpos = 610
    $ harry_chibi_ypos = 250
    show screen harry_ch #Hermione stands still.
    with Dissolve(.5)

    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=600 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.

    $ harry_chibi_xpos = 600 #Near the desk.

    show screen bld1
    with Dissolve(.3)
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ har_body = "f/hr_govor.png" #Sprite of Hermione's upper body.
    show screen harry_main
    show screen harry_ch
    show screen ctc
    with Dissolve(.3)
    show screen harry_main
    with d3
    hide screen ctc
    harr "профессор, я......."
    $ har_body = "f/hr_udivl.png"
    harr "...................."
    $ har_body = "f/hr_udivl.png" #Sprite of Hermione's upper body.
    g4 "..................................."
    hide screen harry_main
    show screen chimi_main
    chi "........."
    hide screen chimi_main
    show screen harry_main
    harr "............"
    g4 "гарри.......{w} ты как раз вовремя"
    harr "професоор......"
    g4 "я как раз закончил.......{w} читать заклинание"
    $ har_body = "f/hr_def.png"
    pause 1.0
    $ har_body = "f/hr_govor.png"
    harr "заклинание?"
    $ har_body = "f/hr_govor.png"
    g4 "да........{w}...............{w} заклинание"
    m "похоже Ворандесорт наложил на нее какой-то очень сильный сглаз"
    $ har_body = "f/hr_udivl.png"
    harr ".........."
    m "да{w}.............{w}..........................{w}..........................."
    m "но сегодняшний эксперимент не прошел зря...."
    g9 "по крайней мере, мы теперь точно знаем, что заклинание держится не за счет одежды"
    $ har_body = "f/hr_def.png"
    pause 1.0
    $ har_body = "f/hr_govor.png"
    harr "одежды?"
    $ har_body = "f/hr_def.png"
    g9 "да, это точно не насисечный сглаз, ты будешь проходить его на следующем курсе"
    $ har_body = "f/hr_udivl.png"
    harr "насисечный сглаз? ого!"
    $ har_body = "f/hr_def.png"
    chi_gipn "так что, вы же хотели заняться с..."
    g4 "мне срочно нужно заняться составлением отчета в министерство магии"
    $ har_body = "f/hr_def.png"
    harr "......."
    m "помоги мисс Чанг дойти до комнаты и.... тебе придется охранять ее этой ночью"
    $ har_body = "f/hr_govor.png"
    harr "охранять?"
    hide screen harry_main
    show screen chimi_main
    chi "так что, вы же хотели...."
    hide screen chimi_main
    show screen harry_main
    $ har_body = "f/hr_morda1.png"
    harr "да, профессор"
    g4 "может хоть так он от меня отстанет"
    show screen blkfade
    pause 0.1
    hide screen harry_main
    hide screen harry_ch
    hide screen chimi_02
    hide screen chimi_01
    hide screen bld1
    hide screen ctc
    $ harry_chimi = 1
    $ harry_chated = 1
    $ chimi_chated = 1
    $ chimi_event = 5
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause .5
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    if daytime:
        jump night_main_menu
    else:

        jump day_main_menu



label thehat:
    menu:
        "saves from any versions of WT":
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




            $ jasm = "jas03"

            $ titfuck_points = 0
            # нужно сделать еще что он должен сначала купить эту книгу
        # ===================\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            $ mizul = 0
            $ ogon_first = 0
            m "Done"
            call screen main_menu_01

        "saves from old version of fanmod":
            $ dap_pod = 0
            $ hagpot = 0 # поушен превращения в хагрида
            $ chimi_level = 0
            $ daphne_publ_request = 0   # триггер публичных заданий дафны от 1 - трусы, 2 - флирт, 3 - свидание - 4 грудь, 5 - мацать, 6 - фап, 7 - минет, 8 - секс
            $ daphne_publ_level = 0
            $ snape_fap = 0
            $ dap_publ = 0   # разговор со снейпом про кубок
            $ harry_chimi = 0
            $ ingridients = 0 # заглушк
            $ snape_fap = 0
            $ chimi_level = 0
            $ flirt_com = 0
            $ date_com = 0
            $ tits_com = 0
            $ fap_com = 0
            $ quest_hagrid = 0
            $ hagrid_potion = 0

            $ fuck_com = 0
            $ hermione_pod_skirt = 0
            $ minet_com = 0
            $ hermione_podd = 0
            $ mats_com = 0
            $ phx_pot = 0
            m "Done"
            call screen main_menu_01
        "-Never mind-":
            call screen main_menu_01


label snape_propaja:
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
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    show screen snape_main
    with Dissolve(.3)
    sna "Джин!"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    m "Что?"
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
    sna "Ты точно не выходил из этих дверей?"
    m "..."
    m "нет"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "и ничего не знаешь об исчезновении учеников?"
    m "....."
    g4 "*черт, опять этот рогатый*"
    m "нет"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "...."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "........"
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"
    sna "Что то сумасшедшее происходит в этом замке"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Может быть такое, что кроме тебя сюда пришел еще кто-то?"
    m "Эм... не знаю"
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "..."
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    sna "ладно, вполне возможно, что они просто решили прогулять уроки или типо того"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "будет лучше если ты не будешь лишний раз никого провоцировать, у меня и так уже голова идет кругом"
    m "..."
    stop music fadeout 1.0
    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ snape_busy = True
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3
    $ chitchated_with_snape = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 0.7
    g4 "Черт, нужно что то делать с этим рогатым"
    m "Это случайно не связано с Чжоу Чанг?"
    m "Можно попробовать спросить у того очкарика, что вчера с ней было"
    $ chimi_event = 11
    return



label after_potion:
    $ menu_x = 0.2 #Menu is moved to the left side.


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ menu_x = 0.2
    $ chimi_chibi_xpos = 320 #Near the desk.
    show screen chimi_02 #Hermione stands still.
    show screen bld1
    with d3
    $ ch_body = "f/cho_def.png" #Sprite of Hermione's upper body.
    show screen chimi_main
    with d3
    $ ch_body = "f/cho_def.png"
    chi "вы звали меня профессор?"
    $ ch_body = "f/cho_def.png"
    m "..."
    m "Как ты себя чувствуешь?"
    $ ch_body = "f/cho_grust.png"
    chi "Эм..."
    chi "как я себя чувствую? Не знаю..."
    g9 "зайду из далека, ты не хочешь ничего взять себе в рот?"
    $ ch_body = "f/cho_udivl.png"
    chi "...."
    $ ch_body = "f/cho_nedov1.png"
    chi "интересно, о чем это вы?"
    $ ch_body = "f/cho_nedov2.png"
    g4 " *Черт, похоже Снейповское зелье уже работает*"
    m "Значит зелье профессора Снейпа тебе помогает?"
    $ ch_body = "f/cho_smile3.png"
    chi "Эм... наверное. По крайней мере, уменя больше нет провалов памяти, как раньше"
    g4 "*Черт*"
    m "*нужно что то придумать, я не хочу просто так отпускать ее*"
    g4 "*Может быть договориться со Снейпом, чтобы как-то чередовать дни с лекарством*"
    $ chimi_event = 8
    jump chimi_menu

label talk_with_snape:
    m "Ты даешь этой Чанг это лекарство?"
    $ s_sprite = "03_hp/10_snape_main/24.png"
    sna "Да. Я не могу вылечить то, что с ней происходит, но по крайней мере, она не будет пытаться никого убить"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    g4 "А... можно как нибудь сделать, чтобы она никого не убивала и в то же время как раньше, была готова на любые шалости?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"
    sna "Хах, нет, если я поменяю состав зелья, то может произойти все что угодно"
    m "все что угодно?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna "в плохом смысле"
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"
    sna "у тебя уже есть целых две маленьких шлюшки, оставь ее, а то потом проблем не оберемся"
    g4 "..."
    m "ладно"
    $ chimi_event = 9
    jump snape_chat

label chochang_ogn:
    if chimi_event == 13:
        jump cho_minet1
    elif chimi_event == 14:
        jump cho_minet2
    elif chimi_event == 15:
        jump cho_gruppa
    elif chimi_event == 16:
        jump harry_demon

label cho_minet1:
    
    play music "music/(Orchestral) Playful Tension by Shadow16nh orig.mp3"

    show screen blkfade
    with Dissolve(0.7)
    $ backgr = "new/chm1/fon.png"
    show screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    m "...."
    g4 "стена?"


    mal "Эм... ты уверена?"
    m "...."
    chi_gipn "Да, давай"
    mal "..."
    mal "Это что, какая-то подстава? Никто не выпрыгнет из-за угла?"
    chi_gipn "О чем ты говоришь, я просто хочу отсосать твой член"
    mal "Просто ты... ведешь себя не очень похоже на себя"
    chi_gipn "ДА какая к черту разница, я ХОЧУ твой член себе в рот, ах"
    mal "..."
    mal "эм... ну ладно..."
    chi_gipn "давай его сюда"
    pause 1.0
    hide screen fruk
    $ backgr = "new/chm1/2-1.png"
    show screen fruk
    with Dissolve(0.7)
    pause 1.0
    g9 "хах, очкарик и правда исполняет поручение следить за ней"
    g4 "то есть он мне врет о том, что она ничего такого не делает"
    mal "не ужели это правда..."
    chi "заткнись, ах...."
    hide screen fruk
    $ backgr = "new/chm1/2.png"
    show screen fruk
    with Dissolve(0.7)
    mal "...."
    hide screen fruk
    $ backgr = "chm_min"
    show screen fruk
    with Dissolve(0.7)
    $ renpy.pause(2.0, hard = True)
    chi "*чавк* *чавк* *чавк*"
    mal "хах"
    mal "вот это круто"
    chi "*Чавк!* *Хлюп!* *Хлюп!*"
    mal "оо даа"
    mal "черт, я надеюсь, что это не сон"
    mal "Чжоу Чанг, одна из самых красивых девушек школы делает мне минет"
    chi "*Чавк!* *Хлюп!* *Хлюп!*"
    mal "ооох"
    
    hide screen fruk
    $ backgr = "new/chm1/2-1.png"
    show screen fruk
    with Dissolve(0.7)
    chi "заткнись"
    mal "черт, это точно не сон"
    hide screen fruk
    $ backgr = "chm_min"
    show screen fruk
    with Dissolve(0.7)
    $ renpy.pause(2.0, hard = True)
    chi "*Чавк!* *Чавк!* *Хлюп!*"
    mal "ааахх"
    chi "*чмок* *чмок* *чмок*"
    mal "Чжоу..."
    hide screen fruk
    $ backgr = "new/chm1/2-1.png"
    show screen fruk
    with Dissolve(0.7)
    chi "кха, что?"
    mal "я люблю тебя"
    hide screen fruk
    $ backgr = "new/chm1/2-1.png"
    show screen fruk
    with Dissolve(0.7)
    chi "ты идиот, хах"
    hide screen fruk
    $ backgr = "new/chm1/2.png"
    show screen fruk
    with Dissolve(0.7)
    chi "черт, как же... хах"
    pause 1.0
    hide screen fruk
    $ backgr = "chm_min"
    show screen fruk
    with Dissolve(0.7)
    pause 0.6
    mal "ооо"
    mal "черт, как же хорошо"
    m "...."
    mal "кажется я..."
    mal "чжоу!"
    chi "*чмок* *чмок* *чмок*"
    mal "я уже..."
    hide screen fruk
    $ backgr = "new/chm1/1-1.png"
    show screen fruk
    with Dissolve(0.7)
    chi "ммм"
    mal "хааа!"
    hide screen fruk
    $ backgr = "new/chm1/1-1c.png"
    show screen fruk
    with Dissolve(0.7)
    chi "мммм"
    play sound "sounds/gulp.mp3"
    hide screen fruk
    $ backgr = "new/chm1/1-1.png"
    show screen fruk
    with Dissolve(0.8)

    mal "ничего себе, ты даже..."
    play sound "sounds/gulp.mp3"
    hide screen fruk
    $ backgr = "new/chm1/2c.png"
    show screen fruk
    with Dissolve(0.8)    
    chi "...."
    mal "я люблю тебя, чжоу..."
    g9 "похоже, что все работает"
    show screen blkfade
    with Dissolve(0.8)
    hide screen backg2
    hide screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    ogn "Электричество кончилось"
    g9 "кажется я нашел себе новое занятие на лунные вечера"
    $ chimi_event = 14
    show screen genie
    hide screen genie_stands
    hide screen chair_02 #Empty chair near the desk.
    hide screen desk
    with Dissolve(0.5)
    jump day_main_menu
    return


label cho_minet2:
    play music "music/(Orchestral) Playful Tension by Shadow16nh orig.mp3"
    show screen blkfade
    with Dissolve(0.7)
    $ backgr = "new/chm1/fon.png"
    show screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    m "..."
    
    mal "черт, ты серьезно"
    chi_gipn "ага, пойдемте уже"
    
    mal2 "это точно не какой-то розыгрышь"
    chi_gipn "хах... ох... какой еще розыгрышь, пойдемте пожалуйста..."
    mal "да ладно чего мы теряем"
    m "это уже кто-то другой"
    chi_gipn "давайте здесь"
    show screen blkfade
    with Dissolve(0.6)
    hide screen blkfade
    hide screen fruk
    $ backgr = "new/chm1/3.png"
    show screen fruk
    with Dissolve(1.5)    
    pause 1.5
    mal "не могу поверить"
    hide screen fruk
    $ backgr = "chm_min2"
    show screen fruk
    with Dissolve(0.9)
    chi "чмок-чмок-чмок"
    mal "оох"
    mal "черт, как хорошо"
    
    mal2 "Эй. мне тоже"
    hide screen fruk
    $ backgr = "new/chm1/3-3.png"
    show screen fruk
    with Dissolve(0.9)
    pause

    hide screen fruk
    $ backgr = "chm_min3"
    show screen fruk
    with Dissolve(0.9)
    chi "хах, *Чавк!* *Хлюп!* *Хлюп!*"
    chi "*чмок* *чмок* *чмок*"
    mal2 "не думал, что мисс Чанг такая похотливая сучка"
    mal "да, она всегда держала нос по ветру"
    chi "*Чавк!* *Чавк!* *Чавк!*"
    mal2 "а оказыватся она не прочь отсосать пару-тройку членов"
    
    chi "мгмл ммглм мглм"
    hide screen fruk
    $ backgr = "new/chm1/3-4.png"
    show screen fruk
    with Dissolve(0.9)
    mal "хахах"
    hide screen fruk
    $ backgr = "chm_min2"
    show screen fruk
    with Dissolve(0.9)
    chi "*чмок* *чмок* *чмок*"
    mal2 "вам там удобно, мисс чанг?"
    chi "мгмл мглм"
    mal "смотри как старается"
    mal2 "хаха"
    chi "*Чавк!* *Чавк!* *Чавк!*"
    mal "черт как же она хорошо сосет"
    mal2 "у нее явно есть опыт"
    mal "может быть... это просто талант?"
    hide screen fruk
    $ backgr = "new/chm1/3-3.png"
    show screen fruk
    with Dissolve(0.9)
    mal2 "хаха, да, наверное она просто прирожденная сосалка"
    mal "хаха"
    hide screen fruk
    $ backgr = "new/chm1/3-3.png"
    show screen fruk
    with Dissolve(0.9)
    pause 1.0
    hide screen fruk
    $ backgr = "new/chm1/3-5.png"
    show screen fruk
    with Dissolve(0.9)
    chi "хватит, нас услышат"
    mal2 "не отвлекайтесь, мисс Чанг"
    hide screen fruk
    $ backgr = "chm_min3"
    show screen fruk
    with Dissolve(0.9)
    chi "..."
    mal "хаха"
    mal "я всем парням расскажу, у нее будет много... поклонников"
    chi "мгмл ммглм мглм"
    mal "да, давай соси"
    mal2 "когтерванская шлюха"
    mal "хаха"
    mal "даже не верится, что она продолжает сосать"
    mal2 "совсем безбашенная сучка"
    mal "как тебе это, шлюха"
    hide screen fruk
    $ backgr = "new/chm1/3-4.png"
    show screen fruk
    with Dissolve(0.9)
    mal "что вы можете скзаать, нам мисс чанг"
    hide screen fruk
    $ backgr = "new/chm1/3-4.png"
    show screen fruk
    with Dissolve(0.9)
    chi "ах... хах"
    hide screen fruk
    $ backgr = "chm_min2"
    show screen fruk
    with Dissolve(0.9)
    pause 2.0
    mal2 "получай!"
    hide screen fruk
    $ backgr = "new/chm1/3-1c.png"
    show screen fruk
    with Dissolve(0.9)
    chi "ммм-ммм-ммм"    
    hide screen fruk
    $ backgr = "new/chm1/3-4c.png"
    show screen fruk
    with Dissolve(0.9)
    chi "...."
    play sound "sounds/spit.mp3"
    hide screen fruk
    $ backgr = "new/chm1/3-4cc.png"
    show screen fruk
    with Dissolve(0.9)
    mal "так намного лучше"
    hide screen fruk
    $ backgr = "chm_min33"
    show screen fruk
    with Dissolve(0.9)
    pause 2.0
    chi "ммм-ммм-ммм"
    hide screen fruk
    $ backgr = "new/chm1/3-3cc.png"
    show screen fruk
    with Dissolve(0.9)
    mal "хаааа!!!"
    hide screen fruk
    $ backgr = "new/chm1/3-5c.png"
    show screen fruk
    with Dissolve(0.9)
    play sound "sounds/spit.mp3"
    hide screen fruk
    $ backgr = "new/chm1/3-5cc.png"
    show screen fruk
    with Dissolve(0.9)
    $ chimi_event = 15
    g9 "вот это зелье так зелье"
    show screen blkfade
    with Dissolve(0.6)
    hide screen backg2
    hide screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    ogn "Электричество кончилось"
    
    show screen genie
    hide screen genie_stands
    hide screen chair_02 #Empty chair near the desk.
    hide screen desk
    with Dissolve(0.5)
    jump day_main_menu
    return



label cho_gruppa:
    play music "music/(Orchestral) Playful Tension by Shadow16nh orig.mp3"
    show screen blkfade
    with Dissolve(0.7)
    $ backgr = "new/chm1/fon.png"
    show screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    m "..."
    chi_gipn "да, вот здесь"
    mal "давайте все, по очереди!"
    g6 "...."
    hide screen fruk
    $ backgr = "new/chm1/5-0.png"
    show screen fruk
    with Dissolve(0.9)
    mal "чур я первый!"
    hide screen fruk
    $ backgr = "new/chm1/5-1.png"
    show screen fruk
    with Dissolve(0.9)
    pause 0.9
    play sound "sounds/gltch.mp3"
    with vpunch
    chi "хах"
    hide screen fruk
    $ backgr = "new/chm1/5-01.png"
    show screen fruk
    with Dissolve(0.9)

    mal "давай, бери"
    hide screen fruk
    $ backgr = "new/chm1/6.png"
    show screen fruk
    with Dissolve(0.9)
    mal "хах"
    hide screen fruk
    $ backgr = "chim_grup"
    show screen fruk
    chi "ммм--ммм"
    mal "оохх... даа... вот так"
    chi "*чмок* *чмок* *чмок*"
    hide screen fruk
    $ backgr = "new/chm1/50.png"
    show screen fruk
    chi "ах"
    hide screen fruk
    $ backgr = "new/chm1/5-01.png"
    show screen fruk
    chi "хах... ааа"
    mal2 "не дергайся шлюха!"
    
    hide screen fruk
    $ backgr = "new/chm1/500.png"
    show screen fruk
    with dissolve
    play sound "sounds/slap.mp3"
    with vpunch
    chi "ах"
    hide screen fruk
    $ backgr = "chim_grup"
    show screen fruk
    chi "ммм--ммм"
    mal2 "вот так"
    mal2 "хах... черт, какая она узкая"
    mal3 "я слышал все азиатки такие"
    mal4 "да ну, что за бред"
    chi "ммм... ах... мм... хааа"
    mal3 "..."
    mal3 "блин, вы там скоро? я тоже хочу"
    hide screen fruk
    $ backgr = "new/chm1/6c.png"
    show screen fruk
    with Dissolve(0.9)
    mal2 "ха!"


    hide screen fruk
    $ backgr = "new/chm1/6-3.png"
    show screen fruk
    with Dissolve(0.9)
    pause 
    mal3 "отлично, теперь я"
    
    hide screen fruk
    $ backgr = "new/chm1/6-4.png"
    show screen fruk
    with Dissolve(0.9)
    chi "...."
    hide screen fruk
    $ backgr = "new/chm1/6-5.png"
    show screen fruk
    with Dissolve(0.9)
    chi "ммм--ммм"
    mal3 "хах, всегда мечтал оседлать эту сучку"
    chi "ах"
    hide screen fruk
    $ backgr = "chim_grup2"
    show screen fruk
    with Dissolve(0.9)
    chi "ммм--ммм"
    $ renpy.pause(3.0, hard = True)
    hide screen fruk
    $ backgr = "new/chm1/6-6.png"
    show screen fruk
    with Dissolve(0.9)
    mal "получай!"
    chi "ммм--ммм"
    hide screen fruk
    $ backgr = "new/chm1/6-7.png"
    show screen fruk
    with Dissolve(0.9)
    pause
    mal4 "я следующий!"
    hide screen fruk
    $ backgr = "new/chm1/6-8.png"
    show screen fruk
    with Dissolve(0.9)
    $ renpy.pause(2.0, hard = True)
    hide screen fruk
    $ backgr = "chim_grup3"
    show screen fruk
    with Dissolve(0.9)
    chi "*Чавк!* *Кулдык!*"
    mal3 "хах, эта шлюха еще и глотает!"
    mal2 "первосортная шлюха"
    "*смех*"
    chi "ммм--ммм"
    chi "*Чавк!* *Чавк!* *Чавк!*"
    mal3 "Черт, эта Чанг действительно съехала с катушек последнее время"
    mal2 "еще месяц назад мне бы и голову не пришло, что она будет так..."
    chi "ммм-- мгмгмгм"
    mal "хаха"
    mal "похоже она решила перестать быть пафосной сучкой и осчастливить весь хогвартс"
    mal2 "хах"
    mal2 "Поттер, ты что там, подсматриваешь?"
    har_stesn "эм... я это..."
    mal3 "гыг, пусть смотрит"
    mal "хаха, да поттер, можешь смотреть как мы трахаем твою любимую чжоу"
    har_visod "почему мою..."
    mal3 "хаха, не отнекивайся, все знают что ты влюлен в нее"
    har_visod "..."    
    g9 "вот это круто"
    show screen blkfade
    with Dissolve(0.8)
    hide screen backg2
    hide screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    ogn "Электричество кончилось"
    $ chimi_event = 16
    show screen genie
    hide screen genie_stands
    hide screen chair_02 #Empty chair near the desk.
    hide screen desk
    with Dissolve(0.5)
    jump day_main_menu
    return



label harry_demon:
    play music "music/(Orchestral) Playful Tension by Shadow16nh orig.mp3"
    show screen blkfade
    with Dissolve(0.7)
    $ backgr = "03_hp/17_ending/02_1.png"
    show screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    $ ch_body = "f/cho_gipn_f.png"
    show screen chimi_main3
    with dissolve
    pause 1.0
    m "опять это место"
    m "в этот раз она одна?"
    $ har_body = "f/hr_sm_smush2.png"
    show screen harry_main2
    with Dissolve(0.8)
    harr "...."
    $ har_body = "f/hr_sm_smush.png"
    harr  "Эм... чжоу..."
    $ har_body = "f/hr_sm_smush2.png"
    $ ch_body = "f/cho_gipn_smile_f.png"
    chi "а... что? это ты..."
    $ ch_body = "f/cho_gipn_smile_f.png"

    $ har_body = "f/hr_sm_smush.png"
    harr "ну...{w} сегодня полнолуние"
    $ har_body = "f/hr_sm_smush2.png"
    $ ch_body = "f/cho_gipn_f.png"
    chi "да, ах..."
    $ har_body = "f/hr_sm_smush.png"
    $ ch_body = "f/cho_gipn_f.png"
    harr "Обычно... когда полнолуние ты...."
    $ har_body = "f/hr_sm_smush2.png"
    $ ch_body = "f/cho_zakr6_f.png"
    chi "черт... хах... как же...."
    $ har_body = "f/hr_sm_smush4.png"
    harr "эм... что с тобой?"
    $ ch_body = "f/cho_gipn_f.png"
    chi "ты хочешь потрахаться?"
    $ ch_body = "f/cho_gipn_f.png"
    $ har_body = "f/hr_sm_smush3.png"
    harr "... эм..."
    $ ch_body = "f/cho_gipn_smile_f.png"
    chi "пойдем в аудиторию"
    $ har_body = "f/hr_sm_smush4.png"
    $ ch_body = "f/cho_gipn_smile_f.png"
    harr  "Что... вот так просто?"
    $ ch_body = "f/cho_gipn_f.png"
    chi "ты будешь трахаться или нет?"
    $ har_body = "f/hr_sm_smile2.png"
    harr "да конечно..."
    $ ch_body = "f/cho_gipn_f.png"
    chi "давай, доставай свой член, черт как же я хочу... ах..."

    harr "да, сейчас..."
    show screen blkfade
    with Dissolve(0.6)
    hide screen fruk
    hide screen blkfade
    hide screen chimi_main3
    hide screen harry_main2
    $ backgr = "new/chm1/8.png"
    show screen harend
    with Dissolve(1.0)
    harr "ох"
    chi "*Чавк!* *Чавк!* *Чавк!*"
    g9 "Ему все таки перепало"
    harr "хах... ох..."
    hide screen harend
    show screen harend3
    #with Dissolve(0.7)
    $ renpy.pause (2.0, hard = True)
    chi_gipn "*чмок* *чмок* *чмок*"

    $ backgr = "new/chm1/8-1.png"
    harr "чжоу..."
    $ backgr = "new/chm1/8-3.png"
    chi_gipn "*Чавк!* *Хлюп!* *Хлюп!*"
    $ backgr = "new/chm1/8-1.png"
    harr "чжоу..."
    hide screen harend3
    show screen harend2
    with Dissolve(0.7)
    $ backgr = "new/chm1/8-1.png"
    chi_gipn "...."
    $ backgr = "new/chm1/8-2.png"
    harr "ты у меня первая..."
    chi_gipn "*чмок* *чмок* *чмок*"
    # слезы
    $ backgr = "new/chm1/8.png"
    harr "...."
    chi_gipn "*Чавк!* *Хлюп!* *Кулдык!*"
    $ backgr = "new/chm1/8-3.png"
    harr "ты..."
    $ backgr = "new/chm1/8-1.png"
    harr "ты всегда мне нр..."
    $ backgr = "new/chm1/8.png"
    harr "аахх черт, ништяк..."
    hide screen harend
    $ backgr = "new/chm1/8-4.png"

    play sound "sounds/attack_snape4.ogg"
    show screen harend2
    with Dissolve(0.6)
    pause 1.0
    hide screen harend2
    show screen harend4
    with Dissolve(0.9)
    pause 2.5
    hide screen harend4
    show screen harend5
    with Dissolve(0.7)
    play music "music/16 The Chess Game.mp3"
    g6 "...."
    $ backgr = "new/chm1/8-6.png"
    dem "а вот и еще один маленький грешник"
    $ backgr = "new/chm1/8-5.png"
    harr "а?"
    $ backgr = "new/chm1/8-7.png"
    dem "еще немного и весь замок пожалеет о том, что посмели призвать меня"
    $ backgr = "new/chm1/8-8.png"
    harr "эм... а вы кто?"
    $ backgr = "new/chm1/8-9.png"
    dem "я тот, кто даст тебе вечную жизнь, полную мучений. Маленький прилюбодей"
    $ backgr = "new/chm1/8-8.png"
    harr "..."
    $ backgr = "new/chm1/7-26.png"
    play sound "sounds/demroar.ogg"
    dem "нужно было быть хорошим мальчиком"
    $ backgr = "new/chm1/7-27.png"
    $ renpy.pause (1.0, hard = True)
    
    hide screen harend5
    $ backgr = "harry_demon"
    show screen harend5
    #$ renpy.pause(3.0, hard = True)
    $ renpy.pause (0.4, hard = True)
    
    play sound "sounds/attack_snape4.ogg"
    stop music fadeout 2.0
    $ renpy.pause (5.0, hard = True)
    play music "music/thekiss.mp3" fadein 2.0
    $ backgr = "new/chm1/8-12.png"
    harr "а, чего?"
    g6 "......"
    g6 "эм... что это было?"
    g4 "он что..."
    g4 "просто так...."
    m "ладно одной проблемой меньше"
    
    hide screen harend5
    $ backgr = "new/chm1/8-11.png"
    show screen harend6
    
    chi  "Эй, что..."

    chi "что за...?!"
    chi "Поттер!"
    hide screen harend6
    $ backgr = "new/chm1/8-11.png"
    show screen harend6
    harr "а?"
    chi "Ты что вытворяешь, бестолоч?!!"
    harr "но..."
    chi "я напишу заявление об изнасиловании!"

    g9 "Эта хах, сколько еще этой сучке придется узнать"
    show screen blkfade
    pause 0.2
    stop music
    $ chimi_event = 17
    hide screen backg2
    hide screen harend5
    hide screen harend6
    hide screen harry_main2
    hide screen harry_main
    hide screen fruk
    hide screen blkfade
    with Dissolve(1.0)
    harr "но я люблю тебя!"
    ogn "Электричество кончилось"
    g9 "наконец то с ним покончено"
    show screen genie
    hide screen genie_stands
    hide screen chair_02 #Empty chair near the desk.
    hide screen desk
    with Dissolve(0.5)
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    jump day_main_menu
    return


label harry_after_attack:
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
    m "..."
    $ har_body = "f/hr_govor.png"
    harr "Профессор..."
    $ har_body = "f/hr_def.png"
    m "да, гарри?"
    $ har_body = "f/hr_def.png"
    harr "я... кажется"
    $ har_body = "f/hr_govor.png"
    harr "Я убил... эм... я не знаю кто это был..."
    $ har_body = "f/hr_def.png"
    m "..."
    g9 "*можно сделать, чтобы он от меня отстал*"
    m "Как не знаешь, Гарри, это же был именно он"
    $ har_body = "f/hr_govor.png"
    harr "но он был не похож..."
    $ har_body = "f/hr_def.png"
    m "я уже год следил за ним, он специально замаскировался, чтобы мы не поняли"
    harr "...."
    m "да, мы наконец то избавились от Волардеморта, Гарри"
    m "и теперь ты можешь успокоиться"
    $ har_body = "f/hr_udivl.png"

    harr "не могу поверить... что все кончилось...."
    m "тебе нужно отдохнуть гарри, ты настоящий герой"
    harr "...."
    $ har_body = "f/hr_smile.png"

    harr "спасибо профессор"
    $ chimi_event = 18
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
    m "*Идиот*"
    #$ herm_vopr = 1
    $ harry_chated = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen harry_ch2 #Hermione stands still.
    if daytime:

        jump night_main_menu
    else:
        jump day_main_menu

label harrycho_not_moon:
    m "Ну что, ты заметил что нибудь?"
    $ har_body = "f/hr_govor.png"
    harr "нет, после того раза ничего такого"
    $ har_body = "f/hr_def.png"
    g4 "совсем ничего?"
    $ har_body = "f/hr_def.png"
    harr "Ну..."
    $ har_body = "f/hr_zlo.png"
    harr "Хотя да, точно!"
    m "Что?"
    $ dsc = renpy.random.randint(1, 3)
    if dsc == 1:
        $ har_body = "f/hr_govor.png"
        harr "Когда я вчера предложил проводить ее до факультетского блока она назвала меня идиотом и ушла"
        $ har_body = "f/hr_def.png"
        m "..."
        m "и...?"
        $ har_body = "f/hr_udivl.png"
        harr "Думаете это Воландеморт заставил ее сделать это?!"
        g4 "...."
        m "определенно, но мы должны ждать когда он подставится под наш удар"
        $ har_body = "f/hr_zlo.png"
        harr "точно!"
        m "не спускай с нее глаз"
        $ har_body = "f/hr_govor.png"
        harr "да профессор!"
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
        with Dissolve(.3)
    
        $ herm_vopr = 1
        $ harry_chated = True
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen harry_ch2 #Hermione stands still.
        if daytime:

            jump night_main_menu
        else:
            jump day_main_menu


    elif dsc == 2:
        $ har_body = "f/hr_govor.png"
        harr "я попробовал пригласить ее на свидание, эм... ну, чтобы можно было наблюдать ее поближе"
        $ har_body = "f/hr_def.png"
        m "угу"
        $ har_body = "f/hr_govor.png"
        harr "Она запустила в меня заклинанием, если бы я не отразил, то блевал слизнями две недели"
        $ har_body = "f/hr_def.png"
        pause 0.6
        $ har_body = "f/hr_govor.png"
        harr "это не выглядело как нападение, я не мог напасть на нее, но Чжоу точно не могла так сделать без чувого влияния!"
        $ har_body = "f/hr_def.png"
        g4 "*идиот*"
        $ har_body = "f/hr_zlo.png"
        harr "Я вывел ее на чистую воду!"
        m "да, отлично, но давай подождем, когда она еще больше подставится"
        $ har_body = "f/hr_udivl.png"
        harr "..."
        $ har_body = "f/hr_govor.png"
        harr "да, профессор"
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
        
        with Dissolve(.3)
        
        $ herm_vopr = 1
        $ harry_chated = True
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen harry_ch2 #Hermione stands still.
        if daytime:

            jump night_main_menu
        else:
            jump day_main_menu
    elif dsc == 3:
        $ har_body = "f/hr_zlo.png"
        harr "Сегодня она просто взяла и ушла с урока"
        m "..."
        g4 "и что?"
        $ har_body = "f/hr_zlo.png"
        harr "когда я подгнал ее и спросил почему она это делает она... эм"
        m "Что?"
        $ har_body = "f/hr_zlo.png"
        harr "атаковала меня"
        m "атаковала?"
        $ har_body = "f/hr_zlo.png"
        harr "да"
        m "заклинанеием?"
        $ har_body = "f/hr_zlo.png"
        harr ".... почти"
        $ har_body = "f/hr_zlo.png"
        harr "до сих пор болят"
        g9 "хаха"
        $ har_body = "f/hr_zlo.png"
        harr "Думаете это Воландеморт заставил ее сделать это?!"
        m "...."
        m "определенно, но мы должны ждать когда он подставится под наш удар"
        $ har_body = "f/hr_zlo.png"
        harr "точно!"
        m "не спускай с нее глаз"
        $ har_body = "f/hr_govor.png"
        harr "да профессор!"
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
        m "*Идиот*"
        $ herm_vopr = 1
        $ harry_chated = True
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen harry_ch2 #Hermione stands still.
        if daytime:

            jump night_main_menu
        else:
            jump day_main_menu

label harry_moon:
    m "ну что, гарри, ты что-нибудь заметил за ней?"
    $ har_body = "f/hr_govor.png"
    harr "эм... да, она вела себя вчера..."
    $ har_body = "f/hr_def.png"
    m "как?"
    $ har_body = "f/hr_govor.png"
    harr "довольно странно"
    $ har_body = "f/hr_def.png"
    g4 "так что ты видел?"
    $ har_body = "f/hr_govor.png"
    harr "эм... хотя, наверное нет, ничего такого"
    $ har_body = "f/hr_def.png"
    m "что?"
    m "а что все таки было?"
    $ har_body = "f/hr_govor.png"
    harr "ну... эм..."
    $ har_body = "f/hr_def.png"
    pause 0.5
    $ har_body = "f/hr_govor.png"
    harr "она общалась с парнями"
    $ har_body = "f/hr_def.png"
    m "и что они делали?"
    $ har_body = "f/hr_govor.png"
    harr "эм..."
    harr "..."
    harr "ну..."
    harr "я не видел"
    $ har_body = "f/hr_def.png"
    g4 "вообще ничего?"
    $ har_body = "f/hr_govor.png"
    harr "эм... нет"
    $ har_body = "f/hr_def.png"
    m "вот лопух"
    $ chimi_event = 12
    jump harry_chat
label cho_uznat:
    m "хм... сегодня полнолуние"
    g9 "можно попробовать проследить что там у Чжоу Чанг"
    return
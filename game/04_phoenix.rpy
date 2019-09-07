label phoenix:
    if (bird_interact >= 2) and (pnx_stage == 0): # Counts how many times you have interacted with the bird.
        if pnx_stage == 0 :
            $ pnx_stage = 1
            hide screen genie
            show screen feeding
            with Dissolve(0.3)
            pause 1
            show screen phoenix_food
            show screen bld1

            ">Когда вы подходите к фениксу, он смотрит на вас ожидающим взглядом и немного оживает."
            m "Ну чего ты, птичка, грустишь? Хоть директора и нет, я о тебе позабочусь. "
            m "Видали и более противных попугаев, и ни чего - в обиду их не давал…"

            ">Феникс указывает вам на книги на камине. Он что-то хочет вам сказать, но не может."
            ">Вы осматриваете полку возле книг и находите записку."

            $ letter_text = "{size=-2}Уважаемый профессор Дамблдор. \n\nНе знаю, что вы за вид оборотня такой, но судя по всему - слизняк, т.к. уже множество месяцев подряд после каждого полнолуния весь пол у вас в чем-то липком и противном. Прошу вас относиться к чистоте в кабинете ответственнее, иначе на вашу башню я более подниматься не буду. {/size}"

            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

            g4 "На башню? Это метафора такая? Он еще и уборщицу трахал?"
            m "Почему нельзя выражаться проще: \"никогда не сяду на ваш член\"?"
            m "Почему все вокруг так любят маскировать пенис под фаллические предметы? Всё равно всем и так ясно, о чём они говорят."
            g9 "Особенно мне."
            pause.5
            m "Хм, я, конечно, понимаю, чем занимался тут профессор, но…"
            m "Так необычно подобранное время…"
            m "Феникс, ты что-то знаешь об этом?"

            ">Феникс смотрит на вас ожидающим взглядом."

            g4 "Господи, надеюсь, он не феникса трахал…"
            g4 "Это же глупость…"
            m "Хотя…"
            g9 "Эй, феникс!"
            g4 "Стоп, джин, это перебор даже для тебя."

            ">Феникс продолжает смотреть на вас ожидающим взглядом."

            m "Он точно что-то знает. Нужно разгадать этот ребус. Мой член в этом заинтересован."

            hide screen bld1
            show screen genie
            hide screen feeding
            with Dissolve(0.3)
        jump day_main_menu
    elif pnx_stage == 1000:
        m "Птица явно стала выглядеть лучше"
        m "Похоже она выглядела больной именно из-за той запечатанной сучки"
        $ pnx_stage = 1001
        jump phxx_new
    elif pnx_stage == 1001:
        jump phoenix_plak
    elif pnx_stage > 1001:
        jump phxx_new

    else:
        jump phxx
    menu phxx:

        "-Дать Фениксу зелье-" if (phx_pot == 5) and (pnx_stage < 1000) and (daytime == False):
            jump phx_last_zel


        "-Выпить зелье-" if (hagpot == 1) and (pnx_stage < 1000):
            if steroids == 0:
                "У вас не волшебного корма для феникса"
                jump phxx
            elif daytime == True:
                
                $ phoenix_is_feed = True
                jump feeding_str
            elif (hagpot == 1) and (phoenix_chated == 0):

                if phx_pot == 0:
                    $ phx_ingr1 = 0
                    $ phx_ingr2 = 0
                    $ phx_ingr3 = 0
                    $ phx_ingr4 = 0
                    jump phoenix_potion
                elif phx_pot == 1:
# здесь изменена ссылка на первый вариант с фениксом
                    jump phoenix_potion2_zel
                    jump phoenix_potion2
                elif phx_pot == 2:
                    jump phx_prinesi

                    jump phoenix_potion3
                elif phx_pot == 3:
                    jump phx_gdezelie

                    jump phoenix_potion4

                elif phx_pot == 4:
                    jump phx_gdezelie
                    jump phoenix_potion5
                elif phx_pot == 5:
                    jump phx_gdezelie
                    jump phoenix_potion5
            else:
                $ phoenix_is_feed = True
                jump feeding


        "- Исследовать -" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            $ tt_xpos=270
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk_02
            with Dissolve(0.5)
            m "Хм....."
            m "Даже эта странная птица излучает магию.."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk_02
            with Dissolve(0.5)
            jump day_main_menu

        "- Перечитать бумажку -" if pnx_stage == 1 :

            $ letter_text = "{size=-2}Уважаемый профессор Дамблдор. \n\nНе знаю, что вы за вид оборотня такой, но судя по всему - слизняк, т.к. уже множество месяцев подряд после каждого полнолуния весь пол у вас в чем-то липком и противном. Прошу вас относиться к чистоте в кабинете ответственнее, иначе на вашу башню я более подниматься не буду. {/size}"

            show screen bld1
            show screen letter
            show screen ctc
            pause
            hide screen letter
            hide screen bld1
            hide screen ctc

            jump phoenix

        "-Волшебный корм для феникса-" if (steroids == 1) and (pnx_stage < 1000):
            if (daytime == False) and (phoenix_chated == 0) and (pnx_stage < 8) and (pnx_stage < 1000):
                call pnx_call from _call_pnx_call
            elif (daytime == False) and (phoenix_chated == 0) and (pnx_stage == 1000):
                $ phoenix_is_feed = True
                jump feeding

            elif (daytime == False) and (phoenix_chated == 0) and (pnx_stage >= 8):
                jump new_fenix1
            elif daytime == True:
                "Днем чары не работают, феникс смотрит на вас как на идиота"
                $ phoenix_is_feed = True
                jump feeding

            else:
                $ phoenix_is_feed = True
                jump feeding

        "- Покормить птицу -" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding

        "- Погладить птицу -" if bird_examined:
            jump petting
        "- Ничего -":
            call screen main_menu_01


### FEEDING ###
label feeding:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3) #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "Держи..."
    else:
        pause.5
    show screen genie
    hide screen feeding
    with Dissolve(0.3)
    call screen main_menu_01


### PETTING ###
label petting:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    show screen sad_phoenix #SMILEY
    pause 1.5
    m "Птица плохо выглядит. Может быть она больна?" #The bird doesn't look good. Is it sick or something
    pause.5



    show screen genie
    hide screen sad_phoenix #SMILEY
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01


label feeding_str:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3) #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "Держи..."
    else:
        pause.5
    ">Днем чары не работают, феникс смотрит на вас как на идиота"
    show screen genie
    hide screen feeding
    with Dissolve(0.3)
    call screen main_menu_01

label phoenix_plak:
    $ renpy.pause(1.0, hard = True)
    g6 "...."
    g7 "Где ты теперь...{w} птичка..."
    g10 "в каком то смысле, это даже хорошо, что она не со мной"
    g4 "....."
    g4 "Так хватит, я все еще развратный джин"
    $ pnx_stage = 1002
    jump phxx

label phxx_new:
    menu:
        "-Feed the bird-" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding

        "-Pet the bird-" if bird_examined:
            jump petting2
        "-Never mind-":
            call screen main_menu_01


label petting2:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    #show screen sad_phoenix #SMILEY
    pause 1.5
    ph "да? что ты хочешь?"
    g4 "Ты умеешь разговаривать?!"
    ph "Конечно"
    menu ph_cheat:
        ph "Что ты хочешь?"

        "Воображение":
            $ imagination = 5
            jump ph_cheat
        "разблокировать публичные услуги Гермионы":
            $ lock_public_favors = False
            $ touched_by_boy = True
            ph "Done"
            jump ph_cheat
        "Гермиона не сердится":
            $ mad = 0
            ph "Done"
            jump ph_cheat
        "Развратность гермионы +1":
            ph "Hermione whoring level was [level] of 10"
            if level == "01":

                $ whoring = 5
                $ level = "02"
                ph "Now it 2"
                jump ph_cheat
            elif level == "02":
                $ whoring = 8
                $ level = "03"
                ph "Now it 3"
                jump ph_cheat
            elif level == "03":
                $ whoring = 11
                $ level = "04"
                ph "Now it 4"
                jump ph_cheat
            elif level == "04":
                $ whoring = 14
                $ level = "05"
                ph "Now it 5"
                jump ph_cheat
            elif level == "05":
                $ whoring = 17
                $ level = "06"
                "ph Now it 6"
                jump ph_cheat
            elif level == "06":
                $ whoring = 20
                $ level = "07"
                ph "Now it 7"
                jump ph_cheat
            elif level == "07":
                $ whoring = 23
                $ level = "08"
                ph "Now it 8"
                jump ph_cheat
            elif level == "08":
                $ whoring = 26
                $ level = "09"
                ph "Now it 9"
                jump ph_cheat
            elif level == "09":
                $ whoring = 29
                $ level = "10"
                ph "Now it 10"
                jump ph_cheat
            else:
                ph "Hermione whoring level already max"
                jump ph_cheat
        "Дафна не сердится":
            $ daphne_moral = 5
            ph "Done"
            jump ph_cheat
        "Слизерин всегда побеждает":
            $ slytherin = 6666
            ph "Done"
            jump ph_cheat
        "Получить журнал Дахра":
            $ cataloug_found = True
            $ have_catalogue = True
            ph "Done"
            jump ph_cheat

        "Дай мне денег":
            $ gold += 10000
            ph "Done"
            jump ph_cheat

        "10 всех вещей":
            $ wine += 10
            $ anal_lube = 10
            $ condoms = 10
            $ candy = 10
            $ chocolate = 10
            $ vibrator = 10
            $ strapon = 10
            $ ballgag = 10
            $ plug = 10
            $ mag1 = 10
            $ mag2 = 10
            $ mag3 = 10
            $ mag4 = 10
            $ beer = 10
            $ owl = 10
            $ sexdoll = 10
            $ lingerie = 10
            $ broom = 10
            $ krum = 10
            $ badge_01 = 10
            $ nets = 10
            $ sexdoll = 10
            $ broom = 10
            ph "Done"
            jump ph_cheat

        "быстрая доставка":
            if delivery_cheat == 0:
                $ delivery_cheat = 1
            else:
                $ delivery_cheat = 0

            ph "Done"
            jump ph_cheat



        "-Назад-":
            show screen genie
            hide screen sad_phoenix #SMILEY
            hide screen petting
            with Dissolve(0.3)
            call screen main_menu_01
   



    show screen genie
    hide screen sad_phoenix #SMILEY
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01


label pnx_call:

        hide screen phoenix
        show screen phoenix_main
        hide screen animation_feather
        hide screen phoenix_food
        show screen new_fenix
        show screen bld1

        $ ph_body = "f/phx1.png"
        show screen heal3
        $ renpy.play('sounds/magic4.ogg')

        pause 3

        hide screen heal3

        if pnx_stage == 0 :
            $ pnx_stage = 1

        if pnx_stage <= 1 :


            g4 "Что… кто… откуда…"
            $ ph_body = "f/phx2.png"

            g4 "ЧТО ТЫ СДЕЛАЛА С ФЕНИКСОМ?!"
            $ ph_body = "f/phx3.png"
            ph "Думаю, вы говорите именно о том фениксе, в которого я была обращена."
            $ ph_body = "f/phx2.png"

            m "Да? Вот это опция…"
            m "А почему ты раньше не вылазила?"
            $ ph_body = "f/phx3.png"
            ph "Я зачарована, сэр. Директор выкупил меня очень давно у арабских купцов. С тех пор я была у него. Правда он уже много лет не менял мое обличие..."
            ph "Но, судя по тому, что его здесь нет, а вы на его месте, он ушел и продал меня вам. Так что теперь вы мой мастер."
            $ ph_body = "f/phx2.png"
            m "...Эм?"
            g9 "Да, я твой мастер! Ты исполняешь желания?"
            $ ph_body = "f/phx3.png"
            ph "А про какие желания вы говорите?"
            g9 "Что значит, “про какие?”"
            g9 "Я - твой мастер, и какие желания я от тебя потребую - такие тебе выполнить и придется."
            $ ph_body = "f/phx3.png"
            ph "Хм…"
            ph "Глупость какая-то. Я же не джин…"
            g9 "О, нет. Желания будут вполне смертными."
            m "И, боюсь, мне придется превратить тебя обратно в птицу, если…"
            $ ph_body = "f/phx3.png"
            ph "В птицу?"
            ph "...Как вам будет угодно."

            ">Девушка элегантно преобразуется в феникса, сидящего на прежнем месте."

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_main
            hide screen new_fenix
            show screen phoenix

            pause 3

            hide screen heal3

            g4 "Что? Стой! Как ты это?.."
            g4 "Так ты можешь сама?! Так, превратись обратно немедленно! Мастер приказывает!"
            g4 "Феникс!"
            m "Пожалуйста…"
            g4 "Как я вообще это сделал? Ты слышишь меня? Тупая курица!"
            m "Прости, прости, это…"
            m "Это у меня комплименты такие…"
            g4 "...Вернись!"
            m "Так, надо понять свою последовательность действий"

        elif pnx_stage == 2 :
            $ ph_body = "f/phx3.png"
            ph "Это снова вы, мастер?"
            $ ph_body = "f/phx2.png"
            m "А ты видишь кого-то еще?"
            $ ph_body = "f/phx3.png"
            ph "А должна?"

            $ ph_body = "f/phx2.png"
            m "Даже не знаю… проехали."
            m "А как я тебя высвободил?"
            $ ph_body = "f/phx3.png"
            ph "Ваше семя попало на мое перо под светом полной луны."
            $ ph_body = "f/phx3.png"
            ph "Это означает, что вы хотите меня видеть."

            $ ph_body = "f/phx2.png"
            m "Странная логика. Ты мне, по сути и не нужна, если я…"
            $ ph_body = "f/phx3.png"

            $ ph_body = "f/phx2.png"
            g9 "“Излил всё семя”..."
            $ ph_body = "f/phx3.png"
            ph "А, так я вам не нужна?"
            ph "Хорошо, тогда не буду вас доставать…"
            g4 "Эй, подожди…"

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_main
            hide screen new_fenix
            show screen phoenix

            pause 3

            hide screen heal3

            m "Нашел, блин, время умничать…"
            m "Мы с ней так далеко не продвинемся."

        elif pnx_stage == 3 :
            $ ph_body = "f/phx3.png"
            ph "Добрый вечер, сэр."
            $ ph_body = "f/phx2.png"
            m "Ты вообще слышишь меня, когда ты в форме феникса?"
            $ ph_body = "f/phx3.png"
            ph "Ну конечно. Просто не понимаю."
            $ ph_body = "f/phx2.png"
            m "...Так, давай вернемся обратно к желаниям."
            $ ph_body = "f/phx3.png"
            ph "Хорошо. Какие у вас будут желания?"
            $ ph_body = "f/phx2.png"
            g9 "(Ну наконец-то)"
            g9 "Хочу, чтобы ты была моей, птичка!"
            $ ph_body = "f/phx3.png"
            ph "Вашей птичкой? Какое-то странное желание…"
            ph "Ну как скажете."
            ph "Зовите, если передумаете"
            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_main
            hide screen new_fenix
            show screen phoenix

            pause 3

            hide screen heal3

            m "..."
            m "Так, нужно быть аккуратнее с желаниями. У нее, судя по всему, и мозг остается от птицы."

        elif pnx_stage ==4 :
            $ ph_body = "f/phx3.png"
            ph "Приветствую, мастер."
            $ ph_body = "f/phx2.png"
            m "Я теперь научен. Буду говорить короткими и недвусмысленными фразами."
            g9 "...Так ты выполняешь интимные желания?"
            $ ph_body = "f/phx3.png"
            ph "Интимные - в смысле..."
            $ ph_body = "f/phx2.png"
            m "Чем вы занимались с Директором?"
            $ ph_body = "f/phx3.png"
            ph "Ну... он заботился обо мне... купал меня..."
            ph "Называл меня дочкой и просил называть его папочкой..."
            $ ph_body = "f/phx2.png"
            g9 "(Ох, старый извращенец)"
            $ ph_body = "f/phx3.png"
            ph "Когда я себя хорошо вела, он позволял мне сидеть на его палочке..."
            $ ph_body = "f/phx2.png"
            m "Так, на этом и остановимся. Давай вообще забудем про Директора. Начнем разговор с начала…"
            $ ph_body = "f/phx3.png"
            ph "Эм... приветствую, мастер..."
            $ ph_body = "f/phx2.png"
            m "(Ух, я был близок. Перемотай она еще чуть-чуть назад...)"
            m "Ты говорила, что при попадании на твое перо семени, ты становишься девушкой..."
            $ ph_body = "f/phx3.png"
            ph "Один раз за ночь..."
            $ ph_body = "f/phx2.png"
            m "(Нужно сразу уточнить все подробности. Главное аккуратно ей...)"
            g9 "...А если я оболью тебя спермой, ты превратишься в феникса обратно?"
            $ ph_body = "f/phx4.png"
            ph "Хм. Я сама, вроде, могу принимать его форму."
            $ ph_body = "f/phx5.png"
            ph "Сейчас покажу..."
            $ ph_body = "f/phx5.png"
            g4 "Стой!"

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_main
            hide screen new_fenix
            show screen phoenix

            pause 3

            hide screen heal3

            g4 "Я уже насмотрелся на это, тупая ты птица."
            g4 "Она опять удрала! Да она это специально делает!"

        elif pnx_stage == 5 :
            $ ph_body = "f/phx3.png"
            ph "Я вам понадобилась, сэр?"
            $ ph_body = "f/phx2.png"
            m "Я бы сказал, что надобность в тебе не пропадала с самой первой встречи."
            m "Давай договоримся так: пока я сам не повелю тебе превратиться обратно, ты не будешь этого делать."
            $ ph_body = "f/phx3.png"
            ph "Хорошо, сэр"
            $ ph_body = "f/phx2.png"
            m "Больше ни каких демонстраций, додумываний и предположений. Либо я тебе прикажу, либо разрешу."
            $ ph_body = "f/phx3.png"
            ph "Я поняла. Простите, сэр."
            $ ph_body = "f/phx2.png"
            g9 "Ничего. Ты сейчас как раз загладишь свою вину."
            g9 "Ты готова выполнять мои сексуальные желания?"
            $ ph_body = "f/phx3.png"
            ph "Готова, сэр."
            g9 "Ох… с чего начнем? Ну… для начала..."
            g9 "Начни с мастурбации. Ты знаешь, что это? Умеешь?"
            $ ph_body = "f/phx3.png"
            ph "Конечно, сэр."
            ph "А кому? Себе или вам?"
            $ ph_body = "f/phx2.png"
            g9 "(Наконец-то мы дошли до этого…)"
            g9 "Ну я даже не знаю. А чего хочешь ты?"
            $ ph_body = "f/phx3.png"
            ph "Я?"
            ph "Я бы хотела..."
            ph "...Сесть на вашу палочку, сэр."
            $ ph_body = "f/phx2.png"
            g9 "Да, детка, вот это взрослый разговор."
            g9 "Так чего же ты ждешь?"
            $ ph_body = "f/phx3.png"
            ph "Вы разрешаете, сэр?"
            $ ph_body = "f/phx2.png"
            g9 "Я приказываю!"
            g4 "Стой, подожди, о какой…"
            $ ph_body = "f/phx3.png"
            ph "Спасибо, сэр."

            ph " ..."

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_no
            show screen phoenix
            hide screen new_fenix
            hide screen phoenix_main

            pause 3

            hide screen heal3

            g4 "..."
            g4 "Ты на этой палочке сидишь целыми днями..."
            m "Я просто в ярости. Ты либо настолько тупая, либо настолько хитрая. Но настолько меня достала..."

        elif pnx_stage == 6 :
            $ ph_body = "f/phx3.png"
            ph "Вы снова вызвали меня, мастер?"
            ph "~n c def c"
            $ ph_body = "f/phx2.png"
            m "Нет, это ты снова убежала. Я вообще не горю желанием превращать тебя в птицу."
            $ ph_body = "f/phx3.png"
            ph "Но мастер, а если кто-то..."

            $ ph_body = "f/phx2.png"
            m "Знаю, тебя не стоит показывать всем подряд. Давай договоримся: будет специальное слово."
            m "И пока ты это слово не услышишь - ни каких подвижек в сторону феникса. Даже если я тебе скажу это напрямую."
            $ ph_body = "f/phx3.png"

            $ ph_body = "f/phx2.png"
            m "Волшебное слово. Понятно?"
            $ ph_body = "f/phx3.png"
            ph "~Эм... понятно, мастер."

            $ ph_body = "f/phx2.png"
            m "И этим волшебным словом будет..."
            $ ph_body = "f/phx3.png"

            g9 "“Проваливай!”"
            $ ph_body = "f/phx3.png"
            ph "...“Проваливай”?"

            ph "~w a def c"
            $ ph_body = "f/phx2.png"
            m "Хм… да, проваливай…"
            g4 "Нет, в смысле не сейчас. Когда ты его услышишь в следующий раз."
            $ ph_body = "f/phx2.png"
            ph "~s c def c"
            m "Запомнила слово?"
            m "Повтори."
            $ ph_body = "f/phx3.png"
            ph "Проваливай..."

            $ ph_body = "f/phx2.png"
            g9 "Умная птичка!"
            m "Превращайся!"
            $ ph_body = "f/phx3.png"
            ph "..."

            $ ph_body = "f/phx2.png"
            m "Стань фениксом!"
            $ ph_body = "f/phx3.png"
            ph "..."

            g9 "Сядь на палочку!"
            $ ph_body = "f/phx3.png"
            ph "..."

            g9 "Хе-хе-хе… Кстати, нужно будет договориться о новом значении последней фразы."
            $ ph_body = "f/phx3.png"
            ph "Хорошо, мастер..."

            $ ph_body = "f/phx2.png"
            m "Тогда сейчас же подойди сюда и повернись ко мне попкой. Буду объяснять тебе значение…"
            $ ph_body = "f/phx3.png"
            ph "Как пожелаете..."

            $ ph_body = "f/phx2.png"
            g9 "Ох, как же тебя сейчас оттрахают..."
            pause.2

            $ renpy.play('sounds/knocking.mp3')
            "> тук-тук"
            sna "Джин, у меня к тебе есть дело..."

            $ ph_body = "f/phx2.png"
            g4 "Проваливай!"
            $ ph_body = "f/phx5.png"
            ph "Я поняла..."
            $ ph_body = "f/phx4.png"
            g4 "Да не ты!.."

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')

            hide screen phoenix_main
            hide screen new_fenix
            show screen phoenix

            pause 3

            hide screen heal3

            g4 "Стой! Тупая ты курица! У тебя вообще есть мозги или они вслед за перьями отваливаются?!"
            g4 "Есть вообще в этом мире существо тупее, чем ты?!"
            g4 "Какой же нужно быть идиоткой, чтобы ты выглядела на ее фоне умнее?! "
            g4 "Я бы превратил тебя в стул, но он был бы и то разумнее!"
            pause.2

            sna "Джин, с кем ты там?"
            m "Оставь меня, пожалуйста..."
            sna "Эм… ну ладно… Завтра зайду."

        elif pnx_stage == 7 :
            $ ph_body = "f/phx2.png"
            ph "..."
            $ ph_body = "f/phx2.png"
            m "Ты сегодня какая-то не разговорчивая."
            $ ph_body = "f/phx3.png"
            ph "Сэр, может я и не понимаю, что вы говорите, но это не значит, что я не запоминаю."
            $ ph_body = "f/phx2.png"
            m "Ой, я как-то не подумал..."
            m "Хотя чего это я? У тебя всё равно мозги птицы, ты, наверное, и половины слов не поняла."
            m " А кричал я… не на тебя. У меня посетитель был..."
            $ ph_body = "f/phx3.png"
            ph "Между прочим я - анимаг. Это я превращаюсь в феникса, а не он в меня."
            $ ph_body = "f/phx2.png"
            m "Тогда я не понимаю, чем вы, анимаги, умнее тех зверей, в которых превращаетесь..."
            ph "Сэр, вы сказали - и я испонила. Вы говорили, что меня не стоит показывать всем..."
            $ ph_body = "f/phx2.png"
            m "Позволь мне самому решать, кому тебя показывать, а под кого и вовсе тебя класть."
            m "Напряги ты хоть одну свою извилинку, ты бы поняла какие слова адресованы тебе, а какие - нет. "
            g4 "Будь ты человеком разумным, ты бы не убегала после каждой глупой фразы!"
            g4 "Но ты ведешь себя, как тупая птица! А я хочу трахать девушку, а не тупую птицу!"
            $ ph_body = "f/phx3.png"
            ph "Ах так? Ладно, я поняла: я - тупая птица и я вам не нужна."
            $ ph_body = "f/phx2.png"
            m "Ну не принимай это настолько близко..."
            $ ph_body = "f/phx5.png"
            ph "Советую разглядеть мой зад хорошенько. Вы видите его последний раз."
            $ ph_body = "f/phx4.png"
            m "Ну не надо настолько радикально-то…"
            $ ph_body = "f/phx5.png"
            ph "Не переживайте. Секс с птицей вам вряд-ли будет интересен..."
            $ ph_body = "f/phx4.png"
            g9 "Да брось, я просто погорячился!"
            $ ph_body = "f/phx5.png"
            ph "Прощайте!"
            show screen heal3
            $ renpy.play('sounds/magic4.ogg')
            hide screen new_fenix
            hide screen phoenix_no
            show screen phoenix
            hide screen phoenix_main
            pause 3

            hide screen heal3

            m "Такая капризная. Нет, она точно девушка."

        elif (pnx_stage >= 8) and (pnx_stage < 100) :
            $ ph_body = "f/phx3.png"
            ph "Вы что-то хотели?"
            $ ph_body = "f/phx2.png"
            g9 "Да. Кого-то. Тебя."
            $ ph_body = "f/phx3.png"
            ph "Зачем? Вы что, зоофил?"
            $ ph_body = "f/phx2.png"
            ph "~a n def c"
            g9 "Да прекрати это. Подойди и обхвати мой член уже."
            $ ph_body = "f/phx3.png"
            ph "Простите, боюсь поцарапать его когтями..."
            ph "...И клювом."
            $ ph_body = "f/phx2.png"
            g9 "Ладно, черт с тобой. Тебе нужно успокоиться. А пока дай хотя бы тебя разглядеть."
            $ ph_body = "f/phx3.png"
            ph "Какой в этом смысл? Я что так птица, что так..."
            $ ph_body = "f/phx2.png"
            m "Ну не придуривайся. В такой птице ты очень даже сексуальная."
            $ ph_body = "f/phx3.png"

            $ ph_body = "f/phx2.png"
            g9 "Хоть и такая же плоская."
            $ ph_body = "f/phx3.png"
            ph "Все с вами ясно."
            $ ph_body = "f/phx5.png"
            ph "Спокойной ночи."

            show screen heal3
            $ renpy.play('sounds/magic4.ogg')
            hide screen new_fenix
            hide screen phoenix_main
            show screen phoenix

            pause 3

            hide screen heal3

            m "Эх... думаю, мы с ней не помиримся..."



        $ pnx_stage += 1
        $ phoenix_chated = 1
        hide screen bld1

        show screen animation_feather
        jump day_main_menu
        if daytime:
           jump night_start
        else:
           jump day_start

label new_fenix1:
    hide screen phoenix
    show screen phoenix_main
    hide screen animation_feather
    hide screen phoenix_food
    show screen new_fenix
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3


    $ ph_body = "f/phx3.png"
    ph "Слушаю, мой господин"
    $ ph_body = "f/phx2.png"
    m "Так, в этот раз у меня для тебя отличная новость"
    $ ph_body = "f/phx3.png"
    ph "новость?"
    $ ph_body = "f/phx2.png"
    g4 "В этот раз у тебя не выйдет меня опрокинуть"
    ph "..."
    g9 "И сегодня у нас будет секс"
    $ ph_body = "f/phx3.png"
    ph "секс?"
    $ ph_body = "f/phx2.png"
    m "да, секс"
    $ ph_body = "f/phx3.png"
    ph "прямо как у принцессы Надин и принца Ламара?"
    $ ph_body = "f/phx2.png"
    m "....................{w}................................................"
    g4 "че?"
    $ ph_body = "f/phx3.png"
    ph "Ты что не знаешь историю про принцессу Надин?"
    $ ph_body = "f/phx2.png"
    m "эм...{w} что?"
    m "какую еще Надин?"
    show screen blkfade
    with Dissolve(3.0)
    g4 "что происходит???"
    jump fenix_skaz

label new_fenix2:
    ph "Слушаю, мой господин"
    m "..."
    ph "..."
    m "..."
    g4 "В этот раз я не поведусь на твои фокусы"
    ph "Фокусы?{w} какие фокусы?"
    m "Я хочу, чтобы ты уяснила, что тебе таки придется отведать моей палочки"
    ph "Палочки?"
    g4 "нет сучка! Стой!"
    ph "...."
    m "не той палочки"
    g9 "той, которая растет прямо из меня"
    ph "прямо как у Расула?"
    g4 "че? какого Расула?"
    ph "10"
    g4 "нееееееееееет! опять это дерьмо!"

    "Оа ты сука! Да! заебись! я твой султан!"
    "....."
    "твою мать, ты опять это сделала!"





label fenix_skaz:
    stop music
    $ pnx_stage = 10
    ph "это было в старом королестве за тридявять земель отсюда"
    hide screen phoenix_main
    hide screen bld1
    hide screen blkfade

    play music "music/GoingtoKillMe.mp3" fadein 1 fadeout 1
    show screen agraba
    with Dissolve(3.0)
    m "....."
    m "что?"
    hide screen agraba

    show screen agraba2
    with dissolve
    au "В королевсвте бескрайних песков, имя которого уже забыто временем"
    g5 "да это же Аграба"
    g4 "черт возьми, что происходит"
    show screen sultan
    au "управлял этим королевством добрый и справедливый султан"
    g5 "Что? Но ведь Аграбой управлял Джафар{w}, или....."
    hide screen sultan
    with dissolve
    au "Но судьба сыграла с султаном злую шутку, на 35 году жизни подарив ему дочь"
    $ jasm = "new/jas03.png"
    show screen jasmin
    with dissolve
    au "Которой было дано имя....."
    g5 "Да это же Жасмин!"
    au "Принцесса с самого начала не слушалась отца"
    hide screen jasmin
    hide screen jasmin2
    m "......"
    show screen bordel
    with dissolve
    au "А злые языки поговаривали, что ее видели подрабатывающей в местном борделе"

    g9 "кто молодоец? вот этот парень!"
    hide screen bordel
    au "когда султан окончательно отчаялся, он решил прибегнуть к чужой помощи"
    m "...."
    m "все было немного не так...."
    $ backgr = "new/market.jpg"
    show screen fruk
    show screen sultan
    with Dissolve(1.5)
    au "и он отправился в город к одному старцу"

    m "....."
    hide screen fruk
    hide screen sultan
    $ backgr = "new/room.jpg"
    show screen fruk
    show screen sultan
    with Dissolve(1.5)
    g4 "что? это же моя старая лавка...."
    au "он спросил у старца...."
    g4 "черт, что? так это я что ли старец?!!"
    sult "ходят слухи, что ты имеешь большой опыт в воспитании юных девушек"
    m "......."
    g9 "ага, еще какой"
    au "Старец сказал ему: великие пески не знают более опытного учителя"
    m ".....{w}.......................{w}....................................."
    g4 "вообще то нет"
    sult "у меня есть для тебя работа"
    m "мое мнение здесь вообще не учитывается?"
    au "старец ответил ему: любое твое желание, о великий султан"
    g4 "великий султан? я великий джин!"
    sult "отлично!"
    sult "это должно остаться в тайне ото всех"
    m "...........{w}....................."
    au "Старец ответил ему: твое желание для меня закон"
    sult "вот и отлично"
    g4 "хватит уже говорить за меня, тупая птица"
    sult "Жасмииин!"
    $ jasm = "new/jas10.png"
    show screen jasmin
    with dissolve
    pause 2.0
    $ jasm = "new/jas08.png"
    jas "Зачем мы приехали сюда?"
    $ jasm = "new/jas10.png"
    sult "с этого дня этот человек будет тебя обучать"
    $ jasm = "new/jas05.png"
    jas "что? все по новой?"
    m "на самом деле я не против"
    $ jasm = "new/jas13.png"
    jas "чему он может меня научить?"
    sult "вести себя не как дешевая девка из местного борделя, конечно же"
    $ jasm = "new/jas11.png"
    g4 "че"
    g4 "все было не так"
    $ jasm = "new/jas08.png"
    jas "это ничего не изменит, папа"
    $ jasm = "new/jas11.png"
    sult "дочь султана не может вести себя как последняя шлюха, дорогая"
    $ jasm = "new/jas08.png"
    jas "вам не понять меня, папа"
    $ jasm = "new/jas15.png"
    jas "я всегда мечатала о карьере, а не о пустом замке с одним только тигром"
    $ jasm = "new/jas11.png"
    sult "если ты не прекратишь, я выдам тебя замуж за самого стремного из всех претендентов"
    $ jasm = "new/jas13.png"
    jas "это кого же?"
    $ jasm = "new/jas05.png"
    sult "за Джафара"
    m "некоторые вещи не меняются даже в рассказах тупой птицы...."
    sult "По окончании учебы моя прекрасная Жасмин должна вести себя как настоящая леди"
    m "......"
    sult "удачи"
    hide screen sultan
    with dissolve
    pause 1.0
    hide screen jasmin
    $ jasm = "new/jas03.png"
    show screen jasmin2
    with dissolve
    m "........{w}...........................{w}..........................................."
    m "эм"
    m "и что..."
    g4 "я что действительно должен это делать?!"
    g4 "птица, ты издеваешься?!"
    au "После того как султан покинул его дом, старец приступил к обучению принцессы"
    m ".............{w} черт"
    m "эм..."
    m "и что мне теперь делать?"
    pause 5.0

    m "ничего?"
    m "............"
    m "хм, ну и ладно"
    $ jasm = "new/jas04.png"
    jas "что ты хочешь, старик?"
    menu:
        jas "что ты хочешь, старик?"

        "станцуй для меня":
            m "Так, начнем первый урок"
            jas "Я не буду этим заниматься"
            m "..."
            m "но ведь твой отец приказал..."
            jas "плевать я хотела что он там сказал!"
            m "он хочет чтобы я была маленькой куколкой, на которую приходили любоваться его друзья"
            jas "А на меня и мои желания ему плевать!"
            m "но если мы ничего не будем делать, он прикажет меня казнить, а тебя выдаст за Джафара"
            jas "....."
            jas "........."
            jas "Что ты хочешь?"
            m "Основой хорошего этикета всегда было..."
            m "...."
            m "........"
            m "танец!"
            jas "....."
            jas "что?"
            m "любая уважающая себя принцесса должна уметь поражать мужчин своим танцем"
            jas "что?"
            jas "хах, после моего танца мужчины валяются передо мной на коленях"
            m "...."
            g9 "потому что ты дочь своего отца"
            jas "что?!"
            jas "ты смеешь сомневаться?!"
            jas "так, сиди здесь"
            hide screen jasmin2
            with dissolve
            g9 "вот дура"
            ">Жасмин выходит на пол минуты и возвращается в открытом наряде"

            $ jasm = "new/jas20.png"
            show screen jasmin2
            with dissolve
            jas "ну, что старик, как тебе?"
            m "......"
            m "мы говорили о танце"
            jas "хах, ну держись, старик"
            hide screen jasmin2
            with dissolve
            show screen tanec
            ">Принцесса Жасмин принимается танцевать развратный танец"
            ">Вы сходу беретесь за свой член"
            jas "старый извращенец"

            g9 "ох да, круто"
            jas "как тебе такое, старик"
            show screen tanec3
            ">Принцесса жасмин снимает с сосков предметы и начинает трясти голой грудью"
            g9 "ох да, сука"
            "вы чувствуете, что сейчас приплывете"
            g9 "оохх ддаааааааа"
            g9 "даааааааааа"
            hide screen tanec
            hide screen fruk
            hide screen tanec3
            hide screen jasmin2
            hide screen agraba2
            show screen phoenix_main
            with Dissolve(1.0)
            show screen genie_jerking_sperm
            g9 "даааааааааааааааааааааа"
            hide screen genie_jerking_sperm
            stop music fadeout 1.0
            m "..........."
            m "эм...."
            g4 "черт побери, что ты сделала"
            $ ph_body = "f/phx3.png"
            ph "я?"
            ph "я просто рассказала историю"
            $ ph_body = "f/phx2.png"
            m "...."
            m "а как я оказался в Аграбе?"
            $ ph_body = "f/phx3.png"
            ph "в Аграбе?"
            ph "вы все время были здесь, мастер"
            $ ph_body = "f/phx2.png"
            m "...."
            ph  "......"
            $ ph_body = "f/phx3.png"
            ph "еще что-то?"
            $ ph_body = "f/phx2.png"
            g4 "черт, теперь не интересно"
            m "сегодня можешь идти, но в следущий раз у тебя так просто не получится"
            $ ph_body = "f/phx5.png"
            ph "да, мастер"
            show screen heal3
            $ renpy.play('sounds/magic4.ogg')
            hide screen new_fenix
            hide screen phoenix_main
            show screen phoenix

            pause 3

            hide screen heal3
            $ phoenix_chated = 1
            hide screen bld1

            show screen animation_feather
            if daytime:
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
            else:
                play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
            jump day_main_menu
            if daytime:
                jump night_start
            else:
                jump day_start

        "подай мне фрукты":
            m "подай мне фрукты"
            $ jasm = "new/jas02.png"
            jas "что?!"
            jas "я принцесса!"
            jas "а ты просто старик!"
            $ jasm = "new/jas04.png"
            m "...."
            m "если ты так ничему и не научишься, то нам обоим придется не сладко"
            $ jasm = "new/jas03.png"
            jas "......"
            jas ".........."
            hide screen jasmin
            hide screen jasmin2
            with dissolve
            show screen blkfade
            with dissolve
            ">Жасмин выходит из комнаты ненадолго"
            ">Вы присаживаетесь на свое старое кресло"
            hide screen jasmin2
            hide screen blkfade
            $ backgr = "new/fruit02.jpg"
            show screen fruk
            ">Появляется Жасмин с блюдом в руках"
            jas "ваши фрукты..."
            ">Жасмин нехотя кормит вас виноградом"
            g9 "да ладно, че ты"
            jas "это глупо"
            m "а что бы ты хотела?"
            m "что бы я хотела?"
            $ backgr = "new/fruit03.jpg"
            jas "...."
            show screen blkfade
            with dissolve
            pause 1.0
            $ backgr = "new/hjob_01.jpg"

            ">Жасмин убирает фрукты в сторону и спускается к вашим ногам"
            hide screen blkfade
            $ backgr = "new/hjob_01.jpg"
            g9 "шаришь"
            ">Вы стягиваете с себя штаны и Жасмин принмается сосать ваш член"
            $ backgr = "new/hjob_03.jpg"
            jas "чавк чавк чавк чавк"
            g9 "все таки хорошие были тогда деньки"
            jas "чавк чавк чавк"
            jas "кха..."
            jas "что?"
            m "у тебя отлично получается"
            jas "...."
            jas "чавк чавк чавк чавк"
            "вы чувствуете, что сейчас приплывете"
            g9 "оохх ддаааааааа"
            g9 "даааааааааа"
            hide screen fruk

            hide screen tanec
            hide screen fruk
            hide screen tanec3
            hide screen bordel
            hide screen agraba2
            show screen phoenix_main
            with Dissolve(1.0)

            show screen genie_jerking_sperm
            g9 "даааааааааааааааааааааа"
            hide screen genie_jerking_sperm
            stop music fadeout 1.0
            m "..........."
            m "эм...."
            g4 "черт побери, что ты сделала"
            $ ph_body = "f/phx3.png"
            ph "я?"
            ph "я просто рассказала историю"
            $ ph_body = "f/phx2.png"
            m "...."
            m "а как я оказался в Аграбе?"
            $ ph_body = "f/phx3.png"
            ph "в Аграбе?"
            ph "вы все время были здесь, мастер"
            $ ph_body = "f/phx2.png"
            m "...."
            ph  "......"
            $ ph_body = "f/phx3.png"
            ph "еще что-то?"
            $ ph_body = "f/phx2.png"
            g4 "черт, теперь не интересно"
            m "сегодня можешь идти, но в следущий раз у тебя так просто не получится"
            $ ph_body = "f/phx5.png"
            ph "да, мастер"
            show screen heal3
            $ renpy.play('sounds/magic4.ogg')
            hide screen new_fenix
            hide screen phoenix_main
            show screen phoenix

            pause 3

            hide screen heal3
            $ phoenix_chated = 1
            hide screen bld1

            show screen animation_feather
            if daytime:
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
            else:
                play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
            jump day_main_menu
            if daytime:
                jump night_start
            else:
                jump day_start


label phoenix_potion:
    g9 "Теперь должно получиться"

    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5


    with Dissolve(0.3)



    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx3.png"
    ph "Я слушаю, мой господ......"
    $ ph_body = "f/phx14.png"
    ph "..........."
    $ ph_body = "f/phx10.png"
    ph "Хагси???"
    $ ph_body = "f/phx15.png"
    m "*похоже сработало*"
    $ ph_body = "f/phx10.png"
    ph "Это ты?"
    $ ph_body = "f/phx15.png"
    m ".....{w} да"
    $ ph_body = "f/phx3.png"
    ph "как ты сюда попал???"
    $ ph_body = "f/phx2.png"
    m "......"
    m "Это долгая история"
    $ ph_body = "f/phx13.png"
    ph "Давай сбежим отсюда, хагси! Забери меня отсюда!"
    $ ph_body = "f/phx13.png"
    m "эм..."
    g4 "это не самая лучшая идея"
    ph "..."
    $ ph_body = "f/phx9.png"
    ph "я понимаю, ты тоже не можешь уйти от старика...."
    $ ph_body = "f/phx2.png"
    m "Я сумел выбраться всего на 15 минут..."
    $ ph_body = "f/phx14.png"
    ph "что? 15 минут?"
    $ ph_body = "f/phx2.png"
    ph "...."
    $ ph_body = "f/phx11.png"
    ph "У нас Нет времени, Хагси...."
    $ ph_body = "f/phx2.png"
    g9 "Что мы будем делать"
    $ ph_body = "f/phx12.png"
    ph "я так давно не видела тебя..."
    g9 "......."
    pause 0.5
    show screen blkfade
    with d8
    ">Феникс сама залезает к вам в штаны и принимается сосать ваш член"
    $ fen_im = "new/f1.png"
    hide screen desk_02
    hide screen desk
    hide screen new_fenix
    hide screen phoenix_main
    hide screen bld1
    hide screen new_fenix
    hide screen feeding
    hide screen gin_fenix



    show screen chair_02
    show screen desk_02
    show screen desk


    show screen fenix_sex4
    pause 1.0
    hide screen blkfade
    with dissolve
    pause 5.0

    ph_5 "я уже забыла какой он у тебя большой"
    hide screen fenix_sex4
    show screen fenix_sex5
    with d3
    pause 5.0
    hide screen fenix_sex5
    show screen fenix_sex4
    with d3
    ph_1 "Как ты оказался тут??"
    g9 "Я....{w} я сильно рисковал...."
    ph_4 "мой храбрый Хагси"
    hide screen fenix_sex4
    show screen fenix_sex5
    with d3
    ph "ЧАВК ЧАВК ЧАВК ЧАВК"
    pause 5.0

    g9 "*черт, как долго я этого ждал*"
    m "*похоже этот старик здорово ее достал*"
    ph "ЧАВК ЧАВК ЧАВК ЧАВК"
    hide screen fenix_sex5
    show screen fenix_sex4
    with d3
    ph_1 "как ты смог сюда попасть без старика?"
    m "эм...."
    m "я обхитрил его"
    ph_4 "мой милый, хитрый хагси"
    hide screen fenix_sex4
    show screen fenix_sex5
    with d3
    ph "ЧАВК ЧАВК ЧАВК ЧАВК"
    ">Вы начинаете приплывать"
    g4 "ааааххаахххххххх"
    $ phx_pot = 1
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex4
    hide screen fenix_sex5
    hide screen gin_fenix
    show screen new_fenix

    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    m "Мне нужно уходить"
    $ ph_body = "f/phx9.png"
    ph "Да, нельзя, чтобы нас поймали"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen fenix_sex4
    hide screen fenix_sex5
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start



label phoenix_potion2_zel:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5

    with Dissolve(0.3)

    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx3.png"
    ph "Я сл...."
    $ ph_body = "f/phx10.png"
    ph "Хагси!"
    $ ph_body = "f/phx3.png"
    ph "Ты снова пришел ко мне!"
    $ ph_body = "f/phx13.png"
    g9 "ты меня знаешь"
    $ ph_body = "f/phx13.png"
    ph "Мой храбрый хагси!"
    $ ph_body = "f/phx13.png"
    g9 "Что же мы будем делать?"
    $ ph_body = "f/phx12.png"
    ph "ты придумал, как нам выбраться отсюда?"
    m "...."
    m "эм... вообще то, нет"
    $ ph_body = "f/phx14.png"
    ph "но..."
    $ ph_body = "f/phx9.png"
    ph "Как же так..."
    $ ph_body = "f/phx14.png"
    ph "неужели, мне придется всю жизнь провести в заперти с этим... этим мерзавцем..."
    g4 "эм..."
    m "ну..."
    m "Может однажды у меня получится чего-то придумать"
    $ ph_body = "f/phx3.png"
    ph "а что у тебя не получается?"
    $ ph_body = "f/phx2.png"
    m "Ну..."
    g9 "Я постоянно придумываю новый план, но снейп каждый раз ходит по пятам и все обламывает"
    $ ph_body = "f/phx3.png"
    ph "Снейп?"
    $ ph_body = "f/phx2.png"
    m "да, это профессор зельеварения"
    $ ph_body = "f/phx3.png"
    ph "зельеварения..."
    $ ph_body = "f/phx10.png"
    ph "точно!"
    $ ph_body = "f/phx15.png"
    ph "Мы должны попробовать приготовить зелье очищения от всех чар"
    m "...{w}......."
    g4 "че?"
    $ ph_body = "f/phx3.png"
    ph "это должно сработать"
    $ ph_body = "f/phx15.png"
    ph "С ним я смогу всегда быть в своем настоящем облике"
    m "... че?"
    $ ph_body = "f/phx3.png"
    ph "кажется я помню ингридиенты"
    $ ph_body = "f/phx2.png"
    g4 "*кто меня за язык тянул, что ей опять взбрело в голову?*"
    $ ph_body = "f/phx3.png"
    ph "пыльца плотоядного фикуса, яйца свинорыла, слюна гразной шлюхи и жабры плавучих слонов"
    $ ph_body = "f/phx2.png"
    m "..."
    $ ph_body = "f/phx13.png"
    ph "достань эти ингридиенты и мы снова сможем быть вместе"
    $ ph_body = "f/phx13.png"
    m "Да но сейчас то почему не..."
    $ phx_pot = 2
    hide screen phoenix_main
    $ ph_body = "f/phx5.png"
    
    show screen phoenix_main
    with dissolve
    ph "я буду ждать тебя, любимый"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather

    m "вот черт"
    g4 "и где интересно мне все это искать?"
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start


label phx_first_potion:
    $ ph_body = "f/phx9.png"
    ph "Как же так..."
    $ ph_body = "f/phx14.png"
    ph "неужели, мне придется всю жизнь провести в заперти с этим... этим мерзавцем..."
    
    m "ну..."
    m "Может однажды у меня получится чего-то придумать"
    $ ph_body = "f/phx3.png"
    ph "а что у тебя не получается?"
    $ ph_body = "f/phx2.png"
    m "Ну..."
    g9 "Я придумываю план, но снейп ходит по пятам и все обламывает"
    $ ph_body = "f/phx3.png"
    ph "Снейп?"
    $ ph_body = "f/phx2.png"
    m "да, это профессор зельеварения"
    $ ph_body = "f/phx3.png"
    ph "зельеварения..."
    $ ph_body = "f/phx10.png"
    ph "точно!"
    $ ph_body = "f/phx15.png"
    ph "Мы должны попробовать приготовить зелье полиморфизма"
    m "..."
    g4 "че?"
    $ ph_body = "f/phx3.png"
    ph "это должно сработать"
    $ ph_body = "f/phx15.png"
    ph "С ним я смогу всегда быть в своем настоящем облике"
    m "... че?"
    $ ph_body = "f/phx3.png"
    ph "кажется я помню ингридиенты"
    $ ph_body = "f/phx2.png"
    g4 "*кто меня за язык тянул, что ей опять взбрело в голову?*"
    $ ph_body = "f/phx3.png"
    ph "2 корня мандрагоры, 7 литров крови девственницы, 1 мазок из жопы грязной шлюхи и 12 лапок гиены"
    $ ph_body = "f/phx2.png"
    m "..."
    $ ph_body = "f/phx13.png"
    ph "достань эти ингридиенты и мы снова сможем быть вместе"
    $ ph_body = "f/phx13.png"
    m "Да но сейчас то почему не..."
    $ pnx_stage = 20
    hide screen phoenix_main
    $ ph_body = "f/phx5.png"
    
    show screen phoenix_main
    with dissolve
    ph "я буду ждать тебя, любимый"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather

    m "вот черт"
    g4 "и где интересно мне все это искать?"
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phx_prinesi:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5


    with Dissolve(0.3)



    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx2.png"
    ph "...."
    $ ph_body = "f/phx10.png"
    ph "Хагси!"
    $ ph_body = "f/phx11.png"
    if phx_pot == 2:
        g9 "it's me"
        m "У нас очень мало времени"
        g9 "Как на счет легкого перепихона"
        $ ph_body = "f/phx14.png"
        ph "не время дурачиться, хагси"
        g4 "..."
    else:
        m "..."
    ph "ты принес ингридиенты?"
    m "..."
    menu:
        "да, я принес жабры плавучих слонов" if phx_ingr1 == 1:
            $ phx_ingr1 = 2
            if (phx_ingr2 == 2) and (phx_ingr3 == 2) and  (phx_ingr4 == 2):
                jump phx_zelie
            else:
                jump phx_ura
            

        "да, я принес пыльцу плотоядного фикуса" if phx_ingr2 == 1:
            $ phx_ingr2 = 2
            if (phx_ingr1 == 2) and (phx_ingr3 == 2) and  (phx_ingr4 == 2):
                jump phx_zelie
            else:
                jump phx_ura
            
        "да, я принес яйца свинорыла" if phx_ingr3 == 1:
            $ phx_ingr3 = 2
            if (phx_ingr2 == 2) and (phx_ingr1 == 2) and  (phx_ingr4 == 2):
                jump phx_zelie
            else:
                jump phx_ura
            

        "да, я принес слюну грязной шлюхи" if phx_ingr4 == 1:
            $ phx_ingr4 = 2
            if (phx_ingr2 == 2) and (phx_ingr3 == 2) and  (phx_ingr1 == 2):
                jump phx_zelie
            else:
                jump phx_ura
            

        "нет, я еще их не достал":
            $ ph_body = "f/phx14.png"
            ph "не достал?"
            $ ph_body = "f/phx9.png"
            ph "но..."
            $ ph_body = "f/phx14.png"
            ph "ты не хочешь, чтобы мы были вместе?"
            g4 "ну почему же..."
            hide screen phoenix_main
            $ ph_body = "f/phx5.png"
            show screen phoenix_main
            with dissolve
            ph "я думала, мы любим друг друга..."
            $ ph_body = "f/phx4.png"
            m "стой..."
            
            show screen heal3
            $ renpy.play('sounds/magic4.ogg')
            hide screen desk
            hide screen chair_02
            hide screen phoenix_main
            hide screen new_fenix
            hide screen feeding
            show screen phoenix
            show screen genie
            pause 3

            hide screen heal3
            $ phoenix_chated = 1
            hide screen bld1

            show screen animation_feather
            pause 1.0
            m "черт"
            g4 "она что, шантажирует меня сексом?"
            jump day_main_menu
            if daytime:
                jump night_start
            else:
                jump day_start

label phx_zelie:
    $ ph_body = "f/phx2.png"
    ph "Это значит...{w} все почти готово..."
    $ ph_body = "f/phx1.png"
    m "Ага"
    m "это..."
    m "как на счет отблагодарить старину хагси?"
    $ ph_body = "f/phx15.png"
    ph "... да"
    g9 "...."
    show screen blkfade
    with dissolve
    ">Феникс распахивает ваш халат и прыгает на член"
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen chair_02
    show screen desk_02
    $ dcr = renpy.random.randint(1,3)
    if dcr == 1:
        show screen fenix_sex1

        #show screen fenix_sex2
        hide screen blkfade
        with dissolve
        pause 5.0
        $ ph_body = "f/phx3.png"
        $ ph_body = "f/phx3.png"
        ph_1 "Давай сбежим отсюда, Хагси, как мы и мечтали"

        g4 "........."
        m "эм...."
        $ ph_body = "f/phx3.png"
        ph_2 "Я не могу больше жить взаперти"
        g4 "......................"
        "*Шлеп*"
        ph_5 "аххааа"
        ph_1 "мы могли бы жить вместе, для этого не нужен этот чертов замок"
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        "Шлеп ШЛЕП ШЛЕП ШЛЕП"
        g4 "надо что-то сделать, чтобы она от меня отстала"
        ph_4 "я всегда хотела увидеть африку, там бы нас не нашли"
        "........"

        $ ph_body = "f/phx3.png"
        ph_5 "ааххх, ты всегда знал, что я люблю"
        "*Шлеп* *Шлеп* *Шлеп*"





    elif dcr == 2:
        #show screen fenix_sex2

        show screen fenix_sex3
        hide screen blkfade
        with Dissolve(1.0)
        


        ph_2 "Этот старик постоянно домогается меня"
        m "....."
        ph_4 "Не хочу, чтобы кто-то кроме тебя прикасался ко мне!"
        m "......"
        ph_6 "Сначала он давал идиотские поручения, а теперь каждый раз пытается меня изнасиловать!"
        g4 "........."
        ph_1 "почему ты молчишь, хагси?"
        g4 "я....{w} просто пытаюсь доставить тебе удовольствие"
        ph_4 "о мой милый хагси!"




        ph_4 "Я так давно тебя не видела"
        g9 "....."
    



    elif dcr == 3:
        show screen fenix_sex3
        hide screen new_fenix
        hide screen blkfade
        with Dissolve(1.0)
        

        ph_1 "этот старик пытался подкатывать ко мне"
        m "ну....."
        m "ты ведь все таки его птица"
        ph_5 "хахаха, он действительно верил, что я не понимаю о чем он"
        m "......"
        ph_3 "хахахахахахахаха"
        g4 ".................."
        m "знаешь, что?"
        ph_1 "что?"
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        "*Шлеп*"
        ph_5 "аааахахххххх.... мой Хагси!"


    
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex1
    hide screen fenix_sex2
    hide screen fenix_sex3
    hide screen fenix_sex4
    hide screen gin_fenix
    show screen new_fenix
    hide screen desk_02
    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    $ ph_body = "f/phx11.png"
    ph "нам остался последний шаг"
    $ ph_body = "f/phx15.png"
    ph "нужно приготовить из этого зелье"
    $ ph_body = "f/phx13.png"
    ph "и тогда мы будем вместе... навсегда..."
    g4 "угу"
    hide screen phoenix_main
    $ ph_body = "f/phx5.png"
    show screen phoenix_main
    with dissolve
    ph "я буду ждать тебя, любимый"
    $ phx_pot = 3
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3
    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1
    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phx_ura:
    $ ph_body = "f/phx10.png"
    ph "Ура!"
    $ ph_body = "f/phx15.png"
    ph "значит нам осталось совсем немного"
    $ ph_body = "f/phx12.png"
    ph "ты наверное хочешь, чтобы я отблагодарила тебя?"
    g9 "ты еще спрашиваешь"
    show screen blkfade
    with dissolve
    ">Феникс распахивает ваш халат и прыгает на член"
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen chair_02
    show screen desk_02
    $ dcr = renpy.random.randint(1,3)
    if dcr == 1:
        show screen fenix_sex1

        #show screen fenix_sex2
        hide screen blkfade
        with dissolve
        pause 5.0
        $ ph_body = "f/phx3.png"
        $ ph_body = "f/phx3.png"
        ph_1 "Давай сбежим отсюда, Хагси, как мы и мечтали"

        g4 "........."
        m "эм...."
        $ ph_body = "f/phx3.png"
        ph_2 "Я не могу больше жить взаперти"
        g4 "......................"
        "*Шлеп*"
        ph_5 "аххааа"
        ph_1 "мы могли бы жить вместе, для этого не нужен этот чертов замок"
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        "Шлеп ШЛЕП ШЛЕП ШЛЕП"
        g4 "надо что-то сделать, чтобы она от меня отстала"
        ph_4 "я всегда хотела увидеть африку, там бы нас не нашли"
        "........"

        $ ph_body = "f/phx3.png"
        ph_5 "ааххх, ты всегда знал, что я люблю"
        "*Шлеп* *Шлеп* *Шлеп*"





    elif dcr == 2:
        #show screen fenix_sex2

        show screen fenix_sex3
        hide screen blkfade
        with Dissolve(1.0)
        


        ph_2 "Этот старик постоянно домогается меня"
        m "....."
        ph_4 "Не хочу, чтобы кто-то кроме тебя прикасался ко мне!"
        m "......"
        ph_6 "Сначала он давал идиотские поручения, а теперь каждый раз пытается меня изнасиловать!"
        g4 "........."
        ph_1 "почему ты молчишь, хагси?"
        g4 "я....{w} просто пытаюсь доставить тебе удовольствие"
        ph_4 "о мой милый хагси!"




        ph_4 "Я так давно тебя не видела"
        g9 "....."
    



    elif dcr == 3:
        show screen fenix_sex3
        hide screen new_fenix
        hide screen blkfade
        with Dissolve(1.0)
        

        ph_1 "этот старик пытался подкатывать ко мне"
        m "ну....."
        m "ты ведь все таки его птица"
        ph_5 "хахаха, он действительно верил, что я не понимаю о чем он"
        m "......"
        ph_3 "хахахахахахахаха"
        g4 ".................."
        m "знаешь, что?"
        ph_1 "что?"
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        pause 0.5
        $ renpy.play('sounds/slap.mp3')
        with vpunch
        "*Шлеп*"
        ph_5 "аааахахххххх.... мой Хагси!"


    
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex1
    hide screen fenix_sex2
    hide screen fenix_sex3
    hide screen fenix_sex4
    hide screen gin_fenix
    show screen new_fenix
    hide screen desk_02
    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    m "Мне нужно идти"
    $ ph_body = "f/phx13.png"
    ph "Я буду ждать, любимый"
    ph "найди ингридиенты"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start


label phx_gdezelie:
    hide screen phoenix
    show screen phoenix_main
    hide screen animation_feather
    hide screen phoenix_food
    show screen new_fenix
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3
    hide screen heal3
    $ ph_body = "f/phx2.png"
    ph "..."
    $ ph_body = "f/phx14.png"
    ph "эм..."
    $ ph_body = "f/phx9.png"
    ph "это было не зелье...."
    $ ph_body = "f/phx2.png"
    m "да"
    $ ph_body = "f/phx3.png"
    ph "ты еще не сделал зелье?"
    $ ph_body = "f/phx2.png"
    m "Пока не успел"
    $ ph_body = "f/phx14.png"
    ph "но..."
    $ ph_body = "f/phx9.png"
    ph "..."
    $ ph_body = "f/phx14.png"
    g9 "может быть немного поиграем, пока старика нет? а то я сильно рисковал, чтобы сюда придти"
    $ ph_body = "f/phx3.png"
    ph "рисковал..."
    $ ph_body = "f/phx14.png"
    ph "но почему ты пришел без зелья?"
    m "ну..."
    $ ph_body = "f/phx3.png"
    ph "с ним мы сможем всегда быть вместе..."
    $ ph_body = "f/phx14.png"
    m "я постараюсь принести в следующий раз"
    hide screen phoenix_main
    $ ph_body = "f/phx5.png"
    show screen phoenix_main
    with dissolve
    ph "я надеюсь на это, хагси"
    $ ph_body = "f/phx4.png"
    g4 "эй, что, куда..."
    $ ph_body = "f/phx5.png"
    ph "принеси зелье..."
    
    
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    g4 "вот ведь ушлая птица"
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phx_last_zelie:
    m "Ну что, дать ей это зелье, как она и просила?"
    menu:
        "дать зелье фениксу":
            jump phx_last_zel

        "Позже":
            m "Ладно, наверное лучше потом"
            return

label phx_last_zel:
    stop music fadeout 2.0
    show screen phoenix_main
    
    show screen phoenix_evil
    show screen bld1
    $ ph_body = "new/ph_wtf2.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    pause 3
    hide screen heal3
    pause 
    ph "...."
    m "неужели сработало?"
    $ ph_body = "new/ph_wtf2.png"
    ph "...."
    play music 'music/16 The Chess Game.mp3'
    $ ph_body = "new/ph_wtf.png"
    ph "это..."
    $ ph_body = "new/ph_wtf2.png"
    pause 0.5
    $ ph_body = "new/ph_wtf.png"
    ph "я снова свободна?"
    $ ph_body = "new/ph_wtf2.png"
    pause 0.5
    $ ph_body = "new/ph_evsm.png"
    ph "это снова я"
    
    g6 "..."
    $ ph_body = "new/ph_def2.png"
    ph "ты..."
    m "..."
    $ ph_body = "new/ph_govor.png"
    ph "ты не Хагрид"
    $ ph_body = "new/ph_def.png"
    g5 "..."
    $ ph_body = "new/ph_sm1.png"
    ph "а я еще думала, с чего бы это вдруг этот трольский выродок вдруг начал слушать что я ему говорю"
    m "эм..."
    $ ph_body = "new/ph_def.png"
    ph "а это оказался лишь ослабевший джин в овечей шкуре"
    m ".....{w} как ты узнала?"
    $ ph_body = "new/ph_sm1.png"
    ph "хах, я вижу все твои низшие чары насквозь"
    $ ph_body = "new/ph_def2.png"
    ph "Ты единственный идиот который мне поверил за все эти 400 лет"
    g4 "что за..."
    $ ph_body = "new/ph_govor.png"
    ph "еще мерлин затачил меня в тело феникса, чтобы только сильный маг мог меня освободить"
    $ ph_body = "new/ph_def2.png"
    ph "он думал, что ни один чародей в светлом уме не станет освобождать Моргану, персидского дракона-убийцу"
    m "..."
    $ ph_body = "new/ph_def.png"
    ph "но он не учел одного глупого похотливого джина"
    m "эм..."
    g4 "что это все значит?"
    $ ph_body = "new/ph_evsm.png"
    ph "это значит, что я сожгу весь этот замок до тла. Вместе с тобой"
    g4 "думаешь, я позволю этому случится?"
    $ ph_body = "new/ph_def.png"
    ph "хаха, ну давай"
    play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
    pause 3
    jump phoenix_duel

label after_duel:
    hide image "03_hp/05_props/06_phoenix.png"
    $ pnx_stage = 1000
    #show screen phoenix
    stop music fadeout 2.0
    show screen points
    show screen phoenix
    show screen phoenix_main
    with dissolve
    pause
    $ ph_body = "new/ph_zlo_s.png"
    ph "... не могу поверить..."
    $ ph_body = "new/ph_govor_s.png"
    ph "наверное ко мне вернулись еще не все силы"
    m "Ну что ж, ты можешь распологаться рядом с фениксом, возьми себе стул"
    $ ph_body = "new/ph_zlo_s.png"
    ph "тебе повезло джин"
    $ ph_body = "new/ph_govor2_s.png"
    ph "в признательность за мое освобождение, я не буду убивать тебя"
    g9 "хах, еще бы, после того как я так тебя отделал"
    $ ph_body = "new/ph_def_s.png"
    ph "прощай, джин"
    hide screen phoenix_main
    with dissolve
    m "эй, стой"
    hide screen phoenix_evil
    hide screen phoenix_evil2
    show screen phoenix_evil3
    pause 0.5
    hide screen phoenix_evil
    hide screen phoenix_evil3
    #hide screen phoenix
    with flashbulb3 
    g4 ".........."
    m "я...{w} даже буду скучать по этой упрямой сучке"
    
    jump day_main_menu

label phoenix_potion2:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5

    with Dissolve(0.3)

    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx3.png"
    ph "Я сл...."
    $ ph_body = "f/phx10.png"
    ph "Хагси!"
    $ ph_body = "f/phx3.png"
    ph "Ты опять смог попасть ко мне"
    $ ph_body = "f/phx13.png"
    g9 "ты же меня знаешь"
    $ ph_body = "f/phx13.png"
    ph "Мой храбрый Хагси!"
    $ ph_body = "f/phx13.png"
    g9 "что мы будем делать"
    $ ph_body = "f/phx12.png"
    ph "твоя птичка давно не сидела на палочке"
    $ ph_body = "f/phx11.png"
    m "....."
    m "ты ведь не про трость, да?"
    $ ph_body = "f/phx12.png"
    ph "а как ты думаешь?"
    $ ph_body = "f/phx12.png"
    g9 "....."
    show screen blkfade
    with dissolve
    ">феникс распахивает ваш халат и буквально бросается на член"
    hide screen phoenix_main
    hide screen bld1

    hide screen feeding
    show screen chair_02
    show screen desk_02
    hide screen new_fenix

    hide screen gin_fenix
    show screen fenix_sex2
    hide screen blkfade
    with dissolve
    pause 5.0
    $ ph_body = "f/phx3.png"
    ph_1 "Давай сбежим отсюда, Хагси, как мы и мечтали"

    g4 "........."
    m "эм...."
    $ ph_body = "f/phx3.png"
    ph_2 "Я не могу больше жить взаперти"
    g4 "......................"
    "*Шлеп*"
    ph_5 "аххааа"
    ph_1 "мы могли бы жить вместе, для этого не нужен этот чертов замок"
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    pause 0.5
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    pause 0.5
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    "Шлеп ШЛЕП ШЛЕП ШЛЕП"
    g4 "надо что-то сделать, чтобы она от меня отстала"
    ph_4 "я всегда хотела увидеть африку, там бы нас не нашли"
    "........"

    $ ph_body = "f/phx3.png"
    ph_5 "ааххх, ты всегда знал, что я люблю"
    "*Шлеп* *Шлеп* *Шлеп*"
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex2
    hide screen gin_fenix
    show screen new_fenix

    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    pause 2.0
    $ ph_body = "f/phx3.png"
    ph "Хагси, так что ты думаешь? Мы ведь так давно мечтали попасть туда, где не будет никаких волшебников, никаких маглов"
    $ ph_body = "f/phx13.png"
    ph"только мы{w}, вместе"
    $ ph_body = "f/phx2.png"
    g4 "........"
    g4 "слышишь? кто-то идет!"
    $ ph_body = "f/phx3.png"
    ph "что? где?"
    $ ph_body = "f/phx2.png"
    m "Мне пора уходить"
    $ ph_body = "f/phx14.png"
    ph "Да, нельзя, чтобы тебя поймали"
    $ phx_pot = 2
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phoenix_potion3:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5


    with Dissolve(0.3)



    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx2.png"
    ph "...."
    $ ph_body = "f/phx10.png"
    ph "Хагси!"
    $ ph_body = "f/phx11.png"
    g9 "это я"
    $ ph_body = "f/phx12.png"
    ph "у нас нет времени"
    $ ph_body = "f/phx12.png"
    g9 "...."
    show screen blkfade
    with dissolve
    ">феникс распахивает ваш халат и буквально бросается на член"
    hide screen feeding
    hide screen phoenix_main
    hide screen new_fenix
    show screen fenix_sex3
    hide screen blkfade
    with Dissolve(1.0)
    ph_2 "Этот старик постоянно домогается меня"
    m "....."
    ph_4 "Не хочу, чтобы кто-то кроме тебя прикасался ко мне!"
    m "......"
    ph_6 "Сначала он давал идиотские поручения, а теперь каждый раз пытается меня изнасиловать!"
    g4 "........."
    ph_1 "почему ты молчишь, хагси?"
    g4 "я....{w} просто пытаюсь доставить тебе удовольствие"
    ph_4 "о мой милый хагси!"




    ph_4 "Я так давно тебя не видела"
    g9 "....."
    show screen blkfade
    with d6
    "..."
    hide screen fenix_sex3
    show screen feeding
    show screen new_fenix
    $ ph_body = "f/phx2.png"

    pause 2.0
    hide screen blkfade
    show screen phoenix_main
    with d6
    $ ph_body = "f/phx13.png"
    ph "Мы должны торопиться, я не смогу долго удерживать старика"
    $ ph_body = "f/phx13.png"
    m "Может быть...{w} не стоит удерживать его?"
    $ ph_body = "f/phx14.png"
    ph "я не позволю никому кроме тебя прикасаться к себе, хагси"
    $ ph_body = "f/phx14.png"
    g4 "...."
    $ ph_body = "f/phx3.png"
    ph "Должен быть способ выбраться отсюда"
    $ ph_body = "f/phx2.png"
    m "......."
    m "я постараюсь"
    $ ph_body = "f/phx13.png"
    ph "Я буду ждать, любимый"
    $ phx_pot = 3
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phoenix_potion4:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5


    with Dissolve(0.3)



    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx2.png"
    ph "...."
    $ ph_body = "f/phx3.png"
    ph "Хагси!"
    $ ph_body = "f/phx2.png"
    g9 "это я"
    $ ph_body = "f/phx3.png"
    ph "у нас нет времени"
    $ ph_body = "f/phx2.png"
    g9 "...."
    show screen blkfade
    with dissolve
    ">феникс распахивает ваш халат и буквально бросается на член"
    hide screen phoenix_main
    show screen fenix_sex11
    hide screen feeding
    show screen chair_02
    show screen desk_02
    hide screen new_fenix
    hide screen blkfade
    with Dissolve(1.0)
    ph_1 "этот старик пытался подкатывать ко мне"
    m "ну....."
    m "ты ведь все таки его птица"
    ph_5 "хахаха, он действительно верил, что я не понимаю о чем он"
    m "......"
    ph_3 "хахахахахахахаха"
    g4 ".................."
    m "знаешь, что?"
    ph_1 "что?"
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    "*Шлеп*"
    ph_5 "аааахахххххх.... мой Хагси!"
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex1
    hide screen gin_fenix
    show screen new_fenix
    hide screen desk_02
    hide screen fenix_sex11
    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    $ ph_body = "f/phx3.png"
    ph "Хагси, ты придумал что-нибудь?"
    $ ph_body = "f/phx2.png"
    g4 "....."
    $ ph_body = "f/phx9.png"
    ph "Я уже 7 лет сижу в этом кабинете"
    $ ph_body = "f/phx14.png"
    ph "Пожалуйста, сделай что-нибудь"
    $ ph_body = "f/phx2.png"
    g4 "я....{w} делаю все что могу"
    m "Мне нужно уходить"
    $ ph_body = "f/phx9.png"
    ph "Да, нельзя, чтобы тебя поймали"
    $ phx_pot = 4
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

label phoenix_potion5:
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    pause.5


    with Dissolve(0.3)



    hide screen phoenix
    hide screen phoenix_food
    show screen new_fenix
    show screen phoenix_main
    hide screen animation_feather
    show screen bld1

    $ ph_body = "f/phx1.png"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')

    pause 3

    hide screen heal3
    $ ph_body = "f/phx2.png"
    ph "...."
    $ ph_body = "f/phx10.png"
    ph "Хагси!"
    $ ph_body = "f/phx11.png"
    g9 "это я"
    $ ph_body = "f/phx12.png"
    ph "у нас нет времени"
    $ ph_body = "f/phx2.png"
    g9 "...."
    show screen blkfade
    with dissolve
    ">феникс распахивает ваш халат и буквально бросается на член"
    hide screen phoenix_main

    hide screen feeding
    show screen chair_02
    show screen desk_02
    $ dcr = renpy.random.randint(1,3)
    if dcr == 1:
        show screen fenix_sex1
    elif dcr == 2:
        show screen fenix_sex2
    elif dcr == 3:
        show screen fenix_sex3
    hide screen new_fenix
    hide screen blkfade
    with Dissolve(1.0)
    ph_1 "этот старик пытался подкатывать ко мне"
    m "ну....."
    m "ты ведь все таки его птица"
    ph_5 "хахаха, он действительно верил, что я не понимаю о чем он"
    m "......"
    ph_3 "хахахахахахахаха"
    g4 ".................."
    m "знаешь, что?"
    ph_5 "что?"
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    pause 0.5
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    pause 0.5
    $ renpy.play('sounds/slap.mp3')
    with vpunch
    "Шлеп ШЛЕП ШЛЕП ШЛЕП"
    ph_5 "аааахахххххх.... мой Хагси!"
    show screen blkfade
    with d8
    pause 0.1
    show screen feeding
    pause 1.0
    hide screen fenix_sex1
    hide screen fenix_sex2
    hide screen fenix_sex3
    hide screen gin_fenix
    show screen new_fenix
    hide screen desk_02
    show screen phoenix_main
    hide screen blkfade
    hide screen chair_02
    with dissolve
    $ ph_body = "f/phx13.png"
    ph "Хагси, ты придумал что-нибудь?"
    $ ph_body = "f/phx13.png"
    g4 "....."
    $ ph_body = "f/phx9.png"
    ph "Я уже 7 лет сижу в этом кабинете"
    $ ph_body = "f/phx3.png"
    ph "Пожалуйста, сделай что-нибудь"
    $ ph_body = "f/phx2.png"
    g4 "я....{w} делаю все что могу"
    m "Мне нужно уходить"
    $ ph_body = "f/phx9.png"
    ph "Да, нельзя, чтобы тебя поймали"
    show screen heal3
    $ renpy.play('sounds/magic4.ogg')
    hide screen desk_02
    hide screen chair_02
    hide screen phoenix_main
    hide screen new_fenix
    hide screen feeding
    show screen phoenix
    show screen genie
    pause 3

    hide screen heal3
    $ phoenix_chated = 1
    hide screen bld1

    show screen animation_feather
    jump day_main_menu
    if daytime:
        jump night_start
    else:
        jump day_start

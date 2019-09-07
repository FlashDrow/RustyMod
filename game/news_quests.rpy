label paper_students_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Сэр, у меня все готово"
    m "Отлично. Давай, выкладывай"
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "В нашей школе многие ученики имеют наглость относится к девушкоам без должного уважения!"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    m "...."
    m "че?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "Постоянные пошлые намеки, скользкие взгляды!"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "Некоторые из них даже трогают их за попу!"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "непонятно куда в это время смотрит администрация?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "Кажется, что это дело пущено на самотек!"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "...."
    m "....."
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Ну как вам?"
    m "Ты это подготовила для газеты?"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "конечно, не буду скрывать, у меня действительно есть талант к публицистике"
    m "Это никуда не годится"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "но как..."
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    m "Ладно, попробуем в следущий раз"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "Да, профессор"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    $ paper_students += 1
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    ">Гермиона передает вам статью для газеты"
    #her "Спасибо, сэр."
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


    
    
    call music_block from _call_music_block_42
    
    return

label paper_students_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    m "Ну что, как новый материал?"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Эм... ну... кажется у меня получилось..."
    m "Давай, по-подробнее"

    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1


    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "Эм... в этот раз я постаралась... кхм..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "придать ему немного..."
    m "немного... ???"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "экспрессии"
    m "давай выкладывай что получилось"

    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Кхм..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Сегодня я шла по коридору"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "так"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "и опять встретила группу студентов"
    $ h_body = "03_hp/13_hermione_main/body_09.png"
    m "они были из Слизерина?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "эм... из разных факультетов"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    m "Что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "Я хотела пройти, но один из них отпустил грязную шуточку в мой адрес"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "Я подошла к ним и хотела высказать ему, что нельзя так вести в стенах школы магии"
    m "ага"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "но он не стал слушать меня и грубо взял за руку"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Вдруг они окружили меня и повели в одну из аудиторий"
    m "уже интереснее... что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_28.png"
    her "С меня сорвали всю одежду и принялись лапать"
    m "отлично"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Они трогали меня везде, профессор"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_47.png"
    her "Один даже прокричал \"гриффиндорская шлюха\""
    m "Ох ништяк"
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "Я плакала, но они не прекращали"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "Когда они закончили, я осталась голой по среди школы, сэр!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Когда я шла по коридору, все видели, что на мне..."
    m "Так вот это давай приберегем для отдельной статьи"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "а...{w} да"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Как я справилась, сэр?"
    m "Отлично, после этого выпуска наша газета точно будет признана лучшей"
    m "С нетерпением жду, когда мы будем делать материал для следующего выпуска"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "следующего?"
    m "ну конечно"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "да, сэр"
    $ whoring += 5
    $ paper_students += 1
    ">Гермиона передает вам статью для газеты"
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_43

    return
label paper_students_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    m "Ну что, как?"
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "кхм"
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    $ h_body = "03_hp/13_hermione_main/body_08.png"
    her "Сегодня я сидела в библиотеке и готовила домашнее задание по зельеварению"
    m "так"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Я старалась сосредоточится на учебе, но мне вдруг мне помешали"
    m "кто это был?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "это был Дра... кхем... один парень из слизерина со своими прихвостнями"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "они очень громко разговаривали. Так, что я не могла заниматься"
    $ h_body = "03_hp/13_hermione_main/body_16.png"
    her "Я сделала им замечание, что в библиотеке нельзя так себя вести, но они не послушали"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Один из них взял и скинул все мои учебники на пол"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "Второй заоломил мне руку и повалил на стол"
    m "... ого"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "Он задрал мне юбку и спустил трусы"
    m "ох черт"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "я пыталась достать свою палочку, чтобы превратить их всех в лягушек, но двое парней начали держать меня за руки"
    $ h_body = "03_hp/13_hermione_main/body_26.png"
    her "один был сзади, потом другой подошел спереди"
    m "да, круто"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Они делали это одновременно"
    m "ништяк"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "потом они поменялись"
    m "даа"
    $ h_body = "03_hp/13_hermione_main/body_26.png"
    her "Когда они ушли я еле сползла со стола и не могла двигаться"
    m "даа, крутяк"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "в этот раз у меня получилось еще лучше, да профессор?"
    m "а? да это будет бомба а не выпуск"
    m "ты отлично постаралась"
    $ h_body = "03_hp/13_hermione_main/body_68.png"
    her "Это отличная практика для меня, пусть это и всего лишь статьи для газеты"
    m "возможно когда нибудь тебе вручат пулицерскую премию"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Вы думаете?"
    m "конечно"
    $ h_body = "03_hp/13_hermione_main/body_75.png"
    her "хи-хик"
    $ paper_students += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_44
    return


label paper_prepods_04:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m ".................."
    $ h_body = "03_hp/13_hermione_main/body_95.png"
    her ".................."
    m ".................."
    $ h_body =  "03_hp/13_hermione_main/body_73.png"
    her "Сэр ?"
    m "Я рассматривал тебя для того, чтобы стимулировать свое воображение."
    $ h_body =  "03_hp/13_hermione_main/body_71.png"
    her "Профессор, вы всегда придумываете что-то неприличное !"
    her "Лучше я начну, чтобы поскорее кончить."
    g9 "................................."
    $ h_body =  "03_hp/13_hermione_main/body_50.png"
    her "Закончить, сэр ! Завершить !"
    $ h_body =  "03_hp/13_hermione_main/body_04.png"
    her "Итак, сегодня я снова помогла своему факультету."
    m "Так так."
    her "Нам были очень нужны очки, все только об этом и говорили."
    $ h_body =  "03_hp/13_hermione_main/body_05.png"
    her "Ведь слизеринки вовсю жульничали, они только и делают, что продают се..."
    m "Гермиона, ближе к теме !"
    m "(Про снейповских шлюх я уже достаточно слышал от него самого.)"
    $ h_body =  "03_hp/13_hermione_main/body_10.png"
    her "Мммм да. Хорошо, сэр."
    her "Был вечер и уроки уже закончились. Но было одно место, где еще можно было обнаружить задержавшегося учителя и немного заработать."
    m "Продолжай, мне начинает нравиться."
    $ h_body =  "03_hp/13_hermione_main/body_11.png"
    her "И вот, я прошла по темному коридору к заветной двери. Внутри сидел наш профессор зельеварения..."
    her "Я знала, что он именно тот, кто действительно ценит услужливость..."
    g9 "Да, да !"
    m "То есть нет ! Нельзя вот так прямо порочить настоящего учителя !"
    $ h_body =  "03_hp/13_hermione_main/body_12.png"
    her "Но сэр ! Почему нет ? Ведь он действительно любитель..."
    g4 "Стоп ! Подумай сама, ведь если мы хотим обличить всех непорядочных учителей, нельзя спугнуть их раньше времени !"
    m "(Уф. Выкрутился.)"
    $ h_body =  "03_hp/13_hermione_main/body_24.png"
    her "О да, сэр, я поняла ! Но можно распустить хотя бы маленький слух, что именно о нем речь в рассказе..."
    m "На твоем месте я бы больше беспокоился о слухах, кто его автор."
    $ h_body =  "03_hp/13_hermione_main/body_12.png"
    her "Ох. Я поняла, профессор. Лучше я продолжу."
    her "Итак, высокая худая фигура примерно 180 см роста в черной мантии с длинными темными волосами и крючковатым носом ждала меня."
    her "\"Не желаете ли чего, профессор\", - спросила я."
    her "Но преподаватель ответил презрительным молчанием и продолжил проверять работы по зельев... по своему предмету."
    m "(Как точно описано. Хм.)"
    $ h_body =  "03_hp/13_hermione_main/body_16.png"
    her "Тогда я снова стала намекать на то, как сильно наш факультет и лично я нуждаемся в очках."
    her "Вволю насладившись своей властью, он зло усмехнулся и кивнул."
    m "(Она просто не могла это придумать. Неужели ? Да нет, не может быть...)"
    $ h_body =  "03_hp/13_hermione_main/body_31.png"
    her "\"Ваша грудь не соответствует уставу\" - мрачно заметил он. Форма ученицы не должна быть так сильно натянута. Это просто неприлично !"
    her "\"Но сэр\", - ответила я, - \"Я же не виновата в этом !\""
    $ h_body =  "03_hp/13_hermione_main/body_15.png"
    her "Сэр, что с вами ?"
    her "Профессор ?"
    g7 "А ? Да, продолжай же, не останавливайся."
    $ h_body =  "03_hp/13_hermione_main/body_14.png"
    her "И вот он заявляет, что должен проверить, действительно ли грудь настоящая, или я намеренно хочу ввести всех в заблуждение..."
    her "\"Я дам тебе пять очков за это\", - обещает он, и его глаза загораются."
    g9 "(Готов поклясться, что она сосредоточилась на совсем иных книгах, чем до нашей встречи.)"
    $ h_body =  "03_hp/13_hermione_main/body_33.png"
    her "И вот я смущенно соглашаюсь и замираю."
    m "О да, продолжай !"
    $ h_body =  "03_hp/13_hermione_main/body_34.png"
    her "Сне... Учитель дотрагивается до моей груди и начинает мять ее. В этот момент я замечаю, что дверь приоткрыта, и кто-нибудь может увидеть нас."
    her "Собрав все силы, я остаюсь неподвижной до конца."
    m "Эх, а я уже надеялся..."
    $ h_body =  "03_hp/13_hermione_main/body_47.png"
    her "Сэр, мне и так было трудно все это расска... то есть придумать !"
    m "Хорошо, но признайся, ведь это было на самом деле ?"
    $ h_body =  "03_hp/13_hermione_main/body_50.png"
    her "Сэр ! Как вы можете такое говорить ? И потом мы не договаривались, что я буду выдавать свои секреты."
    her "Вы хотели получить рассказ ! Вот вам рассказ."
    m "Ладно, ты можешь идти."
    $ h_body =  "03_hp/13_hermione_main/body_56.png"
    her "(Неужели он действительно догадался ?)"
    m "(А ведь Снейп ничего мне не рассказал об этом. Вот же...)"
    $ paper_prepods += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_45
    return
label paper_prepods_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Что у тебя получилось на этот раз?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Кхм..."
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Как то раз я пришла к одному учителю, чтобы уточнить один момент, который он не объяснил на уроке"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "так"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Он сказал мне сесть за парту"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "ага"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Когда я разложила все учебники, я услышала, что он закрыл кабинет на ключ"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_28.png"
    her "Он... сказал, что я должна раздеться"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "На мои возражения он сказал, что может превратить мою жизнь в этой школе в ад"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "а если я буду хорошей девочкой, он даже поможет с очками для моего факультета"
    m "хах, и что ты сделала?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "я... мне пришлось"
    m "что пришлось?"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "помочь своему факультету"
    m "что ты сделала?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Он положил свои руки мне на плечи"
    m "хах, а потом?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "а потом опустился ниже и начал лапать мою грудь"
    m "круто"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "потом опустился еще ниже..."
    m "ништяк"
    m "что было потом"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "Он снял штаны, я уже хотела закричать, но..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "похоже что он перевозбудился и... сделал это, забрызгав мою одежду"
    m "....{w}....."
    g4 "какого черта"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "как вам, профессор?"
    m "тебе еще нужно много учится писательскому ремеслу"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "Ну а что, разве вы не почувствовали интригу?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "Тебе нужно поработать над счастливыми концовками, девочка"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "...{w} да профессор"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    $ paper_prepods += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Спасибо, сэр."
    $ h_body = "03_hp/13_hermione_main/body_01.png"
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_46
    return
label paper_prepods_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "что на этот раз?"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Как то раз я не успела подготовится в экзамену"
    m "Такое бывает?"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "Это же рассказ, это не было на самом деле"
    m "Кхм, ну да, конечно же"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Эм... я сидела один на один с листочком и не знала что писать"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "Студенты один за одним садились и сдавали экзамен, с переменным успехом"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Я ничего не знала, поэтому очень боялась идти"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "Еще я не хотела, чтобы кто-то услышал, как я отвечаю, что ничего не знаю"
    m "*зевок* что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_14.png"
    her "Когда последний студент сдал экзамен мы остались с ним в кабинете одни"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "уже интереснее, что потом?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Он увидел мой пустой листок и..."
    m "....{w} и?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Он предложил сделку"
    m "какую?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Что поставит мне тройку, если я дам потрогать ему свою грудь"
    m "хм... уже не плохо"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "Но я отказалась"
    g4 "что? почему?"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "я никак не могла принять его гнусное предложение, ведь..."
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "ведь я круглая отличница, мне не нужна была тройка!"
    m "и что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Он засмеялся и... и снял штаны"               
    m "хах, что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_79.png"
    her "Я смотрела на него, потом на его..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "мне нужна была эта пятерка"
    m "и что ты сделала?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "я... мне пришлось..."
    m "что там было?"
    $ h_body = "03_hp/13_hermione_main/body_68.png"
    her "я сделала ему лучший минет в его жизни, чтобы у него не осталось даже и мысли поставить мне что то отличное от пятерки"
    m "хм, неплохо"
    m "отлично мисс Грейнджер вы явно делаете успехи"
    $ paper_prepods += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_47   
    return
label paper_prepods_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Давай выкладывай"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "кхем..."
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Как-то раз я зашла в кабинет одного нашего учителя, чтобы взять дополнительное домашнее задание для учеников, которые хотят чего-то добиться в жизни"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "Когда я сказала ему, что хочу стать первой в рейтинге студентов, он осмотрел меня с ног до головы и сказал, что может помочь мне в этом"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "хм... истории на реальных событиях всегда интереснее"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "я уже было обрадовалась и достала блокнот, чтобы записать задание..."
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "Но он..."
    m "что он?"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "Он распахнул свою мантию!"
    m "и что там было?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "под ней он был абсолютно голый!"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "я даже взвизгнула от неожиданности"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "он сказал... сказал..."
    m "что он сказал?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "он сказал{w} \"Вот твое задание\""
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "....."
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "ну как вам, сэр?"
    m ".... "
    g4 "а что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "эм... дальше?"
    g4 "дальше!"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "ну, я подумала, что стоит оставить концовку открытой"
    m "а ты что смеешься что ли"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "многие великие писатели использовали этот прием"
    m ".... ну ладно"
    m "но в следующий раз это уже не прокатит"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "да, сэр"
    $ paper_prepods += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_48
    return
label paper_prepods_05:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1

    m "Выкладывай"
    $ h_body = "03_hp/13_hermione_main/body_14.png"
    her "Недавно в нашей школе проходил чемпионат дуэльного клуба"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    m "что за чемпионат"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "эм...{w} он проводился вашим приказом, сэр"
    m "ах да, точно"
    $ h_body = "03_hp/13_hermione_main/body_14.png"
    her "призом были целых 50 очков для факультета победителя, поэтому я никак не могла пройти мимо этого турнина"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "только был один момент... я никогда не учавстовала в дуэлях"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "поэтому я попросила одного из учителей, проводивших этот турнир, помочь мне с тренировками"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "я пришла к нему в кабинет в один из вечеров, чтобы потренироваться, как мы и договаривались"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "мы встали в стойки, и..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Он сразу же, без предупреждения, выкрикнул какое-то заклинание, которое я не слышала до этого"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "после этого я поняла, что не могу двигаться"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "я не сразу поняла его замысел. Сначала я ждала когда он снимет это заклинание и мы продолжим заниматься, но он начал идти по направлению ко мне"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "Когда он начал снимать с меня одежду у меня началась паника"
    m "не плохо"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "он начал трогать мои груди, потом... потом ноги... и попу..."
    m "крутяк"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "у меня потекли слезы, сэр"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_26.png"
    her "я стояла в полном бессилии как либо себя защитить, пока он... он... глумился надо мной"
    m "что еще он делал"
    $ h_body = "03_hp/13_hermione_main/body_28.png"
    her "я плакала от своей беззащитности, а он лишь смеялся глядя мне в глаза"
    m "а потом?"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "он... он поцеловал меня в губы"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "а потом не только в губы..."
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "потом он достал свой член и...."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "ему было не очень удобно делать это, ведь я не могла двигаться, но он не останавливался"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "эта пытка длилась, наверное больше часа, пока он не использовал каждую мою дырочку"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "он оставил меня в кладовке... раздетую и всю перемазанную в..."
    show screen jerking_off_cum
    g4 "хааа!"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "профессор!"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "вы что?!"
    hide screen jerking_off_cum
    g9 "это отличная статья, она точно обеспечит нам первое место"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "спасибо, профессор"
    $ paper_prepods += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_49
    return

label paper_podder_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, уже готово?"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "В общем..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Чтобы написать эту статью мне пришлось самой вступить в группу поддержки нашей команды"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_14.png"
    her "я даже не думала, что там все так серьезно"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "когда ты смотришь матч, и видишь их, кажется, что это всего лишь танцующие девушки"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "но на самом деле все не так"
    $ h_body = "03_hp/13_hermione_main/body_11.png"
    her "когда я пришла, меня встретил капитан"
    m "ага"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "когда со стандартными вопросами было покончено, он встал изза стола и..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "он сказал, что мне придется выполнять много сложных акробатических движений"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "и он..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "и он должен убедиться в уровне моей физической подготовки"
    m "каким образом?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "мне пришлось... эм..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "мне пришлось снять с себя всю одежду"
    m "круто, что дальше"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "он долго рассматривал меня, потом начал \"проверять мышцы\""
    m "чего делать?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "он начал трогать меня"
    m "ништяк"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "он всю меня облапал и сказал, что я принята"
    m "..."
    m "неплохо, для начала"
    $ paper_podder += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_50
    return
label paper_podder_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Выкладывай"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Кхем - кхем"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "После того как я попала в команду группы поддержки, мне пришлось очень много тренироваться"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я даже не думала, что все эти танцы могут оказаться настолько сложными"
    $ h_body = "03_hp/13_hermione_main/body_16.png"
    her "я бы даже не стала называть это танцами, это самый настоящий спорт!"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    m "..."
    g4 "ближе к делу"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "как то раз, я не смогла выполнить один очень сложный прыжок и навернулась с большой высоты"
    m "..."

    her "у меня очень сильно болела нога"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "сначала я даже подумала, что у меня перелом"
    m "и что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_14.png"
    her "Наш капитан сказал, что мне нужно оказать первую медицинскую помощь и отнес меня в раздевалку"
    m "так..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "он начал натирать мою ногу"
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "я до этого слышала о спортивном массаже, но не думала, что это так больно"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "после пары минут боль утихла... а его...{w} прикосновения стали нежнее"
    m "так..."
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "и он переключился на... другие части тела..."
    m "хах... какие же?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "на все..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "наша форма достаточно открытая и он имел доступ почти ко всему"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "в итоге вместо массажа он меня просто облапал"
    m "..."
    m "тебе понравилось?"
    $ h_body = "03_hp/13_hermione_main/body_119.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "как вы можете?"
    $ h_body = "03_hp/13_hermione_main/body_120.png"
    her "конечно же д... нет!"
    $ paper_podder += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_51
    return
label paper_podder_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Есть успехи?"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "Недавно состоялся матч нашей команды с командой Слизерина"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "и мы победили их!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "счет был разгромный, 160:30"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "по этому случаю была организована вечеринка"
    m "хм... вечеринка?"
    m "что там было?"
    $ h_body = "03_hp/13_hermione_main/body_70.png"
    her "а... да, так, ничего интересного, мне было скучно"
    m "....."
    g4 "какого черта"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "поэтому я решила пойти подготовить уроки"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "я уже почти дошла до библиотеки, но меня встретили несколько членов нашей комнады"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    m "..."
    m "что они хотели?"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "один из них подошел ко мне и сказал, что сегодня моя очередь"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_22.png"
    her "я спросила о чем он говорит, на что он мне ответил, что по давней Гриффиндорской традиции одна девушка из группы поддержки спит со всей командой"
    m "хах, и что ты сделала?"
    $ h_body = "03_hp/13_hermione_main/body_43.png"
    her "ну... я правда всего пару недель была в команде, поэтому не знала всех правил"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "пришлось выполнять традиции"
    g9 "хах"
    m "сколько их было?"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "пятеро... или шестеро..."
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "правда когда я спросила остальных девочек, они тоже ничего подобного не слышали"
    $ h_body = "03_hp/13_hermione_main/body_28.png"
    her "наверное тоже недавно в команде"
    g9 "да... скорее всего"
    $ paper_podder += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_52
    return
label paper_comand_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Ну что, как успехи?"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "ну... я стала членом сборной гриффиндора по квидичу"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "тренер не очень тепло это воспринял"
    m "что он сказал?"
    $ h_body = "03_hp/13_hermione_main/body_77.png"
    her "что мне лучше идти готовить борщи"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "это подстягнуло меня еще больше!"
    $ h_body = "03_hp/13_hermione_main/body_16.png"
    her "я поняла, что буду играть в команде до тех пор, пока этот мужлан не извинится!"
    m "*зевок* есть что-то интересное?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "ну... пока что... наверное нет"
    m "черт"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "ах, да. Я забыла попросить вас!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Можно ли выделить место для женской душевой?"
    m "душевой?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "да, мне было не по себе, когда после тренировки пришлось мыться в одной душевой со всеми"
    m "...."
    g9 "это будет отличный выпуск"
    $ paper_comand += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_53
    return
label paper_comand_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "что нового?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Эм... кхм..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Мне всегда плохо давалась маневренность"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "За долгое время тренировок, я таки научилась развивать неплохую скорость по прямой, но у меня никак не получалось вписываться в повороты"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Я с дикой завистью смотрела на моих товарищей, которые могли выписывать в воздухе любые, самые сложные фигуры"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "Я очень старалась их повторять, но у меня ничего не получалось"
    m "мне уже скучно..."
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "но однажды....!"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "После того, как наша команда потерпела поражение, в основном из-за меня, я не смогла вовремя поймать снитч..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я уже почти поймала его, но он быстро повернул влево... а я...."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "а я не смогла вовремя повернуть за ним...."
    $ h_body = "03_hp/13_hermione_main/body_21.png"
    her "вместо того, чтобы резко развернуться и догнать его, я на всей скорости врезалась в стену"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "и пока я падала..."
    $ h_body = "03_hp/13_hermione_main/body_22.png"
    her "я видела, как ловец другой команды, летящий прямо за мной, буквально пронесся мимо меня и поймал его"

    m "ближе к делу"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Чувство стыда тогда перебило боль от удара"
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "Упав на землю, я плакала, сэр"
    $ h_body = "03_hp/13_hermione_main/body_26.png"
    her "Но не от боли..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "После проигранного матча, ко мне подошел тренер"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Я уже думала, что он хочет сказать, что я больше не буду играть с командой, но..."
    m "но...?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "он отвел меня в свой кабинет и показала кое, что..."
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "Он сказал, что это старое приспособление, которое признали нарушающим права женщин"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Но оно должно было решить мою проблему..."
    m "Что это было?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "эм... ну... оно крепилось прямо на метлу и..."
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "я должна была садится прямо на него"
    m "..."
    m "что?! что это было?!!"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "эм... это был вибратор с креплением"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "сначала я не поверила, но все же попробовала"
    $ h_body = "03_hp/13_hermione_main/body_128.png"
    her "результат превыси все ожидания"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "С его помощью управление метлой стало таким легким... и..."
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "приятным"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "если раньше приходилось управлять ногами, то теперь я управляла своей... кхм..."
    $ h_body = "03_hp/13_hermione_main/body_122.png"
    her "теперь у меня даже было преимущество перед остальными игроками..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я против нечестной игры, но.... это было так...."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "хорошо"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_122.png"
    her "Вам понравилось?"
    m "Отлично"
    m "Завтра выпуск будет готов"
    $ paper_comand += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
    $ h_body = "03_hp/13_hermione_main/body_01.png"
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_54
    return
label paper_comand_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Уже готово?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "кхем-кхем"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "Эм... вообще я никогда особо не интересовалась спортом"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Я вообще начала играть для того, чтобы доказать, что девушки могут могут показывать хорошие результаты в спорте на равне с мужчинами"
    m "угу..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "но это оказалось не так просто, как я думала"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "Мне казалось, что у меня очень даже неплохо получается"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "Но тренер совсем не давал мне шансов"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "На тренировках лишь отрабатывала разные элементы, но мне совсем не давали игровых минут"
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "В то время как в основном составе несколько человек вообще ничего не делали, просто висели в воздухе!"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Я даже слышала, что половина команды ходит на тренировки только для освобождения от пары лекций"
    $ h_body = "03_hp/13_hermione_main/body_66.png"
    her "и в такой ситуации я почти не получала игрового времени"
    m "*зевок* ага"
    $ h_body = "03_hp/13_hermione_main/body_68.png"
    her "Чтобы продемонстрировать, что девушки тоже могут играть в квиддич мне нужно было попасть в основной состав!"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "Поэтому я подошла к тренеру и сказала ему, что тоже хочу учавствовать в реальных матчах"
    m "..."
    m "что он сказал?"
    $ h_body = "03_hp/13_hermione_main/body_65.png"
    her "он предложил учавствовать в костюме талисмана"
    m "хах"
    m "Что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "Я не хотела сдаваться! Ведь он просто посмеялся надо мной!"
    $ h_body = "03_hp/13_hermione_main/body_28.png"
    her "Мне показалось отличной идеей предложить продемонстрировать ему чем я выгодно отличаюсь от своих конкурентов..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "думаю, мне бы не составило труда победить в соревновании пару лентяев из команды"
    $ h_body = "03_hp/13_hermione_main/body_20.png"   
    her "он долго смотрел на меня недоумевающим взглядом, как будто я сморозила глупость, потом... потом..."
    m "..."
    m "что потом?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Мне кажется он немного неправильно меня понял"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "он закрыл дверь на ключ, подошел ко мне и сказал, что я могу начинать"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "Я переспросила его, что он имеет ввиду"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "он ответил \"как что? демонстрировать свои достоинства\""
    m "круть"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Сначала я не поверила, но когда он встал и расчехлил свой член, я поняла, что он серъезно хочет..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "в тот момент я поняла, что у девушек даже есть некоторое преимущество"
    $ h_body = "03_hp/13_hermione_main/body_69.png"
    her "эта было одной из причин по которой я начала заниматься ООП"
    m "..."
    m "так что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "ах..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "эм... я не хотела сдаваться и... ну..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_75.png"
    her "на следующий день я уже играла в стартовом составе"
    m "..."
    m "......"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "ну как?"
    m "почему так мало?"
    g4 "наша аудитория хочет захватывающих историй"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да но..."
    g4 "так  мы никогда не сможем победить!"
    $ h_body = "03_hp/13_hermione_main/body_67.png"
    her "...."
    m "ты что, хочешь посрамить всю школу?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "нет сэр!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "в следующий раз я постараюсь лучше"
    m "очень на это надеюсь"
    $ paper_comand += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_55

    return
label paper_comand_04:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "Кхем"
    $ h_body = "03_hp/13_hermione_main/body_127.png"
    her "Чтож, как я и говорила, я получила место в стартовом составе..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Получив реальное игровое время, я быстро поняла, что играть не так просто, как кажется со стороны"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Теперь на тренировках я играла вместе со всеми и... мне кажется это не очень устроило большинство ребят"
    m "хм... почему?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "я не знаю почему... но они явно пытались досадить мне!"
    m "как?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "по крайней мере трое игроков только и делали, что швыряли в меня бладжеры!"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "Ну и что, что они защитники, на поле кроме меня еще 10 игроков! А они как будто вообще не целились в кого то кроме меня!"
    m "ближе к делу"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "да..."
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "вскоре пришло время для первого матча с моим участием"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "это было ужастно"
    m "*зевок*"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "я не могла сделать буквально ничего, меня сбивали раз разом!"
    her "у меня не получалось даже подняться в воздух, в меня сразу же прилетал мяч"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Наша команда проиграла с разгромным счетом... это был позор..."
    m "*zzzz*"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "после матча ко мне подошли остальные члены команды"
    m "а?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "их лица выражали презрение"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "Один из них подошел ко мне и сказал, что я позор граффиндора"
    $ h_body = "03_hp/13_hermione_main/body_142.png"
    her "после этих слов я заплакала, сэр"
    $ h_body = "03_hp/13_hermione_main/body_141.png"
    her "как он смел... после всего того, что я сделала...."
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "я сказала, что исправлюсь... буду играть лучше..."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "но он... он..."
    m "что он?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "он потребовал извинений..."
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "они обступили меня и..."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "начали трогать..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я не знала что делать, ведь... если я закричу, то уже никогда не смогу играть в этой команде..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "мне пришлось... пришлось..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "...{w} извиняться..."
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "с меня в мгновение сорвали всю одежду... а их руки..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "они были везде..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_141.png"
    her "кто-то из них повалил меня и я оказалась на полу..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я попыталась встать, но мне не дали подняться..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "я оказалась окружена их членами со всех сторон"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "и... и...{w} мне пришлось..."
    $ h_body = "03_hp/13_hermione_main/body_142.png"
    her "они уходили только тогда, когда кончали мне на лицо"
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "и мне пришлось отсосать у каждого..."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "после того дня у меня как то само собой получилось играть лучше..."
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "..."
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "ну как?"
    m "ништяк, это будет просто бомбезный выпуск"
    $ paper_comand += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_56


    return

label paper_holm_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что получлось?"
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "я караулила там каждый вечер в течении недели, сэр"
    m "это было ради чести школы, девочка"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "да, но... я не могу сказать, что результат превзошел мои ожидания"
    m "что ты нашла?"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "эм... ну..."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "В один из дней, когда я сидела в кустах, я наконец таки услышала кое-что"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "мне кажется... это были... эм... вздохи сэр"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Я пыталась понять с какой стороны шел звук, но он разносился эхом по всему холму"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "Мне пришлось обойти все кусты, но я так и не смогла их найти"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "И так получилось, что я только слушала, как они..."
    m "как долго это продолжалось?"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "эм... не знаю, наверное минут 10"
    m "ладно, этого хватит, может быть в следующий раз у тебя получится найти больше"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "да, сэр"
    $ paper_holm += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_57
    return
label paper_holm_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Ну что, как прошло?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "В этот раз все прошло несколько удачней"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "рассказывай"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "я сидела в засаде, как вы и говорили"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "в один прекрасный момент я все таки увидела одну пару!"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "они шли, держа друг друга за руки"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "мне пришлось проследовать за ними некоторое время, чтобы убедиться в их намерениях"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "и я была права, они действительно шли на тот самый холм"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "эм... я дождалась, когда они начнут и вышла из кустов, чтобы взять у них интервью"
    g9 "хах"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "но у меня не получилось этого сделать"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "едва увидев меня, девушка закричала на всю округу и сразу отпрыгнула куда-то"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "ее парень был не таким робким и сразу же достал свою волшебную палочку"
    g9 "какую из них?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "это не смешно, профессор, я рисковала собственной жизнью"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "он начал пулять в меня атакующими заклинаниями"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "мне повезло, что он, видимо, был двоечник и не знал действительно сильных заклинаний"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "на самом деле было забавно наблюдать как голый парень со стоящим членом стреляет в меня заклинаниями"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "мне пришлось ретироваться"
    m "в следующий раз попробуй подойти к ним не прямо во время секса"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "да, наверное..."
    $ paper_holm += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_58
    return
label paper_holm_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ sperm_on_tits = True
    $ h_body = "03_hp/13_hermione_main/body_91.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    g4 "ого"
    $ h_body = "03_hp/13_hermione_main/body_97.png"
    her "сэр... я... я..."
    $ h_body = "03_hp/13_hermione_main/body_98.png"
    her "я больше не буду делать репортажи про это место!"
    m "что случилось?"
    $ h_body = "03_hp/13_hermione_main/body_89.png"
    her "они... они..."
    m "что произошло?"
    $ h_body = "03_hp/13_hermione_main/body_99.png"
    her "я как обычно сидела в засаде и ждала когда появится новая парочка"
    $ h_body = "03_hp/13_hermione_main/body_97.png"
    her "не знаю как, но я не заметила как ко мне подлетел столбняковый москит"
    m "кто?"
    $ h_body = "03_hp/13_hermione_main/body_104.png"
    her "он укусил меня и меня схватил паралич"
    m "а..."
    $ h_body = "03_hp/13_hermione_main/body_191.png"
    her "и тут как на зло появились эти парни из слизерина"
    $ h_body = "03_hp/13_hermione_main/body_192.png"
    her "я совсем не могла двигаться, поэтому надеялась, что они меня не заметят, но...{w} но..."
    m "но?"
    $ h_body = "03_hp/13_hermione_main/body_105.png"
    her "они заметили меня, сэр!"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_95.png"
    her "они...{w} воспользовались мной как куклой..."
    $ h_body = "03_hp/13_hermione_main/body_89.png"
    her "я не могла двигаться, но видела и чувствовала все, что они выделывали со мной"
    $ h_body = "03_hp/13_hermione_main/body_98.png"
    her "я больше никогда не пойду в этом место, сэр"
    m "ну и ладно, на самом деле получилось даже лучше"
    $ h_body = "03_hp/13_hermione_main/body_105.png"
    her "да? ну... эм... ладно..."
    $ h_body = "03_hp/13_hermione_main/body_103.png"
    m "пойду приведи себя в порядок"
    $ h_body = "03_hp/13_hermione_main/body_101.png"
    her "да, сэр"
    $ paper_holm += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_100.png"
    her "Спасибо, сэр."
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

    $ sperm_on_tits = False
    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_59
    return
label paper_forest_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1

    m "Ну что, как прошло?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "Я даже не знаю сэр"
    m "что произошло?"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "я шла по лесу, хотела найти единорога"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "но наткнулась на озеро"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "и увидела там парня из пуффендуя"
    m "что он там делал?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "в том то и дело!"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "он был там не один"
    m "а с кем?"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "он разговаривал... даже нет... он... общался с русалкой"
    m "...."
    m "русалкой?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да, я тоже не думала, что у нас в лесу есть озеро с руаслками, обычно они встречаются в более крупных водоемах"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "но это определенно была именно русалка, сэр"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "было похоже на то, что он выучил язык подводных людей, потому что они явно общались между друг другом посредством какого-то... шепота"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "я не стала им мешать и спряталась за деревом"
    m "и... что потом?"
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "я не уверена..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "он достал из кармана какую-то блестяшку и отдал ей, после чего она исчезла в воде"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "....{w} и все?"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "нет"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "она вернулась буквально через пол минуты"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "потом он снял штаны и..."
    m "....{w} что?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "она начала... эм..."
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "она...{w} делала это"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "она сосала его член, сэр"
    $ h_body = "03_hp/13_hermione_main/body_71.png"
    her "при чем я удивилась ее технике, я даже не знала что так можно..."
    m "как долго это продолжалось?"
    $ h_body = "03_hp/13_hermione_main/body_44.png"
    her "ох, его на долго хватило, мне пришлось сидеть там пол часа"
    g4 "пол часа?! черт возьми, где находится это озеро?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "эм... для чего вам, сэр?"
    g4 "я хочу...{w} провести важный эксперимент"
    $ h_body = "03_hp/13_hermione_main/body_04.png"
    her "впрочем, это не имеет значения, потому что нашла это озеро только потому, что заблудилась"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    g4 "что?!"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "у меня получилось вернуться в хогвартс только взлетев вверх на метле, я не смогу найти это место"
    m "......"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "...."
    m "ладно"
    $ paper_forest += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_60
    return
label paper_forest_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
   
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "f/rip13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    #$ h_body = "03_hp/13_hermione_main/body_01.png"
    $ h_body = "f/rip9.png"
    her "сэр..."
    m "...."
    m "что с тобой?"
    $ h_body = "f/rip10.png"
    her "на меня... напали сэр..."
    $ h_body = "f/rip9.png"
    m "кто?"
    $ h_body = "f/rip10.png"
    her "тентакула!"
    $ h_body = "f/rip9.png"
    m "...."
    m "кто?"
    $ h_body = "f/rip2.png"
    her "тентакула! изза темноты, я не заметила как подошла к ее кусту"
    $ h_body = "f/rip12.png"
    her "я поняла что случилось, когда уже висела вверх ногами, а ее ветки елозили по всему моему телу"
    m "...{w} хах"
    $ h_body = "f/rip5.png"
    her "я нашла глазами свою палочку на земле, но у меняне было и шанса дотянуться..."
    m "что было дальше?"
    $ h_body = "f/rip12.png"
    her "она подвесила меня за руки и ноги в воздухе"
    $ h_body = "f/rip13.png"
    her "я не могла ничего с этим сделать"
    $ h_body = "f/rip9.png"
    her "ее ветки начали рвать на мне одежду, сэр!"
    m "хах, неплохо"
    $ h_body = "f/rip12.png"
    her "потом они обвились вокруг моих грудей..."
    $ h_body = "f/rip11.png"
    m "..."
    $ h_body = "f/rip9.png"
    her "они сжимали их..."
    $ h_body = "f/rip11.png"
    her "потом они забрались в...."
    m "...."
    m "куда?"
    $ h_body = "f/rip6.png"
    her "ко мне в трусики...!"
    $ h_body = "f/rip13.png"
    her "я ничего не могла сделать с этим..."
    $ h_body = "f/rip4.png"
    her "они так... елозили там..."
    m "...{w} тебе понравилось?"
    her "...... что?"
    $ h_body = "f/rip11.png"
    her "как вы можете сэр?"
    $ h_body = "f/rip10.png"
    her "меня почти что изнасиловали"
    m "ты записала это?"
    $ h_body = "f/rip7.png"
    her "...."
    m "Гермиона передает вам статью для газеты"

    m "отлично"
    $ paper_forest += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "f/rip5.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_61
    return
label paper_forest_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "Ну что, в этот раз у тебя получилось найти единорога?"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "эм... единорога?"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "ах, да... ну..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "вообще-то нет"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    m "хм... но ты не сильно расстроена?"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "ну... немного, наверное"
    m "что там было?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "в этот раз, чтобы не произошло ничего подобного, как раньше, я позвала с собой Гарри и Рона"
    m "хм..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "мы шли в глубь леса, но ничего не могли найти"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "изрядно устав, мы решили сделать привал"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "и услышали пение птицы"
    m "... птицы?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "да..."
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "оно было такое...{w} приятное"
    m "приятное?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "да... мы до этого не слышали ничего подобного"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "и не проходили такой птицы на уроках"
    $ h_body = "03_hp/13_hermione_main/body_128.png"
    her "мы чувствовали такое... умиротворение..."
    m "и что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "эм... мы почему то вообще забыли зачем пошли в лес"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "и...{w} Рон поцеловал меня..."
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "я давно замечала, как он на меня смотрит, но он никак не мог осмелиться и наконец созрел"
    m "что было потом?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "потом тоже самое сделал Гарри"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "я не думала, что он тоже..."
    $ h_body = "03_hp/13_hermione_main/body_78.png"
    her "они оба принялись целовать меня..."
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "я даже не знаю, что это было... все получилось само собой... мы скинули одежду и..."
    $ h_body = "03_hp/13_hermione_main/body_74.png"
    her "мне показалось, что это длилось не больше пары минут"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "потом этот звук исчез и мы очнулись глубокой ночью..."
    m "отлично"
    m "ты записала это?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "конечно, сэр"
    $ paper_forest += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_62
    return



label paper_room_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    $ h_body = "03_hp/13_hermione_main/body_10.png"
    her "кхем, если говорить о достопримечательностях хогвартса, то нельзя не упомянуть о секс комнате"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "..."
    m "секс комнате?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "так ее называют старшекурсники, которые уже...{w} кхм... старшекурсники"
    m "что это за комната?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Обычно ее все называют выручай-комната"
    $ h_body = "03_hp/13_hermione_main/body_16.png"
    her "она появляется тогда, когда тебе что то очень нужно и ты трижды проходишь мимо нее"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    g4 "что за бред"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "Ее обнаружили не так давно..."
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "Дело в том, что в нашей школе действительно дефицит мест, где можно было бы уединиться"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "и старшекурсникам она стала попадаться весьма часто"
    m "с чем это связано?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я думаю, что не обошлось без влияния нашей газеты, сэр"
    g9 "хах"
    m "что в этой комнате?"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "все зависит от того, что человеку нужно в данный момент"
    $ h_body = "03_hp/13_hermione_main/body_24.png"
    her "так как всем нужно лишь место для... эм... общения..."
    $ h_body = "03_hp/13_hermione_main/body_74.png"
    her "обычно это просто комната с кроватью и пачкой... кхм... подручных средств"
    g9 "хах"
    m "решено!"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "эм... решено?"
    m "в этот раз мы опубликуем эту статью, но в следующий раз мне нужен будет репортаж с места событий"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "блин...."
    $ paper_room += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_63
    return

label paper_room_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, у тебя получилось?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "эм... я не уверена..."
    m "что это значит?"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "я сделала все, что нужно было для того чтобы найти эту комнату"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я нашла парня, с которым... эм... хотела бы уединиться"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "трижды прошла мимо нее"
    m ".... "
    m "и что потом?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "я нашла комнату, которой не должно было быть, но..."
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    m "что но?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "это была какая-то ошибка!"
    m "что такое?"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "когда мы зашли туда, там..."
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "там был настоящий склад бдсм игрушек!"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "меня никогда не интересовали подобные вещи!"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "это какая-то ошибка"
    m "может быть ты еще не доконца разобралась в себе?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "сэр, я... да я бы никогда!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я не представляю, что нужно делать с половиной из них"
    $ h_body = "03_hp/13_hermione_main/body_71.png"
    her "какая-то часть чем то напоминает вполне обычные игрушки, но некоторые вещи..."
    m "то есть... ты успела подробно изучить их? вы все перепробовали?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "сэр!"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "конечно же нет"
    m "хах, ну да"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "Это наверное была какая-то ошибка, мне точно не была нужна такая комната!"
    m "хм..."
    m "может быть это не ты нашла эту комнату?"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "что вы имеете ввиду?"
    $ h_body = "03_hp/13_hermione_main/body_18.png"
    her "Джейк??"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "маньяк!"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "извращенец!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я больше никогда не буду с ним разговаривать"
    m "да ладно, может быть у него просто пара необычных желаний"
    m "неплохо, хватит на статью"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "отлично"
    $ paper_room += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_64
    return
label paper_room_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "Я сделала!"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "отчет о комнате"
    m "отлично, выкладывай"
    $ h_body = "03_hp/13_hermione_main/body_74.png"
    her "В этот раз я взяла Рона и сказала ему, что покажу кое-что интересное"
    $ h_body = "03_hp/13_hermione_main/body_128.png"
    her "и я специально не брала с собой презервативов"
    
    m "и что из этого вышло?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "мы минут 10 кружили по всему этажу и наконец нашли дверь, которой раньше не было"
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "когда мы вошли, там была огромная кровать, пачка презервативов, смазка и душ"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "я даже не думала, что в нашем замке можно так легко... кхм..."
    m "и что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "эм... ну..."
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "мы использовали ее по назначению"
    m "как?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "ну... сели писать доклад, конечно же"
    m "сколько докладов вы написали?"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "его хватило только на 3 раза... то есть доклада, сэр"
    m "отлично"
    ">Гермиона передает вам материал о тайной комнате"
    $ paper_room += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_65
    return
label paper_puffend_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "эм... ничего"
    m "совсем?"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "я весь день ходила рядом с их корпусом"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "я видела как они пожирают меня глазами, но они продолжали только смотреть"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "в итоге я не выдержала и сама подошла к одному из них"
    m "отлично, и что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "он покраснел, начал тяжело дышать и убежал"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я до самого конца считала, что все эти слухи про пуффендуй - обычные предрассудки"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "но похоже, что это чистая правда"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    m "да ладно. МОжет быть ты подошла не к тому парню"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "Вы думаете?"
    m "Тебе нужно набрать еще материала"
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да сэр"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    ">Гермиона передает вам статью  о пуффендуе"
    m "возможно в следующий раз получится лучше"
    $ paper_puffend += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "Спасибо, сэр."
    $ h_body = "03_hp/13_hermione_main/body_01.png"

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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_66

    return
label paper_puffend_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, как прошло?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "лучше чем в прошлый раз, но все равно ужасно"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "больше никогда не буду тратить свое время на этих соплежуев"
    m "что случилось?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "как и в прошлый раз, мне пришлось проявить инициативу"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "и представьте себе, в этот раз один из них даже пригласил меня на свидание"
    m "уже лучше"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "но оно было ужасно скучным"
    m "почему?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "он все время что-то мямлил себе под нос"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "я потратила на него несколько часов и как только появилась возможность, убежала к вам, сэр"
    $ h_body = "03_hp/13_hermione_main/body_71.png"
    her "похоже все эти слухи были правдой"
    m "какие слухи?"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "о том, что шляпа отправляет в пуффендуй самых бестолковых студентов, сэр"
    m "ты записала все это?"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "конечно, сэр"
    ">гермиона предает вам статью для газеты"
    
    $ paper_puffend += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_67
    return
label paper_puffend_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, получилось в этот раз?"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "эм... ну..."
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "можно сказать и так"
    m "но ты все равно не выглядишь удовлетворенной?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "еще бы!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "они неисправимы эти пуффендуйцы!"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "мне показалось, что я нашла единственного нормального парня во всем факультете!"
    m "и что случилось?"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "ох, он был очень обходителен"
    $ h_body = "03_hp/13_hermione_main/body_78.png"
    her "и так настойчив!"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "так получилось, что... эм... вскоре мы оказались наедине"
    m "наконец-то"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "и он кончил едва прикоснувшись ко мне!"
    m "...."
    g4 "опять"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "наверное, те слухи действительно были правдой"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "хотя, конечно, это проявление расизма с моей стороны и придется описать все это в более сдержанных тонах"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "но настоящую правду я никогда не забуду!"
    ">Гермиона передает вам статью"
    $ paper_puffend += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_68
    return

label paper_kogt_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, получилось что-нибудь?"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "ох, в этот раз все было совсем по-другому"
    $ h_body = "03_hp/13_hermione_main/body_75.png"
    her "сразу видно, что это не пуффендуй"

    #her "ох, все получилось довольно неплохо"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "не прошло и 10 минут с того момента, как я появилась рядом с их корпусом, как ко мне подошел один высокий, темноволосый красавец"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "он был такой голантный"
    $ h_body = "03_hp/13_hermione_main/body_128.png"
    her "я даже не заметила как согласилась на свидание с ним"
    m "оно уже было?"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "только что"
    g9 "круть"
    m "что на нем было?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "мы дошли до озера, смотрели на звезды... он читал мне стихи..."
    $ h_body = "03_hp/13_hermione_main/body_128.png"
    her "потом мы поцеловались..."
    m "что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_03.png"
    her "дальше?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "на что вы намекаете, профессор?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "неужели я похожа на девушку, которая....?!"
    m "ну... учитывая то, чем мы занимаемся здесь..."
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "я делаю это ради своего факультета, это совсем другое!"
    m "ну да, конечно"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "интересно, что будет на следующем свидании?"
    m "дай угадаю..."
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "опять ваши намеки?!"
    m "какие уж намеки"
    ">гермиона передает вам статью для газеты"
    $ paper_kogt += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_69
    return
label paper_kogt_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "все удалось?"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "еще как сэр!"
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "Когтерванцы это вам не пуффендуйцы"
    m "хах, так что там было?"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "в этот раз мы пошли в библиотеку"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "сначала я даже удивилась, ведь это явно не лучшее место для свиданий"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "но как только мы дошли, он сразу взял инициативу и мы..."
    m "..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_78.png"
    her "мы делали это прямо между шкафов с книгами"
    $ h_body = "03_hp/13_hermione_main/body_124.png"
    her "мне кажется, кроме нас, там был кто-то еще"
    $ h_body = "03_hp/13_hermione_main/body_46.png"
    her "интересно нас кто-то слышал?"
    $ h_body = "03_hp/13_hermione_main/body_123.png"
    her "я старалась не шуметь, но..."
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Все таки когтерван, наверное, лучший факультет{w}. После гриффиндора конечно"
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "ах да, я сделала статью"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    ">гермиона передает вам статью для газеты"
    $ paper_kogt += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_06.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_70
    return
label paper_kogt_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, как прошло?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "ужасно!"
    m "..."
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "они... они все подонки, сэр!"
    m "что случилось?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "этот парень из когтервана - мошенник!"
    m "....{w} мошенник?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "поверить не могу, как я могла так ошибаться"
    m "объясни, что черт возьми произошло?"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "я пошла на свидание с парнем из когтервана"
    m "так..."
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "и... ну... эм... так получилось, что я проспорила ему минет"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "мы дошли до леса, чтобы нас никто не заметил и я... эм..."
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "начала выполнять условия спора"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "но нас отвлекла пара, которая пришла на то же место"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "это был тот парень!"
    m "какой?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "тот, который был первый?"
    m "а, так ты разве пошла не с ним?"
    $ h_body = "03_hp/13_hermione_main/body_29.png"
    her "что? конечно же нет! для чистоты эксперимента мне нужно было несколько испытуемых"
    m "хах, испытуемых... ну хорошо"
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "так вот, когда он увидел меня, делающую королевский минет другому, он едко поздоровался и просто ушел дальше!"
    m "...."
    m "и что?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "как что?!"
    $ h_body = "03_hp/13_hermione_main/body_142.png"
    her "он даже ни капельки не возмутился, что я была с другим"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_141.png"
    her "Я думала, что Когтерванцы такие же как Гриффиндорцы, но ничего подобного..."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "они... подлецы, сэр!"
    m "ну... вы же не договаривались, что..."
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "как он мог использовать меня... для одноразового секса..."
    m "но ведь ты же тоже использовала его..."
    $ h_body = "03_hp/13_hermione_main/body_141.png"
    her "да, но я делала это ради нашей школы... я делала минет тому парню, но в тот момент мне было очень стыдно..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "в отличае от этого подонка!"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "я все написала про их факультет!"
    ">Гермиона передает вам статью для газеты"
    $ paper_kogt += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_71


    return
label paper_slytherin_01:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, как твое исследование?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_20.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "вы еше спрашиваете?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "я же сразу говорила, что они мерзкие, высокомерные слизняки!"
    m "что произошло?"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я как всегда пошла к их корпусу"
    $ h_body = "03_hp/13_hermione_main/body_33.png"
    her "я даже не успела подойти, как меня уже заметила компания слизеринских девочек"
    m "девочек?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "они начали обзываться и кричать, чтобы я эм... покинула это место"
    m "но ты ведь не сдалась?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "конечно нет! за исключением корпусов других факультетов и запретного леса, я могу ходить где хочу!"
    m "и что было потом?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "поняв, что я не уйду, они начали выкрикивать разные... эм... слухи обо мне..."
    m "*хах, могу себе представить, что о ней говорят после наших уроков*"
    
    m "ну ладно, это девушки, а что парни? неужели никто не вступился?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "парни?!"
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "они кричали громче девочек"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "кто-то из них начал постоянно использовать заклинание Вингардиан Левиоссо на мою юбку и кричать, что я... эм... ветренная"
    m "...."
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "почему они все такие.... такие...."
    $ h_body = "03_hp/13_hermione_main/body_27.png"
    her "мерзкие, подлые, узколобые, глупые, ..."
    m "стой"
    m "но ведь зато у тебя теперь достаточно материала"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "..... "
    $ h_body = "03_hp/13_hermione_main/body_15.png"
    her "да"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "но, сразу говорю, мне пришлось очень сильно постараться, чтобы не переходить на мат, сэр"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "хотя мне кажется, такой материал все равно никто не пропустит в печать"
    m "да ладно, это уже мне решать"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_02.png"
    her "да, сэр"
    $ h_body = "03_hp/13_hermione_main/body_13.png"
    $ paper_slytherin += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_72
    return
label paper_slytherin_02:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "ну что, как прошло в этот раз?"
    $ h_body = "03_hp/13_hermione_main/body_117.png"
    her "это было ужасно, сэр!"
    m "опять?"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "конечно! что и требовалось доказать!"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "в этот раз я не стала никуда идти, ввиду бесперспективности этой затеи"
    $ h_body = "03_hp/13_hermione_main/body_87.png"
    her "я кое как выцепила одного на вид не такого уж плохого слизеринца и намекнула, что у меня есть свободный вечер"
    m "и что было дальше?"
    $ h_body = "03_hp/13_hermione_main/body_19.png"
    her "Он сразу пригласил меня на свидание..."
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "на котором сразу же вцепился в мою грудь!"
    g9 "*шарит*"
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я попыталась ему объяснить, что его поведение недопустимо, по крайней мере на первом свидании..."
    $ h_body = "03_hp/13_hermione_main/body_34.png"
    her "но в ответ он предложил сделать ему минет!"
    g9 "*сразу видна школа Снейпа*"
    $ h_body = "03_hp/13_hermione_main/body_141.png"
    her "я ни на секунду не сомневалась, что все слизеринцы такие!"
    m "ну, по крайней мере он не обзывал тебя шлюхой или еще как-то"
    $ h_body = "03_hp/13_hermione_main/body_05.png"
    her "да, но это ничто по сравнению с тем, что он сделал потом"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_132.png"
    her "в благодарность за королевский минет, вместо того чтобы предупредить меня, он просто напросто залил все мое лицо и одежду своей спермой"
    m "..."
    m "так ты все таки согласилась?"
    $ h_body = "03_hp/13_hermione_main/body_118.png"
    her "эм... ну..."
    $ h_body = "03_hp/13_hermione_main/body_12.png"
    her "я подумала... мне ведь нужно как то набирать материал..."
    g9 "ты выбрала лучший способ из всех"
    ">Гермиона передает вам статью для газеты"
    $ paper_slytherin += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_01.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_73
    return  
label paper_slytherin_03:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_91.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    $ paper_level += 1
    $ paper = 3
    $ paper_event = 1
    m "...."
    m "что случилось? почему ты голая?"
    $ h_body = "03_hp/13_hermione_main/body_97.png"
    her "сэр!"
    m "что?"
    $ h_body = "03_hp/13_hermione_main/body_98.png"
    her "мне нужна ваша помощь!"
    $ h_body = "03_hp/13_hermione_main/body_99.png"
    m "что произошло?"
    $ h_body = "03_hp/13_hermione_main/body_103.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_98.png"
    her "я пострадала при выполнении вашего задания!"
    m "..."
    m "как?"
    $ h_body = "03_hp/13_hermione_main/body_103.png"
    her "ну..."
    $ h_body = "03_hp/13_hermione_main/body_105.png"
    her "я познакомилась с одним слизеринским парнем и..."
    m "и... что?"
    $ h_body = "03_hp/13_hermione_main/body_103.png"
    her "и его друзьями"
    m "хах, неплохо"
    $ h_body = "03_hp/13_hermione_main/body_196.png"
    her "они все время вели себя по хамски, но я уже привыкла к тому, что слизерин не отличается манерами"
    $ h_body = "03_hp/13_hermione_main/body_191.png"
    her "но в этот раз они перешли черту!"
    m "так что все таки было?"
    $ h_body = "03_hp/13_hermione_main/body_99.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_103.png"
    her "они провели меня в свой кампус в подземелье, где мы и продолжили общение"
    m "общение? хах"
    $ h_body = "03_hp/13_hermione_main/body_112.png"
    her "их было так много... мне кажется туда сбежался весь их факультет"
    g9 "*похоже наши уроки не прошли даром*"
    $ h_body = "03_hp/13_hermione_main/body_97.png"
    her "но это это не главное... я отчетливо слышала щелчки фотоаппарата"
    $ h_body = "03_hp/13_hermione_main/body_114.png"
    her "а после того как все закончилось они взяли и выкинули меня из своего кампуса без одежды!"
    m "хах"
    $ h_body = "03_hp/13_hermione_main/body_91.png"
    her "у них есть фотографии, сэр!"
    m "..."
    $ h_body = "03_hp/13_hermione_main/body_99.png"
    her "что теперь делать..."
    $ h_body = "03_hp/13_hermione_main/body_89.png"
    her "если они разойдутся по всей школе.... я..."
    $ h_body = "03_hp/13_hermione_main/body_98.png"
    her "помогите мне, профессор!"
    $ h_body = "03_hp/13_hermione_main/body_99.png"
    m "*ого*"
    m "ладно, не бойся, мы просто укажем в нашем выпуске, что слизеринцы злоупотребляют заклинанием адобус-фотошопус, изменяющим облик на фотографии"
    $ h_body = "03_hp/13_hermione_main/body_89.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_94.png"
    her "эм..."
    $ h_body = "03_hp/13_hermione_main/body_101.png"
    her "никогда не слышала о таком заклинании"
    m "никто не слышал и никто не знает как его использовать"
    g9 "кроме слизеринцев"
    $ h_body = "03_hp/13_hermione_main/body_89.png"
    her "ах... точно"
    $ h_body = "03_hp/13_hermione_main/body_109.png"
    her "спасибо, сэр!"
    $ h_body = "03_hp/13_hermione_main/body_108.png"
    her "правда я не успела подготовить статью для вас... я сразу побежала сюда..."
    g9 "не беспокойся, у меня достаточно материала"
    $ h_body = "03_hp/13_hermione_main/body_109.png"
    her "да, сэр"
    $ paper_slytherin += 1
    $ gryffindor += 10 #75
    m "10 очков \"Гриффиндору\"!"
    $ h_body = "03_hp/13_hermione_main/body_108.png"
    her "Спасибо, сэр."
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


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_74
    return


label stengazeta:
    "{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}"
    "{size=-4}Дорогой профессор Дамблдор.\n\nМы хотим сообщить Вам, что Сообщество Магов в целом (в лице Министерства Магии) "
    "и попечительский совет Хогвартса в частности хотели бы, чтобы ваша Школа организовала свой печатный орган.\n\n"
    "В связи с Вашим вызывающим уважение мастерством документооборота мы считаем, что Вас не затруднит "
    "Организовать в Хогвартсе небольшую редакцию и приступить к изданию стенгазеты.\n\n"
    "Т.к. данное поручение связано с новыми стандартами образования учеников и было "
    "инициировано во имя высших ценностей, мы будем следить за популярностью данного издания в Школе "
    "и выплачивать соответствующую компенсацию за ваши усилия и для поддержания журналистской деятельности.\n\n{/size}"
    "{size=-4}Вы можете распоряжаться данными фондами по своему усмотрению.\n\nТакже мы понимаем, что освоение такого "
    "необычного для традиционной Школы Волшебников рода деятельности требует немалых усилий, "
    "выбор сотрудников редакции из числа учеников и преподавателей остается на ваше усмотрение.\n\n{/size}"
    "{size=-3}С уважением,\nМинистерство Магии.{/size}"

    $ paper_level = 2

    m "Во имя Великого Песчаного Кактуса!.."
    m "Я должен выжать из этой возможности все что можно. Фонды, значит..."
    m "Нужно обязательно расспросить дружище Северуса об этом."
    m "Но делиться галлеонами - это не по мне."
    m "Думаю, однако, что привлечь Гермиону к написанию статей будет нелишне."
    m "Но сначала придется разобраться, что к чему. Да, нужно поговорить со Снейпом !"

    call screen main_menu_01

label playwizard:

    $ letter_text = "В редацию школьной газеты Хогвартса. Здравствуйте, ваш новый автор под псевдонимом \"Горячая Ведьмочка\" в одночасье стала звездой всей магической порноиндустрии. Мы  бы хотели видеть ее на обложке нашего журнала ПлэйВизард. Мы готовы щедро вас отблагодарить. С наилучшими пожеланиями, Геф Гефнер."
    show screen letter
    pause 
    m "хах"
    m "отличная возможность сделать ее еще более популярной, да еще и заработать"
    hide screen letter 
    
    $ playwizard = 2
    return
label herm_jurnal:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    pause 1.0
    $ h_body = "03_hp/13_hermione_main/body_145.png"
    her "профессор!"
    $ h_body = "03_hp/13_hermione_main/body_146.png"
    her "все... на меня весь день показывают пальцем..."
    $ h_body = "03_hp/13_hermione_main/body_145.png"
    m "..."
    m "почему?"
    $ h_body = "03_hp/13_hermione_main/body_148.png"
    her "почему?!"
    $ h_body = "03_hp/13_hermione_main/body_147.png"
    her "может быть из-за обложки в порножурнале?!!"
    $ h_body = "03_hp/13_hermione_main/body_145.png"
    her "зачем... зачем вы это сделали? как мне теперь жить?"
    m "...."
    m "ну... ты ведь хотела стать известной"
    $ h_body = "03_hp/13_hermione_main/body_143.png"
    her "да, но не так!"
    g9 "ну...{w} и издание действительно очень крупное и известное"
    $ h_body = "03_hp/13_hermione_main/body_145.png"
    her "теперь вся школа и... вообще весь мир видел меня голой!"
    m "верно...{w} теперь ты настоящая звезда"
    $ h_body = "03_hp/13_hermione_main/body_144.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_142.png"
    her "звезда?"
    m "конечно. как ты думаешь, сколько парней будут засыпать, глядя на эту фотографию?"
    $ h_body = "03_hp/13_hermione_main/body_144.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_154.png"
    her "думаете, они будут..."
    $ h_body = "03_hp/13_hermione_main/body_152.png"
    m "ох, я даже не сомневаюсь"
    $ h_body = "03_hp/13_hermione_main/body_153.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_155.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_154.png"
    her "но девочки все равно будут считать меня шлюхой"
    $ h_body = "03_hp/13_hermione_main/body_152.png"
    m "конечно, потому что будут завидовать"
    $ h_body = "03_hp/13_hermione_main/body_155.png"
    her "..."
    $ h_body = "03_hp/13_hermione_main/body_158.png"
    her "спасибо, сэр"
    m "да незачто"
    $ h_body = "03_hp/13_hermione_main/body_152.png"
    her "...."
    $ h_body = "03_hp/13_hermione_main/body_154.png"
    her "ладно, я пойду..."
    $ h_body = "03_hp/13_hermione_main/body_153.png"
    her "хочу увидеть лицо этой суки Пэтти, ссгорающей от зависти"
    $ h_body = "03_hp/13_hermione_main/body_156.png"
    her "хи-хик"
    $ playwizard = 8
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
    with Dissolve(0.3)


    
    
    $ hermione_sleeping = True
    
    call music_block from _call_music_block_75
    return

label thehatt:
    menu:
        "Я здесь после тестовой версии":
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
            if daytime:
                        
                jump night_main_menu
            else:
                        
                jump day_main_menu

        "нет":
            if daytime:
                        
                jump night_main_menu
            else:
                
                jump day_main_menu



    



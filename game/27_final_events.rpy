label want_to_rule:
    
    $ event_chairman_happened = True #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
   
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    her "Профессор Дамблдор?"
    m "Мисс Грейнджер, чем могу быть полезен?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Сэр, вы еще не решили, кто будет курировать \"КООБ\" в этом году?"
    m "\"КООБ\"?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "\"Комитет по Организации Осеннего Бала\", сэр..."
    m "Эм... Конечно..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Пожалуйста извините, но я скажу прямо, сэр..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я думаю, что я должна курировать его."
    her "Я курировала его в прошлом году и это был самый лучший осенний бал за последние годы."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Вы так сами сказали, сэр. Вы помните?"
    m "Да, конечно..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "То есть вы согласны?"
    her "Это значит, что я буду курировать бал и в этом году?"
    menu:
        m "..."
        "\"Вы должны курировать бал, мисс Грейнджер.\"":
            jump one_thing
        "\"Нет. Профессор Снейп должен быть главным!\"":
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Профессор Снейп, сэр?"
            her "Но традиционно за организацию и проведение бала были ответственны ученики..."
            her "Учителя всего лишь почетные гости..."
            m "Ну конечно... Я просто пошутил."
            m "Вы должны быть главной, мисс Грейнджер..."
            label one_thing:
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
            her "Благодарю вас, сэр."
            m "Хотя, есть одно условие..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Условие, сэр"
            
            $ d_flag_04 = False
            label no_sleeping_with_professor:
                pass
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            menu:  
                m "..."
                "\"Сначала покажи мне сиськи.\"":
                    $ mad += 9
                    $ d_flag_01 = True
                    pass
                "\"Сначала покажи мне свою киску.\"":
                    $ mad += 9
                    $ d_flag_02 = True
                    pass
                "\"Сначала разденься.\"":
                    $ mad += 17
                    $ d_flag_03 = True
                    pass
                "\"Тебе придется переспать со мной.\"" if not d_flag_04:
                    $ mad += 17
                    $ d_flag_04 = True
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Мне придется... переспать...?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "..................."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Я не дура, сэр... Даже наоборот."
                    her "И я понимаю, что сущность услуг, что я продаю вам в последнее время..."
                    her "...Могла навести вас на мысль, что в конце концов я смогу..."
                    her "... позволить вам обращаться с собой, так, как вам захочется, сэр..."
                    m "Что-о-о-о...? Да я бы никогда-"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Пожалуйста, дайте мне закончить, сэр."
                    m "Ладно..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я знаю, что вы сами достаточно мудрый человек, сэр."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Так что пожалуйста... поймите..."
                    her "Я может и могу принести в жертву свою честь и даже свое достоинство во благо своего факультета..."
                    her "Но переспать с директором?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Пожалуй здесь я нарисую черту, которую нельзя переступать, сэр."
                    m "Понятно. Просто забудь о том, что я только что сказал."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_141.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "{size=-5}(Хотелось бы...){/size}"
                    jump no_sleeping_with_professor
    
                    
                    
                    
       
                "\"Неважно. Должность твоя.\"":
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    show screen blkfade 
                    with d5
                    pause.7
                    pass
    

            if d_flag_01 or d_flag_02 or d_flag_03:
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Что?!"
                m "Что?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Профессор!"
                m "Что?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Вы пользуетесь своим положением, сэр. Опять!"
                m "Ты серьезно? После всех тех услуг, что ты продала мне?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Это было во благо моего факультета, сэр."
                m "Ну, а это во благо \"Осеннего Выпускного\"."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "\"Осеннего Бала\", сэр..."
                m "Ох, да брось..."
                m "Доверить это кому-либо еще будет преступлением, и ты знаешь это."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her ".........."
                m "Тебе совсем плевать на своих одноклассников?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Что?"
                m "Может ты перестанешь быть эгоисткой, хоть ненадолго?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "... эгоисткой?"
                m "Твои одноклассники заслуживают самого лучшего осеннего бала в мире!"
                m "И только {size=+5}ТЫ{/size} можешь дать такой им!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "...ну да, это так."
                m "Люди надеются на тебя, девочка!"
                if d_flag_01:
                    m "Так что я предлагаю тебе перестать быть эгоисткой и показать мне сиськи!"
                elif d_flag_02:
                    m "Так что я предлагаю тебе перестать быть эгоисткой и показать мне свою киску!"
                elif d_flag_03:
                    m "Так что я предлагаю тебе перестать быть эгоисткой и раздеться!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Вы совершенно правы, профессор!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Я должна сделать это. Все расчитывают на меня."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Подождите секунду, пожалуйста..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d5   
                m "............"
                if d_flag_01: # SHOW ME TITS
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    hide screen blkfade
                    with d3
                    hide screen bld1
                    with d3
                    hide screen hermione_main
                    with d5
                    $ menu_x = 0.5 #Default menu position restored.
                    show screen ctc
                    pause.3
                    show screen hermione_04
                    with fade
                    pause
                    show screen bld1
                    with d3
                    
                    $ badges = False
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    show screen ctc
                    pause
                    hide screen ctc
                    m "Очень хорошо, мисс Грейнджер..."
                    m "Твои большие сиськи всегда притягивали мой взгляд..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...................."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d5   
                    show screen blkfade 
                    with d5
                    pause.7
                elif d_flag_02: # SHOW ME PUSSY
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    $ only_upper = True
                    
                    hide screen blkfade
                    with d3
                    hide screen bld1
                    with d3
                    hide screen hermione_main
                    with d5
                    $ menu_x = 0.5 #Default menu position restored.
                    show screen ctc
                    pause
                    show screen hermione_03
                    with fade
                    pause
                    show screen bld1
                    with d3
            
                    $ uni_sperm = True
                    $ u_sperm = "03_hp/13_hermione_main/panties.png" #Panties
            
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_60.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    show screen ctc
                    pause
                    hide screen ctc
                    
                    her ".............................."
                    with hpunch
                    g4 "Что вы делаете?!"
                    g4 "Я ваш директор! Вы совсем стыд потеряли?!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Что?! Но-"
                    g9 "Хе-хе... Расслабься, девочка. Я просто шучу."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_62.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Профессор, это было жестоко."
                    g9 "Хе-хе..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_61.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "....................................."
                    m "Мне нравится твоя маленькая гладенькая киска..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_61.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her ".....спасибо, сэр."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    show screen blkfade 
                    with d5
                    pause.7
                    $ uni_sperm = False
                
                elif d_flag_03: # STRIP NAKED
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    # (Hermione locks the door).
                    hide screen bld1
                    with d3
                    pause.3
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen ctc
                    pause
                    m "?!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ h_ypos=0
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her "Просто на всякий случай..."
                    show screen ctc
                    pause
                    hide screen ctc
                    show screen blkfade
                    with d5
                    m ".........................."
                    ">Гермиона медленно раздевается..."
                    ">Жилетка, рубашка, юбка и наконец... трусики."
                    
                    $ only_upper = True
                    
                    
                    hide screen hermione_main
                    
                    $ hermione_chibi_xpos = 310 # Default 360
                    #$ hermione_chibi_ypos = 210
                    $  h_c_u_pic = "03_hp/08_animation_02/01.png" #Hermione naked. 
                    show screen h_c_u 
                    
                    hide screen blkfade
                    with d7
                    show screen ctc
                    pause
                    hide screen ctc
                    
                    $ badges = False # Turns off badges layer.
                    
                    #add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
                    g9 "Щик-а-а-арно!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_105.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    show screen ctc
                    pause
                    hide screen ctc
                    her "*Всхлип!*"
                    m "Хах?"
                    
                    $ h_tears = True
                    $  u_tears_pic = "03_hp/13_hermione_main/tears_01.png"
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_107.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ох, пожалуйста, не обращайте на меня внимания, сэр."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_105.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Просто наслаждайтесь... {w}ви... {w}видом..."
                    m "Ты... плачешь?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_97.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Всхлип!* Нет, совсем нет, сэр... *всхлип!*..."
                    her "Просто я стою перед директором совсем голая... *ВСХЛИП!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_114.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Это слезы стыда, сэр."
                    her "Я ничего не могу с этим поделать! *Всхлип!*"
                    m "Ты уверена, что все в порядке?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $  u_tears_pic = "03_hp/13_hermione_main/tears_04.png"
                    $ h_body = "03_hp/13_hermione_main/body_101.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Да, да, сэр, пожалуйста.... *Всхлип!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_104.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Пожалуйста продолжайте смотреть на мое обнаженное тело... *Всхлип!*"
                    g4 "(Что за...?)"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Сэр, я умоляю вас!"
                    m "Немного смахивает на приказ-"       
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_192.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Мне нужно это!"
                    her "...Мне нужно показывать вам свое обнаженное тело, пока вам это не понравится!"
                    m ".............?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_193.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Мне нужно почувствоватьь это смущение и унижение! *ВСХЛИП!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_194.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Судьба \"Осеннего бала\" зависит от этого..."
                    her "Так что, прошу, сэр..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_195.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Продолжайте смотреть на мою грудь и мою киску..."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_196.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Да! Заставьте меня гореть от стыда, сэр... *Всхлип!*"
                    m "Эм.. хорошо... ладно..."
                    m "Слушай, я думаю, что этого хватит..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Вы уверены, сэр?"
                    her "Вы уверены, что вы унизили меня достаточно, сэр?"
                    m "...................."
                    m "(Ее это возбуждает? Это сарказм? Не могу понять...)"
                    her ".........................."
                    show screen ctc
                    pause
                    hide screen ctc
                    m "Просто оденьтесь, мисс Грейнджер. Я чувствую себя неловко."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_103.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Как пожелаете, сэр..."
                    
                    show screen ctc
                    pause 
                    hide screen ctc
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    show screen ctc
                    pause 
                    hide screen ctc
                    
                    $  u_tears_pic = "03_hp/13_hermione_main/tears_03.png"
                    show screen blkfade 
                    with d5
                    pause.7
                
                    
                    
                    
                    
                    
                             
                        
                    
                    
                    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.             
                    
    $ hermione_chibi_xpos = 360 # Default 360
    show screen hermione_02 #Hermione stands still.
    hide screen blkfade
    with d5
    
    $ badges = True
    
    show screen ctc
    pause 
    hide screen ctc
    $ only_upper = False
    $ badges = True # Turns badges layer back ON.
    show screen bld1
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Итак, теперь я официально курирую \"Комитет по Организации Осеннего Бала\"?"
    m "Да, ты теперь главная."
    her "Спасибо, сэр! Вы не пожалеете об этом, обещаю!"
    m "{size=-4}(А почему я должен?){/size}"
    m "{size=-4}(Мне как-то плевать...){/size}"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ну, я, пожалуй, пойду. У меня теперь столько дел!"
    m "Конечно, мисс Грейнджер. Удачи."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3 
    
    hide screen bld1


    hide screen hermione_02


    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    pause.2
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    pause.5
    show screen bld1
    with d3
    m "........................................"
    m "Бал, да?"
    m "Интересно, придется ли мне на нем показаться..?"
    hide screen bld1
    with d3
    $ hermione_takes_classes = True
    $ days_without_an_event = 0

    $ h_tears = False
    
    call music_block from _call_music_block
    
    return
    
#==========================
    
label against_the_rule:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    $ snape_against_chairman_hap = True # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ days_without_an_event = 0
    
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
    with Dissolve(.3)
    
    
                
    sna "Ты, мать твою, псих?!"
    m "Знаешь, я порой думаю, что да..."
    
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ tt_xpos=120 #Defines position of the Snape's full length sprite. Right - 300                      #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Ты назначил эту девку главой \"Комитета по Организации Осеннего Бала\"?!!"
    m "Похоже это плохо?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Плохо?{w} {size=+5}ПЛОХО?!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_15.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "{size=+5}Это катастрофа!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Прошлогодний бал бы абсолютно ужасен!"
    m "Да? Я слышал другое..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Да ты что? И кто тебе это сказал?"
    m "Определенно не самый надежный источник..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Проклятье... Пропади все пропадом..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_07.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "У меня были большие планы на бал..."
    m "Правда? Например?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Ох, теперь это неважно..."
    #sna "The girl is a complete control freak..."
    sna "Теперь эта девка будет использовать старост или призраков для того чтобы следить за мной..."
    m "Кстати..."
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Huh?"
    m "Я должен буду показаться там?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Показаться?"
    sna "Ты должен быть ведущим всей этой хрени!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Но не волнуйся! Я что-нибудь придумаю!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Хм... Возможно мне придется быть ведущим..."
    m "............"
#    sna ".................."
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Yes! I will do it!"
#    sna "And I shall be on my best behavior!"
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Yes, that'll show her!"
#    m "................"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Что ж, Осенний бал на носу и Гермиона Грейнджер главная..."
    sna "Теперь этого не исправить..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Прости за то, что сорвался..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Эта девка меня доведет..."
    m "Не извиняйся..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "А знаешь что...?"
    sna "Я не хочу работать сегодня..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "У тебя еще осталось Дамблдорское вино?"
    m "Вроде бы..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Отлично! Налей мне немного..."
    m "Серьезно? Ты собираешься вот так вот просто прогулять свои же уроки?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Ага, свежие новости - я ненавижу свою работу."
    sna "И так как ты мой босс..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Я даже не знаю, зачем я вообще заморачиваюсь учить так называемых учеников..."
    m "Чтобы поддержать легенду?"
    m "По той же самой причине, по какой я никогда не покидаю эту комнату...?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Верно..."
    sna "Но ты знаешь, что еще может навредить нашему маленькому предприятию?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_07.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Я, со сорванной во время уроков крышой, и придушивший парочку \"Гриффиндорских\" засранцев голыми руками..."
    m "Хм... Ты прав, пожалуй..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Серьезно, чувак... Мне нужно выпить..."

    show screen blkfade
    with d3
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk
    
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    
    hide screen blkfade
    with d3
    $ fire_in_fireplace = True
    
    show screen bld1
    with d3
    "Профессор Снейп проводит день в твоих палатах, заливая горе вином."
    
    if not sfmax:# Turns TRUE when friendship with Snape been maxed out.
        ">Ваши с ним отношения улучшились."
        $ snape_friendship +=1
   
    show screen blkfade
    with d3
    hide screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    hide screen fireplace_fire
    show screen genie
    show screen chair
    show screen desk
    hide screen desk
    
    hide screen bld1

    stop bg_sounds #Stops playing the fire SFX.
   
    jump night_start
         
#    hide screen snape_main
#    hide screen bld1
#    with d3
    
#    $ walk_xpos=360 #Animation of walking chibi. (From desk) 360
#    $ walk_xpos2=610 #Coordinates of it's movement. (To the door) 610
    
#    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
#    show screen snape_walk_01_f 
#    pause 3
#    hide screen snape_walk_01_f 
#    show screen snape_01_f #Snape stands still. (Mirrored).
#    pause.2
#    who2 "................."
#    who2 "One more thing..."
#    show screen bld1
#    show screen snape_main
#    with Dissolve(.3)
#    who2 "You must dismiss any lies you hear about me and those slytherin girls..."
#    m "You got it!"
#    hide screen bld1
#    hide screen snape_main
#    hide screen snape_01_f #Snape stands still. (Mirrored).
#    with Dissolve(.3)
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

#    return
    
#============================

label crying_about_dress:
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    her "Мои родители прислали мне не то платье!"
    m "Ты серьезно!?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Они прислали мне платье, которое я одела на бал в прошлом году..."
    m "Невнимательные сволочи!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_67.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Вам весело от этого, сэр?"
    m "Разве я виноват в этом?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я стану посмешищем всего Хогвартса! *Всхлип!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Моей репутации придет конец! *Всхлип!*"
    m "Серьезно? После всех тех услуг, что ты продала мне, тебя еще волнуют такие вещи?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Носить одно и то же платье на \"Осенний Бал\" два года подряд в разы унизительней всех тех услуг, что я вам продала, сэр."
    with hpunch
    g4 "Да ты шутишь..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ох, вам не понять..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_148.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Вы точно такой же, как мой отец!"
    m "Прошу прощения?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "В смысле... эм..."
    her "Простите, сэр..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я не знаю, почему я вообще рассказываю вам все это..."
    m "................"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "......................*всхлип!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я думаю, мне лучше уйти...*всхлип*"
    m "Чтож, не смею вас более задерживать, мисс Грейнджер...."
    # Walks to the door.
    
 
    

    
    
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
    

    $ hermione_chibi_xpos = 610 # Stands near the door.
    show screen hermione_01_f #Hermione stands still.
    pause.3
    $ h_body = "03_hp/13_hermione_main/body_145.png"                                                                                                                                                         # HERMIONE HEAD
    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390                                # HERMIONE HEAD
    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.       # HERMIONE HEAD
    show screen bld1
    with d3
    show screen h_head2                                                                                                                                                                                                                    # HERMIONE HEAD         
    her "(Моя жизнь разрушена...)"
    hide screen h_head2       
    hide screen hermione_01_f #Hermione stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
   
    
    pause.5
    m "Хм... Я не помню, чтобы видел ее в таком отчаянии..."
    m "И это несмотря на все, что было..."
    m "Судя по всему, для нее продавать себя за очки значительно меньшая проблема, чем не иметь приличного бального платья..."
    m ".............."
    m "Школьницы..."
       
    hide screen bld1
    with d3
    
    $ hermione_takes_classes = True
    
    call music_block from _call_music_block_1
    
    return 
    
#===========================
label sorry_about_hesterics:
    $ sorry_for_hesterics = True # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    $ days_without_an_event = 0
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    
    m "Мисс Грейнджер?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Извините, что отвлекаю вас, сэр..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я пришла извиниться за мое..."
    her "...мое истеричное поведение вчера."
    m "Конечно, не переживай на этот счет."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Спасибо, сэр."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Однако, я не могу не чувствовать себя ужасно из-за той сцены..."
    m "Так значит проблема решилась?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Не совсем..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Вернее, совсем нет..."
    m "Хм..?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Но это не так важно..."
    her "Просто я излишне драматизирую..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    her "Я не смогу попасть на бал в этом году... ну и что?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я потратила бессчетные часы, организовывая его..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE

    $ h_tears = True
    $  u_tears_pic = "03_hp/13_hermione_main/tears_01.png"
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я так старалась... и..."
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_tears = False
    $ h_body = "03_hp/13_hermione_main/body_139.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "И теперь я даже не смогу по... пo... *Всхлип!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Пo... *ВСХЛИП!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Простите, сэр!"
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    
    $ walk_xpos=370 #Animation of walking chibi. (From) 300
    $ walk_xpos2=750 #Coordinates of it's movement. (To) 610
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen. 0.02
    hide screen no_groping_02
    hide screen bld1
    show screen genie
    show screen hermione_run
    #with fade
    pause 1.3 # .9
    hide screen hermione_run
    with Dissolve(.1)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    pause.5
    
    show screen bld1
    with d3
    
    m "......................................."
    m "Хм..."
    $ hermione_takes_classes = True
    hide screen bld1
    with d3
    
    call music_block from _call_music_block_2
    
    return
    
    
#=========================
label giving_thre_dress:
    $ gave_the_dress = True #Turns True when Hermione has the dress.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    stop music fadeout 1.0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/01.png" # DRESS.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дарите бальное платье Гермионе..."
    hide screen gift
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Хм...? Что это?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    with hpunch
    her "{size=+7}ПЛАТЬЕ?!{/size}"
    m "Я думал, что тебе-"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    her "ПРОФЕССОР!"
    g4 "Что? Что такое? Только не говори мне, что это не тот цвет или что-то еще!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Оно идеально, сэр...*всхлип!*"
    her "Оно идеально... *всхлип!* ...мне нравится."
    m "Тебе определенно оно не нравится..."
    her "Простите, сэр... *Всхлип!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я... Я просто..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я так счастлива..."
    her "Спасибо, сэр. Огромное вам спасибо."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я не могу поверить, что вы могли сделать для меня нечто подобное..."
    m "Ну, я сделал. А теперь хватит реветь."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_147.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Я не могу, сэр. Я так счастлива и так благодарна..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Хотите я отсосу вам, сэр?"
    m "Что?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Потому что я отсосу!"
    her "И все проглочу!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "И вам не придется платить мне не единого очка!"
    m "Кхм... Может как-нибудь в следующий раз..."
    m "Это не тот тип рыданий, что может меня возбудить..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Извините, сэр. Я так разревелась..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Но это так неожиданно..."
    her "Вы сделали меня такой счастливой, сэр...*всхлип!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Спасибо, сэр! *ВСХЛИП!* Спасибо! *Всхлип!*"
    m "Ну... эмм... ну будет тебе, будет..."
    m "Лучше прекрати плакать, пока не промочила новое платье насквозь в своих слезах..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_147.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Мое новое платье! *ВСХЛИП!*"
    m "Хорошо, знаешь что? Просто выметайся из моего кабинета."
    m "Забирай свое платье и уходи."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Конечно... Извините, сэр!"
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3          
    
    
    
    
    
    
    
    
  
   
   
   
   
   

    
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3






    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.8
    show screen bld1
    with d3
    m "......................"
    m "Бабы..."
    hide screen bld1
    with d3

    call music_block from _call_music_block_3
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
    
    
    
###======================================================================
    
    
label good_bye_snape:

    $ days_without_an_event = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To) 360
    show screen snape_walk_01 
    #with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.1)
    

    sna "Джинни..."
    m "Северус?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ tt_xpos=120 #Defines position of the Snape's full length sprite. Right - 300                      #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
#    sna "The \"Autumn Ball\" is tonight..."
#    m "Is it...?"
#    sna "....................."
#    m ".....?"
    sna "Я думаю, что понял, почему твоя магия не работает в полную силу..."
    g4 "Серьезно?!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Да..."
    sna "Вообще то, это было достаточно очевидно... Странно, что я раньше до этого не додумался."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Видишь ли, дело в том, что на каждое здание в \"Хогвартсе\" наложены всевозможные виды защитных заклинаний..."
    m "Защитные заклинания?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Да..."
    sna "Очень мощная, старая и противная магия..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Даже сама земля сильно зачарована на километры вокруг..."
    m "Хм..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Такое большое количество заклинаний должно мешать твоим силам здесь..."
    m "Стой, тогда почему у тебя нет проблем с магией?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Мой друг, моя магия это \"Хогвартская\" магия..."
    sna "Готов поспорить, что твою силы достаточно \"чужие\", чтобы их можно было считать угрозой."
    m "Интересно..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Я думаю, что если ты уйдешь достаточно далеко от школы..."
    m "Я смогу попасть домой... наконец-то..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Да, и лучшее время, чтобы сделать это - сегодня вечером..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Пока все будут поглощены этим чертовым \"Осенним балом\", ты сможешь прокрасться незамеченным..."
    
    hide screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    
    show screen blkfade
    with d5
    hide screen genie
    hide screen bld1
    hide screen snape_02 #Snape stands still.
    show screen chair_02
    show screen g_c_u
    $ genie_chibi_xpos = 80
    $ genie_chibi_ypos = 205
    $ g_c_u_pic = "03_hp/05_props/hand_00.png"
    play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 # EPIC THEME.
    pause 1
    m "Точно, сегодня будет \"Осенний бал\"..."
    m "Итак, тогда все закончится сегодня вечером..."
    $ s_head_xpos = 330 # x = 330,
    $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    show screen s_head2
    sna_17 "Похоже на то..."
    hide screen s_head2
    hide screen blkfade 
    with d3
    pause.5

    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Если я окажусь прав, то я никогда тебя больше не увижу..."
    hide screen s_head2
    m "Точно..."
    show screen blkfade
    with d3
    $ g_c_u_pic = "03_hp/05_props/hand_01.png"
    hide screen blkfade
    with d3
    pause 2
    show screen bld1
    with d3
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"
    sna2 "Последние несколько месяцев были лучшими месяцами в моей жизни, Джинни..."
    sna2 "Спасибо тебе за это, невероятный путешественник из другого мира..."
    sna "Спасибо тебе, мой друг..."
    hide screen s_head2
    m "Я даже не знаю, что сказать, Северус..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Тогда ничего не говори..."
    sna2 "Просто отправляйся в свое следующее приключение..."
    sna "Наш мир держал тебя слишком долго..."
    hide screen s_head2
    m "Спасибо за то, что составлял мне компанию и был единственным другом здесь, Северус."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_27.png"
    sna "Спасибо за то, что был моим..." #TEARS?
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Я, пожалуй, пойду..."
    #Goes to the door, stops and turns around.
    
    hide screen s_head2
    show screen blkfade
    with d5
    show screen genie
    hide screen bld1
    hide screen chair_02
    hide screen g_c_u

    pause.5
    # SNAPE LEAVES
    
    hide screen ctc
    
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    hide screen blkfade 
    with d3
    pause 3
    
    hide screen snape_walk_01_f 


    show screen snape_01_f #Snape stands still near the door. (Mirrored).
    pause.5
    show screen snape_01#Snape stands still.
    
    
    
    
    
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d5
    
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Хотя, еще кое-что..."
    hide screen s_head2
    m "Да?"
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/24.png"
    sna "Если все пойдет как надо..."
    sna2 "Завтра в этом кресле я увижу настоящего Альбуса Дамблдора?"
    hide screen s_head2
    m "Скорее всего..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    sna "Хм..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    sna2 "Альбус не знает, что я был вкурсе его отсутствия..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Есть способ, чтобы различить вас?"
    hide screen s_head2
    m ".............."
    m "Как насчет секретного пароля?"
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Пароля?"
    hide screen s_head2
    m "Да... просто спроси меня завтра: \"Кто рулит?\"."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "\"Кто рулит?\""
    hide screen s_head2
    g9 "\"Акабур рулит!\""
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    sna "Акуба... эм... Что это значит?"
    hide screen s_head2
    m "Просто фраза, котрую ты сможешь услышать только от настоящего меня..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"
    sna "Ясно..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "Тогда ладно..."
    sna "Счастливого пути..."
    hide screen s_head2
    m "Спасибо. Повеселись на балу..."
    show screen s_head2
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "*Вздох*"
    hide screen s_head2
    pause.3
    hide screen bld1
    with d3
    pause.3
    
    stop music fadeout 1.0

    show screen snape_01_f#Snape stands still.

    pause.5
    hide screen snape_01#Snape stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f#Snape stands still.
    
    pause 1
    show screen ctc
    pause
    hide screen ctc
    
    
    
    m "............................"
    m "Вот и все, да...?"
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    m "Похоже, мое время в этом мире подошло к концу..."
    m "......................."
    if not public_whore_ending: #YOUR PERSONAL WHORE ENDING. WRITING A LETTER.
        m "Это значит, что я скорее всего больше никогда не увижу девочку вновь..."
        m "..........."
        m "Когда я встретил ее впервые, она была такой надоедливой..."
        m "Если честно, все тренировки, через которые она прошла не очень-то изменили ее в этом плане.."
        m "Но у нас было несколько особенных моментов вместе..."
        m ".............."
        m "......................"
        m "Я чувствую, что неправильно поступаю, уходя не попрощавшись..."
        m "И все же, я не хочу терять свой шанс прокрасться незамеченным..."
        m "Я не люблю долгих прощаний..."
        m "Хм..."
        m "Думаю, я мог бы оставить ей записку..."
        
        m "Посмотрим..."
        show screen bld1
        with d3
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "\"Дорогая...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "Хм... Как мне обратиться к ней?"
        menu:
            m "Дорогая..."
            "\"Мисс Грейнджер\"":
                 $ word_01 = "мисс грейнджер" 
            "\"Грязная шлюха\"":
                $ word_01 = "грязная шлюха"
            "\"Потаскуха\"":
                $ word_01 = "потаскуха"
            "\"Спермоглотка\"":
                $ word_01 = "спермоглотка"
            "\"Человеческая самка\"":
                $ word_01 = "человеческая самка"
            "\"Подруга\"":
                $ word_01 = "подруга"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Да, \"Дорогая [word_01]\" подходит идеально..."
        ">чирк-чирк-чирк..."
        ">чирк-чирк-чирк..."
        m "\"...пора мне вернуться назад...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "Что я должен написать теперь?"
        menu:
            m "...пора вернуться назад..."
            "\"домой\"":
                $ word_02 = "домой"
            "\"на родной корабль-матку\"":
                $ word_02 = "на родной корабль-матку"
            "\"в Измерение \"X\"":
                $ word_02 = "в Измерение \"X\""
            "\"в мой мир\"":
                $ word_02 = "в мой мир"
            "\"на мою родную планету - Криптон\"":
                $ word_02 = "на мою родную планету - Криптон"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Да, \"Пора вернуться назад [word_02]\" пойдет..."
        ">чирк-чирк-чирк..."
        ">чирк-чирк-чирк..."
        m "\"...прощай, моя маленькая...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "Что я должен написать?"
        menu:
            m "...прощай, моя маленькая... "
            "\"Членолюбка\"":
                $ word_03 = "членолюбка"
            "\"Спермобаза\"":
                $ word_03 = "спермобаза"
            "\"Девочка\"":
                $ word_03 = "девочка"
            "\"Ведьма\"":
                $ word_03 = "ведьма"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Да, \"прощай, моя маленькая [word_03]\" звучит в самый раз..."
        ">чирк-чирк-чирк..."
        ">чирк-чирк-чирк..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "И теперь подпись..."
        label stupid_kent:
            pass
        menu:
            m "..."
            "\"Джинни\"":
                $ word_04 = "Джинни"
            "\"Кларк Кент\"":
                $ word_04 = "Кларк Кент"
                hide screen genie
                show screen paperwork
                with Dissolve(0.3)
                m "Да, \"искренне твой, [word_04]\"..."
                show screen genie
                hide screen paperwork
                with Dissolve(0.3)
                m "..........."
                m "Не, это какая-то чушь..."
                jump stupid_kent
            "\"Лорд Волан-де-Морт\"":
                $ word_04 = "Лорд Волан-де-Морт"
            "\"Странник\"":
                $ word_04 = "Странник"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Да, \"[word_04]\"..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "........................"
        m "Ну, пойдет..."
    hide screen bld1
    with d3
    m "Что ж, теперь мне пора..."
    
    show screen blkfade
    with d5

    $ g_c_u_pic = "03_hp/05_props/walk_01.png"
    $ genie_chibi_xpos = 270
    $genie_chibi_ypos = 260
    hide screen genie
    show screen chair_02
    hide screen desk
    show screen desk
    show screen g_c_u
    pause.5
    hide screen blkfade
    with d5
    
    
    
    m "........."
        
    

    

    $ walk_xpos=270 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    hide screen g_c_u
    show screen genie_walk
    hide screen blkfade 
    pause 3
    
    hide screen genie_walk


    $ genie_chibi_xpos = 610
    show screen g_c_u
    pause 1
    m "...................."
    m "Аграба... я иду..."
    
    show screen ctc
    pause
    hide screen ctc
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen g_c_u
    pause.3
    show screen ctc
    pause
    hide screen ctc
    ">.......................{w}............................{w}.....................{w}......................"
    pause.7
    show screen blkfade
    with d7
    pause 1
    
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}За пределами Хогвартса{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    $ end_u_1_pic =  "03_hp/17_ending/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    hide screen blkfade 
    with d7
    
    show screen ctc
    pause
    hide screen ctc
    

    
    m "Северус был прав..."
    pause.5
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "03_hp/17_ending/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    
    
    m "Чем дальше я от школьных земель..."
    m "Тем могущественнее я становлюсь..."
    
    $ end_u_4_pic =  "03_hp/17_ending/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    m "Я думаю, что я отошел достаточно далеко..."
    m "Пришла пора отменить заклинание и вернуться домой..."
    m ".........."
    m "...................."
    m "Аграба, вот и я..."
    if not persistent.game_complete: # FIRST PLAYTHOURGH. 
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        with d9
        pause .5
        
        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.
        
        centered "{size=+7}{color=#cbcbcb}Поздравляем с завершением игры!{/color}{/size}\n\n\
                  {size=+5}{color=#cbcbcb}Это концовка \"00\" из \"02\".{/color}{/size}"
        
        centered "{size=+7}{color=#cbcbcb}Спасибо за ваше то, что играли!{/color}{/size}\n\n\
                  {size=+5}{color=#cbcbcb}AKABUR 2014{/color}{/size}"
        
        
        #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
        #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
        #scene image "08_ending/e05.png" with Dissolve(2)
        # show akaani with d5

        
        centered "{cps=20}{size=+5}{color=#ea91b0}-Hermione Trainer-{/color}{/size}\n\n\
        {size=+5}{color=#e5e297}-Продюсер-{/color}{/size}\n{color=#cbcbcb}AKABUR{/color}\n\n\
        {size=+5}{color=#e5e297}-Программист-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n\
        {size=+5}{color=#e5e297}-Сценарист-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n\
        {size=+5}{color=#e5e297}-Художник-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n\
        {size=+5}{color=#e5e297}-Второй художник-{/color}{/size}\n     {color=#cbcbcb}DAHR{/color}\n\n\
        {size=+5}{color=#e5e297}-Звуковые эффекты-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n"
    #    {size=+5}{color=#e5e297}-МУЗЫКА-{/color}{/size}\n\n

    #    {color=#e5e297}(From \"NEWGROUNDS\")\n
    #    {color=#e5e297}\"Eastern Journey\" {/color}{color=#cbcbcb}by Pike270.{/color}\n
    #    {color=#e5e297}\"Grape Soda Is Fucking Raw\"{/color} {color=#cbcbcb}by jrayteam6.{/color}\n
    #    {color=#e5e297}\"The Eastern Wind\"{/color} {color=#cbcbcb}by roensb.{/color}\n
    #    {color=#e5e297}\"Silly Cat\" {/color}{color=#cbcbcb}by Maverlyn.{/color}\n
    #    {color=#e5e297}\"Kabul Flight\" {/color}{color=#cbcbcb}by Jumpstart.{/color}\n
    #    {color=#e5e297}\"Sleep Walking\" {/color}{color=#cbcbcb}by hektikmusic.{/color}{/cps}"
        nvl clear
    #    hide akaani
        
        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Стоять, я еще здесь!"
        centered "{size=+7}{color=#cbcbcb}ЧТО?!{/color}{/size}"
        g4 "Я сказал, что я все еще здесь, вашу мать!"
        centered "{size=+7}{color=#cbcbcb}Ох... :({/color}{/size}"
        
        
        
        hide screen end_u_4                                           #<---- SCREEN
        with d1
        hide screen blkfade 
        with d9
        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
        
    m "....................."
    if persistent.game_complete:
        m "Нет, я не могу просто взять и уйти!"
    else:
        m "Нет, я не могу просто взять и уйти!"
    
    m "Я должен увидеть девочку в последний раз..."
    
    show screen ctc
    pause
    hide screen ctc
    
    show screen blkfade
    with d7
    
    stop music fadeout 1.0
    
    if not persistent.game_complete: # FIRST PLAY THROUGH.
        centered "{size=+7}{color=#cbcbcb}Хорошо, черт с тобой..{/color}{/size}"
    play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
    centered "{size=+7}{color=#cbcbcb}\"Ежегодный Хогвартский Осенний Бал\"{/color}{/size}"

    hide screen end_u_4                                           #<---- SCREEN
    jump your_whore
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
transform custom_walk_02(x,x2): #Same custom walk but for Hermione.
    xpos x #координата X, из которой облако начинает движение
    ypos 250 #высота, на котором плывет облако
    linear hermione_speed xpos x2 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется

transform custom_walk(x,x2): #Метод ATL для задания движения облаков. Более продвинутый и современный, чем move. Про его возможности читать здесь: http://www.renpy.org/wiki/atl 
    xpos x #координата X, из которой облако начинает движение
    ypos 210 #высота, на котором плывет облако
    linear snapes_speed xpos x2 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
    
transform genie_walk(x,x2): #Метод ATL для задания движения облаков. Более продвинутый и современный, чем move. Про его возможности читать здесь: http://www.renpy.org/wiki/atl 
    xpos x #координата X, из которой облако начинает движение
    ypos 260 #высота, на котором плывет облако
    linear snapes_speed xpos x2 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
    
    

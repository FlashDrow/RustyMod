label cupboard:
    menu:
        "- Осмотреть шкаф -" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 #Empty chair near the desk.
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Шкаф..."
            m "Может порыться в нем чуть позже..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "- Рыться в шкафу -" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}- Рыться в шкафу -{/color}" if searched and not day == 1:
            call already_did from _call_already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        "- Ваши вещи -" if not day == 1:
            label possessions:
            menu:

                "- журнал \"playwizard\"-" if playwizard > 4:
                    show screen playwizard
                    with dissolve 
                    pause 
                    g9 "неплохо"
                    hide screen playwizard
                    with dissolve
                    jump possessions


                "- Чупа-чупс -([candy])" if candy >= 1:
                    $ the_gift = "03_hp/18_store/11.png" # CANDY.
                    show screen gift
                    with d3
                    ">Чупа-чупс. Взрослая конфета для детей или детская конфета для взрослых?"
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Шоколад -([chocolate])" if chocolate >= 1:
                    $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                    show screen gift
                    with d3
                    call choco_text from _call_choco_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Плюшевая сова -([owl])" if owl >= 1:
                    $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
                    show screen gift
                    with d3
                    call owl_text from _call_owl_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Сливочное пиво -([beer])" if beer >= 1:
                    $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER
                    show screen gift
                    with d3
                    call beer_text from _call_beer_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Обучающий журнал -([mag1])" if mag1 >= 1:
                    $ the_gift = "03_hp/18_store/17.png" #MAGAZINE # 1
                    show screen gift
                    with d3
                    call mag1_text from _call_mag1_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Женский журнал -([mag2])" if mag2 >= 1:
                    $ the_gift = "03_hp/18_store/18.png" #MAGAZINE # 2
                    show screen gift
                    with d3
                    call mag2_text from _call_mag2_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Журнал для взрослых -([mag3])" if mag3 >= 1:
                    $ the_gift = "03_hp/18_store/19.png" #MAGAZINE # 3
                    show screen gift
                    with d3
                    call mag3_text from _call_mag3_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Порно журнал -([mag4])" if mag4 >= 1:
                    $ the_gift = "03_hp/18_store/20.png" #MAGAZINE # 4
                    show screen gift
                    with d3
                    call mag4_text from _call_mag4_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Постер Виктора Крама -([krum])" if krum >= 1:
                    $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                    show screen gift
                    with d3
                    ">Мастер по квиддичу, Виктор был выбран, чтобы играть за национальную сборную Болгарии по квиддичу. Несмотря на то, что он все еще ходит в школу, он по праву считается одним из лучших игроков в мире."
                    hide screen gift
                    with d3
                    jump possessions

                "- Сексуальное нижнее белье -([lingerie])" if lingerie >= 1:
                    $ the_gift = "03_hp/18_store/24.png" # LENGERIE.
                    show screen gift
                    with d3
                    ">Сексуальное нижнее белье \"Добрая Фея\". В постели она станет подобна императрице или сестрам Саббат."
                    hide screen gift
                    with d3
                    jump possessions

                "- Упаковка презервативов -([condoms])" if condoms >= 1:
                    $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
                    show screen gift
                    with d3
                    call con_text from _call_con_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Вибратор -([vibrator])" if vibrator >= 1:
                    $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
                    show screen gift
                    with d3
                    call vib_text from _call_vib_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Банка лубриканта -([anal_lube])" if anal_lube >= 1:
                    $ the_gift = "03_hp/18_store/09.png" # Anal lubricant.
                    show screen gift
                    with d3
                    call lub_text from _call_lub_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Кляп и наручники -([ballgag])" if ballgag >= 1:
                    $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
                    show screen gift
                    with d3
                    call ball_text from _call_ball_text
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Анальная пробка -([plug])" if plug >= 1:
                    $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
                    show screen gift
                    with d3
                    call anal_text from _call_anal_text
                    hide screen gift
                    with d3
                    jump possessions

                "- Страпон \"Фестрал\" -([strapon])" if strapon >= 1:
                    $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
                    show screen gift
                    with d3
                    call str_text from _call_str_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Леди Спид Стик-2000 -([broom])" if broom >= 1:
                    $ the_gift = "03_hp/18_store/25.png" # BROOM.
                    show screen gift
                    with d3
                    ">\"Леди Спид Стик-2000\", элегантный способ передвижения для страстных ведьм. Торговой маркой гарантируется полное удовлетворение от эффекта. Закажите одну штуку для вашей ведьмы, и она больше не будет использовать ее скучную старую метлу!"
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Секс-кукла \"Джуаннf\" -([sexdoll])" if sexdoll >= 1:
                    $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                    show screen gift
                    with d3
                    ">Секс-кукла \"Джуаннf\"... Очень реалистичная. Выглядит почти как настоящий человек под каким-то заклинанием."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Бальное платье -" if "ball_dress" in gifts12 and not gave_the_dress:
                    $ the_gift = "03_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    m "Вечернее платье, которое я купил..."
                    m "Надеюсь, что оно подойдет."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- \"А.В.Н.Э.\" знак -" if badge_01 == 1:
                    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE
                    show screen gift
                    with d3
                    m "\"А.В.Н.Э.\" Знак..."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Ажурные чулки -" if nets == 1:
                    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text from _call_nets_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Школьная мини-юбка -" if have_miniskirt:
                    $ the_gift = "03_hp/18_store/07.png" # MINISKIRT.
                    show screen gift
                    with d3
                    m "Просто школьная мини-юбка...поможет в поднятии оценок."
                    hide screen gift
                    with d3
                    jump possessions
                
                "- Вино Дамблдора -([wine])" if wine >= 1:
                    $ the_gift = "03_hp/18_store/27.png" # WINE.
                    show screen gift
                    with d3
                    ">Бутылка из тайника профессора Дамблдора..." 
                    hide screen gift
                    with d3
                    jump possessions
                    
                    
                "- Неизвестное зелье -([potions])" if  potions >= 1:
                    $ the_gift = "03_hp/18_store/32.png" # HEALING POTION.
                    show screen gift
                    with d3
                    ">Какое-то зелье..." 
                    hide screen gift
                    with d3
                    jump possessions
                    
                "- Ничего -":
                    jump cupboard

        "- Священные свитки. Часть I -" if not day == 1 and cataloug_found:
            label sc_col_men:
            menu:
                "- С.01: [scroll_01_name] -" if sscroll_01 or persistent.ss_01:
                    $ the_gift = "03_hp/19_extras/01.png" # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.02: [scroll_02_name] -" if sscroll_02 or persistent.ss_02:
                    $ the_gift = "03_hp/19_extras/02.png" # SACRED SCROLL 02.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.03: [scroll_03_name] -" if sscroll_03 or persistent.ss_03:
                    $ the_gift = "03_hp/19_extras/03.png" # SACRED SCROLL 03.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.04: [scroll_04_name] -" if sscroll_04 or persistent.ss_04:
                    $ the_gift = "03_hp/19_extras/04.png" # SACRED SCROLL 04.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.05: [scroll_05_name] -" if sscroll_05 or persistent.ss_05:
                    $ the_gift = "03_hp/19_extras/05.png" # SACRED SCROLL 05.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.06: [scroll_06_name] -" if sscroll_06 or persistent.ss_06:
                    $ the_gift = "03_hp/19_extras/06.png" # SACRED SCROLL 06.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.07: [scroll_07_name] -" if sscroll_07 or persistent.ss_07:
                    $ the_gift = "03_hp/19_extras/07.png" # SACRED SCROLL 07.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.08: [scroll_08_name] -" if sscroll_08 or persistent.ss_08:
                    $ the_gift = "03_hp/19_extras/08.png" # SACRED SCROLL 08.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.09: [scroll_09_name] -" if sscroll_09 or persistent.ss_09:
                    $ the_gift = "03_hp/19_extras/09.png" # SACRED SCROLL 09.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.10: [scroll_10_name] -" if sscroll_10 or persistent.ss_10:
                    $ the_gift = "03_hp/19_extras/10.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.11: [scroll_11_name] -" if sscroll_11 or persistent.ss_11:
                    $ the_gift = "03_hp/19_extras/11.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.02: [scroll_12_name] -" if sscroll_12 or persistent.ss_12:
                    $ the_gift = "03_hp/19_extras/12.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.03: [scroll_13_name] -" if sscroll_13 or persistent.ss_10:
                    $ the_gift = "03_hp/19_extras/10.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.04: [scroll_14_name] -" if sscroll_14 or persistent.ss_14:
                    $ the_gift = "03_hp/19_extras/14.png" # SACRED SCROLL 10.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.05: [scroll_15_name] -" if sscroll_15 or persistent.ss_15:
                    $ the_gift = "03_hp/19_extras/15.png" # SACRED SCROLL 15.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men

                "- Ничего -":
                    jump cupboard
            
            
        "- Священные свитки. Часть II -" if not day == 1 and cataloug_found:
            label sc_col_men2:
            menu:
                "- С.16: [scroll_16_name] -" if sscroll_16 or persistent.ss_16:
                    $ the_gift = "03_hp/19_extras/16.png" # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.17: [scroll_17_name] -" if sscroll_17 or persistent.ss_17:
                    $ the_gift = "03_hp/19_extras/17png" # SACRED SCROLL 02.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.18: [scroll_18_name] -" if sscroll_18 or persistent.ss_18:
                    $ the_gift = "03_hp/19_extras/18.png" # SACRED SCROLL 03.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.19: [scroll_19_name] -" if sscroll_19 or persistent.ss_19:
                    $ the_gift = "03_hp/19_extras/19.png" # SACRED SCROLL 04.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.20: [scroll_20_name] -" if sscroll_20 or persistent.ss_20:
                    $ the_gift = "03_hp/19_extras/20.png" # SACRED SCROLL 05.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.21: [scroll_21_name] -" if sscroll_12 or persistent.ss_12:
                    $ the_gift = "03_hp/19_extras/21.png" # SACRED SCROLL 21.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.22: [scroll_22_name] -" if sscroll_22 or persistent.ss_22:
                    $ the_gift = "03_hp/19_extras/22.png" # SACRED SCROLL 22.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.23: [scroll_23_name] -" if sscroll_23 or persistent.ss_23:
                    $ the_gift = "03_hp/19_extras/23.png" # SACRED SCROLL 23.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.24: [scroll_24_name] -" if sscroll_24 or persistent.ss_24:
                    $ the_gift = "03_hp/19_extras/24.png" # SACRED SCROLL 24.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                    
                "- С.25: [scroll_25_name] -" if sscroll_25 or persistent.ss_25:
                    $ the_gift = "03_hp/19_extras/25.png" # SACRED SCROLL 25.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.26: [scroll_26_name] -" if sscroll_26 or persistent.ss_26:
                    $ the_gift = "03_hp/19_extras/26.png" # SACRED SCROLL 26.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.27: [scroll_27_name] -" if sscroll_27 or persistent.ss_27:
                    $ the_gift = "03_hp/19_extras/27.png" # SACRED SCROLL 27.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.28: [scroll_28_name] -" if sscroll_28 or persistent.ss_28:
                    $ the_gift = "03_hp/19_extras/28.png" # SACRED SCROLL 28.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.29: [scroll_29_name] -" if sscroll_29 or persistent.ss_29:
                    $ the_gift = "03_hp/19_extras/29.png" # SACRED SCROLL 29.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men
                
                "- С.05: [scroll_30_name] -" if sscroll_30 or persistent.ss_30:
                    $ the_gift = "03_hp/19_extras/30.png" # SACRED SCROLL 30.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men

                "- Ничего -":
                    jump cupboard
            
        "- Ничего -":
            jump day_main_menu
 
label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">Вы роетесь в шкафу..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "03_hp/18_store/32.png" # CANDY.
            show screen gift
            with d3
            ">Вы нашли какое-то зелье..." 
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start

    if rum_times == 15 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "03_hp/18_store/dahr2.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">Вы нашли каталог \"Приблуды Дахра\"... \n>Теперь вы можете использовать каталог для заказа товаров с помощью совы."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    
    if i_of_iv == 4: # Found something.
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">Вы нашли секс-куклу \"Джуанну\"!" 
                hide screen gift
                with d3
            elif one_of_tw == 1 or one_of_tw == 2:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">Вы нашли конфету..." 
                hide screen gift
                with d3
            elif one_of_tw >= 3 and one_of_tw <= 9  or one_of_tw == 18: # GOLD.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">ВЫ нашли [gold1] золота..." 
                $ gold = gold + gold1
                hide screen gift
                with d3
            elif one_of_tw >= 10 and one_of_tw <= 16: # WINE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">Вы нашли бутылку из тайника Дамблдора..." 
                hide screen gift
                with d3
            elif one_of_tw == 17: # CHOCOLATE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">Вы нашли плитку шоколада..."
                hide screen gift
                with d3
            elif one_of_tw == 19: # LINGERIE.
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">Вы нашли сексуальное нижее белье..."
                hide screen gift
                with d3
                
          
        ### EVENT LEVEL 02 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">Вы нашли секс-куклу \"Джуанну\"!" 
                hide screen gift
                with d3
            elif one_of_tw == 1 or one_of_tw ==2:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">Вы нашли конфету..." 
                hide screen gift
                with d3
            elif one_of_tw >= 3 and one_of_tw <= 10 or one_of_tw == 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">Вы нашли [gold2] золота..." 
                $ gold = gold + gold2
                hide screen gift
                with d3
            elif one_of_tw >= 11 and one_of_tw <= 15:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">Вы нашли бутылку из тайника Дамблдора..." 
                hide screen gift
                with d3
            elif one_of_tw == 16:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">Вы нашли сексуальное нижее белье..."
                hide screen gift
                with d3
            elif one_of_tw == 17:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">Вы нашли плитку шоколада..."
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">Вы нашли постер..."
                hide screen gift
                with d3
         
         
         
         
        ### EVENT LEVEL 03 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">Вы нашли секс-куклу \"Джуанну\"!" 
                hide screen gift
                with d3
            elif one_of_tw >= 1 and one_of_tw <= 4:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ owl += 1
                $ the_gift = "03_hp/18_store/22.png" # OWL.
                show screen gift
                with d3
                ">Вы нашли плюшевую игрушку..." 
                hide screen gift
                with d3
            elif one_of_tw == 5 or one_of_tw == 6:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ candy += 1
                $ the_gift = "03_hp/18_store/11.png" # CANDY.
                show screen gift
                with d3
                ">Вы нашли конфету..." 
                hide screen gift
                with d3
            elif one_of_tw >= 7 and one_of_tw <= 14:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">Вы нашли [gold3] золота..." 
                $ gold = gold + gold3
                hide screen gift
                with d3
            elif one_of_tw >= 15 and one_of_tw <= 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ wine += 1
                $ the_gift = "03_hp/18_store/27.png" # WINE
                show screen gift
                with d3
                ">Вы нашли бутылку вина в тайнике Дамблдора..." 
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">Вы нашли постер..."
                hide screen gift
                with d3
            
        ### EVENT LEVEL 04 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 18: # Lv 7+  
            if one_of_tw == 20:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ sexdoll += 1
                $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
                show screen gift
                with d3
                ">Вы нашли секс-куклу \"Джуанну\"!" 
                hide screen gift
                with d3
            elif one_of_tw >= 1 and one_of_tw <= 4:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ owl += 1
                $ the_gift = "03_hp/18_store/22.png" # OWL.
                show screen gift
                with d3
                ">Вы нашли плюшевую игрушку..." 
                hide screen gift
                with d3
            elif one_of_tw >= 5 and one_of_tw <= 8:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ chocolate += 1
                $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                show screen gift
                with d3
                ">Вы нашли плитку шоколада..."
                hide screen gift
                with d3
            elif one_of_tw >= 9 and one_of_tw <= 16:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ the_gift = "03_hp/18_store/28.png" # GOLD.
                show screen gift
                with d3
                ">Вы нашли [gold4] золота..." 
                $ gold = gold + gold4
                hide screen gift
                with d3
            elif one_of_tw == 17:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ broom += 1
                $ the_gift = "03_hp/18_store/25.png" # BROOM.
                show screen gift
                with d3
                ">Вы нашли метлу..."
                hide screen gift
                with d3
            elif one_of_tw == 18:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ krum += 1
                $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
                show screen gift
                with d3
                ">Вы нашли постер..."
                hide screen gift
                with d3
            elif one_of_tw == 19:
                $ renpy.play('sounds/win2.mp3')   #Not loud.
                $ lingerie += 1
                $ the_gift = "03_hp/18_store/24.png" # LINGERIE
                show screen gift
                with d3
                ">Вы нашли сексуальное нижнее белье..."
                hide screen gift
                with d3
            

    else: #Didn't find anything.
        ">...Вы не нашли ничего ценного." 
    

    
    show screen cupboard
    show screen genie
    hide screen rum_screen
    
    hide screen bld1
    with d3
    
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
        
        
        
        
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "Я сегодня уже занимался этим..."
    hide screen bld1
    with d3
    return
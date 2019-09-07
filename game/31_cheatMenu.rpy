label cheatMenu:
    $ pat = 1
    menu:
        "-Помощь-" if pat == 0:
            menu:
                "Слизерин всегда должен лидировать":
                    $ slytherin = 6666
                    m "Невиданным образом у Слизерина стало 6666 очков"
                    call screen main_menu_01 # jump desk

                "Дай мне денег":
                    $ gold += 10000
                    m "Откуда ни возьмись, мой карман тяжелеет на 10000 галеонов"
                    call screen main_menu_01 # jump desk

                "Баг с почтой":
                    $ order_placed = False
                    $ package_is_here = False
                    $ days_in_delivery = 0
                    hide screen gift
                    hide screen package
                    m "Исправлено"
                    call screen main_menu_01 # jump desk
                "Назад":
                    call screen main_menu_01 # jump desk
        "-Помощь-" if pat == 1:
            menu:
                "Ваучер":
                    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                    call screen main_menu_01 # jump desk

                #"Бонусы из книг + ваучер":
                #    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                #    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                #    $ waifu_book_completed = True
                #    $ complited_shea_already = True
                #    $ complited_stevens_already = True
                #    $ complited_leena_already = True
                #    call screen main_menu_01 # jump desk
                    
                "Улучшить фантазию":
                    $ imagination = 5
                    call screen main_menu_01 # jump desk
                "Разблокировать публичные задания":
                    $ lock_public_favors = False
                    $ touched_by_boy = True
                    "Публичные задания разблокированы"
                    call screen main_menu_01 # jump desk
                "Гермиона больше не злится на вас":
                    $ mad = 0
                    "Исполнено"
                    call screen main_menu_01 # jump desk
                "Гермиона стала более распутной":
                    "Уровень распутности гермионы был [level] из 10 возможных..."
                    if level == "01":

                        $ whoring = 5
                        $ level = "02"
                        "Повышен до 2"
                        call screen main_menu_01 # jump desk
                    elif level == "02":
                        $ whoring = 8
                        $ level = "03"
                        "Повышен до 3"
                        call screen main_menu_01 # jump desk
                    elif level == "03":
                        $ whoring = 11
                        $ level = "04"
                        "Повышен до 4"
                        call screen main_menu_01 # jump desk
                    elif level == "04":
                        $ whoring = 14
                        $ level = "05"
                        "Повышен до 5"
                        call screen main_menu_01 # jump desk
                    elif level == "05":
                        $ whoring = 17
                        $ level = "06"
                        "Повышен до 6"
                        call screen main_menu_01 # jump desk
                    elif level == "06":
                        $ whoring = 20
                        $ level = "07"
                        "Повышен до 7"
                        call screen main_menu_01 # jump desk
                    elif level == "07":
                        $ whoring = 23
                        $ level = "08"
                        "Повышен до 8"
                        call screen main_menu_01 # jump desk
                    elif level == "08":
                        $ whoring = 26
                        $ level = "09"
                        "Повышен до 9"
                        call screen main_menu_01 # jump desk
                    elif level == "09":
                        $ whoring = 29
                        $ level = "10"
                        "Повышен до 10"
                        call screen main_menu_01 # jump desk
                    else:
                        "Уровень распутности Гермионы достиг максимума"
                        call screen main_menu_01 # jump desk
                "Дафна больше не злится на вас":
                    $ daphne_moral = 5
                    call screen main_menu_01 # jump desk
                "Слизерин всегда должен лидировать":
                    $ slytherin = 6666
                    m "Невиданным образом у Слизерина стало 6666 очков"
                    call screen main_menu_01 # jump desk
                "Получить каталог Приблуды Дахра":
                    $ cataloug_found = True
                    $ have_catalogue = True
                    m "Ах, точно, вот где он был"
                    call screen main_menu_01 # jump desk

                "Дай мне денег":
                    $ gold += 10000
                    m "Откуда ни возьмись, мой карман тяжелеет на 10000 галеонов"
                    call screen main_menu_01 # jump desk
                "Баг с почтой":
                    $ order_placed = False
                    $ package_is_here = False
                    $ days_in_delivery = 0
                    hide screen gift
                    hide screen package
                    m "Исправлено"
                    call screen main_menu_01 # jump desk



                "Все предметы":
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
                    m "Done"
                    call screen main_menu_01 # jump desk

                "Доставка в 1 день":
                    if delivery_cheat == 0:
                        $ delivery_cheat = 1
                    else:
                        $ delivery_cheat = 0

                    m "Done"
                    call screen main_menu_01 # jump desk

                "Назад":
                    call screen main_menu_01 # jump desk

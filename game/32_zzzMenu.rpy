label zzzMenu:
    if daytime and not day == 1:
        jump night_start
    elif not daytime and not day == 1:
        jump day_start
    #menu:
        #"- Дремать -" if daytime and not day == 1:
        #    jump night_start
        #"- Спать -" if not daytime and not day == 1:
        #    jump day_start
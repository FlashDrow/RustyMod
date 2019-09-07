label dahrChoise:
    if order_placed or package_is_here:
        show screen bld1
        with d3
        dahr "Пожалуйста, потерпи чуть-чуть. Сова уже в пути."
        hide screen bld1
        with d3
        call screen main_menu_01
    else:
        jump the_oddities
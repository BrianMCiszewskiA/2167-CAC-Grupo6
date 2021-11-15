def subcampeon(puntajes):
    campeon = 0
    subcampeon = 0
    for n in puntajes:
        if n>campeon:
            subcampeon = campeon
            campeon = n
        elif n<campeon and n>subcampeon:
            subcampeon = n
    return subcampeon
     

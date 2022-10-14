def sortiertest(liste):
    aufsteigend = True
    absteigend = True

    for i in range(len(liste) - 1):
        derzeitiger_wert = liste[i]
        nachfolgender_wert = liste[i + 1]

        if aufsteigend:
            aufsteigend = derzeitiger_wert <= nachfolgender_wert
        if absteigend:
            absteigend = derzeitiger_wert >= nachfolgender_wert

        if not aufsteigend and not absteigend:
            return 0

    if aufsteigend and absteigend:
        return 3
    elif aufsteigend:
        return 1
    elif absteigend:
        return 2

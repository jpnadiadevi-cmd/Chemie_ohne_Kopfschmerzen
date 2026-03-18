def berechne_molare_masse(verbindung, periodensystem):
    gesamtmasse = 0

    for element, anzahl in verbindung:
        if element in periodensystem:
            gesamtmasse += periodensystem[element] * anzahl
        else:
            raise ValueError(f"Element {element} nicht gefunden")

    return gesamtmasse

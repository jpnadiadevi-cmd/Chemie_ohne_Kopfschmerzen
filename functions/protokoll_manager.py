from datetime import datetime
from zoneinfo import ZoneInfo


def erstelle_neues_protokoll(name):

    return {
        "erstellt": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "titel": name,
        "ziel": "",
        "material": "",
        "durchführung": "",
        "beobachtung": "",
        "auswertung": "",
        "fazit": ""
    }


def experiment_name_ungueltig(name):

    return name.strip() == ""


def experiment_existiert(name, protokolle):

    return name in protokolle


def loesche_protokoll(protokolle, name):

    if name in protokolle:
        del protokolle[name]

    return protokolle
def berechne_molaritaet(n, V):

    if V > 0:
        result = n / V

        return {
            "status": "ok",
            "value": result,
            "label": "Molarität c"
        }

    return {
        "status": "error",
        "message": "ℹ️ Bitte gib ein Volumen > 0 ein"
    }


def berechne_molalitaet(n, m):

    if m > 0:
        result = n / m

        return {
            "status": "ok",
            "value": result,
            "label": "Molalität β"
        }

    return {
        "status": "error",
        "message": "ℹ️ Bitte gib eine Masse > 0 ein"
    }


def berechne_teilchenzahl(n, avogadro):

    result = n * avogadro

    return {
        "status": "ok",
        "value": result,
        "label": "Teilchenzahl N"
    }
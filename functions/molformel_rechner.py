def berechne_molformel(n, m, M):
    eingegeben_count = sum([n > 0, m > 0, M > 0])

    if n > 0 and m > 0 and M == 0:
        result = m / n

        return {
            "status": "ok",
            "result_key": "M",
            "result_value": result,
            "label": "Molare Masse M [g/mol]"
        }

    if n > 0 and M > 0 and m == 0:
        result = M * n

        return {
            "status": "ok",
            "result_key": "m",
            "result_value": result,
            "label": "Masse m [g]"
        }

    if m > 0 and M > 0 and n == 0:
        result = m / M

        return {
            "status": "ok",
            "result_key": "n",
            "result_value": result,
            "label": "Stoffmenge n [mol]"
        }

    if eingegeben_count == 1:
        return {
            "status": "warning",
            "message": "⚠️ Bitte gib mindestens zwei Werte ein!"
        }

    if eingegeben_count == 0:
        return {
            "status": "info",
            "message": "👆 Bitte gib zwei Werte ein, um den dritten zu berechnen."
        }

    return {
        "status": "error",
        "message": "❌ Bitte gib nur zwei Werte ein!"
    }
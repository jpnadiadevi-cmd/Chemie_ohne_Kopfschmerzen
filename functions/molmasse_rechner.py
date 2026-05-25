def berechne_gesamtmasse(elemente_liste):

    total_mass = 0

    for el in elemente_liste:
        total_mass += el["atommasse"]

    return total_mass


def erstelle_element_counts(elemente_liste):

    element_counts = {}

    for el in elemente_liste:

        symbol = el["symbol"]

        element_counts[symbol] = (
            element_counts.get(symbol, 0) + 1
        )

    return element_counts


def erstelle_formel_string(element_counts):

    formula_str = ""

    for symbol, count in element_counts.items():

        if count == 1:
            formula_str += symbol

        else:
            formula_str += f"{symbol}{count}"

    return formula_str


def erstelle_formel_html(element_counts):

    formula_html = ""

    for symbol, count in element_counts.items():

        if count == 1:

            formula_html += (
                f"<span style='font-size: 24px; font-weight: bold;'>"
                f"{symbol}"
                f"</span>"
            )

        else:

            formula_html += (
                f"<span style='font-size: 24px; font-weight: bold;'>"
                f"{symbol}"
                f"<sub style='font-size: 18px;'>{count}</sub>"
                f"</span>"
            )

    return formula_html
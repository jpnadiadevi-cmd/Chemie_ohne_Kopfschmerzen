def erstelle_element_grid(elemente_sortiert):

    element_grid = {}

    for el in elemente_sortiert:

        periode = el["periode"]
        gruppe = el["gruppe"]

        if periode not in element_grid:
            element_grid[periode] = {}

        element_grid[periode][gruppe] = el

    return element_grid


def hole_farbe(kategorie, farben_kategorien):

    return farben_kategorien.get(
        kategorie,
        "#FFFFFF"
    )


def formatiere_elektronegativitaet(wert):

    if wert is not None:
        return f"{wert:.2f}"

    return "N/A"
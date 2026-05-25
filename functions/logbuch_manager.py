import pandas as pd


def hole_dataframe(daten):

    return pd.DataFrame(daten)


def sammle_exportdaten(logbuch_daten):

    exportdaten = []

    for kategorie, daten in logbuch_daten.items():

        for eintrag in daten:

            exporteintrag = eintrag.copy()

            exporteintrag["Kategorie"] = kategorie

            exportdaten.append(exporteintrag)

    return exportdaten


def erstelle_export_dataframe(exportdaten):

    return pd.DataFrame(exportdaten)


def leere_kategorie(logbuch_daten, kategorie):

    logbuch_daten[kategorie] = []

    return logbuch_daten
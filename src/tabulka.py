def tabulka(
    frame, titulek="", bez_tecky=[], na_procenta=[], poradi=False, bez_zavorek=True
):
    dataframe = frame

    def cela(x):
        try:
            x = int(x)
        except:
            x = "–"
        return x

    import re

    if poradi:
        sloupce = dataframe.columns.tolist()
        dataframe = dataframe.reset_index(drop=True)
        dataframe[" "] = pd.to_numeric(dataframe.index)
        dataframe[" "] = dataframe[" "].apply(lambda x: str(x + 1) + ".")
        nove_sloupce = [" "]
        for s in sloupce:
            nove_sloupce.append(s)
        print(nove_sloupce)
        dataframe = dataframe[nove_sloupce]

    if len(bez_tecky) > 0:
        for b in bez_tecky:
            dataframe[b] = dataframe[b].apply(lambda x: cela(x))

    if len(na_procenta) > 0:
        for p in na_procenta:
            dataframe[p] = dataframe[p].apply(lambda x: "{:.1%}".format(x))
            dataframe[p] = (
                dataframe[p]
                .astype("string")
                .apply(lambda x: x.replace(".", ",").replace("%", " %"))
            )

    dataframe = re.sub("\\n\s*", "", dataframe.to_html(index=False))
    dataframe = (
        dataframe.replace("<th>", '<th class="text-nowrap">')
        .replace("<tbody>", '<tbody class="text-sm">')
        .replace(
            '<table border="1" class="dataframe">',
            '<table class="dataframe table table--responsive table--w100p table--striped-red table--plain">',
        )
    )

    if len(titulek) > 0:
        dataframe = dataframe.replace("<thead", f"<caption>{titulek}</caption><thead")

    if bez_zavorek:
        dataframe = re.sub("\([\d]*\)", "", dataframe)
        dataframe = dataframe.replace(" </td>", "</td>")

    print(dataframe)

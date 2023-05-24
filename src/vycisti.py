def vycisti(dataframe, opravy):

    # Funkce čistí dataframe z filmy od zahraničních a exilových filmů, 
    # od duplicit, od německých verzi prvorepulikových filmů a od filmů, 
    # které nemají jako zemi původu uvedené ani Česko(slovensko), 
    # ani Rakousko-Uhersko.

    from datetime import datetime

    filmu_pred = dataframe.shape[0]

    dataframe = dataframe[~(dataframe["Film"].isin(opravy["zahranicni"]))]
    dataframe = dataframe[~(dataframe["Film"].isin(opravy["exil"]))]
    dataframe = dataframe[~(dataframe["Film"].isin(opravy["duplicity"]))]
    dataframe = dataframe[~(dataframe["Film"].str.contains("německá verze", na=False))]

    if "Země původu" in dataframe.columns.to_list():
        dataframe = dataframe[
            dataframe["Země původu"].str.contains("Česk|Rakousko-Uhersko", na=True)
        ]

    filmu_po = dataframe.shape[0]

    print(
        f"""{datetime.now().strftime("%Y/%m/%d %H:%M:%S")} z {filmu_pred} filmů odstraněno {filmu_pred - filmu_po}. Aktuální dataframe obsahuje {filmu_po} filmů."""
    )

    return dataframe

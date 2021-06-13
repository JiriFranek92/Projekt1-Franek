def bar_chart(dictionary, labels=("LABEL", "VALUE"), symbol="*", sort=True, desc=False):
    """ vezme slovník, kde všechny hodnoty jsou integer a vypíše sloupcový graf, kde popisky jsou klíče grafu
    :param dictionary: Zdrojový slovník.
    :param labels: List nebo tuple s nadpisy.
    :param symbol: Symbol, který se používá pro sloupce.
    :param sort: Jestli má být graf seřazen abecedně podle klíče.
    :param desc: Jestli se má graf řadit sestupně.
    """

    if not isinstance(dictionary, dict):
        exit("Input must be a dictionary!")
    if not any((isinstance(labels, list), isinstance(labels, tuple)) or len(labels) == 2):
        exit("'labels' argument must be a list or a tupple of lenght 2!")
    if not all(isinstance(item, int) for item in dictionary.values()):
        exit("Every dictionary value must be an integer!")

    # ----- pomocné proměnné pro správné formátování -----
    # šířka sloupce popisků
    # (co je delší: délka nejdelšího popisku, nebo délka textu záhlaví)
    label_col_width = \
        max(max([len(str(key)) for key in dictionary.keys()]),
            len(str(labels[0])))
    # šířka sloupce hodnot
    # (co je delší: délka sloupce + délka textu popisku + mezera
    # NEBO délka textu záhlaví)
    values_col_width = max(max(dictionary.values()) +
                           len(str(max(dictionary.values()))) + 1,
                           len(str(labels[1])))

    # tiskni záhlaví
    # (margin_label)POPISEK|(margin_value)HODNOTA
    margin_label = (label_col_width - len(str(labels[0]))) * " "
    margin_value = ((values_col_width - len(str(labels[1]))) // 2) * " "
    print(f"{margin_label}{str(labels[0])}|{margin_value}{str(labels[1])}")

    print("-" * (label_col_width + values_col_width + 2))
    # tiskni jednotlivé údaje do grafu
    # (margin_label)popisek|****** (číslo)
    for label, value in sorted(dictionary.items(), reverse=desc) if sort else dictionary.items():
        margin_label = (label_col_width - len(str(label))) * " "
        print(f"{margin_label}{str(label)}|{value * str(symbol)} {str(value)}")


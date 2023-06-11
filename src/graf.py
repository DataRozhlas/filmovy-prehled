def graf(
    carovy=[],
    sloupcovy=[],
    procenta=[],
    skryte=[],
    histogram=[],
    max_procenta=100,
    target="",
    titulek="",
    podtitulek="",
    osay="",
    osay2="",
    kredity="",
    zaokrouhleni=2,
    prvni=True,
    skladany=False,
):
    import os
    from highcharts_core.chart import Chart
    from highcharts_core.options.series.area import LineSeries
    from highcharts_core.options.series.bar import ColumnSeries
    from highcharts_core.options.series.histogram import HistogramSeries
    from highcharts_core.options.title import Title
    from highcharts_core.options.subtitle import Subtitle
    from highcharts_core.options.credits import Credits

    if prvni:
        with open(os.path.join("grafy", "styly.css"), encoding="utf-8") as styly:
            styly = styly.read()
        zdrojaky = f"""<script src="https://code.highcharts.com/highcharts.js"></script><style type="text/css">{styly}</style>"""
    else:
        zdrojaky = ""

    pred = f"""{zdrojaky}
        <figure id="{target}">
        <div id="container"></div>
        </figure>
        <script>"""

    if len(carovy) > 0:
        categories = carovy[0].index.to_list()
    if len(sloupcovy) > 0:
        categories = sloupcovy[0].index.to_list()
    categories = [str(x) for x in categories]

    nastaveni = {}
    nastaveni["xAxis"] = {"categories": categories, "min": 0}
    nastaveni["yAxis"] = [{"title": {"text": osay}}]

    if skladany:
        nastaveni["plotOptions"] = {"column": {"stacking": "normal"}}
    if histogram:
        nastaveni["plotOptions"] = {"column": {"pointPadding": 0, "borderWidth": 0, "groupPadding": 0, "shadow": False}}

    if len(procenta) > 0:
        osa_procent = {
            "title": {"text": osay2},
            "max": max_procenta,
            "min": 0,
            "labels": {"format": "{value} %"},
        }

        if len(procenta) != len(carovy) + len(sloupcovy):
            osa_procent["opposite"] = True
            druha_osa = 1
            nastaveni["yAxis"].append(osa_procent)
            nastaveni["alignTicks"] = False
        if len(procenta) == len(carovy) + len(sloupcovy):
            nastaveni["yAxis"] = [osa_procent]
            druha_osa = 0

    my_chart = Chart(container=target, options=nastaveni)

    procenta = [p.name for p in procenta]
    skryte = [s.name for s in skryte]

    def vykresleni(serie, typ):
        for s in serie:
            popisek = s.name
            if s.name in skryte:
                viditelnost = False
            else:
                viditelnost = True
            if s.name in procenta:
                s = [round(x * 100, zaokrouhleni) for x in s.fillna(0).to_list()]
                my_chart.add_series(
                    typ(
                        data=s,
                        visible=viditelnost,
                        name=popisek,
                        y_axis=druha_osa,
                        tooltip={"valueSuffix": " %"},
                    )
                )
            else:
                my_chart.add_series(
                    typ(
                        data=s.fillna(0).to_list(),
                        visible=viditelnost,
                        name=popisek,
                        y_axis=0,
                    )
                )

    if len(sloupcovy) > 0:
        vykresleni(sloupcovy, ColumnSeries)
    if len(carovy) > 0:
        vykresleni(carovy, LineSeries)

    my_chart.options.colors = [
        "#b2e061",
        "#7eb0d5",
        "#fd7f6f",
        "#bd7ebe",
        "#ffb55a",
        "#ffee65",
        "#beb9db",
        "#fdcce5",
        "#8bd3c7",
    ]

    my_chart.options.title = Title(text=titulek, align="left", margin=30)

    if len(podtitulek) > 0:
        my_chart.options.subtitle = Subtitle(text=podtitulek, align="left")

    my_credits = Credits(text=kredity[0], enabled=True, href=kredity[1])
    my_chart.options.credits = my_credits

    as_js_literal = my_chart.to_js_literal()

    code = f"<html><head><title>{titulek}</title></head><body>{pred}{as_js_literal}</script></body></html>"

    if not os.path.exists("grafy"):
        os.mkdir("grafy")

    with open(os.path.join("grafy", target + ".html"), "w+") as f:
        f.write(code)

    with open(os.path.join("grafy", target + ".txt"), "w+") as f:
        f.write(as_js_literal)

        print("Graf uložen.")
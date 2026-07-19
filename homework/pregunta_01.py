"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os

    import matplotlib.pyplot as plt
    import pandas as pd

    news = pd.read_csv("files/input/news.csv", index_col=0)

    colors = {
        "Television": "grey",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }
    linewidths = {
        "Television": 1.5,
        "Newspaper": 1.5,
        "Internet": 3.0,
        "Radio": 1.5,
    }

    fig, ax = plt.subplots(figsize=(7, 5))

    for column in news.columns:
        ax.plot(
            news.index,
            news[column],
            color=colors[column],
            linewidth=linewidths[column],
        )

        first_x, first_y = news.index[0], news[column].iloc[0]
        last_x, last_y = news.index[-1], news[column].iloc[-1]

        ax.plot(first_x, first_y, "o", color=colors[column])
        ax.plot(last_x, last_y, "o", color=colors[column])

        ax.annotate(
            f"{column} {first_y}%",
            xy=(first_x, first_y),
            xytext=(-10, 0),
            textcoords="offset points",
            ha="right",
            va="center",
            color=colors[column],
        )
        ax.annotate(
            f"{last_y}%",
            xy=(last_x, last_y),
            xytext=(10, 0),
            textcoords="offset points",
            ha="left",
            va="center",
            color=colors[column],
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.set_yticks([])

    ax.set_xticks(news.index)
    ax.set_xticklabels(news.index)

    fig.suptitle("How people get their news", fontsize=16, y=0.98)
    ax.set_title(
        "An increasing proportion cite the internet as their primary news source",
        fontsize=9,
        loc="center",
        pad=15,
    )

    fig.tight_layout(rect=(0, 0, 1, 0.94))

    os.makedirs("files/plots", exist_ok=True)
    fig.savefig("files/plots/news.png")

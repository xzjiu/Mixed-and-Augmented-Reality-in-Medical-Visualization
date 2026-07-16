"""Shared plotting helpers imported by the .qmd dashboard pages."""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.io as pio

PROCESSED = Path("data/processed")

TEMPLATE = "plotly_white"
COLOR_SEQ = px.colors.qualitative.Safe
ACCENT = "#2c7fb8"

# plotly.js (bundled with plotly 6.8) drops bar text labels when the
# template's layout.font is incomplete (as plotly_white ships, color-only)
# or when an "Open Sans" family is combined with a font color — use a
# complete spec with a plain system font stack.
pio.templates[TEMPLATE].layout.font = dict(
    family="Helvetica, Arial, sans-serif", size=12, color="#2a3f5f"
)
pio.templates.default = TEMPLATE


def load(name):
    return pd.read_csv(PROCESSED / name)


def load_summary():
    with open(PROCESSED / "summary_counts.json") as f:
        return json.load(f)


def count_bar(labels, title=None, color=ACCENT, orientation="h"):
    """Horizontal bar chart of value counts for a label Series."""
    counts = labels.value_counts()
    if orientation == "h":
        counts = counts.sort_values()
        fig = px.bar(x=counts.values, y=counts.index, orientation="h", title=title)
        fig.update_layout(xaxis_title="Number of studies", yaxis_title=None)
    else:
        fig = px.bar(x=counts.index, y=counts.values, title=title)
        fig.update_layout(yaxis_title="Number of studies", xaxis_title=None)
    if orientation == "h":
        hover = "%{y}<br>%{x} studies<extra></extra>"
    else:
        hover = "%{x}<br>%{y} studies<extra></extra>"
    fig.update_traces(marker_color=color, hovertemplate=hover)
    fig.update_layout(margin=dict(l=10, r=10, t=40 if title else 10, b=10))
    return fig


def heatmap(cross, title=None, xlab=None, ylab=None):
    """Annotated heatmap from a crosstab DataFrame."""
    fig = px.imshow(
        cross,
        text_auto=True,
        color_continuous_scale="Blues",
        aspect="auto",
        title=title,
    )
    fig.update_layout(
        xaxis_title=xlab,
        yaxis_title=ylab,
        xaxis_tickangle=-40,
        coloraxis_showscale=False,
        margin=dict(l=10, r=10, t=40 if title else 10, b=10),
    )
    fig.update_traces(
        hovertemplate="%{y} × %{x}<br>%{z} studies<extra></extra>"
    )
    return fig

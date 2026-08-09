from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


BRAND_COLORS = {
    "blue": "#2789D8",
    "green": "#2FAE83",
    "coral": "#E07A5F",
    "navy": "#173B67",
    "light_blue": "#68A9E6",
    "blue_graphite": "#52677C",
    "cool_gray": "#89939D",
    "amber": "#E4A03A",
    "red": "#C94F56",
    # Background and structural colors
    "figure_background": "#FFFFFF",
    "axes_background": "#EEF0F5",
    "axes_edge": "#D7DCE3",
    "grid": "#FFFFFF",
    # Chart semantic colors
    "primary_line": "#2789D8",
    "marker_fill": "#EEF0F5",
    "marker_edge": "#2789D8",
}

BRAND_PALETTE = list(BRAND_COLORS.values())


def set_brand_theme() -> None:
    """Apply the project-wide Seaborn and Matplotlib theme."""

    sns.set_theme(
        style="darkgrid",
        context="notebook",
        palette=BRAND_PALETTE,
        rc={
            "figure.facecolor": BRAND_COLORS["figure_background"],
            "axes.facecolor": BRAND_COLORS["axes_background"],
            "axes.edgecolor": BRAND_COLORS["axes_edge"],
            "axes.labelcolor": BRAND_COLORS["navy"],
            "text.color": BRAND_COLORS["navy"],
            "xtick.color": BRAND_COLORS["blue_graphite"],
            "ytick.color": BRAND_COLORS["blue_graphite"],
            "grid.color": BRAND_COLORS["grid"],
            "grid.linewidth": 1,
        },
    )


def format_axes(ax: plt.Axes) -> None:
    """Apply common formatting to an axes object."""

    ax.grid(False, axis="x")
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)

    sns.despine(
        ax=ax,
        left=True,
        bottom=True,
    )


def add_chart_title(
    ax: plt.Axes,
    title: str,
    subtitle: str | None = None,
) -> None:
    """Add a standard title and optional subtitle."""

    ax.set_title(
        title,
        loc="left",
        fontsize=18,
        fontweight="semibold",
        pad=28 if subtitle else 18,
    )

    if subtitle:
        ax.text(
            0,
            1.02,
            subtitle,
            transform=ax.transAxes,
            fontsize=11,
            color=BRAND_COLORS["blue_graphite"],
        )


def save_figure(
    fig: plt.Figure,
    filename: str,
    output_dir: str | Path = "reports/figures",
) -> Path:
    """Save a figure using consistent export settings."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / filename

    fig.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight",
        facecolor=fig.get_facecolor(),
    )

    return file_path

import numpy as np


def column_autolabel(ax, total_ratio=None):
    """
    Adds a label to the top of each bar of a barplot. If total_ratio is passed,
    the label will show the ratio between the bar and total_ratio. If not, the
    label will show the value of each bar.

    Parameters
    ----------
    ax : matplotlib.axes object
        ax object to label
    total_ratio : float, default=None
        Number to calculate the ratio to show in the label. If provided,
        the label will show the ratio between the bar and total_ratio. If not,
        the label will show the value of each bar.

    Examples
    --------
    Draw a label on a seaborn plot and label each column with the % that each
    category represent vs the count of all categories:

    >>> fig = plt.figure(figsize = (15,5))
    >>> df = pd.DataFrame({
    ...     'col1': ['cat1', 'cat1', 'cat2'],
    ...     'col2': [1, 2, 3]
    ... })
    >>> ax = sns.countplot(
    ...     data=df,
    ...     x=col1
    ... )
    >>> column_autolabel(ax=ax, total_ratio=df.shape[0])

    """

    ax.set_ylim(top=ax.get_ylim()[1] * 1.025)
    for p in ax.patches:
        height = np.nan_to_num(p.get_height())

        if total_ratio is None:
            ax.text(
                p.get_x() + p.get_width() / 2.0,
                height * 1.02,
                "{:1.0f}".format(height),
                ha="center",
            )

        else:
            ax.text(
                p.get_x() + p.get_width() / 2.0,
                height * 1.02,
                "{:.2%}".format(height / total_ratio),
                ha="center",
            )


def apply_venn_format(plot, ax):
    """
    Applies a blue color scale to venn diagram passed with plot argument, and
    annotates the intesection.
    """
    plot.get_patch_by_id("10").set_color((43 / 255, 123 / 255, 186 / 255))
    plot.get_patch_by_id("11").set_color((219 / 255, 233 / 255, 246 / 255))
    plot.get_patch_by_id("01").set_color((137 / 255, 190 / 255, 220 / 255))

    plot.get_patch_by_id("10").set_alpha(0.9)
    plot.get_patch_by_id("11").set_alpha(0.9)
    plot.get_patch_by_id("01").set_alpha(0.9)

    ax.set_title(
        label="Overlap between unique IDs on users.csv and sessions.csv", fontsize=16
    )
    ax.annotate(
        text="IDs suitable to be\nincluded in the analysis",
        xy=(-0.015, 0.03),
        xytext=(0.65, 0.45),
        fontsize=12,
        arrowprops=dict(
            facecolor="darkslategray",
            edgecolor="darkslategray",
            headwidth=8,
            headlength=20,
            width=2.5,
        ),
    )

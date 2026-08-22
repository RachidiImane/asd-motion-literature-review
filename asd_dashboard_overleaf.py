import matplotlib.pyplot as plt
from matplotlib.patches import (
    FancyBboxPatch, Circle, Rectangle, Polygon
)
from matplotlib.lines import Line2D
import numpy as np


# ============================================================
# DATA
# ============================================================

TOTAL = 36

# A. Movement type
movement_labels = [
    "Gait-related Analysis",
    "Stereotyped Motor Movements (SMMs)",
    "Fine Motor Movements",
    "Hand/Wrist Movements",
    "Gesture Patterns",
    "Other / Whole-body"
]

movement_values = [18, 7, 4, 3, 3, 1]

# B. Methodological approach
# IMPORTANT: corrected total = 36
method_labels = [
    "Traditional / Classical ML",
    "Deep Learning",
    "Hybrid (ML + DL / Transformers, etc.)",
    "Statistical / Validation"
]

method_values = [20, 12, 2, 2]

# C. Learning type
learning_labels = [
    "Supervised Learning",
    "Statistical / Validation"
]

learning_values = [34, 2]

# Performance
performance_labels = ["< 80%", "80–89%", "90–94%", "≥ 95%"]
performance_counts = [2, 9, 9, 13]
performance_pct = [6.1, 27.3, 27.3, 39.4]

average_performance = 90.9


# ============================================================
# COLORS
# ============================================================

BLUE = "#1268C4"
DARK_BLUE = "#073D87"

ORANGE = "#FF6500"

GREEN = "#3E9D4B"
DARK_GREEN = "#00652D"

PURPLE = "#6541B5"
CYAN = "#1193AA"
NAVY = "#2C4C68"
GREY = "#777777"

RED = "#E62621"
YELLOW = "#F4A900"

movement_colors = [
    BLUE,
    ORANGE,
    GREEN,
    PURPLE,
    CYAN,
    NAVY
]

method_colors = [
    ORANGE,
    BLUE,
    GREEN,
    PURPLE
]

learning_colors = [
    GREEN,
    GREY
]

performance_colors = [
    RED,
    YELLOW,
    GREEN,
    BLUE
]


# ============================================================
# BASIC HELPERS
# ============================================================

def pct(v):
    return v / TOTAL * 100


def rounded_box(
    ax,
    x,
    y,
    w,
    h,
    edge,
    face="white",
    lw=1.2,
    radius=0.012
):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.006,rounding_size={radius}",
        transform=ax.transAxes,
        facecolor=face,
        edgecolor=edge,
        linewidth=lw,
        clip_on=False
    )

    ax.add_patch(p)
    return p


def add_header(ax, text, color):

    header = FancyBboxPatch(
        (0.01, 0.94),
        0.98,
        0.055,
        boxstyle="round,pad=0.004,rounding_size=0.008",
        transform=ax.transAxes,
        facecolor=color,
        edgecolor=color
    )

    ax.add_patch(header)

    ax.text(
        0.50,
        0.967,
        text,
        transform=ax.transAxes,
        ha="center",
        va="center",
        color="white",
        fontsize=17,
        fontweight="bold"
    )


# ============================================================
# DONUT WITH EXTERNAL CALLOUTS
# ============================================================

def donut_with_callouts(
    ax,
    values,
    colors,
    outside_indices=None,
    outside_positions=None
):

    if outside_indices is None:
        outside_indices = []

    if outside_positions is None:
        outside_positions = {}

    wedges, _ = ax.pie(
        values,
        startangle=90,
        counterclock=True,
        colors=colors,
        wedgeprops=dict(
            width=0.50,
            edgecolor="white",
            linewidth=1.2
        )
    )

    total = sum(values)

    for i, (wedge, value) in enumerate(zip(wedges, values)):

        percentage = value / total * 100

        theta = np.deg2rad(
            (wedge.theta1 + wedge.theta2) / 2
        )

        # ----------------------------------------------------
        # EXTERNAL percentage + leader line
        # ----------------------------------------------------

        if i in outside_indices:

            # edge point on donut
            x1 = 0.93 * np.cos(theta)
            y1 = 0.93 * np.sin(theta)

            # small extension
            x2 = 1.08 * np.cos(theta)
            y2 = 1.08 * np.sin(theta)

            # custom text position
            if i in outside_positions:
                tx, ty = outside_positions[i]
            else:
                tx = 1.32 * np.cos(theta)
                ty = 1.32 * np.sin(theta)

            # determine elbow direction
            if tx >= 0:
                elbow_x = tx - 0.07
                ha = "left"
            else:
                elbow_x = tx + 0.07
                ha = "right"

            # first diagonal segment
            ax.plot(
                [x1, x2],
                [y1, y2],
                color="black",
                linewidth=1.2
            )

            # horizontal segment
            ax.plot(
                [x2, elbow_x],
                [y2, ty],
                color="black",
                linewidth=1.2
            )

            ax.text(
                tx,
                ty,
                f"{percentage:.1f}%",
                ha=ha,
                va="center",
                fontsize=10,
                fontweight="bold",
                color="black"
            )

        # ----------------------------------------------------
        # INTERNAL percentage
        # ----------------------------------------------------

        else:

            radius = 0.79

            x = radius * np.cos(theta)
            y = radius * np.sin(theta)

            ax.text(
                x,
                y,
                f"{percentage:.1f}%",
                ha="center",
                va="center",
                fontsize=7.6,
                fontweight="bold",
                color="white"
            )

    # center
    ax.text(
        0,
        0,
        "36\nStudies",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        linespacing=1.15
    )

    ax.set_aspect("equal")

    # Extra room for labels
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.25, 1.30)

    ax.axis("off")

# ============================================================
# SPECIAL DONUT C — LEARNING TYPE
# ============================================================

def donut_learning_exact(ax, values, colors):

    # IMPORTANT:
    # clockwise orientation so purple is LEFT of grey
    wedges, _ = ax.pie(
        values,
        startangle=90,
        counterclock=False,
        colors=colors,
        wedgeprops=dict(
            width=0.50,
            edgecolor="white",
            linewidth=1.2
        )
    )

    total = sum(values)

    for i, (wedge, value) in enumerate(zip(wedges, values)):

        percentage = value / total * 100

        theta = np.deg2rad(
            (wedge.theta1 + wedge.theta2) / 2
        )

        # ----------------------------------------------------
        # PURPLE 2.7% — OUTSIDE
        # ----------------------------------------------------
        if i == 1:

            # point inside/edge of purple slice
            x1 = 0.92 * np.cos(theta)
            y1 = 0.92 * np.sin(theta)

            # small elbow outside
            x2 = x1 - 0.10
            y2 = y1 + 0.05

            # short diagonal line
            ax.plot(
                [x1, x2],
                [y1, y2],
                color="black",
                linewidth=1.1
            )

            # short horizontal line to the left
            ax.plot(
                [x2, -0.88],
                [y2, y2],
                color="black",
                linewidth=1.1
            )

            # 2.7% text
            ax.text(
                -0.93,
                y2,
                f"{percentage:.1f}%",
                ha="right",
                va="center",
                fontsize=8.0,
                fontweight="bold",
                color="black"
            )

        # ----------------------------------------------------
        # GREY 5.4% + GREEN 91.9% — INSIDE
        # ----------------------------------------------------
        else:

            radius = 0.79

            x = radius * np.cos(theta)
            y = radius * np.sin(theta)

            ax.text(
                x,
                y,
                f"{percentage:.1f}%",
                ha="center",
                va="center",
                fontsize=7.0,
                fontweight="bold",
                color="white"
            )

    # CENTER
    ax.text(
        0,
        0,
        "36\nStudies",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        linespacing=1.15
    )

    ax.set_aspect("equal")

    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.25, 1.30)

    ax.axis("off")
# ============================================================
# HEADINGS A / B / C
# ============================================================

def heading(ax, x, letter, title, color, total_center):

    circle = Circle(
        (x, 0.885),
        0.028,
        transform=ax.transAxes,
        facecolor=color,
        edgecolor=color
    )

    ax.add_patch(circle)

    ax.text(
        x,
        0.885,
        letter,
        transform=ax.transAxes,
        ha="center",
        va="center",
        color="white",
        fontsize=13,
        fontweight="bold"
    )

    ax.text(
        x + 0.045,
        0.885,
        title,
        transform=ax.transAxes,
        ha="left",
        va="center",
        color=color,
        fontsize=11.3,
        fontweight="bold",
        linespacing=1.05
    )

    ax.text(
        total_center,
        0.842,
        "Total Studies (n = 36)",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold"
    )


# ============================================================
# LEGENDS
# ============================================================

def add_legend(
    ax,
    labels,
    values,
    colors,
    x,
    y,
    width,
    spacing,
    fontsize=6.8
):

    for i, (lab, value, color) in enumerate(
        zip(labels, values, colors)
    ):

        yy = y - i * spacing

        ax.add_patch(
            Rectangle(
                (x, yy - 0.006),
                0.010,
                0.010,
                transform=ax.transAxes,
                facecolor=color,
                edgecolor=color
            )
        )

        ax.text(
            x + 0.016,
            yy,
            lab,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=fontsize
        )

        ax.text(
            x + width,
            yy,
            f"{value} ({pct(value):.1f}%)",
            transform=ax.transAxes,
            ha="right",
            va="center",
            fontsize=fontsize,
            fontweight="bold"
        )


# ============================================================
# ICONS
# ============================================================

def gait_icon(ax, cx, cy, color=BLUE):
    """Compact walking-person icon, drawn in a square inset to avoid distortion."""
    size = 0.082
    iax = ax.inset_axes([cx-size/2, cy-size/2, size, size])
    iax.set_xlim(-1.2, 1.2); iax.set_ylim(-1.2, 1.2)
    iax.set_aspect("equal"); iax.axis("off")

    # head
    iax.add_patch(Circle((0.00, 0.72), 0.20, facecolor=color, edgecolor=color))
    # torso
    iax.plot([0.00, -0.10], [0.48, -0.18], color=color, linewidth=5.2, solid_capstyle="round")
    # arms
    iax.plot([-0.02, -0.52], [0.28, 0.02], color=color, linewidth=4.3, solid_capstyle="round")
    iax.plot([0.00, 0.52], [0.28, 0.10], color=color, linewidth=4.3, solid_capstyle="round")
    # legs
    iax.plot([-0.10, -0.48], [-0.18, -0.82], color=color, linewidth=5.0, solid_capstyle="round")
    iax.plot([-0.10, 0.42], [-0.18, -0.66], color=color, linewidth=5.0, solid_capstyle="round")


def ai_icon(ax, cx, cy, color=ORANGE):
    """Brain icon closer to the reference artwork."""
    size = 0.082
    iax = ax.inset_axes([cx-size/2, cy-size/2, size, size])
    iax.set_xlim(-1.25, 1.25); iax.set_ylim(-1.25, 1.25)
    iax.set_aspect("equal"); iax.axis("off")

    # brain outline built from connected rounded lobes
    lobes = [
        (-0.42, 0.55, 0.30), (-0.68, 0.18, 0.28), (-0.62, -0.25, 0.28), (-0.32, -0.58, 0.28),
        ( 0.42, 0.55, 0.30), ( 0.68, 0.18, 0.28), ( 0.62, -0.25, 0.28), ( 0.32, -0.58, 0.28),
    ]
    for x,y,r in lobes:
        iax.add_patch(Circle((x,y), r, facecolor="none", edgecolor=color, linewidth=2.3))
    iax.plot([0,0],[-0.78,0.82], color=color, linewidth=2.2)
    # inner neural-looking curves
    iax.plot([-0.52,-0.20,-0.42], [0.32,0.12,-0.08], color=color, linewidth=1.6)
    iax.plot([ 0.52, 0.20, 0.42], [0.32,0.12,-0.08], color=color, linewidth=1.6)
    iax.plot([-0.48,-0.18],[-0.38,-0.52], color=color, linewidth=1.5)
    iax.plot([ 0.48, 0.18],[-0.38,-0.52], color=color, linewidth=1.5)


def graduation_icon(ax, cx, cy, color=DARK_GREEN):
    """Graduation-cap icon matching the reference proportions."""
    size = 0.082
    iax = ax.inset_axes([cx-size/2, cy-size/2, size, size])
    iax.set_xlim(-1.25, 1.25); iax.set_ylim(-1.25, 1.25)
    iax.set_aspect("equal"); iax.axis("off")

    cap = Polygon([[-1.02,0.25],[0,0.86],[1.02,0.25],[0,-0.28]], closed=True,
                  facecolor=color, edgecolor=color)
    iax.add_patch(cap)
    iax.add_patch(Polygon([[-0.58,-0.06],[0.58,-0.06],[0.50,-0.60],[-0.50,-0.60]],
                          closed=True, facecolor=color, edgecolor=color))
    iax.plot([0.72,0.84],[0.22,-0.62], color=color, linewidth=2.2)
    iax.add_patch(Circle((0.84,-0.66),0.065,facecolor=color,edgecolor=color))


def target_icon(ax, cx, cy, color=DARK_GREEN):
    """Round target with arrow, close to the reference icon."""
    size = 0.145
    iax = ax.inset_axes([cx-size/2, cy-size/2, size, size])
    iax.set_xlim(-1.28,1.28); iax.set_ylim(-1.28,1.28)
    iax.set_aspect("equal"); iax.axis("off")
    for r in [0.82,0.54,0.27]:
        iax.add_patch(Circle((0,0),r,facecolor="none",edgecolor=color,linewidth=2.5))
    iax.add_patch(Circle((0,0),0.085,facecolor=color,edgecolor=color))
    iax.plot([0.02,0.68],[0.02,0.68],color=color,linewidth=3.1,solid_capstyle="round")
    iax.add_patch(Polygon([[1.03,1.03],[0.50,0.95],[0.60,0.60],[0.94,0.50]],
                          closed=True,facecolor=color,edgecolor=color))


def star_icon(ax, cx, cy, color=DARK_GREEN):
    """Single round star badge."""
    size = 0.074
    iax = ax.inset_axes([cx-size/2, cy-size/2, size, size])
    iax.set_xlim(-1.15,1.15); iax.set_ylim(-1.15,1.15)
    iax.set_aspect("equal"); iax.axis("off")
    iax.add_patch(Circle((0,0),0.90,facecolor="white",edgecolor=color,linewidth=2.0))
    pts=[]
    for k in range(10):
        a=np.deg2rad(90+k*36)
        r=0.56 if k%2==0 else 0.25
        pts.append((r*np.cos(a), r*np.sin(a)))
    iax.add_patch(Polygon(pts,closed=True,facecolor=color,edgecolor=color))


# ============================================================
# FIGURE
# ============================================================

fig = plt.figure(
    figsize=(18, 10),
    facecolor="white"
)

gs = fig.add_gridspec(
    1,
    2,
    width_ratios=[2.42, 1.05],
    left=0.018,
    right=0.982,
    top=0.975,
    bottom=0.035,
    wspace=0.040
)


# ============================================================
# LEFT PANEL
# ============================================================

ax_left = fig.add_subplot(gs[0, 0])
ax_left.axis("off")

rounded_box(
    ax_left,
    0, 0,
    1, 1,
    BLUE
)

add_header(
    ax_left,
    "1. OVERVIEW BY STUDY CHARACTERISTICS (n = 36)",
    DARK_BLUE
)

# separators
for xx in [0.333, 0.666]:

    ax_left.plot(
        [xx, xx],
        [0.22, 0.93],
        transform=ax_left.transAxes,
        linestyle="--",
        linewidth=0.8,
        color="#D5D5D5"
    )


# ============================================================
# TITLES
# ============================================================

heading(
    ax_left,
    0.055,
    "A",
    "MOVEMENT TYPE",
    DARK_BLUE,
    0.168
)

heading(
    ax_left,
    0.385,
    "B",
    "METHODOLOGICAL\nAPPROACH",
    ORANGE,
    0.500
)

heading(
    ax_left,
    0.720,
    "C",
    "LEARNING TYPE",
    DARK_GREEN,
    0.835
)


# ============================================================
# DONUT A
# ============================================================

ax_a = ax_left.inset_axes(
    [0.010, 0.445, 0.315, 0.385]
)

donut_with_callouts(
    ax_a,
    movement_values,
    movement_colors,
    outside_indices=[5],
    outside_positions={
        5: (0.35, 1.15)
    }
)

# ============================================================
# DONUT B
# ============================================================

ax_b = ax_left.inset_axes(
    [0.350, 0.445, 0.315, 0.385]
)

# Hybrid 5.4 and Statistical 5.4 outside
donut_with_callouts(
    ax_b,
    method_values,
    method_colors,
    outside_indices=[],
    outside_positions={}
)


# ============================================================
# DONUT C
# ============================================================

ax_c = ax_left.inset_axes(
    [0.674, 0.445, 0.315, 0.385]
)

donut_with_callouts(
    ax_c,
    learning_values,
    learning_colors
)

# ============================================================
# LEGENDS
# ============================================================

add_legend(
    ax_left,
    movement_labels,
    movement_values,
    movement_colors,
    0.025,
    0.415,
    0.285,
    0.030,
    8.5
)

add_legend(
    ax_left,
    method_labels,
    method_values,
    method_colors,
    0.355,
    0.415,
    0.285,
    0.038,
    8.5
)

add_legend(
    ax_left,
    learning_labels,
    learning_values,
    learning_colors,
    0.685,
    0.390,
    0.285,
    0.045,
    8.5
)


# BOX 1
rounded_box(
    ax_left,
    0.025,
    0.045,
    0.295,
    0.145,
    BLUE
)

ax_left.add_patch(
    Circle(
        (0.090, 0.118),
        0.044,
        transform=ax_left.transAxes,
        facecolor="white",
        edgecolor=BLUE,
        linewidth=1.2
    )
)

gait_icon(
    ax_left,
    0.090,
    0.118
)

ax_left.text(
    0.150,
    0.118,
    "Gait analysis is the most\n"
    "frequently investigated\n"
    "movement type, covering\n"
    "nearly half of the included\n"
    "studies (50.0%).",
    transform=ax_left.transAxes,
    ha="left",
    va="center",
    fontsize=7.0,
    fontweight="bold",
    color=DARK_BLUE,
    linespacing=1.30
)


# BOX 2
rounded_box(
    ax_left,
    0.350,
    0.045,
    0.295,
    0.145,
    ORANGE
)

ax_left.add_patch(
    Circle(
        (0.410, 0.118),
        0.044,
        transform=ax_left.transAxes,
        facecolor="white",
        edgecolor=ORANGE,
        linewidth=1.2
    )
)

ai_icon(
    ax_left,
    0.410,
    0.118
)

ax_left.text(
    0.470,
    0.118,
    "Traditional machine learning\n"
    "approaches remain the most\n"
    "commonly used (55.6%),\n"
    "followed by deep learning\n"
    "methods (33.3%).",
    transform=ax_left.transAxes,
    ha="left",
    va="center",
    fontsize=7.4,
    fontweight="bold",
    color=ORANGE,
    linespacing=1.30
)


# BOX 3
rounded_box(
    ax_left,
    0.675,
    0.045,
    0.295,
    0.145,
    DARK_GREEN
)

ax_left.add_patch(
    Circle(
        (0.730, 0.118),
        0.044,
        transform=ax_left.transAxes,
        facecolor="white",
        edgecolor=DARK_GREEN,
        linewidth=1.2
    )
)

graduation_icon(
    ax_left,
    0.730,
    0.118
)

ax_left.text(
    0.790,
    0.118,
    "Supervised learning\n"
    "is dominant in the\n"
    "literature (94.4%).",
    transform=ax_left.transAxes,
    ha="left",
    va="center",
    fontsize=7.9,
    fontweight="bold",
    color=DARK_GREEN,
    linespacing=1.35
)
# ============================================================
# RIGHT PANEL
# ============================================================

ax_right = fig.add_subplot(gs[0, 1])
ax_right.axis("off")

rounded_box(
    ax_right,
    0, 0,
    1, 1,
    DARK_GREEN
)

add_header(
    ax_right,
    "2. PERFORMANCE SUMMARY",
    DARK_GREEN
)


# ============================================================
# AVERAGE PERFORMANCE
# ============================================================

rounded_box(
    ax_right,
    0.055,
    0.790,
    0.890,
    0.125,
    "#BFD9C4",
    "#FBFDFB",
    0.9
)

target_icon(
    ax_right,
    0.180,
    0.852
)

ax_right.text(
    0.615,
    0.875,
    "AVERAGE PERFORMANCE\n(ACCURACY OR EQUIVALENT)",
    transform=ax_right.transAxes,
    ha="center",
    va="center",
    fontsize=7.5,
    fontweight="bold",
    color=DARK_GREEN
)

ax_right.text(
    0.615,
    0.837,
    "90.9%",
    transform=ax_right.transAxes,
    ha="center",
    va="center",
    fontsize=21,
    fontweight="bold",
    color=DARK_GREEN
)

ax_right.text(
    0.615,
    0.807,
    "(Based on 33 studies reporting percentage-based performance)",
    transform=ax_right.transAxes,
    ha="center",
    va="center",
    fontsize=7.0
)


# ============================================================
# PERFORMANCE BAR CHART
# ============================================================

rounded_box(
    ax_right,
    0.055,
    0.405,
    0.890,
    0.350,
    "#BFD9C4",
    "#FBFDFB",
    0.9
)

ax_right.text(
    0.50,
    0.726,
   "PERFORMANCE DISTRIBUTION\n(BY PERCENTAGE-BASED METRICS)",
    transform=ax_right.transAxes,
    ha="center",
    va="center",
    fontsize=9.3,
    fontweight="bold",
    color=DARK_GREEN
)

ax_bar = ax_right.inset_axes(
    [0.165, 0.465, 0.720, 0.225]
)

x = np.arange(4)

bars = ax_bar.bar(
    x,
    performance_counts,
    width=0.55,
    color=performance_colors
)

ax_bar.set_ylim(0, 20)
ax_bar.set_yticks([0, 5, 10, 15, 20])

ax_bar.set_xticks(x)
ax_bar.set_xticklabels(
    performance_labels,
    fontsize=8
)

ax_bar.set_ylabel(
    "Number of Studies",
    fontsize=9
)

ax_bar.set_xlabel(
    "Performance Range",
    fontsize=9
)

ax_bar.grid(
    axis="y",
    linestyle="--",
    alpha=0.30
)

ax_bar.spines["top"].set_visible(False)
ax_bar.spines["right"].set_visible(False)

for bar, value in zip(
    bars,
    performance_counts
):

    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.45,
        str(value),
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )


# ============================================================
# ACCURACY TABLE
# ============================================================

rounded_box(
    ax_right,
    0.055,
    0.175,
    0.890,
    0.205,
    "#BFD9C4",
    "#FBFDFB",
    0.9
)

ax_right.text(
    0.50,
    0.355,
    "PERFORMANCE RANGE SUMMARY (n = 33)",
    transform=ax_right.transAxes,
    ha="center",
    va="center",
    fontsize=9.2,
    fontweight="bold",
    color=DARK_GREEN
)

ax_right.text(
    0.105,
    0.316,
    "Performance Range",
    transform=ax_right.transAxes,
    fontsize=7.2,
    fontweight="bold",
    color=DARK_GREEN
)

ax_right.text(
    0.545,
    0.316,
    "Number of Studies",
    transform=ax_right.transAxes,
    fontsize=7.2,
    fontweight="bold",
    color=DARK_GREEN,
    ha="center"
)

ax_right.text(
    0.83,
    0.316,
    "Percentage",
    transform=ax_right.transAxes,
    fontsize=7.2,
    fontweight="bold",
    color=DARK_GREEN,
    ha="center"
)

ys = [
    0.282,
    0.250,
    0.218,
    0.186
]

for i, yy in enumerate(ys):

    ax_right.add_patch(
        Rectangle(
            (0.105, yy - 0.009),
            0.023,
            0.018,
            transform=ax_right.transAxes,
            facecolor=performance_colors[i],
            edgecolor=performance_colors[i]
        )
    )

    ax_right.text(
        0.145,
        yy,
        performance_labels[i],
        transform=ax_right.transAxes,
        va="center",
        fontsize=7.4
    )

    ax_right.text(
        0.545,
        yy,
        str(performance_counts[i]),
        transform=ax_right.transAxes,
        ha="center",
        va="center",
        fontsize=7.4
    )

    ax_right.text(
        0.83,
        yy,
        f"{performance_pct[i]:.1f}%",
        transform=ax_right.transAxes,
        ha="center",
        va="center",
        fontsize=7.4
    )


# ============================================================
# FINAL BOX
# ============================================================

rounded_box(
    ax_right,
    0.055,
    0.030,
    0.890,
    0.112,
    "#BFD9C4",
    "#FBFDFB",
    0.9
)

star_icon(
    ax_right,
    0.150,
    0.085
)

ax_right.text(
    0.225,
    0.085,
    "More than one-third of the studies (39.4%) report high\n"
    "performance (≥95%), highlighting the\n"
    "potential of AI methods for movement-based\n"
    "ASD analysis.",
    transform=ax_right.transAxes,
    ha="left",
    va="center",
    fontsize=7.4,
    fontweight="bold",
    color=DARK_GREEN,
    linespacing=1.35
)


# ============================================================
# SAVE
# ============================================================

plt.savefig(
    "/Users/imanerachidi/Downloads/asd_dashboard_overleaf_36.pdf",
    bbox_inches="tight",
    dpi=300
)

plt.savefig(
    "/Users/imanerachidi/Downloads/asd_dashboard_overleaf_36.png",
    bbox_inches="tight",
    dpi=300
)
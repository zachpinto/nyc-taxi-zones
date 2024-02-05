import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def create_very_small_color_spectrum_image():
    passenger_counts = ['> 1000', '> 500', '> 250', '> 100', '> 50', '> 25', '≤ 25']
    colors = ['#ffaf08', '#f7b731', '#f5c767', '#f5d084', '#f2d8a2', '#f7e9cb', '#ffffff']

    fig, ax = plt.subplots(figsize=(0.5, 1))  # Even more reduced figure size
    for i, (count, color) in enumerate(zip(passenger_counts, colors)):
        rect = mpatches.Rectangle((0, i), 1, 1, color=color)
        ax.add_patch(rect)
        ax.text(1.5, i + 0.5, count, va='center', fontsize=4)  # Further reduced font size

    ax.set_xlim(0, 3)
    ax.set_ylim(0, len(passenger_counts))
    ax.axis('off')
    plt.tight_layout()

    # Save with a transparent background
    plt.savefig('/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/color_spectrum_transparent.png', dpi=300, bbox_inches='tight', transparent=True)
    plt.close()


create_very_small_color_spectrum_image()

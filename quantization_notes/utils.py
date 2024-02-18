import numpy as np
import matplotlib.pyplot as plt


def format_float(value, precision=3):
    """
    Format a floating-point number to show significant digits
    while removing trailing zeroes after the decimal point.
    """
    formatted_value = f"{value:.{precision}f}"  # Format with fixed-point representation
    if "." in formatted_value:
        formatted_value = formatted_value.rstrip("0").rstrip(
            "."
        )  # Remove trailing zeroes and decimal point if it's the last character
    return formatted_value


def plot_table(data, filename, cmap_background, grid_color, text_color):
    # Define the dimensions of the table
    rows, columns = data.shape

    # Plot the table with uniform background color for all cells
    plt.figure(figsize=(rows, columns))
    plt.imshow([[1]], cmap=cmap_background, aspect="auto", extent=(0, columns, 0, rows))

    # Draw gridlines
    for i in range(1, rows + 1):
        plt.axhline(y=i, color=grid_color, linewidth=1)  # Horizontal lines
    for j in range(1, columns + 1):
        plt.axvline(x=j, color=grid_color, linewidth=1)  # Vertical lines

    # Display numbers in the cells with specified text color
    for i in range(rows):
        for j in range(columns):
            cell_value = data[i, j]
            plt.text(
                j + 0.5,
                i + 0.5,
                format_float(cell_value),
                ha="center",
                va="center",
                color=text_color,
            )  # Setting text color

    plt.gca().invert_yaxis()  # Invert y-axis to start from top-left

    # Hide axes
    plt.axis("off")

    # Save the plot as a PNG image
    plt.savefig(filename, bbox_inches="tight", pad_inches=0)

    plt.show()

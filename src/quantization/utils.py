import numpy as np
import matplotlib.pyplot as plt
import os


def plot_table(data, filename, cmap_background, grid_color, text_color):
    # Define the dimensions of the table
    rows, columns = data.shape

    # Plot the table with uniform background color for all cells
    plt.figure(figsize=(rows, columns))
    plt.imshow(
        [[1]], cmap=cmap_background, aspect="auto", extent=(0, columns, 0, rows)
    )  # Uniform background color

    # Draw gridlines
    for i in range(1, rows + 1):
        plt.axhline(y=i, color=grid_color, linewidth=0.5)  # Horizontal lines
    for j in range(1, columns + 1):
        plt.axvline(x=j, color=grid_color, linewidth=0.5)  # Vertical lines

    # Display numbers in the cells with specified text color
    for i in range(rows):
        for j in range(columns):
            cell_value = data[i, j]
            plt.text(
                j + 0.5,
                i + 0.5,
                f"{cell_value:2.3f}",
                ha="center",
                va="center",
                color=text_color,
            )  # Setting text color

    # Hide axes
    plt.axis("off")

    # Save the plot as a PNG image
    plt.savefig(filename, bbox_inches="tight", pad_inches=0)

    plt.show()


os.makedirs("output", exist_ok=True)

# Example usage
# data = np.random.uniform(-1000, 1000, size=(3, 3))  # Random data
data = np.array(
    [
        [673.46100787, 65.88205512, 139.08433858],
        [929.669, -695.42169291, -849.14648819],
        [505.09575591, 21.96068504, -292.80913386],
    ]
)
plot_table(data, "output/random-table.png", "Oranges", "black", "black")

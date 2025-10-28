"""
data_visualizer.py
Author: Sparsh Gupta
Purpose: A simple Python script to visualize data using matplotlib.
Hacktoberfest Contribution
"""

import matplotlib.pyplot as plt
import numpy as np


def generate_data():
    """Generate random data for visualization"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)
    return x, y


def visualize_data(x, y):
    """Plot the generated data"""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="Sine Wave with Noise", linewidth=2)
    plt.title("Data Visualization Example", fontsize=14)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x_data, y_data = generate_data()
    visualize_data(x_data, y_data)

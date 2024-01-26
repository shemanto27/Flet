import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    # Create a Matplotlib figure and axis
    fig1, ax = plt.subplots()
    x = np.arange(11)
    y = x**2
    ax.plot(x,y,"g--")
    
    page.add(
        MatplotlibChart(fig1, expand = True, original_size = True)
    )
    


ft.app(target=main)

"""In Matplotlib, when you want to create a plot, 
    you typically start by creating a figure and an axis. 
    The figure is like a blank canvas, and the axis is the area where you'll 
    actually draw your plot. Here's a breakdown:

    1) plt.subplots(): This function is used to create a new figure and axis. 
    It returns two objects - a figure (fig) and an axis (ax). 
    Think of the figure as the entire window or canvas, 
    and the axis as the area inside the window where you'll draw your plot.
    
    2)ax.plot(x, y, "g--"): Now that you have a figure and an axis, 
    you can use the plot method of the axis (ax) to draw a plot on it. 
    In your case, you're plotting x against y with a green dashed line ("g--").
    
    3)This line essentially tells Matplotlib to draw 
    a plot of x and y on the axis ax with a green dashed line.
    MatplotlibChart(fig, expand=True): Finally, you use the MatplotlibChart 
    class to convert your Matplotlib figure (fig) into a format that can be 
    used by the Flet library. This step is necessary to integrate Matplotlib 
    plots into the Flet app.
    
    4)The expand=True argument is used to ensure that 
    the Matplotlib plot takes up the entire available space in the Flet app."""
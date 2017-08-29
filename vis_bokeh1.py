# Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider
from numpy.random import random
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import numpy as np

N = 300
x = random(N)
y = random(N)

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x':x, 'y':y})

# Add a line to the plot
plot = figure()
plot.x('x', 'y', source=source)

# Create a slider: slider
slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)

# Add the layout to the current document
curdoc().add_root(layout)

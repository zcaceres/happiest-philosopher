import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools
plotly.tools.set_credentials_file(username="YOUR USERNAME HERE ", api_key='YOUR API KEY HERE')

"""
        HANDLES ALL GRAPH-RELATED TASKS
"""


# Formats name strings from directory name (author name) and file name (work name)
def format_x_val_names(work_names, author_names):
    formatted_names = []
    counter = 0
    for work in work_names:
        work = "{0} – {1}".format(author_names[counter], work[:-4])
        formatted_names.append(work)
        counter += 1
    return formatted_names

# Converts values into lists ready for plotting
def convert_data_for_plotting(work_names, polarity_vals, subjectivity_vals):
    x_vars = []
    y_vars = []
    y2_vars = []
    for work in work_names:
        x_vars.append(work)
    for p_val in polarity_vals:
        y_vars.append(p_val)
    for s_val in subjectivity_vals:
        y2_vars.append(s_val)
    print("X_Vars has length {0}".format(len(x_vars)))
    print("Y_Vars has length {0}".format(len(y_vars)))
    print("Y2_Vars has length {0}".format(len(y2_vars)))
    create_graphs(x_vars, y_vars, y2_vars)

# Creates two graphs, one for polarity and one for subjectivity
def create_graphs(x_vals, y_vals, y2_vals):
    trace = go.Scatter(
        x= x_vals,
        y= y_vals,
        textposition='top center',
        mode='markers+text',
    )
    data = [trace]
    layout = go.Layout(
        title="Polarity of Philosophical Works"
    )
    figure = go.Figure(data=data, layout=layout)
    py.plot(figure, filename='happiest-philosopher-polarity')

    # Generate second graph
    trace2 = go.Scatter(
        x=x_vals,
        y=y2_vals,
        textposition='top center',
        mode='markers+text',
    )
    data2 = [trace2]
    layout = go.Layout(
        title="Subjectivity of Philosophical Works"
    )
    figure = go.Figure(data=data2, layout=layout)
    py.plot(figure, filename='happiest-philosopher-subjectivity')

import networkx 
import pandas
import matplotlib.pyplot as plt
from matplotlib import cm

print('running')
# Here, I'm going to create a pandas dataframe with example data
def create_df():
    return pandas.DataFrame(
        # Naming the nodes A,B,C,D, and E
        {'node_name':['A','B','C','D','E'],
         # Edges refers to which nodes each node is connected to
         'edges':[
             ['B'],
             ['A','C','D'],
             ['B','D','E'],
             ['B','C'],
             ['C']
             ]},
        # Index number can be used instead of name for any node
         )

def create_graph(nodes_df):
    # First, we must create a graph object
    graph = networkx.Graph()
    # Then we can add nodes to the graph
    # Use [graph.add_node()] to add nodes one at a time. Maybe add to for loop?
    # Or, use [graph.add_nodes_from()] to add all the nodes in a list!
    graph.add_nodes_from(nodes_df.node_name) 
    # Now it's time to add the connections between the nodes
    for row in nodes_df.iterrows(): #<- Pandas iterrows returns iterable list of tuples
        # Here, [row] is a tuple: ('index', pd.Series)
        # We can iterate over every neighbor in the series like this...
        for neighbor in row[1].edges:
            # Adding an edge for every neighbor
            graph.add_edge(row[1].node_name, neighbor)
    # Returning graph
    return graph


if __name__ == '__main__':
    # Creating the pandas dataframe
    nodes = create_df()
    # Creating the networkx graph
    display = create_graph(nodes)
    
    # Creating a matplotlib figure and axis
    fig, axis = plt.subplots()

    # [draw_networkx] can be used to add additional features
    networkx.drawing.nx_pylab.draw_networkx(display,
                                            # Forcing nodes to locations
                                            pos={'A':(1,1),'B':(1,2),'C':(2,2),'D':(2,1),'E':(4,4)},
                                            # Changing the size of the nodes, default=300
                                            node_size = 750,
                                            # Changing node to a pentagon shape
                                            node_shape = 'p',
                                            # Changing node colors, default=’#1f78b4’, must have same number as nodes
                                            node_color = ['b','g','y','brown','r'],
                                            # Changing edge width, default = 1
                                            width = 5,
                                            # Changing font color, default = 'k' for black
                                            font_color = 'w',
                                            # Changing font size, default = 12
                                            font_size = 8,
                                            # I'm going to add this drawing to the matplotlib axis we created above
                                            # This is because matplotlib has many more features for graph drawing
                                            # Networkx is only inteded for designing graphs, not displaying them,
                                            # and the ability to display with networkx is likely to be depreciated soon
                                            ax = axis
                                            )

    # Now we can change our graph a bunch using matplotlib! Hurray!!!
    fig.suptitle('Here is a title!', fontsize=16)
    # These lims change the x and y limits, basically zooms out or in.
    axis.set_xlim(0,5)
    axis.set_ylim(0,5)
    #
    axis.set_xlabel('Here is a handy label', fontsize=8)
    axis.set_ylabel('Here is another handy label', fontsize=8, color='y')
    # You can add all sorts of features with matplotlib
    axis.text(3.5,3, 'This is a red node', color='r')
    # Google for more ideas!

    # This will display the plot
    plt.show(fig)
    input('done?')
    # All matplotlib figures will remain open in the background of your computer,
    # and bog down your system. Make sure to close them all before making more!
    plt.close('all')

    # OR save them with the savefig method.







import pickle
import streamlit as st
import pandas as pd
import networkx as nx

# Set the page configuration to change the tab title and favicon
st.set_page_config(
    page_title="DMS / DAA EL Phase II",
    page_icon="https://rvce.edu.in/sites/default/files/logo_new.png"  # Favicon URL
)

# Custom styling for the Streamlit app
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1483375801503-374c5f660610?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.0);
    background-color: rgba(0,0,0,0.0);
}
h1{
    color: black; /* Change title color to black */
}
table{
    background-color: #FFFFFF;

    text-align: center;
}
.stDataFrame {
    background-color: white; /* Set table background color to white */
    color: white; /* Set text color to white */
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Flight Netowrk Analysis Using Graph Theory")
st.title("By - Aditya Sharma, Aryan Chaturvedi, Mehar Kulkarni, Tanisha Agarwal")

# Load data with error handling
def load_pickle(file_name):
    try:
        with open(file_name, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading {file_name}: {e}")
        return None

airport = load_pickle('airport.pkl')
nod = load_pickle('graph.pkl')
airportname = load_pickle('airport_code.pkl')
statename = load_pickle('state_code.pkl')
nearairport = load_pickle('nearairport.pkl')

if nod is None or airport is None or airportname is None or statename is None or nearairport is None:
    st.stop()

# Ensure `nod` is a NetworkX graph
if not isinstance(nod, (nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph)):
    st.error("Loaded graph is not a recognized NetworkX graph type.")
    st.stop()

# Print number of Airports and Flights
st.header("Number Of Airports: ")
st.write(nod.number_of_nodes())
st.header("Number Of Flights: ")
st.write(nod.number_of_edges())

# Listing busiest Airports
st.header("Busiest Airports ")
air1 = st.slider('Enter The No Of Airports Required', 0, 130, 25)
if st.button('Find Stations'):
    l = list(nod.degree(list(nod.nodes())))
    l.sort(key=lambda x: x[1], reverse=True)
    busy = l[:air1]
    bstation = pd.DataFrame(busy, columns=['Airports', 'No Of Flights'])
    st.table(bstation)

# Centrality Measure Calculation
G2 = nx.Graph(nod)  # Ensure conversion to a standard Graph
st.header("Centrality Measure Calculation")
centrality = st.selectbox('Select Centrality Type', ('Degree Centrality', 'Closeness Centrality', 'Betweenness Centrality', 'Eigenvector Centrality'))
if st.button('Calculate'):
    if centrality == 'Degree Centrality':
        st.write("Degree Centrality: ", nx.degree_centrality(nod))
    elif centrality == 'Closeness Centrality':
        st.write("Closeness Centrality: ", nx.closeness_centrality(nod))
    elif centrality == 'Betweenness Centrality':
        st.write("Betweenness Centrality: ", nx.betweenness_centrality(nod))
    elif centrality == 'Eigenvector Centrality':
        st.write("Eigenvector Centrality: ", nx.eigenvector_centrality(G2))

# Shortest Path Calculation
st.header("Shortest Path Calculation For Flight Route")
option1 = st.selectbox('Select Source Airport', airportname.values())
option2 = st.selectbox('Select Destination Airport', airportname.values())

if st.button('Find Route'):
    try:
        source = [i for i in airportname if airportname[i] == option1]
        target = [i for i in airportname if airportname[i] == option2]

        if not source or not target:
            st.error(f"Selected airports are not found in the airport code mapping.")
            st.stop()

        source = source[0]
        target = target[0]

        if source not in nod:
            st.error(f"Source airport {option1} ({source}) not found in the graph.")
        elif target not in nod:
            st.error(f"Target airport {option2} ({target}) not found in the graph.")
        else:
            p = nx.shortest_path(nod, source=source, target=target, weight="l")
            q = nx.shortest_path_length(nod, source=source, target=target, weight="l")
            st.write("Route Found")
            st.write("Route is:")
            shrt_path = pd.DataFrame(p, columns=['Airport'])
            st.table(shrt_path)
            st.write('Distance traveled is: ', q, 'km')
    except nx.NetworkXNoPath:
        st.error("No path found between the selected airports.")
    except Exception as e:
        st.error(f"Error finding route: {e}")

# Articulation Points Calculation
st.header("Articulation Points Calculation")
if st.button('Calculate Articulation Points'):
    try:
        articulation_points = list(nx.articulation_points(G2))
        st.write("Articulation Points: ", articulation_points)
        st.write("Number of Articulation Points: ", len(articulation_points))
    except Exception as e:
        st.error(f"Error calculating articulation points: {e}")

# Efficiency Calculation
st.header("Efficiency Calculation")
if st.button('Calculate Global Efficiency'):
    try:
        efficiency = nx.global_efficiency(G2)
        st.write("Global Efficiency: ", efficiency)
    except Exception as e:
        st.error(f"Error calculating global efficiency: {e}")

su1 = st.selectbox('Select Source Airport:', airport)
des1 = st.selectbox('Select Destination1 Airport:', airport)
des2 = st.selectbox('Select Destination2 Airport:', airport)
if st.button('Calculate Efficiency'):
    try:
        efficiency1 = nx.efficiency(G2, su1, des1)
        efficiency2 = nx.efficiency(G2, su1, des2)
        st.write("Efficiency from Source to Destination1: ", efficiency1)
        st.write("Efficiency from Source to Destination2: ", efficiency2)
    except Exception as e:
        st.error(f"Error calculating efficiency: {e}")

# Stations In A State
st.header("Find Airports In A State")
option = st.selectbox('Select State', statename.values())
if st.button('Find Airports:'):
    try:
        temp = {airportname[z]: nod.degree(z) for z in statename if statename[z] == option}
        temp = {k: v for k, v in temp.items() if isinstance(v, int)}
        temp = {k: v for k, v in sorted(temp.items(), key=lambda item: item[1], reverse=True)}
        st.write("Airports Found")
        st.write("Airports are:")
        st.write(temp)
    except Exception as e:
        st.error(f"Error finding airports in state: {e}")

# Airports within a distance from a particular airport
st.header("Find Airports Nearer From A Particular Airport")
option8 = st.selectbox('Select Airport', airportname.values())
dist = st.slider('Enter The Number Of Airports', 0, 20, 5)
if st.button('Find Airports Nearer:'):
    try:
        n = nearairport[[i for i in airportname if airportname[i] == option8][0]].sort_values().head(dist)
        n = n.to_dict()
        blank = {i: int(n[i][0]) for i in n}
        state_airport = pd.DataFrame.from_dict(blank, orient='index', columns=['No Of Flights'])
        st.write("Airports Found")
        st.write("Airports are:")
        st.markdown('<style>.stDataFrame { background-color: white; color: white; }</style>', unsafe_allow_html=True)
        st.table(state_airport)
    except Exception as e:
        st.error(f"Error finding nearer airports: {e}")


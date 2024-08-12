# Flight Network Analysis using Graph Theory


## Overview

The **Flight Network Analysis using Graph Theory** project uses Python to visualize and analyze network data related to airports and flight routes. This repository includes tools for exploring various aspects of the flight network using graph theory concepts, such as centrality measures, shortest paths, and articulation points.

The main script, `flight.py`, leverages Streamlit for an interactive web application and NetworkX for graph analysis.

## Features

- **Visualize Flight Network:** Display the number of airports and flights.
- **Busiest Airports:** Identify and list the busiest airports.
- **Centrality Measures:** Calculate different centrality metrics for nodes in the network.
- **Shortest Path:** Find the shortest flight route between two airports.
- **Articulation Points:** Identify articulation points in the network.
- **Efficiency Calculation:** Compute global and pairwise efficiencies of the network.
- **State-wise Airports:** Find airports located in a particular state.
- **Nearby Airports:** Identify airports within a specific distance from a given airport.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mehark56/FlightNetworkAnalysis.git
    cd FlightNetworkAnalysis
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should include the necessary packages:

    ```
    streamlit
    pandas
    networkx
    ```

## Usage

1. **Prepare the data:**

    Ensure the following pickle files are present in the directory:
    - `airport.pkl`
    - `graph.pkl`
    - `airport_code.pkl`
    - `state_code.pkl`
    - `nearairport.pkl`

2. **Run the Streamlit application:**

    ```bash
    streamlit run flight.py
    ```

3. **Interact with the application:**

    Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser. You can then use the interface to analyze the flight network according to the features listed above.

## Data Files

- **`airport.pkl`**: Contains information about airports.
- **`graph.pkl`**: Contains the graph object representing the flight network.
- **`airport_code.pkl`**: Maps airport codes to their full names.
- **`state_code.pkl`**: Maps airport codes to state names.
- **`nearairport.pkl`**: Contains information about nearby airports.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Streamlit**: For creating the interactive web application framework.
- **NetworkX**: For providing tools to analyze and visualize complex networks.
- **Unsplash**: For the background image used in the Streamlit app.




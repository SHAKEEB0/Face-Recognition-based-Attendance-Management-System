import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk  # Optional for advanced map visualization

# ----------------------------
# 🎉 Streamlit App Title
# ----------------------------
st.title('🌍 Face Recognition-based Attendance Management System')
st.header('Random Geographical Data Visualization')

# ----------------------------
# 🎉 User Input for Number of Points
# ----------------------------
num_points = st.slider('Select the number of random points to generate:', min_value=100, max_value=1000, value=500, step=50)

# ----------------------------
# 📍 Generate Random Geographical Data
# ----------------------------
df = pd.DataFrame(
    np.random.randn(num_points, 2) / [50, 50] + [37.76, -122.4],  # Random points centered around San Francisco
    columns=['lat', 'lon']
)

st.subheader('Generated Data (first 5 rows)')
st.dataframe(df.head())  # Display the first 5 rows of the DataFrame

# ----------------------------
# 🌐 Simple Map View (Streamlit's Default Map)
# ----------------------------
st.subheader('Simple Map View')
st.map(df)  # Displays the points on the map

# ----------------------------
# 🚀 Advanced Map View (Using PyDeck)
# ----------------------------
st.subheader('Advanced Map View (with Custom Viewport)')
view_state = pdk.ViewState(
    latitude=37.76, 
    longitude=-122.4, 
    zoom=12, 
    pitch=50
)

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[lon, lat]',
    get_radius=200,
    get_fill_color=[255, 0, 0],  # Red color points
)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(deck)

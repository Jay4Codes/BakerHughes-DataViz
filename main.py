import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
import pydeck as pdk
import leafmap.foliumap as leafmap
import os

st.set_page_config(
    page_title="Gas Turbine Baker Hughes",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

site_df = pd.read_csv(
    './data/site_metadata-7fc535965d0c074cea0be6786fc9518e.csv')

st.sidebar.title('Gas Turbine Baker Hughes')
rad1 = st.sidebar.radio("Navigation", ["Plant Locations", "Customer Plants",
                        "Elevation", "Thermal Efficiency", "N2 Emmission", "Operational Hours"])

if rad1 == "Plant Locations":
    st.title('Gas Turbine Baker Hughes')

    st.subheader('Locate Plants')

    site_df = pd.read_csv(
        './data/site_metadata-7fc535965d0c074cea0be6786fc9518e.csv')

    m = folium.Map(location=[site_df['LATITUDE'].mean(
    ), site_df['LONGITUDE'].mean()], zoom_start=4, control_scale=True)
    for index, location_info in site_df.iterrows():
        folium.Marker([location_info["LATITUDE"], location_info["LONGITUDE"]],
                      popup=location_info["PLANT_NAME"]).add_to(m)

    folium_static(m)

if rad1 == "Customer Plants":
    st.title('Gas Turbine Baker Hughes')

    st.subheader('Customer Plants Numbers')

    values = site_df['CUSTOMER_NAME'].value_counts().to_dict()

    chart_data = pd.DataFrame(list(values.values()), list(values.keys()))

    st.bar_chart(chart_data)

if rad1 == "Elevation":
    st.title('Gas Turbine Baker Hughes')

    st.subheader('Plant Elevations')

    ele_df = pd.DataFrame(
        np.random.randn(40, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=ele_df,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=ele_df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

if rad1 == "Thermal Efficiency":
    st.title('Gas Turbine Baker Hughes')

    st.subheader('Thermal Efficiency')

    downloaded_data_list_1 = os.listdir('data/PLANTS')
    plant_names = []
    for file in downloaded_data_list_1:
        plant_names.append(file[:-4])

    selected_plant = st.selectbox('Plant Names', plant_names)

    plant_df = pd.read_csv(f'./data/PLANTS/{selected_plant}.csv')

    line_date = pd.DataFrame(plant_df['THERMAL_EFF'])

    line_df = plant_df['THERMAL_EFF']

    intervals = ('Daily', 'Weekly', 'Monthly', 'Quaterly')
    input = st.selectbox('Interval', intervals)

    if input == 'Daily':
        interval = '1d'
    elif input == 'Weekly':
        interval = '1wk'
    elif input == 'Monthly':
        interval = '1mo'
    elif input == 'Quaterly':
        interval = '3mo'
    else:
        interval = '1d'

    input_months = None
    input_months = st.number_input(
        'Enter No of previous Months Historical Data', min_value=0, max_value=12, value=0, step=1)

    st.area_chart(line_df)

if rad1 == "N2 Emmission":
    m = leafmap.Map(tiles="stamentoner")
    st.title('Gas Turbine Baker Hughes')

    st.subheader('N2 Emmission')

    heat_map_df = site_df[['LATITUDE', 'LONGITUDE', 'FUEL_N2_MOL_PCT']]

    m.add_heatmap(
        heat_map_df,
        latitude="LATITUDE",
        longitude="LONGITUDE",
        value="FUEL_N2_MOL_PCT",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=500)

if rad1 == "Operational Hours":

    st.title('Gas Turbine Baker Hughes')

    st.subheader('Operational Hours')

    st.write("ABORIGINAL-PICULET - 3243 hours")

    st.write("SPIRITUAL-POLECAT - 2846 hours")

    st.write("PREHISTORIC-PETREL - 4395 hours")

    st.write("BIPEDAL-UAKARI - 4536hours")

    st.write("TOURMALINE-MOUSE - 3452 hours")

    st.write("LUSH-CHIPMUNK - 2468 hours")

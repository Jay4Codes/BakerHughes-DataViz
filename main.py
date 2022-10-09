import numpy as np
import pandas as pd
import datetime
import streamlit as st
from streamlit_folium import folium_static
import folium

st.set_page_config(
    page_title="Gas Turbine Baker Hughes",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title('Gas Turbine Baker Hughes')
rad1 = st.sidebar.radio("Navigation", ["Home", "Profile", "About-Us"])

if rad1 == "Home":

    st.title('Gas Turbine Baker Hughes')
    selected_stock = st.text_input('Enter Your Plant Name')
    stocks = ('')
    selected_stock = st.selectbox('Plant Names', stocks)

    n_years = st.slider('Years of historical data:', 1, 10)
    period = n_years * 365

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

    if input_months == 0:
        START = (datetime.date.today() - datetime.timedelta(period))
    else:
        START = datetime.date.today() - datetime.timedelta(30*(input_months))
    TODAY = datetime.date.today() + datetime.timedelta(7)

    st.subheader('Raw Data')

    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # st.table(data.tail())

    # def plot_raw_data():
    #     fig = go.Figure()
    #     fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    #     fig.layout.update(title_text=selected_stock, xaxis_rangeslider_visible=True)
    #     st.plotly_chart(fig)

    # plot_raw_data()

    # df = data.copy()

    # df.reset_index(inplace=True)

    # x_future = np.array(df.Close.rolling(7).mean()[-7:])

    # scale = max(x_future) - min(x_future)
    # minimum = min(x_future)

    # for i in range(0, len(x_future)):
    #     x_future[i] = (x_future[i] - minimum) / scale

    # x_future = np.reshape(x_future, (1, 7, 1))

    # y_future = []

    # while len(y_future) < 7:
    # #     Predicting future values using 7-day moving averages of the last day 7 days.
    #     p = model.predict(x_future)[0]

    # #     Appending the predicted value to y_future
    #     y_future.append(p)

    # #     Updating input variable, x_future
    #     x_future = np.roll(x_future, -1)
    #     x_future[-1] = p

    # y_future = np.array(y_future)
    # y_future = np.reshape(y_future, (7))

    # for i in range(0, len(y_future)):
    #     y_future[i] = (y_future[i] * scale) + minimum

    # y_future = np.reshape(y_future, (7, 1))

    # last7 = pd.DataFrame(df.Close[-7:])
    # last7.reset_index(drop=True, inplace=True)
    # y_future = pd.DataFrame(y_future, columns=['Close'])
    # predictions = pd.concat([last7, y_future], ignore_index=True)

    # prev_7 = datetime.date.today() - datetime.timedelta(7)
    # predictions['Date'] = [prev_7 + datetime.timedelta(x) for x in range(0, 14)]

    st.subheader('Predicted Data')

    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # st.table(predictions[8:13])

    # def plot_predicted_data():
    #     fig = go.Figure()
    #     fig.add_trace(go.Scatter(x=data['Date'][-7:], y=data['Close'][-7:], name='current_stock_price'))

    #     fig.add_trace(go.Scatter(x=predictions['Date'][8:13], y=predictions['Close'][7:], name='predicted_stock_price'))
    #     fig.add_trace(go.Scatter(x=predictions['Date'][7:9], y=predictions['Close'][6:8], name = '--', mode='lines', line=dict(color='royalblue', width=4, dash='dot')))
    #     fig.layout.update(title_text = selected_stock, xaxis_rangeslider_visible=True)
    #     st.plotly_chart(fig)

    # plot_predicted_data()

if rad1 == "About-Us":
    st.title("Gas Turbine Baker Hughes")

    st.subheader('Locate Us')

    site_df = pd.read_csv('./data/site_metadata-7fc535965d0c074cea0be6786fc9518e.csv')
    
    m = folium.Map(location=[site_df['LATITUDE'].mean(), site_df['LONGITUDE'].mean()], zoom_start=1, control_scale=True)
    for index, location_info in site_df.iterrows():
        folium.Marker([location_info["LATITUDE"], location_info["LONGITUDE"]],
                      popup=location_info["PLANT_NAME"]).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)

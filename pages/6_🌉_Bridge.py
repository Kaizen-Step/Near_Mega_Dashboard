# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Bridge - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌉Bridge')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'bridge_out_daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d59ec417-b905-445c-9d10-e61344b42394/data/latest')
    elif query == 'Distribution_bridged_out_Volume':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d9346ec3-b6d2-45da-ba43-41b03afd888c/data/latest')
    elif query == 'Distribution_transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2e347a2a-488f-40da-a826-f7529be78fba/data/latest')
    elif query == 'daily_bridge_detail':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3b5c115f-5335-4233-b6a8-9bd9ffec9226/data/latest')
    return None


bridge_out_daily = get_data('bridge_out_daily')
Distribution_bridged_out_Volume = get_data('Distribution_bridged_out_Volume')
Distribution_transactions = get_data('Distribution_transactions')
daily_bridge_detail = get_data('daily_bridge_detail')

st.subheader('Transaction Charts')

df = bridge_out_daily
df2 = Distribution_bridged_out_Volume
df3 = Distribution_transactions
df4 = daily_bridge_detail

# Daily bridged out volume
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["VOLUME"],
                     name='Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["CUMULATIVE_VOLUME"],
                      name='CUMULATIVE Volume'), secondary_y=True)
fig.update_layout(
    title_text='Daily bridged out volume'.title())
fig.update_yaxes(
    title_text='Volume', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Volume', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Beidge out-Daily Users
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["ACTIVE_USERS"],
                     name="ACTIVE USERS".title()), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["CUMULATIVE_USERS"],
                      name="CUMULATIVE USERS".title()), secondary_y=True)
fig.update_layout(
    title_text='Beidge out Daily Users'.title())
fig.update_yaxes(
    title_text='ACTIVE USERS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE USERS', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Distribution of users based on "bridged out" Volume
fig = px.bar(df2, x="BRIDGE_RANGE", y="NUMBER_OF_USERS",
             color="BRIDGE_RANGE", title='Distribution of users based on bridge Out Volume')
fig.update_layout(showlegend=True, xaxis_title='NUMBER OF USERS'.title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Distribution of transactions based on "bridged out" Volume
fig = px.bar(df3, x="BRIDGE_RANGE", y="NUMBER_OF_BRIDGES",
             color="BRIDGE_RANGE", title='Distribution of transactions based on bridged out Volume'.title())
fig.update_layout(showlegend=True, xaxis_title='NUMBER OF Bridge'.title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily bridged out Transactions-(Normalized)
fig = px.histogram(df4, x="DATE", y="NUMBER_OF_TRANSACTIONS", color="BLOCKCHAIN",
                   title='Daily bridged out Transactions', barnorm='percent')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'categoryorder': 'category ascending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily bridged out Users-(Normalized)
fig = px.histogram(df4, x="DATE", y="BRIDGER", color="BLOCKCHAIN",
                   title='Daily bridged out Users', barnorm='percent')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'categoryorder': 'category descending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily bridged out Volume-(Normalized)
fig = px.histogram(df4, x="DATE", y="VOLUME", color="BLOCKCHAIN",
                   title='Daily bridged out Volume', barnorm='percent')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'categoryorder': 'category descending'})
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bridge out Transactions based on Blockchains
fig = px.pie(df4, values="NUMBER_OF_TRANSACTIONS",
             names="BLOCKCHAIN", title='Bridge out Transactions based on Blockchains')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bridge out users based on Blockchains
fig = px.pie(df4, values="BRIDGER",
             names="BLOCKCHAIN", title='Bridge out users based on Blockchains')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bridge out volume based on Blockchains
fig = px.pie(df4, values="VOLUME",
             names="BLOCKCHAIN", title='Bridge out volume based on Blockchains')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

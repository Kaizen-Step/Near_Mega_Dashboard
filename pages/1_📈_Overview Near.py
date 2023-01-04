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
st.set_page_config(page_title='Overview Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Overview')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources


@st.cache()
def get_data(query):
    if query == 'Overview_Total_Contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d02e98af-3135-42ab-9944-595940ba8dba/data/latest')
    elif query == 'Overview_NearTX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1d7988f8-5b04-4e61-87fb-fde67fa81633/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')
    elif query == 'Overview_Total_Staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/97a71654-c83b-4f34-be2c-6f9f826822fd/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    return None


Overview_Total_Contracts = get_data('Overview_Total_Contracts')
Overview_NearTX = get_data('Overview_NearTX')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')

# Single Number Overview
st.subheader('Overview')
df = Overview_Total_Contracts
df2 = Overview_NearTX
df3 = Overview_Contract_Deployed
df4 = Overview_Total_Staking_Reward
df5 = Overview_bridge_out

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Total Number of Contracts**',
              value=str(df["total Number of contracts"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Transactions Success Rate**',
              value=df2["SUCCESS_RATE"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total NEAR Unique Users**',
              value=df2["UNIQUE_USERS"].map('{:,.0f}'.format).values[0])
with c2:
    st.metric(label='**Total NEAR Transactions **',
              value=str(df2["TOTAL_TRANSACTIONS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Daily Transactions**',
              value=df2["AVERAGE_DAILY_TRANSACTION"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Staking Reward**',
              value=df4["CUMULATIVE_STAKING_REWARDS"].map('{:,.0f}'.format).values[0])
with c3:
    st.metric(label='**Bridge out-Number of Unique Users**',
              value=str(df5["ACTIVE_USERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Bridge out-Total TX of luna**',
              value=df5["NUMBER"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Bridge out-Total volume of luna**',
              value=df5["VOLUME"].map('{:,.0f}'.format).values[0])

st.subheader('Activity Over Time')

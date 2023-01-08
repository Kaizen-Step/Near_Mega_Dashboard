# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Overview - Near Dashboard',
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
    elif query == 'Overview_Supply':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/902720b8-fb3c-4361-8479-fb9f45e389d7/data/latest')
    elif query == 'Overview_NEAR_supplystaking':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/53d2d65e-e026-4867-bb58-3178af45b61c/data/latest')
    elif query == 'Overview_Near_Bridge':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9e9700a4-aed9-4a1b-bbc8-7803fc4aced7/data/latest')
    elif query == 'Overview_HeatmapTX2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cadf8686-2873-4a46-9fd4-2b406d3ae2d6/data/latest')
    elif query == 'Overview_NEARheatmap2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/119a1f32-294a-4749-9d0b-746120829567/data/latest')
    return None


Overview_Total_Contracts = get_data('Overview_Total_Contracts')
Overview_NearTX = get_data('Overview_NearTX')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_Supply = get_data('Overview_Supply')
Overview_NEAR_supplystaking = get_data('Overview_NEAR_supplystaking')
Overview_Near_Bridge = get_data('Overview_Near_Bridge')
Overview_HeatmapTX2 = get_data('Overview_HeatmapTX2')
Overview_NEARheatmap2 = get_data('Overview_NEARheatmap2')
# Single Number Overview
st.text(" \n")
st.subheader('Glance')


df = Overview_Total_Contracts
df2 = Overview_NearTX
df3 = Overview_Contract_Deployed
df4 = Overview_Total_Staking_Reward
df5 = Overview_bridge_out
df6 = Overview_Supply
df7 = Overview_NEAR_supplystaking
df8 = Overview_Near_Bridge
df9 = Overview_HeatmapTX2
df10 = Overview_NEARheatmap2
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Total Number of Contracts**',
              value=str(df["total Number of contracts"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Transactions Success Rate**',
              value=df2["SUCCESS_RATE"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total NEAR Unique Users**',
              value=df2["UNIQUE_USERS"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Bridge TX Ethereum to NEAR**',
              value=df8["NUMBER_TRANSACTIONS"].map('{:,.0f}'.format).values[0])
with c2:
    st.metric(label='**Total NEAR Transactions**',
              value=str(df2["TOTAL_TRANSACTIONS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Near USN supply**',
              value=df6["SUPPLY"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Avg Stake Volume per User**',
              value=df7["NEAR_PER_STAKER"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Bridged Ethereum to NEAR [USD]**',
              value=df8["USD_VOLUME"].map('{:,.0f}'.format).values[0])
with c3:
    st.metric(label='**Number of Stake transaction**',
              value=str(df7["STAKES"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Stake Volume**',
              value=df7["STAKED_NEAR"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Number of Stakers**',
              value=df7["STAKES"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Users Bridged Ethereum to NEAR**',
              value=df8["UNIQUE_USERS"].map('{:,.0f}'.format).values[0])

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('HeatMaps')

# Failed transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df9, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                         histfunc='avg', title='Failed transactions per minute on hour of day (UTC)', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Failed transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Success transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df9, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Success transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="Success transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Success transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Block per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                         histfunc='avg', title="Block per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# User per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                         histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

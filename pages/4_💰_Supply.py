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
st.set_page_config(page_title='Supply - Nera Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💰Supply')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NEAR_supplystaking1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ab53f9b1-d914-4d76-8dd7-a0c87420c2e2/data/latest')
    elif query == 'NEAR_Top10Validator':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/182bf73e-da3c-4b88-99f1-99e8112dd5f7/data/latest')
    elif query == 'NEAR_supply_richest':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9de75ce-2ed2-4394-ba02-55921a2b9aa0/data/latest')
    elif query == 'NEAR_Balance_Range':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/070d0011-42bc-465c-896f-d1a3f269e7d2/data/latest')
    return None


NEAR_supplystaking1 = get_data('NEAR_supplystaking1')
NEAR_Top10Validator = get_data('NEAR_Top10Validator')
NEAR_supply_richest = get_data('NEAR_supply_richest')
NEAR_Balance_Range = get_data('NEAR_Balance_Range')

st.subheader('Supply Charts')

df = NEAR_supplystaking1
df2 = NEAR_Top10Validator
df3 = NEAR_supply_richest
df4 = NEAR_Balance_Range

# Top 10 Validator
fig = px.bar(df2, x="VALODATOR", y="AMOUNT",
             color="VALODATOR", title='Top 10 Validator')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Validator')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Stake volume and With cumulative stake volume
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Staked"],
                     name="NEAR Staked".title()), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE_STAKE"], y=df["TOTAL_STAKED"],
                      name="TOTAL STAKED".title()), secondary_y=True)
fig.update_layout(
    title_text='Stake volume and With cumulative stake volume')
fig.update_yaxes(
    title_text="NEAR Staked".title(), secondary_y=False)
fig.update_yaxes(title_text="TOTAL STAKED".title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily net stake volume
fig = px.bar(df.sort_values(["DATE_STAKE", "DAILY_NET"], ascending=[
             True, False]), x="DATE_STAKE", y="DAILY_NET", title='Daily net stake volume'.title())
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="DAILY NET")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily stakers vs Unstakers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Stakers"],
                     name="Stakers".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["Unstakers"],
                     name="Unstakers".title()), secondary_y=False)
fig.update_layout(
    title_text='Daily stakers vs Unstakers')
fig.update_yaxes(
    title_text="Stakers".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Near stake vs Unstake
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Staked"],
                     name="NEAR Staked".title()), secondary_y=False)
fig.add_trace(go.Bar(x=df["DATE_STAKE"], y=df["NEAR Unstaked"],
                     name="NEAR Unstaked".title()), secondary_y=False)
fig.update_layout(
    title_text='Near stake vs Unstake')
fig.update_yaxes(
    title_text="Stakers".title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Richest Users
fig = px.bar(df3, x="RECEIVER", y="BALANCE", color="RECEIVER",
             title='Richest Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="BALANCE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR supply- distrbution users based on Balance Range
fig = px.bar(df4.sort_values(["WALLET_NUMBER", "BALANCE_RANGE"], ascending=[
             True, False]), x="WALLET_NUMBER", y="BALANCE_RANGE", title='NEAR supply- distrbution users based on Balance Range'.title(), color="BALANCE_RANGE")
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="BALANCE_RANGE")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

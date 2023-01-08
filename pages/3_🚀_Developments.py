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
st.set_page_config(page_title='Development - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Developments')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_Dev_New_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/82a59d16-929f-409b-98ae-7a78757268b5/data/latest')
    elif query == 'Near_DevTopnew_weekly_transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b79d62ba-f40c-4c76-a301-bdb28ad03fc4/data/latest')
    elif query == 'Near_TopContracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7893cc65-c539-435e-b7e3-36aaa926db27/data/latest')
    elif query == 'Near_TopNew_Fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/786bee4c-7f76-4bcf-a690-01071a24d40b/data/latest')
    elif query == 'NearTop10Contracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1e7ec242-f80e-4075-b30a-7432ec3cc266/data/latest')
    elif query == 'NearTop_newcontracts_fee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3861369a-98db-4743-a531-2db1860d5cc8/data/latest')
    elif query == 'NearWeekly_TopContracts_users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4651d25e-65b6-4fbe-bac1-843c86f093ca/data/latest')
    return None


Near_Dev_New_contracts = get_data('Near_Dev_New_contracts')
Near_DevTopnew_weekly_transactions = get_data(
    'Near_DevTopnew_weekly_transactions')
Near_TopContracts_Transactions = get_data('Near_TopContracts_Transactions')
Near_TopNew_Fee = get_data('Near_TopNew_Fee')
NearTop10Contracts_Transactions = get_data('NearTop10Contracts_Transactions')
NearTop_newcontracts_fee = get_data('NearTop_newcontracts_fee')
NearWeekly_TopContracts_users = get_data('NearWeekly_TopContracts_users')

st.text(" \n")
st.subheader('New Contract Metrics')


df = Near_Dev_New_contracts
df2 = Near_DevTopnew_weekly_transactions
df3 = Near_TopContracts_Transactions
df4 = Near_TopNew_Fee
df5 = NearTop10Contracts_Transactions
df6 = NearTop_newcontracts_fee
df7 = NearWeekly_TopContracts_users

# Top new contracts based on weekly transactions
fig = px.bar(df2.sort_values(["DATE", "TRANSACTIONS"], ascending=[
    True, False]), x="DATE", y="TRANSACTIONS", color="TX_RECEIVER", title='Top new contracts based on weekly transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='TX Number')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# New Contract Deployed Daily
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['DATE'], y=df["NEW_CONTRACTS"],
                     name="New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["CUM_NEW_CONTRACTS"],
                      name="Cum New Contract"), secondary_y=True)
fig.update_layout(
    title_text='New Contract Deployed Daily')
fig.update_yaxes(
    title_text="New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top new contracts Based on average transactions fee
fig = px.area(df6, x="DATE", y="AVG_TX_FEE", color="TX_RECEIVER",
              title='Top new contracts Based on average transactions fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='AVG TX Fee')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Top New Contracts Based on Total Transactions Fee
fig = px.bar(df4, x="TX_RECEIVER", y="TOTAL_TX_FEE", color="TX_RECEIVER",
             title='Top New Contracts Based on Total Transactions Fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TOTAL TX FEE".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Overall Contract Metrics')


# Weekly Top Contracts Based on Transactions
fig = px.bar(df3.sort_values(["DATE", "COUNT"], ascending=[
    True, False]), x="DATE", y="COUNT", color="CONTRACT", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on users
fig = px.bar(df7.sort_values(["DATE", "USERS"], ascending=[
    True, False]), x="DATE", y="USERS", color="CONTRACT", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Transactions')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Most popular Contracts Based on Transactions
fig = px.pie(df3, values="COUNT",
             names="CONTRACT", title='Most popular Contracts Based on Transactions')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Most popular Contract based on users
fig = px.pie(df7, values="USERS",
             names="CONTRACT", title='Most popular Contract based on users')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Near Dev- Top 10 Contracts Based on Transactions
fig = px.bar(df5, x="CONTRACT_ADDRESS", y="TRANSACTIONS", color="CONTRACT_ADDRESS",
             title='Top 10 Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TRANSACTIONS".title())
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

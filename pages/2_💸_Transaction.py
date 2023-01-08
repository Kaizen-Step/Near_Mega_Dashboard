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
st.set_page_config(page_title='Transactions - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NEAR_TX1':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7ccd4486-ebc8-4d20-b5e8-7d4b342ff259/data/latest')
    elif query == 'NEAR_TX3':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d124f6e9-6a76-4a84-bbfc-8cef231add75/data/latest')
    elif query == 'Near_TX_Interval':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/54c4f0e2-95b1-4720-b54d-c1352bd68381/data/latest')
    return None


NEAR_TX1 = get_data('NEAR_TX1')
NEAR_TX3 = get_data('NEAR_TX3')
Near_TX_Interval = get_data('Near_TX_Interval')

st.text(" \n")
st.subheader('Transaction Charts')

df = NEAR_TX1
df2 = NEAR_TX3
df3 = Near_TX_Interval

tab_Overtime, tab_Averages = st.tabs(['**Over Time**', '**Averages**'])

with tab_Overtime:
    interval = st.radio('**Time Interval**',
                        ['Daily', 'Weekly', 'Monthly'], key='fees_interval', horizontal=True)

    if st.session_state.fees_interval == 'Daily':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_TRANSACTIONS_DAILY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_FEE_DAILY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["AVG_BLOCK_TIME_DAILY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='Block Time daily')
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

     # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TPS_DAILY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Daily ')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Weekly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_BLOCK_WEEKLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_FEE_WEEKLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["AVG_BLOCK_TIME_WEEKLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME WEEKLY'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TPS_WEEKLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Weekly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Monthly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["MONTH"], y=df3["CUMULATIVE_TRANSACTIONS_MONTHLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df3["MONTH"], y=df3["CUMULATIVE_BLOCK_MONTHLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["AVG_BLOCK_TIME_MONTHLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME Monthly'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df3["MONTH"], y=df3["TPS_MONTHLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Monthly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Averages:

    # Number of Transaction With Standard Moving Averages
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df2['DATE'], y=df2["NUMBER_OF_TRANSACTIONS"],
                         name="NUMBER OF TRANSACTIONS".title()), secondary_y=False)
    fig.add_trace(go.Line(x=df2['DATE'], y=df2["MA26_TX"],
                          name='Daily Moving average (MA26)'), secondary_y=True)
    fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA52_TX'],
                          name='Daily Moving average (MA52))'), secondary_y=True)
    fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA100_TX'],
                          name='Daily Moving average (MA100)'), secondary_y=True)
    fig.update_layout(
        title_text='Number of Transaction With Standard Moving Averages')
    fig.update_yaxes(
        title_text="NUMBER OF TRANSACTIONS".title(), secondary_y=False)
    fig.update_yaxes(title_text='Moving averages Volume', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average Transaction Fee Per Transaction Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TRANSACTION_FEE_WEEKLY"],
                         name="AVG TRANSACTION FE WEEKLY".title()), secondary_y=False)
    fig.update_layout(
        title_text='Average Transaction Fee Per Transaction Per Week')
    fig.update_yaxes(
        title_text="AVG TRANSACTION FE WEEKLY".title(), secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average TPS Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TPS"],
                         name="AVG TPS"), secondary_y=False)
    fig.update_layout(
        title_text='Average TPS Per Week')
    fig.update_yaxes(
        title_text="AVG TPS", secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average Block Time Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_BLOCK_TIME"],
                         name="AVG BLOCK TIME".title()), secondary_y=False)
    fig.update_layout(
        title_text='Average Block Time Per Week')
    fig.update_yaxes(
        title_text="AVG BLOCK TIME".title(), secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Weekly Transactions Succes Rate
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["WEEKLY_SUCCESS_RATE"],
                         name="WEEKLY SUCCESS RATE".title()), secondary_y=False)
    fig.update_layout(
        title_text='Weekly Transactions Succes Rate')
    fig.update_yaxes(
        title_text="WEEKLY SUCCESS RATE".title(), secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

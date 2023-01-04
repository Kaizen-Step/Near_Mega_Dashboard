# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Near MegaDashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('Near Dashboard')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/near-logo.png'))


st.write(""" # Introduction #

NEAR Protocol is a smart contract capable, public Proof-of-Stake (PoS) blockchain that was conceptualized as a community-run cloud computing platform. 
Built by the NEAR Collective, NEAR was designed to host decentralized applications (dApps), and strives to compete with Ethereum and other leading smart contract-enabled blockchains like EOS and Polkadot.
 NEAR’s native token is also called NEAR, and is used to pay for transaction fees and storage.
 NEAR tokens can also be staked by token holders who participate in achieving network consensus as transaction validators.
NEAR Protocol is focused on creating a developer and user friendly platform. 
To accommodate this mission, NEAR has incorporated features like human-readable account names as opposed to only cryptographic wallet addresses, and the ability for new users to interact with dApps and smart contracts without requiring a wallet at all.

Projects building on NEAR include Mintbase, a non-fungible token (NFT) minting platform, and Flux, a protocol that allows developers to create markets based on assets, commodities, real-world events, and more.

""")

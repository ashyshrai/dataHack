import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('pwd.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


st.write()
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
    )

with st.expander(label= "Fill the below form to register and get  your credentials"):
    st.write("https://docs.google.com/forms/d/1o_8Q8kKBjuqx4AXLXSigS1TBKFUT8jsIQdk3o-B9_hs/prefill")

with st.expander(label="Cick to Login"):
    name, authentication_status, username = authenticator.login('Welcome to DataHack! Please enter your credentials', 'main')




if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')



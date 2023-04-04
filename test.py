import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['t1', 't2']).generate()
print(hashed_passwords)


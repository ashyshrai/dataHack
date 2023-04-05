import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['my_secure_password']).generate()

with open('hashed_passwords.txt', 'w') as f:
    f.write(hashed_passwords)
print("Hashed passwords generated and stored securely.")

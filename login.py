import streamlit as st
import hashlib


# Main app function
def app():
    # Create a dictionary of valid usernames and hashed passwords for demonstration
    USER_CREDENTIALS = {
    "admin": hashlib.sha256("password123".encode()).hexdigest(),
    "user1": hashlib.sha256("mypassword".encode()).hexdigest(),
    "user2": hashlib.sha256("test123".encode()).hexdigest(),
    }

    # Authentication function
    def authenticate(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return username in USER_CREDENTIALS and USER_CREDENTIALS[username] == hashed_password

    # Initialize session state variables
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["username"] = None

    # If user is authenticated, display a welcome message
    if st.session_state["authenticated"]:
        st.success(f"Welcome, {st.session_state['username']}!")
        if st.button("Log out"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = None
            st.rerun()
    else:
        # UI components for login
        st.title("Sign In")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", placeholder="Enter your password", type="password")

            if st.button("Login"):
                if not username or not password:
                    st.warning("Please enter both username and password.")
                elif authenticate(username, password):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.rerun()
                else:
                    st.error("Invalid username or password. Please try again.")


#app()
import streamlit as st

st.set_page_config(
    page_title="PCOS We Care",
    page_icon=":heart:",  # You can choose a relevant icon
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: sans-serif;
    }
    .header {
        background-color: #f05094; /* Pink header */
        #color: white;
        padding: 1rem;
        display: flex;
        justify-content: space-between; /* Align items to edges */
        align-items: center; /* Vertically center items */
    }
    .header-title {
        font-weight: bold;
        font-size: 1.5em; /* Adjust as needed */
    }
    .nav-links {
        display: flex;
    }
    .nav-links a {
        color: white;
        text-decoration: none;
        margin-left: 1rem; /* Space between links */
        padding: 0.5rem 1rem; /* Add some padding */
        border-radius: 5px; /* Rounded corners */
        background-color: #d13f7f; /* Slightly darker pink */
    }
    .content {
        padding: 2rem;
        text-align: center; /* Center the text */
    }
    .highlighted-text {
        font-size: 1.2em;
        line-height: 1.5; /* Improve readability */
        margin-bottom: 2rem;
    }
    .begin-test-button {
        background-color: #F3AFAF; /* Pink button */
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px;
        font-size: 1.1em;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown("<span class='header-title'>PCOS We Care</span>", unsafe_allow_html=True)
st.markdown("<div class='nav-links'>", unsafe_allow_html=True)
def go_home():
    
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url=/1home.py"> 
        """,
        unsafe_allow_html=True,
    ) 
st.button(
    label="Home", 
    on_click=go_home,  # Call the go_home function on click
    key="home_button" # Give it a unique key
)
def go_about():
    
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; url=pages/2about.py"> 
        """,
        unsafe_allow_html=True,
    ) 
st.button(
    label="About", 
    on_click=go_about,  # Call the go_home function on click
    key="about_button" # Give it a unique key
)
#st.markdown("<a href='#'>Home</a>", unsafe_allow_html=True)
#st.markdown("<a href='#'>About</a>", unsafe_allow_html=True)
st.markdown("<a href='#'>Contact</a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Main content area
st.markdown("<div class='content'>", unsafe_allow_html=True)
st.markdown("<div class='highlighted-text'>", unsafe_allow_html=True)
st.markdown("IF YOU HAVE EVER STRUGGLED WITH") 
st.markdown("IRREGULAR PERIODS, MOOD SWINGS, IRRITABILITY, ETC.")
st.markdown("THESE SYMPTOMS MIGHT LOOK NORMAL BUT IT COULD ALSO BE ")
st.markdown("THE SYMPTOMS OF POLYCYSTIC OVARY SYNDROME (PCOS)",
 unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

if st.button("BEGIN YOUR TEST", key="begin_test"):  # Added a key here
    # Redirect or do something when the button is clicked
       st.session_state.test_started = True  # Set a flag in session state

if "test_started" in st.session_state and st.session_state.test_started:
    # Redirect using JavaScript (more seamless)
    st.markdown(
        """
        <meta http-equiv="refresh" content="0; 
        url=pages/3test.py">
        """,
        unsafe_allow_html=True,
    )
    #st.write("Test started (placeholder)")  # Replace with your test logic
st.markdown("</div>", unsafe_allow_html=True)
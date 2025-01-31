import streamlit as st

# Set page configuration (optional)
st.set_page_config(
    page_title="PCOS We Care",
    page_icon="🩺",  # You can use an emoji or image icon
    layout="wide"  # or "centered"
)

# --- Header Section ---
col1, col2 = st.columns([1, 2])  # Adjust ratio as needed
st.title("PCOS WE CARE") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
html_temp = """ 
	<div style ="background-color:#F3AFAF;padding:13px"> 
	<h1 style ="color:black;text-align:left;">HOME</h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True)

with col2:
    st.markdown(
        """
        <div style="text-align: right;">  
            <a href="#" style="margin: 0 10px; text-decoration: none; color: #333;">Home</a>
            <a href="#" style="margin: 0 10px; text-decoration: none; color: #333;">About</a>
            <a href="#" style="margin: 0 10px; text-decoration: none; color: #333;">Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("""
    <style>
        .button-container {
            position: fixed;
            top: 10px;
            right: 10px;
            background-color: #f3afaf;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stButton > button {
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Create a container for the buttons
with st.container():
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
""", unsafe_allow_html=True)
if st.button("Home"):
    st.switch_page("1home.py")
if st.button("ABOUT"):
    st.switch_page("pages/2about.py")
if st.button("BEGIN YOUR TEST"):
    st.switch_page("pages/3test.py")
    

# --- Main Content Section ---
st.markdown("---")  # Separator line

st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <p style="font-size: 24px;">IF YOU HAVE EVER STRUGGLED WITH</p>
        <p style="font-size: 24px;">IRREGULAR PERIODS, MOOD SWINGS,</p>
        <p style="font-size: 24px;">IRRITABILITY, ETC.</p>
        <p style="font-size: 24px;">THESE SYMPTOMS MIGHT LOOK</p>
        <p style="font-size: 24px;">NORMAL BUT IT COULD ALSO BE THE</p>
        <p style="font-size: 24px;">SYMPTOMS OF POLYCYSTIC OVARY</p>
        <p style="font-size: 24px;">SYNDROME (PCOS)</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Button Section ---
st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <button style="background-color: #F3AFAF; border: none; color: #FFF; padding: 15px 30px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px;">
            BEGIN YOUR TEST
        </button>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Styling (Optional) ---
st.markdown(
    """
    <style>
        body {
            font-family: sans-serif; /* Choose your preferred font */
            color: #333; /* Dark gray text color */
        }
        .main {
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)




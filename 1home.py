import streamlit as st

# Set page configuration (optional)
st.set_page_config(
    page_title="PCOS We Care",
    page_icon="🩺",  # You can use an emoji or image icon
    layout="wide"  # or "centered"
)

# --- Header Section ---
col1, col2 = st.columns([1, 2])  # Adjust ratio as needed
#st.title("PCOS WE CARE") 

# here we define some of the front end elements of the web page like 
# the font and background color, the padding and the text to be displayed 
html_temp = """  
    <h1 style ="color:#DC3C68;text-align:center;font-family:Geneva;">PCOS WE CARE</h1> 
    """
with col2:
        st.markdown(            """
    <div style="text-align: right;">  
    <a href="1home.py" style="margin: 0 10px; text-decoration: none; color: #333;">Home</a>
    <a href="./pages/2about.py" style="margin: 0 10px; text-decoration: none; color: #333;">About</a>
    <a href="pages/3test.py" style="margin: 0 10px; text-decoration: none; color: #333;">Begin Your Test</a>
        </div>
        """,
    unsafe_allow_html=True,
        )

    
# this line allows us to display the front end aspects we have 
# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True)

#with col2:
  #  st.markdown(
  #      """
   #     <div style="text-align: right;">  
   #         <a href="1home.py" style="margin: 0 10px; text-decoration: none; color: #333;">Home</a>
   #         <a href="./pages/2about.py" style="margin: 0 10px; text-decoration: none; color: #333;">About</a>
   #         <a href="pages/3test.py" style="margin: 0 10px; text-decoration: none; color: #333;">Begin Your Test</a>
   #     </div>
   #     """,
   #     unsafe_allow_html=True,
    #)

# --- Main Content Section ---
st.markdown("---")  # Separator line

st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <p style="font-size: 24px;font-family:GEORGIA">IF YOU HAVE EVER STRUGGLED WITH IRREGULAR PERIODS, MOOD SWINGS,IRRITABILITY, ETC. THESE SYMPTOMS MIGHT LOOK NORMAL BUT IT COULD ALSO BE THE SYMPTOMS OF POLYCYSTIC OVARY SYNDROME (PCOS)</p>
        
    </div>
    """,
    unsafe_allow_html=True,
)
st.image("pcos1.jpg", caption="Comparison of Healthy and Polycystic Ovary" )
# --- Button Section ---
st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <a href="pages/3test.py" style="background-color: #F3AFAF; border: none; color: #000000; padding: 15px 30px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius:25px;">
            BEGIN YOUR TEST
        </a>
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

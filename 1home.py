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
    <div style ="background-color:#F3AFAF;padding:13px"> 
    <h1 style ="color:black;text-align:center;">PCOS WE CARE</h1> 
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

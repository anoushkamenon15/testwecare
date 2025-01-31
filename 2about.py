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
    </div> 
    """
    
# this line allows us to display the front end aspects we have 
# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True)

html_temp = """ 
    <h1 style ="color:#F3AFAF;text-align:left;">About</h1> 
    </div> 
    """
    
# this line allows us to display the front end aspects we have 
# defined in the above code 
st.markdown(html_temp, unsafe_allow_html = True)

with col2:
    st.markdown(
        """
        <div style="text-align: right;">  
            <a href="1home.py" style="margin: 0 10px; text-decoration: none; color: #FFFFF;">Home</a>
            <a href="./pages/2about.py" style="margin: 0 10px; text-decoration: none; color: #FFFFF;">About</a>
            <a href="pages/3test.py" style="margin: 0 10px; text-decoration: none; color: #FFFFF;">Begin Your Test</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Main Content Section ---
st.markdown("---")  # Separator line
st.markdown("<div class='text-justified'>", unsafe_allow_html=True)  # Start justified block
st.markdown(
    """
    <div style="text-align: justify;font-family:GEORGIA">
        Polycystic Ovary Syndrome (PCOS) is a problem with hormones that happens during the reproductive years . If you have PCOS, you may not have periods very often. Or you may have periods that last many days. You may also have too much of a hormone called androgen in your body.With PCOS, many small sacs of fluid develop along the outer edge of the ovary. These are called cysts. The small fluid-filled cysts contain immature eggs. These are called follicles. The follicles fail to regularly release eggs.The exact cause of PCOS is unknown. Early diagnosis and treatment along with weight loss may lower the risk of long-term complications such as type 2 diabetes and heart diseasePolycystic Ovary Syndrome (PCOS) is one of the most common reproductive disorders in women and despite this, diagnostic challenges, delayed diagnosis and less than optimal treatment regimens plague the condition. PCOS is a hormonal disorder affecting 6% - 26% of women in the reproductive age group worldwide. Early detection will facilitate timely intervention, helping to manage symptoms and reduce the risk of long-term complications associated with PCOS.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)  

st.markdown("""<div style="text-align: justify;font-family:GEORGIA">  
    Polycystic ovary syndrome (PCOS) is associated with an increased risk of several health conditions including<br>          
    Type 2 diabetes: More than half of people with PCOS develop type 2 diabetes by age 40.<br>
    Heart disease: PCOS can increase the risk of heart disease.<br>
    Endometrial cancer: PCOS can increase the risk of endometrial cancer, which is cancer of the inner lining of the uterus.<br>
    High blood pressure: PCOS can increase the risk of high blood pressure.<br>
    High cholesterol: PCOS can increase the risk of high cholesterol.<br>
    Gestational diabetes: PCOS can increase the risk of gestational diabetes.<br>
    Sleep apnea: PCOS can increase the risk of sleep apnea.<br>
    Stroke: PCOS can increase the risk of stroke.<br>
 </div>
    """,
    unsafe_allow_html=True,
)

st.image("pcos2.jpg", caption="Lifecycle of Ovum in Healthy and Polycystic Ovary")

import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

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
    <h1 style ="color:#DC3C68;text-align:center;font-family:Geneva;;border-radius:15px">PCOS WE CARE</h1> 
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

# loading in the model to predict on the data 
pickle_in = open('classifier4.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

def prediction(weight,height,cycleri,cyclelength,weightgain,hairgrowth,skindark,hairloss,pimples): 

	
	# Placeholder for demonstration - Adjust to your model's needs
	prediction = classifier.predict([[weight, height,
								   		1 if cycleri == "Yes" else 0,  
		  								1 if weightgain == "Yes" else 0,
										cyclelength,
										1 if hairgrowth == "Yes" else 0,
										1 if skindark == "Yes" else 0, 
										1 if hairloss == "Yes" else 0, 
          								1 if pimples == "Yes" else 0 
         ]])

	
	if prediction == [1]:
			return("You are at risk of having PCOS");
	else:
			return("You are not at risk of having PCOS")  
	

# this is the main function in which we define our webpage 

def main(): 
	# giving the webpage a title 
	
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<h1 style ="color:#F3AFAF;text-align:left;">Risk Assessment</h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) # Fixed indentation
	st.markdown("---")  # Separator line
	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction 
	# Setting appropriate min_value, you can change them according to your data
	weight = st.number_input("Enter weight in kg", min_value=0.00, value=0.00, step = 0.01)
	height = st.number_input("Enter height in m", min_value=0.00, value=0.00, step = 0.01)
	cycleri = st.selectbox("Do you have regular periods?", ["Select","Yes","No"])  # Key added
	cyclelength = st.number_input("Enter Cycle length", min_value=0, value=0)
	weightgain = st.selectbox("Have you gained weight?",["Select","Yes","No"])  # Key added
	hairgrowth = st.selectbox("Do you have increased hair growth?",["Select","Yes","No"])  # Key added  Corrected label
	skindark = st.selectbox("Has your skin darkened?",["Select","Yes","No"])  # Key added
	hairloss = st.selectbox("Do you have hair loss?", ["Select","Yes","No"])  # Key added
	pimples = st.selectbox("Do you have pimples?", ["Select","Yes","No"])  # Key added
	result = ""
	 
	if st.button("Predict"): 
		result = prediction(weight,height,cycleri,cyclelength,weightgain,hairgrowth,skindark,hairloss,pimples) 
	st.success(' {}'.format(result)) 
	

if __name__=='__main__': 
	main()

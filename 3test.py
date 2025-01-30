import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 

# loading in the model to predict on the data 
pickle_in = open('classifier3.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

def welcome(): 
	return 'welcome all'

#bmi = calculate_bmi(weight_kg, height_m)
# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction(weight,height,bmi,cycleri,cyclelength,weightgain,hairgrowth,skindark,hairloss,pimples): 

	# Assuming your classifier expects a list or numpy array
	# Replace with the correct column names your model expects 
	# prediction = classifier.predict([[weight, height, bmi, cycleri, cyclelength, weightgain, skindark, hairloss, pimples, follleft, follright]])  
	
	# Placeholder for demonstration - Adjust to your model's needs
	prediction = classifier.predict([[weight, height,bmi,
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
	st.title("PCOS WE CARE") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """ 
	<div style ="background-color:#F3AFAF;padding:13px"> 
	<h1 style ="color:black;text-align:left;">Risk Assessment</h1> 
	</div> 
	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) # Fixed indentation
	
	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction 
	# Setting appropriate min_value, you can change them according to your data
	weight = st.number_input("Enter weight in kg", min_value=0.00, value=0.00, step = 0.01)
	height = st.number_input("Enter height in m", min_value=0.00, value=0.00, step = 0.01)
	bmi = st.number_input("Enter BMI")
	cycleri = st.radio("Do you have regular periods?", ["Yes", "No"], key="cycle_regular")  # Key added
	cyclelength = st.number_input("Enter Cycle length", min_value=0, value=0)
	weightgain = st.radio("Have you gained weight?", ["Yes", "No"], key="weight_gain")  # Key added
	hairgrowth = st.radio("Do you have increased hair growth?", ["Yes", "No"], key="hair_growth")  # Key added  Corrected label
	skindark = st.radio("Has your skin darkened?", ["Yes", "No"], key="skin_darkened")  # Key added
	hairloss = st.radio("Do you have hair loss?", ["Yes", "No"], key="hair_loss")  # Key added
	pimples = st.radio("Do you have pimples?", ["Yes", "No"], key="pimples")  # Key added
	#follleft = st.number_input("Enter number of follicles in left ovary", min_value=0, value=0)
	#follright = st.number_input("Enter number of follicles in right ovary", min_value=0, value=0)
	result = ""
	 
	if st.button("Predict"): 
		result = prediction(weight,height,bmi,cycleri,cyclelength,weightgain,hairgrowth,skindark,hairloss,pimples) 
	st.success(' {}'.format(result)) 
	

if __name__=='__main__': 
	main()

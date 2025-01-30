import streamlit as st

st.set_page_config(
    page_title="PCOS We Care",
    page_icon=":heart:",
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
        color: white;
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
    .text-justified {  /* Class for justified text */
        text-align: justify;
        max-width: 800px;  /* Adjust as needed */
        margin: 0 auto;   /* Center the text block */
        line-height: 1.6; /* Improve readability */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown("<span class='header-title'>PCOS We Care</span>", unsafe_allow_html=True)
st.markdown("<div class='nav-links'>", unsafe_allow_html=True)
st.markdown("<a href='#'>Home</a>", unsafe_allow_html=True)
st.markdown("<a href='#'>About</a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Main content area
st.markdown("<div class='content'>", unsafe_allow_html=True)

# Justified text block
st.markdown("<div class='text-justified'>", unsafe_allow_html=True)  # Start justified block

st.markdown("Polycystic Ovary Syndrome (PCOS) is one of the most common reproductive disorders in women and despite this, diagnostic challenges, delayed diagnosis and less than optimal treatment regimens plague the condition. PCOS is a hormonal disorder affecting 6 - 26% of women in the reproductive age group worldwide. Early detection will facilitate timely intervention, helping to manage symptoms and reduce the risk of long-term complications associated with PCOS.", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close justified block

st.markdown("</div>", unsafe_allow_html=True)
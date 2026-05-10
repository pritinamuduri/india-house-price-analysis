import streamlit as st
st.title("Business Insights")
#st.image("")
st.info("Key finding: Proximity to IT hubs is the strongest driver of price growth")
#C:\Users\namud\Downloads\Project 3 Labmentix\Business Insight.py
st.set_page_config(page_title="Proper Analysis", layout="wide")
st.image("C:/Users/namud/Downloads/Streamlit generator.webp",width=150)
with st.sidebar:
    st.header("Insights Summary")
    st.markdown("""
    **Key Takeaways:**
    * Market Trends by Neighborhood
    * Investment Opportunities
    * Price per SqFt analysis
    """)
#st.info("Navigate here to see thehigh-level business impacton the data.")
#st.subheader
st.text("Most properties are in lower to mid range houses, which shows higher demand for these kind of houses, so focus can be centralised on these kind of houses.")
st.text("Price Per Sqft for Apartments is higher compared to luxury houses, reason being better location, amenities.") 
st.text("Fully Furnished properties are priced at higher values, because of furnished status. While unfurnished properties at valued at lower price.")
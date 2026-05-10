import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
st.set_page_config(page_title="Proper Analysis", layout="wide")
# everything inside this block moves to the left sidebar
with st.sidebar:
    st.header("Graph Controls")
    st.markdown("""
    **Property Analysis:**
    * Price vs Size
    * Distribution by BHK
    * Furnishing Status Impact
    """)
    # --- Main Page Area ---
    #st.title("Data Visualisation")
    # Adding a filter here is a great way to use the space
    #select_neighbourhood = st.multiselect("Filter by Neighbourhood", options=df['NEIGHBORHOOD'].unique())
#st.sidebar
#with st.sidebar:
    #st.header("Filters")
    #city_select = st.multiselect("Select City", options=df['City'].unique())
    #price_range = st.slider("Price Range", 0, int(df["Total_Price_Full"].max()), (0, 1000000))
st.title("Data Visualisation")
st.image("C:/Users/namud/Downloads/Streamlit generator.webp",width=150) 
# Load Data
df = pd.read_csv("C:/Users/namud/Downloads/Project 3 Labmentix/cleaned_india_housing_prices.csv")
st.title("Property Analysis")
st.header("Plotly Chart")
st.subheader("Distribution of Property Price by Size")
# Define the figure
fig = px.bar(df, x="Size_in_SqFt", y="Total_Price_Full")
# Placement: Update layout before displaying
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
# Display instreamlit
st.plotly_chart(fig)
st.header("BHK Distribution by City")
st.subheader("Stacked Bar Chart")
# Prepare the data(Ensure 'City' and 'BHK' are columns)
# We count the number of properties for each BHKtype per city
df_counts = df.groupby(['City', 'BHK']).size().reset_index(name='Count')
# Build the stacked bar chart
fig =px.bar(
    df_counts,
    x="City",
    y="Count",
    color="BHK",
    title="Count of BHK Types across Cities",
    barmode="stack", # Change to "group" for side-by-side bars
    template="plotly_white",
    color_discrete_sequence=px.colors.qualitative.Vivid
)
# Clean styling (Remove grid and dollar signs)
fig.update_layout(yaxis_tickprefix="", xaxis_showgrid=False, yaxis_showgrid=False)
st.plotly_chart(fig, use_container_width=True)
st.header("Price Distribution by Furnishing Status")
st.subheader ("Grouped Box Plot")
fig =px.box(
    df,
    x="Furnished_Status",
    y="Total_Price_Full",
    color="Furnished_Status",
    notched=True, # Adds a 'notch' to help compare medians visually
    title="Statistical Price Spread by Furnishing"
)
st.plotly_chart(fig, use_container_width=True)
#st.subheader("Price Distribution by Furnishing Status")
# Ensure 'Furnished_Status' is on x and 'Total_Price_Full'is on y
#fig =px.violin(
    #df,
    #x="Furnished_Status",
    #y="Total_Price_Full",
    #color="Furnished_Status",
    #box=True,  # Adds a small box plot inside the violin
    #points="all",  # Shows individualdata pointsto see density
   # title="Price Range vs Furnishing Status",
    #template="plotly_white"

# Remove dollar signs and grid for a clean look
#fig.update_layout(
    #yaxis_tickprefix="",
    #xaxis_showgrid=False,
    #yaxis_showgrid=False,
    #showlegend=False


#st.plotly_chart(fig, use_container_width=True)


# Create the chart
#ax = sns.barplot(x='Size_in_SqFt', y='Total_Price_Full')
# Placement: Turn off grid here
#plt.grid(False)
#sns.despine() # Bonus: removes the top/right border for a cleaner look
# Show the chart
#plt.show()

# Group Data by property type and get the mean price
# This prepares the data specifically for a bar chart
#chart_data = df.groupby('Property_Type')['Total_Price_Full'].mean()
# Display the Bar Chart
#st.subheader ("Average Price by Property Type")
#st.bar_chart(chart_data)
#fig.update_layout(template="plotly_white")
# Create the figure
#fig = px.bar(df, x='Propert_Type',y='Total_Price_Full')
# update bar graph to make the bars thinner (0.1 is thick, 0.9 is very thin)
#fig.update_layout(bargraph=0.6)
#Display in streamlit
#st.plotly_chart(fig, use_cotainer_width=True)
#fig = px.box(df, x="Furnished_Status", y="Total_Price_Full", title="Price Distribution by Furnishing")
#st.plotly_chart(fig)
#df = pd.read_csv("C:/Users/namud/Downloads/Project 3 Labmentix/cleaned_india_housing_prices.csv")
#count the number of IDs for each Furnished_Status
# value_counts is the fastest way to get these counts
#status_counts = df['Availability_Status'].value_counts()
# Display the chart
#st.subheader("Total Count by Status")
#st.bar_chart(status_counts)
# we  use "size" for both the position(x) and the color
#fig = px.box(df, x="Size_in_SqFt", y="Total_Price_Full",
#title="Price Distribution by Size",
#color="size", # This colorseach box differentlybased on the size name
#title="Price Distribution by Size"
#st.plotly_chart
# We use "size" for both the position (x) and the color
#fig = px.box(df,
#x="Size_in_SqFt",
#y="Total_Price_Full",
#color="size", # This colors each boxdifferentlybased on thesize name
#title="Price Distribution by Size")
#st.plotly_chart(fig)
# Title for your section
#st.header("Relationship between Size and Price")
# Create the scatter plot
# We use 'size' for the x-axis and 'price for the y-axis
#fig =px.scatter(df,
#x="Size_in_SqFt",
#y="Total_Price_Full",
#title="Scatter Plot of Price vs Size",
#hover_data=["Total_Price_Full"]) # options: adds extrainfo on hover
# Display the chart in streamlit
#st.plotly_chart(fig)
#if st.checkbox("Show Scatter Plot"):
    #st.plotly_chart(fig)
# Shows cpount of each BHKtype per City
#fig = px.histogram(df,
#x="City",
#color="BHK",
#barmode="group",
#title="BHK Distribution by City")
#st.plotly_chart(fig)
# 'owner_type' is your categorical column(Owner, Agent, etc.,)
#fig = px.pie(df,
#names='Owner_Type',
#title="Property Distribution by Owner Type",
#hole=0.4) # Makes it a Donut chart for a modern look
#st.plotly_chart(fig)
# A simple box plot to isolate price outliers
#fig = px.box(df,
#y="Total_Price_Full",
#points="Outliers", # Options: (default), 'all', or False
#title= "Price Outlier Detection")
#st.plotly_chart(fig)
# Outliers in Price
#fig = px.box(df,y= "Total_Price_Full",
#title="Detection of Price Outliers",
#points="outliers") # This specifically highlightsthe outlier dots
#st.plotly_chart(fig)
# Shows the percentage share of each status
#fig_pie = px.pie(df,
#names="Availability_Status",
#title="Market Share byPropert Status")
#st.plotly_chart(fig_pie)





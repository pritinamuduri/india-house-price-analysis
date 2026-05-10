import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Proper Analysis", layout="wide")
st.image("C:/Users/namud/Downloads/Streamlit generator.webp",width=150)
#col1, col2 = st.columns([1,2]) # Adjust ratios as needed
#with coll1:
    #st.image("C:/Users/namud/Downloads/Project 3 Labmentix/cleaned_india_housing_prices.csv")
#st.rerun()
# Move to the sidebar
with st.sidebar:
    st.title("Data Cleaning")
    st.info("Upload your dataset and select cleaning options below.")
    # Add a file uploaderor controls here
    upload_file = st.file_uploader("C:/Users/namud/Downloads/Project 3 Labmentix\cleaned_india_housing_prices.csv")
#st.sidebar
st.title("Data Cleaning")
st.write("Here we demonstrate the steps taken to prepare our dataset.")
# Example placeholder code
st.code("""
# Handling missing values
#df.dropna(inplace=True)
# Removing duplicates
df.drop_duplicates(inplace=True)
""")
#df = pd.read_csv("C:/Users\namud\Downloads\india_housing_prices.xlsx - india_housing_prices.csv"
#df = pd.read_csv("C:/Users/namud/OneDrive/Priti/india_housing_prices.csv")
#st.table(df)
#
#st.title("T")
#st.image("C:/Users/namud/Downloads/Logo for streamlit project.jpg")
#st.image("C:/Users/namud/Downloads/Streamlit generator.webp",width=150)
st.subheader("Dataframe")
df = pd.read_csv("C:/Users/namud/OneDrive/Priti/india_housing_prices.csv")
st.dataframe(df,use_container_width=True)
#st.write(df)
df.info()
print(df.describe())
st.write(df.describe())
#df['Size_in_SqFt'] = df['Price_per_SqFt'].replace(0, nan)
#['Size_in_SqFt'] = df['Price_per_SqFt'].fillna(df['Price_per_SqFt'].median())
#df['Size_in_SqFt'] = df['Price_per_SqFt'].replace(0, np.nan)
#df['Size_in_SqFt'] = df['Price_per_SqFt'].fillna(df['Price_per_SqFt'].median())
#st.write(df.describe())
# step A convert everything to number(handles text '0' too)df['Size_in_SqFt'] = pd.to_numeric(df['Price_per_SqFt'], errors='coerce')
# Step B. Replace 0 with NaN and SAVE it
df.loc[df['Price_per_SqFt'] == 0, 'Price_per_SqFt'] = np.nan
# Step C Fill NaN's with median and SAVE it
df['Price_per_SqFt'] = df['Price_per_SqFt'].fillna(df['Price_per_SqFt'].median())
# Step D. Show the results in Streamlit
st.write("Cleaned Summary")
st.write(df['Price_per_SqFt'].describe())
#df['Price_per_SqFt'] = df['Price_per_SqFt'].astype('int64')
#st.write(df['Price_per_SqFt'].dtype)
#st.text ("After fixing 0 values in Price per SqFt column they were replaced with NaN and post that these NaN values were assigned median vales")
#st.text( "Then converted from float64 to int 64")
#st.write(df.dtypes)
#st.subheader ("Converting datatype of Price in Lakhs cloumn from float64 to int 64")
# 1. Convert to  nullable integer
#df['Price_in_Laks'] = df['Price_in_Lakhs'].astype('int64')
# 2. Display the result in your Streamlit app
#st.write("Price in Lakhs (as int64):")
#st.write(df[['Price_in_Lakhs']].head())
# 1. Create the new column (Total_Price)
# Note: Ensure both columns are numeric first to avoid errors
#df['Total_Price'] = df['Size_in_SqFt'] * df['Price_per_SqFt']
df['Total_Price'] = df['Size_in_SqFt'] * df['Price_per_SqFt']
# 2. Display the result in yopur streamlit
st.subheader ("Calculated Total Price")
st.write(df[['Size_in_SqFt', 'Price_per_SqFt', 'Total_Price']].head())
# Round to the nearest whole number and convert to int
#df['Price_per_Sqft'] = df['Price_per_SqFt'].round().astype(int)
# Display in streamlit
#st.write("Price Per SqFt (Whole Numbers):")
#st.write(df[['Price_per_SqFt']].head())
# Multiply by 1000 first(To use values as whole number)
#df['Price_per_Sqft'] = df['Price_per_SqFt'] * 1000
# force streamlit to show the updated DataFreame
#st.write(df[['Size_in_SqFt', 'Price_per_SqFt']].head())
# Round and convert to nullable integer type
# using int64 (capital I) prevents errors if there are still NaN's
#df['Price_per_Sqft'] = df['Price_per_SqFt'].round(0).astype('int64')
# Force streamlit to show updated DataFrame
#st.write(df[['Size_in_SqFt', 'Price_per_SqFt']].head())
# Create the new xolumn by multiplying existing Total_Price
df['Total_Price_Full'] = df['Total_Price'] * 100000
# Display the result in ypur Streamlit app
st.subheader ("New Column: Total Price In Absolute Figure")
st.write(df[['Total_Price', 'Total_Price_Full']].head())
# CAlculate the derived price per SqFt
# We divide the full absoluteprice by the total size
df['Derived_Price_per_SqFt'] = df['Total_Price_Full'] / df['Size_in_SqFt']
# Display the result in ypur Streamlit app
st.subheader("Derived Price per SqFt Calculation")
#st.write('Total_Price_Full', 'Size_in_SqFt', Derived_Price_per_SqFt']].head())
#st.write('Total_Price_Full', 'Size_in_SqFt', Derived_Price_per_SqFt']].head())
st.write(df[['Total_Price_Full', 'Size_in_SqFt', 'Derived_Price_per_SqFt']].head())
# If floor_no is higher, set Total_Floor toequal Floor_no
#df['Total_Floors'] = np.where(df['Floor_no'] > df['Total_Floors'],df['Floor_no'],df['Total_Floors'])
# Replace 0s with NaN in Total_Floor
df['Total_Floors'] = df['Total_Floors'].replace(0, np.nan)
# Fill those NaNs with the median(realistic building height)
df['Total_Floors'] = df['Total_Floors'].fillna(df['Total_Floors'].median())
# Final safety check: if Floor_no is still higher, make Total_Floorsequal to Floor_No
df['Total_Floors'] = np.where(df['Floor_No'] > df['Total_Floors'],df['Floor_No'], df['Total_Floors'])
#st.write(df.head())
# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_india_housing_prices.csv', index=False)
# Adda confirmationmessage in your Streamlit app
st.success("Dataset successfullysaved as cleaned_india_housing_prices_csv!")
#f = st.file_uploader("C:/Users/namud/Downloads/Project 3 Labmentix/cleaned_india_housing_prices.csv")
#if f:
    #st.image(f)

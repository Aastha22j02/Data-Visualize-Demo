import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()

# Sidebar for selecting columns
st.sidebar.title("Select Columns")
columns = st.sidebar.multiselect("Choose columns", df.columns)

# Show the data
st.title("Data Explorer")
st.write(df[columns])

# Visualizations
st.title("Visualizations")
st.subheader("Histogram")
fig, ax = plt.subplots()
ax.hist(df[columns[0]], bins=20)
st.pyplot(fig)

st.subheader("Scatterplot")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x=columns[0], y=columns[1], ax=ax)
st.pyplot(fig)
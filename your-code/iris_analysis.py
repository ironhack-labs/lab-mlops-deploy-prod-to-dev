import seaborn as sns
import streamlit as st
st.set_page_config(
    page_title="Iris Analysis",
    page_icon="🌸",
    layout="wide"
)
st.title("🌸 Iris Flower Analysis App")
st.sidebar.header("About")
st.sidebar.info("""
This app explores the famous Iris dataset.
Select features to visualize relationships between different flower measurements.
""")
iris_df = sns.load_dataset("iris")
st.sidebar.metric("Total Samples", len(iris_df))
st.sidebar.metric("Features", len(iris_df.columns))
st.sidebar.metric("Species", iris_df['species'].nunique())
st.header("Dataset")
st.write(iris_df)
st.header("Dataset description")
st.write(iris_df.describe())
x = st.selectbox(
    "Enter x-axis column: ", 
    options=iris_df.columns
    ) 
y = st.selectbox(
    "Enter y-axis column: ",
    options=iris_df.columns
    )
st.scatter_chart(
    x=x, 
    y=y, 
    data=iris_df, 
    color="species", 
    ) 
st.markdown("---")
st.subheader("📥 Download Data")

csv = iris_df.to_csv(index=False)
st.download_button(
    label="Download Iris Dataset as CSV",
    data=csv,
    file_name="iris_data.csv",
    mime="text/csv"
)

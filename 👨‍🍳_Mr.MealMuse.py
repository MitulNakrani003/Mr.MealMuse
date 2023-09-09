import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Mr.MealMuse",
    page_icon="🫕",
)

st.sidebar.success("Select a page above.")
   
image = Image.open("Mr.MealMuse.png")
st.image(image)  
st.markdown(
        "##### What are some dishes that can be prepared using the ingredients available in your apartment......? :house:🍜"
    ) 

st.markdown(
        "##### Mr.MealMuse, an AI-based model will help to find matches for you..:mag: "  
    ) 
st.markdown(
        "##### Mr. MealMuse provides two different types of meal recommendations."  )
st.markdown("-1) ChefChoice")
st.markdown("-2) NutriChoice")

st.markdown(
        "###### Select your preferred option from the sidebar and enjoy your experience!...↖️😋 "  )

st.write("------------------")
st.subheader("👨‍💻👩‍💻 developed by Donut Bytes ✨")
st.write("------------------")
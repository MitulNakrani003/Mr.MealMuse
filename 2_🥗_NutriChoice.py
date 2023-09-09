import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import warnings
import time
import random

import nltk
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

warnings.filterwarnings('ignore')

df = pd.read_csv('dataset.csv')

st.set_page_config(
    page_title="NutriChoice",
    page_icon="🥗",
)

  
class Profile:
    
    df = pd.read_csv('dataset.csv') # static variable
    
    
    
    def __init__(self,diet,disease,Nutrient,food_type,favorite_food):
        self.diet = diet
        self.disease = disease
        self.nutrient = Nutrient
        self.type = food_type
        self.like = favorite_food
        self.df2 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df3 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df4 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df5 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df6 = pd.DataFrame(columns=list(Profile.df.columns))
        
    def removestop(self,tokens):
        stop = set(stopwords.words('english'))
        file = open('stopwords.txt','r')
        l = list(file.read().split())
        stop = list(stop) +l
        l = [token for token in tokens if token not in stop]
        return l
            
    def inputs(self,diet,disease,Nutrient,food_type,favorite_food):
        
        if Nutrient:
            self.df2 = Profile.df[Profile.df.Nutrient.isin(Nutrient)]
            self.df2 = self.df2.reset_index()
       
        if food_type:
            self.df2 = self.df2[self.df2.Veg_Non.isin(food_type)]
            self.df2 = self.df2.reset_index()
      
        if diet:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i,'Diet']).split()
                
                for d in diet:
                    if d in l:
                        self.df4=self.df4.append(self.df2.loc[i])
 
        if disease:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i,'Disease']).split()
                for d in disease:
                    if d in l:
                        self.df5=self.df5.append(self.df2.loc[i])

        if favorite_food:
            f = self.removestop(favorite_food.split())
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'Name']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(Profile.df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'description']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'catagory']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(Profile.df.loc[i])
            
        return self.df2,self.df3,self.df4,self.df5,self.df6
    
    def get_profile(self):
        df2,df3,df4,df5,df6 = self.inputs(self.diet,self.disease,self.nutrient,self.type,self.like)
        
        df_merge = pd.concat([df2,df3,df4,df5,df6],axis=0).drop_duplicates(subset='Name')
        df_merge = df_merge.filter(['Name','description'])
        ans = df_merge.head(7)
     
        return ans
 

image = Image.open("choice2.png").resize((700, 300))
st.image(image)  
st.markdown(
        "##### NutriChoice : A food recommendation app that helps you make nutritious choices by suggesting meals based on your dietary needs and preferences."
    ) 


st.markdown(
        "###### Try it out for yourself below! :arrow_down:😋"  
    ) 
   
with st.form("recommendation_form"):
   
    options3 = ["veg","non-veg"]
    food_type = st.multiselect("Do you enjoy vegetarian cuisine or do you prefer non-vegetarian dishes?",options3)
    
    options1 = ['fiber', 'vitamin_a', 'calcium', 'magnesium', 'sodium','vitamin_c', 'protien', 'vitamin_e', 'iron', 'selenium','carbohydrates', 'chloride', 'potassium', 'vitamin_d', 'manganese','phosphorus', 'iodine']
    Nutrient = st.multiselect("What is your favorite nutrient to include in your meals for optimal health?",options1)

    options2 = ['low_fat_diet', 'low_sodium_diet ', 'high_fiber_diet', 'high_protien_diet', 'gluten_free_diet', 'low_carb_diet ','ketogenic_diet', 'omni_diet ', 'hormone_diet ']
    diet = st.multiselect("Do you have a preference for a certain type of diet, such as a high-protien-diet or gluten-free diet?",options2)
    
    disease = st.multiselect("Do you have any health issues that I should be aware of?",['obesity ', 'diabeties ', 'pregnancy ', 'cancer', 'anemia ', 'hypertension ','kidney_disease ', 'goitre ', 'scurvy ', 'heart_disease ', 'eye_disease'])

    favorite_food =st.text_input("Do you have a craving for something")
    
    generated = st.form_submit_button("Generate")
    
    
        
if generated:
    st.session_state.generated=True

    with st.spinner(text="Sit tight while I come up with some meal ideas that I think you'll love."):
        time.sleep(2)
    st.success('Mr.MealMuse has successfully created a list of meal ideas that we believe would be a great fit for you.!')
    ob = Profile(diet,disease,Nutrient,food_type,favorite_food)
    profile = ob.get_profile()        
    st.write(profile)
    
    st.write("------------------")
    st.subheader("👨‍💻👩‍💻 developed by Donut Bytes ✨")
    st.write("------------------")

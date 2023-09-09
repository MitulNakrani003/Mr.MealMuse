import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import warnings
import time
import random
import nltk
from nltk.corpus import stopwords


st.set_page_config(
    page_title="ChefChoice",
    page_icon="🍜",
)

nltk.download('stopwords')

warnings.filterwarnings('ignore')

df = pd.read_csv('cuisines.csv')


class Profile:
    
    df = pd.read_csv('cuisines.csv') # static variable
    
    def __init__(self,diet,cuisine,course,prep_time,ingredients):
        self.diet = diet
        self.cuisine = cuisine
        self.course = course
        self.prep_time = prep_time
        self.ingredients = ingredients
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
            
    def inputs(self,diet,cuisine,course,prep_time,ingredients):
        
        if cuisine:
            self.df2 = Profile.df[Profile.df.cuisine.isin(cuisine)]
            self.df2 = self.df2.reset_index()
       
        if course:
            self.df2 = self.df2[self.df2.course.isin(course)]
            self.df2 = self.df2.reset_index()
      
        if diet:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i,'diet']).split()
                
                for d in diet:
                    if d in l:
                        self.df4=self.df4.append(self.df2.loc[i])
 
        if prep_time:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i,'prep_time']).split()
                for d in prep_time:
                    if d in l:
                        self.df5=self.df5.append(self.df2.loc[i])

        if ingredients:
            f = self.removestop(ingredients.split())
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'name']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(Profile.df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'ingredients']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i,'cuisine']).split()]
                for j in n:
                    for k in f:
                        if k==j:
                            self.df6=self.df6.append(Profile.df.loc[i])
            
        return self.df2,self.df3,self.df4,self.df5,self.df6
    
    def get_profile(self):
        df2,df3,df4,df5,df6 = self.inputs(self.diet,self.cuisine,self.course,self.prep_time,self.ingredients)
        
        
        df_merge = pd.concat([df2,df3,df4,df5,df6],axis=0).drop_duplicates(subset='name')
        df_merge = df_merge.filter(['name','image_url','instructions'])
        print(df_merge.shape)
        ans = df_merge.head(7)
     
        return ans
    


    
image = Image.open("ChefChoice.png").resize((700, 300))
st.image(image)  
st.markdown(
        "##### ChefChoice: An app that suggests meal recipes and combinations that cater to your dietary preferences, while also allowing you to mix and match different cuisines and courses."
    ) 
  
     
st.markdown(
        "###### Try it out for yourself below! :arrow_down:😋"  
    ) 
   
with st.form("recommendation_form"):
   
    options3 = ["Vegetarian","High Protein Vegetarian","Non Vegeterian","Diabetic Friendly","High Protein Non Vegetarian"]
    diet = st.multiselect("Do you enjoy vegetarian cuisine or do you prefer non-vegetarian dishes?",options3)
    
    options1 = ['North Indian Recipes', 'Indian', 'South Indian Recipes', 'Bengali Recipes', 'Tamil Nadu']
    cuisine = st.multiselect("What type of regional cuisine are you craving for?",options1)

    options2 = ['Lunch', 'Side Dish ', 'Dinner', 'Dessert', 'South Indian Breakfast']
    course = st.multiselect("Can you specify whether you prefer to have lunch, dinner or breakfast??",options2)
    
    options3 = ['Total in 15 min', 'Total in 20 min', 'Total in 30 min', 'Total in 50 min']
    prep_time = st.multiselect("Can you specify how much time you have available to cook your meal?",options3)

    ingredients =st.text_input("Do you have a craving for something")
    
    generated = st.form_submit_button("Generate")
    
    
        
if generated:

    with st.spinner(text="Sit tight while I come up with some meal ideas that I think you'll love."):
        time.sleep(2)
    st.success('Mr.MealMuse has successfully created a list of meal ideas that we believe would be a great fit for you.!')
    ob = Profile(diet,cuisine,course,prep_time,ingredients)
    profile = ob.get_profile()        
    st.write(profile)
    
    st.write("------------------")
    st.subheader("👨‍💻👩‍💻 developed by Donut Bytes ✨")
    st.write("------------------")

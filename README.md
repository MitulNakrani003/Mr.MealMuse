## ✨ Mr.MealMuse👨‍🍳: Satisfy your cravings with a personalized recommendation🍜	

## 💥 Inspiration
Meal planning can be time-consuming and challenging, especially for people with specific dietary requirements or preferences. Many people struggle to find meals that fit their nutritional needs and taste preferences, This can lead to frustration, wasted time and effort, and unhealthy eating habits. Furthermore, the vast amount of recipe and food information available online can be overwhelming, making it difficult for users to find the right meal for their needs. Therefore, my team, Donut Byte developed Mr.MealMuse: Satisfy your cravings with a personalized recommendation.

## 🖥️	 How we built it
To build this project, we have used two datasets from Kaggle . The first dataset contains 4226 unique recipes along with descriptions, ingredients, and instructions to cook and another contains 400 unique values with descriptions, nutrients available in the recipe, and diet preferences such as low fat, low sodium, and diseases.

After collecting the data, we applied data cleaning to remove redundant information that would not help distinguish recipes. Using Natural Language Processing we removed stopwords and cooking measures such as pounds and grams and also removed the punctuations

The Machine learning-based recommendation system was built using a content-based-filtering approach which enables us to recommend recipes to people based on the preferences the user provides. To measure the similarity between user-given preferences and recipes K-nearest-neighbor approach was used.

The recommendation model computes distance and indices for K nearest-neighbor between the inputted user preference and all recipes in the corpus. It then outputs the top-7 most similar recipes, along with their ingredients and URLs, and descriptions for the user to choose from.

After that, we Built a user-friendly app using Streamlit.

## 🚀 Challenges we ran into
One of the biggest challenges of a hackathon is the limited amount of time available to complete the project. we had no prior knowledge or experience in building a recommender system from scratch. However, we learned the required skills during the hackathon. While working with the data, particularly during the recommendation stage, I encountered several errors. Fortunately, we both were able to resolve these issues.

## 👀 Try it out 😋
Try it out for yourself below! ⬇️

https://esha411-mr-mealmuse--mr-mealmuse-56ezes.streamlit.app/

## 👨‍💻👩‍💻 Developed by Team Donut Bytes ✨
- [🙋‍♀️ @Esha Patel](https://github.com/esha411)
- [🙋 @Mitul Nakrani](https://github.com/MitulNakrani003)

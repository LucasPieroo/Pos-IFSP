
# D3TOP: Anime Recommendation System
This project is an anime recommendation system that primarily recommends animes based on the similarity of their synopses. It also uses a fuzzy logic mechanism to ignore variations of the same anime series for more accurate recommendations. Furthermore, the system considers the genres of the anime to further increase the precision of the suggestions.

Dataset
The anime data used in this project has been sourced from Kaggle at this link https://www.kaggle.com/datasets/natlee/myanimelist-comment-dataset. 

Please note that this data doesn't include the anime synopsis. Therefore, it was necessary to web scrape the synopses and pre-process them before using it for recommendations.

## Preprocessing Steps
The preprocessing steps mainly aim to clean and normalize the dataset, especially the synopses of the animes. This is a crucial part of any data analysis and machine learning workflow because it enhances the model's performance and accuracy. Here is a breakdown of what's involved:

- Duplicate Removal: This process is essential as duplicates can distort analysis results and cause machine learning models to overfit. Thus, duplicates were eliminated to ensure that each anime appears only once in the dataset.

- Handling Missing Values: Missing values can also skew results and are handled differently by different machine learning algorithms. To ensure consistency across the dataset, missing values were replaced with an empty string.

- Stemming and Lemmatization: These are methods used to reduce words to their base or root form. Stemming crudely chops off prefixes and suffixes from a word, while lemmatization takes into account the morphological analysis of the language to return the root word. Both methods serve to decrease the dimensionality of the data and improve the model's performance.

- Stopwords Removal: Stopwords are common words that don't contribute much semantic value to a sentence and could introduce noise into the data (for example, 'is', 'and', 'the'). By removing these, the model can focus more on the words that matter.

- Text Preprocessing: Several steps were performed to clean the text data. These include removing HTML tags, URLs, emojis, special characters, extra spaces, converting to lowercase, and applying the previously mentioned lemmatization and stemming. All these steps contribute to normalizing the text data, making it more easily interpretable for the machine learning model.


# App Deployment
The application is built using Streamlit and follows several crucial steps in order to provide the user with anime recommendations based on a selected anime.

- Data Loading: All necessary data, including anime descriptions, is loaded into the application.

- Text Vectorization: This is an essential step in processing the data for our machine learning model. Our application employs Term Frequency-Inverse Document Frequency (TF-IDF) Vectorization, a commonly used technique in natural language processing. It turns our anime descriptions into numerical representations (vectors) that our machine learning model can understand and work with. This conversion allows the model to recognize patterns in the text data. TF-IDF not only takes into account the frequency of a word appearing in a particular document (in this case, an anime synopsis) but also offsets that frequency against the frequency of the word in the entire corpus of documents. This helps balance the importance of the word in the context of our data.

- Cosine Similarity Calculation: Once the data is vectorized, we then calculate the Cosine Similarity. Cosine Similarity measures the cosine of the angle between two vectors. This metric allows the model to understand how similar two vectors (and thus, two anime descriptions) are to each other. We use these similarity scores as a foundation for our recommendation system, as animes with higher cosine similarity to the user's selected anime would logically make for good recommendations. The cosine similarity is an important part of this system because it quantifies the similarity between different animes, helping us to recommend the most similar animes based on the chosen one.

- Fuzzy Matching: The system also incorporates Fuzzy Matching to handle anime variants and genres. This method is a form of partial string matching that works well for this context. For instance, if a user enjoys a particular anime, they are likely to enjoy variations or similar genres of that anime. Hence, Fuzzy Matching aids in finding matches even if they are not 100% identical, thus making the recommendations more diverse and relevant.

- User Interface: The user interface is designed to be simple and intuitive. Users can select an anime and specify whether they want the system to ignore anime seasons or not. The system then provides the most similar animes to the chosen one.

- Validation: The effectiveness of the recommendation system was verified by testing whether variations of an anime were recommended when a specific anime was chosen. If a user enjoys an anime, they are likely to enjoy different variants of it. Therefore, the recommendation system's ability to suggest these variations demonstrates its functionality and reliability.

The deployment of this system is significant as it makes the anime recommendation model accessible and interactive for users. It allows users to explore different animes based on their preferences, thereby enhancing their anime discovery experience.

# Accessing the Application
Accessing the Anime Recommendation system is straightforward and user-friendly.

To access the application, simply click on the following link or copy and paste it into your web browser: Anime Recommendation System

https://lucaspieroo-pos-ifsp-d3topinterface-63wjbp.streamlit.app/

The application will open in your default web browser, and you can start exploring anime recommendations based on your chosen anime. Enjoy exploring new animes tailored to your preferences!

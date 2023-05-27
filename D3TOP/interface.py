import streamlit as st
import pandas as pd
import numpy as np
import math
from fuzzywuzzy import fuzz
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(layout='wide')
#aval = pd.read_csv("reviews_tratada.csv")
animes = pd.read_excel("D3TOP/base_tratada_final_animes.xlsx")
#similarity_matrix = np.load("D3TOP/vector.npy")

@st.cache 
def ml_teste():
    # Vectorize the preprocessed anime descriptions
    vectorizer = TfidfVectorizer()
    vectorized_descriptions = vectorizer.fit_transform(animes['synopsis tratada final'])

    # Calculate similarity scores
    similarity_matrix = cosine_similarity(vectorized_descriptions)
    return similarity_matrix

similarity_matrix = ml_teste()

#Função para encontrar top animes:
def get_top_similar_animes(anime_index, similarity_matrix, fuzzy_usar, top_k=5):
    if fuzzy_usar == "No":
        anime_scores = similarity_matrix[anime_index]  # Get similarity scores for the given anime
        top_indices = anime_scores.argsort()[-top_k-1:-1][::-1]  # Get top similar anime indices (excluding the given anime itself)
        return animes.iloc[top_indices]['workId'].values.tolist()
    else:
        anime_scores = similarity_matrix[anime_index]  # Get similarity scores for the given anime
        top_indices = anime_scores.argsort()[-80-1:-1][::-1]  # Get top similar anime indices (excluding the given anime itself)
        return animes.iloc[top_indices]['workId'].values.tolist()

# escrevendo um título na página
st.title('Anime recomendation system')
fuzzy_usar = st.radio(
    "Ignore anime seasons?",
    ('Yes', 'No'))

option = st.selectbox(
    'Para qual anime deseja recomendação?',
    animes["name"])
st.write('You selected:', option)
index = animes[animes["name"] == option].index[0]
genero = animes.loc[index, "genre"]
# Centralized title
st.markdown(f"<h1 style='text-align: center;'>{option}</h1>", unsafe_allow_html=True)

# Centralized image
st.write(f'<p style="text-align:center;"><img src="{animes.loc[index,"IMG"]}"></p>', unsafe_allow_html=True)

# Centralized text
st.markdown(f"<p style='text-align: center;'>{animes.loc[index,'synopsis']}</p>", unsafe_allow_html=True)


st.markdown(f"<h1 style='text-align: center;'>Recomendações</h1>", unsafe_allow_html=True)

#Selecionando as recomendações
similar_animes = get_top_similar_animes(index, similarity_matrix, fuzzy_usar, top_k=10)

base_auxiliar = animes[animes["workId"].isin(similar_animes)]
base_auxiliar["ordem"] = pd.Categorical(base_auxiliar["workId"], categories=similar_animes, ordered=True)
base_auxiliar = base_auxiliar.sort_values("ordem").reset_index()

if fuzzy_usar == "Yes":
    mask = base_auxiliar["name"].apply(lambda x: fuzz.partial_ratio(option, x) < 75)
    filtered_df = base_auxiliar[mask]
    base_auxiliar = filtered_df.reset_index(drop = True)

# Calculate Fuzzy Ratio for each row
base_auxiliar['fuzzy_ratio'] = base_auxiliar['genres'].apply(lambda x: fuzz.ratio(x, genero))

# Create categories based on Fuzzy Ratio
conditions = [
    (base_auxiliar['fuzzy_ratio'] > 0.8),
    (base_auxiliar['fuzzy_ratio'] > 0.5),
    (base_auxiliar['fuzzy_ratio'] > 0.3)
]

values = [3, 2, 1]

base_auxiliar['fuzzy_category'] = np.select(conditions, values, default=0)

# Sort by Fuzzy Ratio categories, then by original order
base_auxiliar.sort_values('fuzzy_category', ascending=False, kind='mergesort', inplace=True)

# You can drop the helper columns if not needed
base_auxiliar.drop(['fuzzy_ratio', 'fuzzy_category'], axis=1, inplace=True)
base_auxiliar.reset_index(inplace = True , drop = True)  
    
# Three columns with Centralized title, centralized image,centralized text in each column
col1, col2, col3 = st.columns(3)
tamanho_max = math.ceil(max(len(base_auxiliar.loc[0,'name']) , len(base_auxiliar.loc[1,'name']), len(base_auxiliar.loc[2,'name']))/46)
with col1:
    st.markdown(
    f'<h3 style="text-align:center; height:{50*tamanho_max}px;">{base_auxiliar.loc[0,"name"]}</h3>',
    unsafe_allow_html=True
    )
    st.write(f'<p style="text-align:center;"><img src="{base_auxiliar.loc[0,"IMG"]}"height="320"></p>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{base_auxiliar.loc[1,'synopsis']}</p>", unsafe_allow_html=True)

with col2:
    st.markdown(
    f'<h3 style="text-align:center; height:{50*tamanho_max}px;">{base_auxiliar.loc[1,"name"]}</h3>',
    unsafe_allow_html=True)
    st.write(f'<p style="text-align:center;"><img src="{base_auxiliar.loc[1,"IMG"]}"height="320"></p>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{base_auxiliar.loc[1,'synopsis']}</p>", unsafe_allow_html=True)

with col3:
    st.markdown(
    f'<h3 style="text-align:center; height:{50*tamanho_max}px;">{base_auxiliar.loc[2,"name"]}</h3>',
    unsafe_allow_html=True)
    st.write(f'<p style="text-align:center;"><img src="{base_auxiliar.loc[2,"IMG"]}"height="320"></p>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{base_auxiliar.loc[2,'synopsis']}</p>", unsafe_allow_html=True)




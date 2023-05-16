import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg

_lock = RendererAgg.lock

st.title('Data Summary')
st.image('images/penguins.jpg', use_column_width='always')

@st.cache_data
def load_data(path):
    data = pd.read_csv(path, index_col=0)
    return data

penguins = load_data('data/clean_penguins.csv')
st.write(penguins.head())

penguin_species = penguins.drop(columns=['island']).groupby(['species', 'sex']).mean()
st.dataframe(penguin_species)
st.table(penguin_species)

species= penguins['species'].value_counts()
st.bar_chart(species)

def plot_hist(data, title):
    fig, ax=plt.subplots()
    ax.hist(data, bins='auto', stacked=True)
    ax.set_title(title)
    return st.pyplot(fig)

cols = list(penguins.columns)
cols.remove('species')
with _lock:
    for col in cols:
        plot_hist(penguins[col], title=f'Distribution of {col}')
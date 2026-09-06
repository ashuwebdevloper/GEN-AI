import streamlit as st
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Load model
model = load_model('nextword_model.h5')


# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)


# Reverse word index
reverse_index = {
    idx: word
    for word, idx in tokenizer.word_index.items()
}


max_len = 44


def generate_text(seed_text, num_words=10):

    text = seed_text

    for _ in range(num_words):

        seq = tokenizer.texts_to_sequences([text])[0]

        padded = pad_sequences(
            [seq],
            maxlen=max_len,
            padding='pre'
        )

        pred = model.predict(
            padded,
            verbose=0
        )[0]

        pos = np.argmax(pred)

        word = reverse_index.get(pos, '')

        text += ' ' + word

    return text


st.title("Text Generation using LSTM")

seed_text = st.text_input(
    "Enter the seed text:"
)

num_words = st.number_input(
    "Enter the number of words to generate:",
    min_value=1,
    max_value=100,
    value=10,
    step=1
)


if st.button("Generate"):

    result = generate_text(
        seed_text,
        num_words
    )

    st.write("Generated Text:")
    st.write(result)
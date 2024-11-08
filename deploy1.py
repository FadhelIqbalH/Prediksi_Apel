import pandas as pd
import numpy as np
import pickle
import streamlit as st

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def prediksi(data):
    data_array = np.asarray(data, dtype=float)
    data_reshape = data_array.reshape(1,-1)
    pred = model.predict(data_reshape)
    print(pred)

    if (pred[0] == 0):
        return "apel anda tidak bagus"
    else:
        return "apel anda bagus"

def main():
    st.title("Prediksi kualitas apel")

    Size = st.text_input("Masukkan ukuran apel:")
    Weight = st.text_input("Masukkan berat apel:")
    Sweetness = st.text_input("Masukkan tingkat kemanisan apel:")
    Crunchiness = st.text_input("Maskkan tingkat kekasar""an apel:")
    Juiciness = st.text_input("Masukkan tingkat kesegaran apel:")
    Ripeness = st.text_input("Masukkan tingkat kematangan apel:")
    Acidity = st.text_input("Masukkan tingkat keasaman apel:")


    hasil = ''

    if st.button("Hasil prediksi apel"):
        hasil = prediksi([float(Size), float(Weight), float(Sweetness), float(Crunchiness), float(Juiciness), float(Ripeness), float(Acidity)])
    
    st.success(hasil)

if __name__ == '__main__':
    main()

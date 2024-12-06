import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    try:
        return pd.read_csv('datos.csv')
    except Exception as e:
        st.error(f"Error al cargar datos.csv: {str(e)}")
        return None

@st.cache_data
def load_geo_data():
    try:
        return pd.read_csv('Reg_Com_Urb.csv', sep=';', encoding='latin1')
    except Exception as e:
        st.error(f"Error al cargar Reg_Com_Urb.csv: {str(e)}")
        return None
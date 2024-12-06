import streamlit as st

def setup_page_config():
    st.set_page_config(
        page_title="Sistema de Predicción de Beneficios",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 24px;
            background-color: #f8f9fa;
            border-radius: 4px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #e9ecef;
        }
        </style>
    """, unsafe_allow_html=True)
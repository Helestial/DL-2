import streamlit as st
from modules.prediction import load_model_resources, make_prediction
from modules.data_loader import load_data, load_geo_data
from modules.ui import setup_page_config
from modules.statistics import display_statistics
from modules.forms import display_prediction_form

def main():
    # Setup page configuration
    setup_page_config()
    
    # Load resources
    model, label_encoders = load_model_resources()
    df = load_data()
    geo_data = load_geo_data()
    
    # Main layout
    st.title("Sistema de Predicción de Beneficios")
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["🔮 Predicción", "📊 Estadísticas"])
    
    with tab1:
        st.header("Predicción de Cobro de Beneficios")
        if model and label_encoders and geo_data is not None:
            result = display_prediction_form(geo_data, label_encoders)
            if result:
                make_prediction(model, result, label_encoders)
        else:
            st.error("Error al cargar los recursos necesarios.")
    
    with tab2:
        st.header("Análisis Estadístico")
        if df is not None:
            display_statistics(df, label_encoders)
        else:
            st.error("Error al cargar los datos para estadísticas.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
        Desarrollado por Rubén Galaz y Francisco Becker con apoyo de ChatGPT de OpenAI
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
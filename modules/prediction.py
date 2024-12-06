import os
import streamlit as st
from tensorflow.keras.models import load_model
import joblib
import numpy as pd

def load_model_resources():
    try:
        model = load_model('RedNeuronal.h5')
        label_encoders = joblib.load('label_encoders.pkl')
        return model, label_encoders
    except Exception as e:
        st.error(f"Error al cargar el modelo o encoders: {str(e)}")
        return None, None

def make_prediction(model, input_data, label_encoders):
    try:
        # Create prediction container with custom styling
        pred_container = st.container()
        with pred_container:
            st.markdown("""
                <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; 
                border-left: 5px solid #4CAF50;'>
                <h3 style='color: #2E7D32; margin-top: 0;'>Resultado de la Predicción</h3>
            """, unsafe_allow_html=True)
            
            # Transform input data
            input_df = pd.DataFrame([input_data])
            for col in input_df.columns:
                if col in label_encoders:
                    input_df[col] = label_encoders[col].transform(input_df[col])
            
            # Make prediction
            prediction_prob = model.predict(input_df)
            prediction = (prediction_prob > 0.5).astype(int)
            
            # Display results
            resultado = "NO COBRARÁ" if prediction[0][0] == 1 else "SÍ COBRARÁ"
            prob_percent = prediction_prob[0][0] * 100 if prediction[0][0] == 1 else (1 - prediction_prob[0][0]) * 100
            
            st.markdown(f"""
                <p style='font-size: 18px; margin-bottom: 10px;'>
                El beneficiario <strong>{resultado}</strong> su beneficio
                </p>
                <p style='color: #666;'>
                Probabilidad: <strong>{prob_percent:.1f}%</strong>
                </p>
                </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Error durante la predicción: {str(e)}")
import streamlit as st

def display_prediction_form(geo_data, label_encoders):
    with st.form("prediction_form"):
        st.markdown("""
            <style>
            .prediction-form {
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            </style>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Región y Comuna
            regiones = sorted(geo_data['REGION'].unique())
            region = st.selectbox("Región", regiones)
            
            comunas = sorted(geo_data[geo_data['REGION'] == region]['COMUNA'].unique())
            comuna = st.selectbox("Comuna", comunas)
            
            # Get urbanidad automatically
            urbanidad = geo_data[
                (geo_data['REGION'] == region) & 
                (geo_data['COMUNA'] == comuna)
            ]['URBANIDAD'].iloc[0]
            
            st.text_input("Urbanidad", urbanidad, disabled=True)
        
        with col2:
            # Demographic information
            sexo = st.selectbox("Sexo", ['FEMENINO', 'MASCULINO', 'INDETERMINADO'])
            nacionalidad = st.selectbox("Nacionalidad", ['CHILENO', 'EXTRANJERO'])
            ecivil = st.selectbox("Estado Civil", label_encoders['ECIVIL'].classes_)
        
        # Benefit information
        col3, col4 = st.columns(2)
        with col3:
            fpago = st.selectbox("Forma de Pago", label_encoders['FPAGO'].classes_)
            tipobeneficio = st.selectbox("Tipo de Beneficio", 
                                       label_encoders['TIPOBENEFICIO'].classes_)
        
        with col4:
            cobromarzo = st.selectbox("Cobro Marzo", label_encoders['COBROMARZO'].classes_)
        
        submitted = st.form_submit_button("Realizar Predicción", 
                                        use_container_width=True,
                                        type="primary")
        
        if submitted:
            return {
                'REGION': region,
                'COMUNA': comuna,
                'URBANIDAD': urbanidad,
                'SEXO': 'F' if sexo == 'FEMENINO' else 'M' if sexo == 'MASCULINO' else 'E',
                'NACIONALIDAD': 'C' if nacionalidad == 'CHILENO' else 'E',
                'ECIVIL': ecivil,
                'FPAGO': fpago,
                'TIPOBENEFICIO': tipobeneficio,
                'COBROMARZO': cobromarzo
            }
    
    return None
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def display_statistics(df, label_encoders):
    st.markdown("""
        <style>
        .stats-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Allow user to select fields for analysis
    col1, col2 = st.columns(2)
    with col1:
        field1 = st.selectbox(
            "Seleccione el primer campo para análisis",
            df.columns,
            key="field1"
        )
    
    with col2:
        field2 = st.selectbox(
            "Seleccione el segundo campo (opcional)",
            ["Ninguno"] + list(df.columns),
            key="field2"
        )
    
    if field2 == "Ninguno":
        # Single field analysis
        fig = create_single_field_chart(df, field1)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display additional statistics
        show_field_statistics(df, field1)
    else:
        # Two-field analysis
        fig = create_two_field_chart(df, field1, field2)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display correlation if numerical
        if df[field1].dtype.kind in 'inf' and df[field2].dtype.kind in 'inf':
            correlation = df[field1].corr(df[field2])
            st.metric("Correlación", f"{correlation:.2f}")

def create_single_field_chart(df, field):
    counts = df[field].value_counts()
    
    fig = go.Figure(data=[
        go.Bar(
            x=counts.index,
            y=counts.values,
            marker_color='rgb(55, 83, 109)'
        )
    ])
    
    fig.update_layout(
        title=f"Distribución de {field}",
        xaxis_title=field,
        yaxis_title="Cantidad",
        template="plotly_white",
        height=500
    )
    
    return fig

def create_two_field_chart(df, field1, field2):
    pivot_table = df.pivot_table(
        index=field1,
        columns=field2,
        aggfunc='size',
        fill_value=0
    )
    
    fig = go.Figure()
    
    for column in pivot_table.columns:
        fig.add_trace(
            go.Bar(
                name=str(column),
                x=pivot_table.index,
                y=pivot_table[column]
            )
        )
    
    fig.update_layout(
        barmode='group',
        title=f"Análisis cruzado: {field1} vs {field2}",
        xaxis_title=field1,
        yaxis_title="Cantidad",
        template="plotly_white",
        height=500
    )
    
    return fig

def show_field_statistics(df, field):
    st.markdown("### Estadísticas Detalladas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Registros", len(df))
    
    with col2:
        st.metric("Valores Únicos", df[field].nunique())
    
    with col3:
        if df[field].dtype.kind in 'inf':
            st.metric("Promedio", f"{df[field].mean():.2f}")
        else:
            mode_value = df[field].mode()[0]
            st.metric("Valor más común", mode_value)
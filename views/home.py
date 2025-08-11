import streamlit as st

def mostrar():
    st.title("bienvenido al simulador de creditos")
    st.markdown("""
        Esta aplicacion te permite simularcreditos hipotecarios
        Proximamente se conectara con supabase para guardar las simulaciones
    """)
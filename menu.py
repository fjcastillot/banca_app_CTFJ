import streamlit as st
from views import home, simulador, reportes

def mostrar_menu():
    opciones = {^
        "Iinicio" : home.mostrar,
        "Simulador de creditos" : simulador.mostrar,
        "Reportes" : reportes.mostrar,
    
    }
    seleccion = st.sidebar.selectbox("Navegacion",list(opciones.keys()))
    opciones[seleccion]()
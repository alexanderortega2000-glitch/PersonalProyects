# -*- coding: utf-8 -*-
import streamlit as st
from datetime import datetime

st.title("Cálculo de Bonificación")

# Entradas del usuario
fecha_contrato = st.date_input("Fecha de inicio de contrato")
salario = st.number_input("Salario mensual", min_value=0.0, step=0.01)

# Parámetros fijos
fecha_fin = datetime(2026, 1, 15)   # Fecha fin de cálculo
total_dias = 365                    # Días del año

if fecha_contrato and salario > 0:
    # Convertir fecha_contrato (date) a datetime
    fecha_contrato_dt = datetime.combine(fecha_contrato, datetime.min.time())
    
    # Calcular cantidad de días trabajados (incluyendo último día)
    dias_trabajados = (fecha_fin - fecha_contrato_dt).days + 1
    
    # Calcular salario aplicable
    salario_aplicable = salario / 2
    
    # Proporción de días
    proporcion_dias = dias_trabajados / total_dias
    
    # Bonificación
    bonificacion = salario_aplicable * proporcion_dias
    
    # Mostrar resultados
    st.write("### Resultados del cálculo")
    st.write(f"- Salario ingresado: ${salario:,.2f}")
    st.write(f"- Fecha inicio contrato: {fecha_contrato.strftime('%d/%m/%Y')}")
    st.write(f"- Fecha fin cálculo: {fecha_fin.strftime('%d/%m/%Y')}")
    st.write(f"- Salario aplicable (Salario / 2): ${salario_aplicable:,.2f}")
    st.write(f"- Cantidad de días: {dias_trabajados}")
    st.write(f"- Proporción de días: {proporcion_dias:.4f}")
    
    st.success(f"### Bonificación: ${bonificacion:,.2f}")

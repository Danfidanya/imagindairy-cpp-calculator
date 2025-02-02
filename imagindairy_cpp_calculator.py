import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def recommend_co2_savings_per_ton():
    # Based on dairy industry benchmarks, ~12.5 tons CO2e per ton of dairy protein is avoided
    return 12.5

def calculate_co2_savings(investment, production, co2_per_ton):
    total_co2_savings = production * co2_per_ton
    co2_per_dollar = total_co2_savings / investment if investment > 0 else 0
    return total_co2_savings, co2_per_dollar

# Streamlit UI
st.title("Imagindairy Climate Performance Potential (CPP) Calculator")

st.sidebar.header("Input Variables")

investment = st.sidebar.number_input("Investment Amount ($M)", min_value=1, max_value=5000, value=50) * 1_000_000
production = st.sidebar.number_input("Annual Production (tons)", min_value=10_000, max_value=1_000_000, value=500_000)

# Use recommended CO2 savings per ton
co2_per_ton = recommend_co2_savings_per_ton()

# Calculate CO2 savings
total_co2_savings, co2_per_dollar = calculate_co2_savings(investment, production, co2_per_ton)

# Display results
st.subheader("Results")
st.write(f"**Total CO2 Savings per Year:** {total_co2_savings:,.2f} tons")
st.write(f"**CO2 Savings per $1 Invested:** {co2_per_dollar:,.2f} tons")
st.write(f"**CO2 Savings per Ton of Dairy Displaced:** {co2_per_ton:,.2f} tons")

# Gauge Meter Visualization
st.subheader("Progress Toward 100M CPP Goal")

import plotly.graph_objects as go

target_cpp = 100_000_000  # 100M CPP Target
progress = min(total_co2_savings / target_cpp * 100, 100)  # Limit to 100%

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=progress,
    title={'text': "CPP Goal Achievement (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, 50], 'color': "red"},
            {'range': [50, 80], 'color': "yellow"},
            {'range': [80, 100], 'color': "green"}
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 100
        }
    }
))

st.plotly_chart(fig)

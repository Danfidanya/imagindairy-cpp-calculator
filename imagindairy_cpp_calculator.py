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

# Line Graph Visualization
st.subheader("CO2 Savings Over Investment Amount vs 100M CPP Target")

investment_values = np.linspace(1_000_000, 5_000_000_000, 100)  # Range from $1M to $5B
co2_savings_values = (investment_values / investment) * total_co2_savings

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(investment_values / 1_000_000, co2_savings_values / 1_000_000_000, color='blue', linewidth=2, label="Projected CO2 Savings")
ax.axhline(y=100, color='red', linestyle='--', label="100M CPP Target")
ax.set_xlabel("Investment Amount ($M)")
ax.set_ylabel("CO2 Savings (Billion Tons per Year)")
ax.set_title("CO2 Savings Based on Investment & Production")
ax.legend()
st.pyplot(fig)

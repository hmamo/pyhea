import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def radar_chart(mechanical_strength_HEAs, corrosion_resistance_HEAs, thermal_stability_HEAs,
                mechanical_strength_Steel, corrosion_resistance_Steel, thermal_stability_Steel,
                mechanical_strength_Aluminum, corrosion_resistance_Aluminum, thermal_stability_Aluminum):
    # Define the properties and their values for HEAs, Steel, and Aluminum
    properties = ['Mechanical Strength', 'Corrosion Resistance', 'Thermal Stability']
    values_HEAs = [mechanical_strength_HEAs, corrosion_resistance_HEAs, thermal_stability_HEAs]
    values_Steel = [mechanical_strength_Steel, corrosion_resistance_Steel, thermal_stability_Steel]
    values_Aluminum = [mechanical_strength_Aluminum, corrosion_resistance_Aluminum, thermal_stability_Aluminum]

    # Number of properties
    num_properties = len(properties)

    # Calculate angles for radar chart
    angles = np.linspace(0, 2 * np.pi, num_properties, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop"
    values_HEAs += values_HEAs[:1]
    values_Steel += values_Steel[:1]
    values_Aluminum += values_Aluminum[:1]
    angles += angles[:1]

    # Create the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values_HEAs, color='blue', alpha=0.25)
    ax.fill(angles, values_Steel, color='red', alpha=0.25)
    ax.fill(angles, values_Aluminum, color='green', alpha=0.25)

    # Draw axis lines for each property
    ax.plot(angles, values_HEAs, color='blue', linewidth=2, linestyle='solid')
    ax.plot(angles, values_Steel, color='red', linewidth=2, linestyle='solid')
    ax.plot(angles, values_Aluminum, color='green', linewidth=2, linestyle='solid')

    # Add labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(properties)

    # Add legend
    ax.legend(['HEAs', 'Steel', 'Aluminum'], loc='upper right')

    plt.title('Comparison of Properties: HEAs vs. Traditional Alloys')

    # Display plot in Streamlit
    st.pyplot(fig)

def main():
    st.title('Radar Chart Comparison')
    st.write('Comparison of Mechanical Strength, Corrosion Resistance, and Thermal Stability for HEAs, Steel, and Aluminum.')

    # Input fields for HEAs
    st.sidebar.header('HEAs')
    mechanical_strength_HEAs = st.sidebar.slider('Mechanical Strength (HEAs)', min_value=0, max_value=100, value=80)
    corrosion_resistance_HEAs = st.sidebar.slider('Corrosion Resistance (HEAs)', min_value=0, max_value=10, value=8)
    thermal_stability_HEAs = st.sidebar.slider('Thermal Stability (HEAs)', min_value=0, max_value=300, value=200)

    # Input fields for Steel
    st.sidebar.header('Steel')
    mechanical_strength_Steel = st.sidebar.slider('Mechanical Strength (Steel)', min_value=0, max_value=100, value=60)
    corrosion_resistance_Steel = st.sidebar.slider('Corrosion Resistance (Steel)', min_value=0, max_value=10, value=5)
    thermal_stability_Steel = st.sidebar.slider('Thermal Stability (Steel)', min_value=0, max_value=300, value=100)

    # Input fields for Aluminum
    st.sidebar.header('Aluminum')
    mechanical_strength_Aluminum = st.sidebar.slider('Mechanical Strength (Aluminum)', min_value=0, max_value=100, value=40)
    corrosion_resistance_Aluminum = st.sidebar.slider('Corrosion Resistance (Aluminum)', min_value=0, max_value=10, value=7)
    thermal_stability_Aluminum = st.sidebar.slider('Thermal Stability (Aluminum)', min_value=0, max_value=300, value=150)

    # Generate radar chart based on user input
    radar_chart(mechanical_strength_HEAs, corrosion_resistance_HEAs, thermal_stability_HEAs,
                mechanical_strength_Steel, corrosion_resistance_Steel, thermal_stability_Steel,
                mechanical_strength_Aluminum, corrosion_resistance_Aluminum, thermal_stability_Aluminum)

if __name__ == "__main__":
    main()

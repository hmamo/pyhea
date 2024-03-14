import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def radar_chart(values_HEAs, values_Steel, values_Aluminum):
    # Define the properties
    properties = ['Mechanical Strength', 'Corrosion Resistance', 'Thermal Stability']

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

    # Input values for each material
    values_HEAs = []
    values_Steel = []
    values_Aluminum = []

    for prop in ['Mechanical Strength', 'Corrosion Resistance', 'Thermal Stability']:
        values_HEAs.append(st.sidebar.slider(f'HEAs {prop}', min_value=0, max_value=100, value=50))
        values_Steel.append(st.sidebar.slider(f'Steel {prop}', min_value=0, max_value=100, value=50))
        values_Aluminum.append(st.sidebar.slider(f'Aluminum {prop}', min_value=0, max_value=100, value=50))

    radar_chart(values_HEAs, values_Steel, values_Aluminum)

if __name__ == "__main__":
    main()

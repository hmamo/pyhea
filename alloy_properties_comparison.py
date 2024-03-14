import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def radar_chart(values_HEAs, values_Steel, values_Aluminum, properties):
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

    # Define properties
    properties = ['Mechanical Strength', 'Corrosion Resistance', 'Thermal Stability']

    # Default values for each material's properties
    default_values_HEAs = [80, 8, 200]
    default_values_Steel = [60, 5, 100]
    default_values_Aluminum = [40, 7, 150]

    # Slider for HEAs
    st.sidebar.subheader('HEAs Values')
    values_HEAs = [st.sidebar.slider(prop, 0, 100, default_values_HEAs[idx], key=f'hea_slider_{idx}') for idx, prop in enumerate(properties)]

    # Slider for Steel
    st.sidebar.subheader('Steel Values')
    values_Steel = [st.sidebar.slider(prop, 0, 100, default_values_Steel[idx], key=f'steel_slider_{idx}') for idx, prop in enumerate(properties)]

    # Slider for Aluminum
    st.sidebar.subheader('Aluminum Values')
    values_Aluminum = [st.sidebar.slider(prop, 0, 200, default_values_Aluminum[idx], key=f'aluminum_slider_{idx}') for idx, prop in enumerate(properties)]

    # Show radar chart
    radar_chart(values_HEAs, values_Steel, values_Aluminum, properties)

if __name__ == "__main__":
    main()

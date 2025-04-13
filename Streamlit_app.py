import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Fibonacci-basierten Wellen
def calculate_elliott_waves(wave1_length):
    # Fibonacci-Verhältnisse für die Impulswellen
    fib_retracements = [0.236, 0.382, 0.5, 0.618]
    fib_extensions = [1.618, 2.618, 4.236]
    
    # Berechnung der Trendpunkte
    wave2_lengths = [wave1_length * fib for fib in fib_retracements]  # Korrekturwellen
    wave3_lengths = [wave1_length * fib for fib in fib_extensions]  # Impulswellen
    wave4_lengths = [wave3_length * 0.382 for wave3_length in wave3_lengths]  # Korrekturwellen
    wave5_lengths = [wave1_length * fib for fib in fib_extensions]  # Impulswellen
    
    # Berechnung der Trendpunkte
    trend_points = {
        "Wave 1 End": wave1_length,
        "Wave 2 End": wave1_length - wave2_lengths[1],  # Typische Korrektur bei 38,2%
        "Wave 3 End": wave1_length + wave3_lengths[0],  # Typische Erweiterung bei 161,8%
        "Wave 4 End": wave1_length + wave3_lengths[0] - wave4_lengths[0],  # Korrektur von Welle 3
        "Wave 5 End": wave1_length + wave3_lengths[0] + wave5_lengths[0],  # Erweiterung für Welle 5
    }
    
    return wave2_lengths, wave3_lengths, wave4_lengths, wave5_lengths, trend_points

# Streamlit-Interface
st.title('Elliott Wave Analysis mit Fibonacci')

# Eingabe für Welle 1
wave1_length = st.number_input('Länge von Welle 1 (z.B. 100):', min_value=1, value=100)

# Berechnungen durchführen
wave2_lengths, wave3_lengths, wave4_lengths, wave5_lengths, trend_points = calculate_elliott_waves(wave1_length)

# Visualisierung der Wellenverläufe
fig, ax = plt.subplots(figsize=(10, 6))

# Welle 1 (grün)
ax.plot([0, wave1_length], [0, wave1_length], label="Welle 1", color="green", lw=2)

# Welle 2 (rote Korrekturwelle)
ax.plot([wave1_length, wave1_length - wave2_lengths[1]], [wave1_length, wave1_length - wave2_lengths[1]], label="Welle 2 (38.2%)", color="red", lw=2)

# Welle 3 (blaue Impulswelle)
ax.plot([wave1_length - wave2_lengths[1], wave1_length - wave2_lengths[1] + wave3_lengths[0]], 
        [wave1_length - wave2_lengths[1], wave1_length - wave2_lengths[1] + wave3_lengths[0]], 
        label="Welle 3 (161.8%)", color="blue", lw=2)

# Welle 4 (orange Korrekturwelle)
ax.plot([wave1_length - wave2_lengths[1] + wave3_lengths[0], wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0]], 
        [wave1_length - wave2_lengths[1] + wave3_lengths[0], wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0]], 
        label="Welle 4 (38.2%)", color="orange", lw=2)

# Welle 5 (violette Impulswelle)
ax.plot([wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0], 
         wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0] + wave5_lengths[0]], 
        [wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0], 
         wave1_length - wave2_lengths[1] + wave3_lengths[0] - wave4_lengths[0] + wave5_lengths[0]], 
        label="Welle 5 (161.8%)", color="purple", lw=2)

# Trendpunkte
for label, value in trend_points.items():
    ax.annotate(f'{label}: {value:.2f}', xy=(value, value), xytext=(value + 5, value + 5),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Achsen und Labels
ax.set_xlabel('Zeit')
ax.set_ylabel('Preis')
ax.set_title('Elliott Wellen mit Fibonacci-Verhältnissen')
ax.legend()

# Graph anzeigen
st.pyplot(fig)

# Ausgabe der Trendpunkte
st.write("**Trendpunkte:**")
for label, value in trend_points.items():
    st.write(f"{label}: {value:.2f}")
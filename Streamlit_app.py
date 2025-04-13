import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Fibonacci-basierten Wellen
def calculate_elliott_waves(wave1_length, num_points=100):
    # Fibonacci-Verhältnisse für die Impulswellen
    fib_retracements = [0.236, 0.382, 0.5, 0.618]
    fib_extensions = [1.618, 2.618, 4.236]
    
    # Erstellen einer X-Achse (Zeitpunkte)
    x = np.linspace(0, wave1_length, num_points)
    
    # Berechnung der Wellen (Sinuswellen, um die Struktur zu erzeugen)
    wave2 = np.sin(x) * wave1_length * fib_retracements[1]  # Korrekturwelle
    wave3 = np.sin(x * 2) * wave1_length * fib_extensions[0]  # Impulswelle
    wave4 = np.sin(x * 0.5) * wave3.max() * 0.382  # Korrekturwelle
    wave5 = np.sin(x * 1.5) * wave1_length * fib_extensions[0]  # Impulswelle

    # Berechnung der Trendpunkte
    trend_points = {
        "Wave 1 End": wave1_length,
        "Wave 2 End": wave2[-1],  
        "Wave 3 End": wave3[-1],
        "Wave 4 End": wave4[-1],
        "Wave 5 End": wave5[-1],
    }

    return x, wave2, wave3, wave4, wave5, trend_points

# Streamlit-Interface
st.title('Elliott Wave Analysis mit Fibonacci')

# Eingabe für Welle 1
wave1_length = st.number_input('Länge von Welle 1 (z.B. 100):', min_value=1, value=100)

# Berechnungen durchführen
x, wave2, wave3, wave4, wave5, trend_points = calculate_elliott_waves(wave1_length)

# Visualisierung der Wellenverläufe
fig, ax = plt.subplots(figsize=(10, 6))

# Wellen zeichnen
ax.plot(x, wave2, label="Welle 2 (Korrektur)", color="red", lw=2)
ax.plot(x, wave3, label="Welle 3 (Impuls)", color="blue", lw=2)
ax.plot(x, wave4, label="Welle 4 (Korrektur)", color="orange", lw=2)
ax.plot(x, wave5, label="Welle 5 (Impuls)", color="purple", lw=2)

# Trendpunkte als vertikale Linien
for label, value in trend_points.items():
    ax.axhline(value, linestyle='--', label=f'{label}: {value:.2f}')

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
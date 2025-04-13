import streamlit as st
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Y-Werte der Wellen
def calculate_wave_y(wave1_length):
    # Fibonacci-basierte Längen
    wave2 = wave1_length * 0.382
    wave3 = wave1_length * 1.618
    wave4 = wave3 * 0.382
    wave5 = wave1_length * 1.0

    waveA = (wave5 - wave2) * 0.5
    waveB = waveA * 0.618
    waveC = waveA * 1.618

    # Y-Punkte (Preisverlauf)
    y0 = 0
    y1 = y0 + wave1_length
    y2 = y1 - wave2
    y3 = y2 + wave3
    y4 = y3 - wave4
    y5 = y4 + wave5
    yA = y5 - waveA
    yB = yA + waveB
    yC = yB - waveC

    y = [y0, y1, y2, y3, y4, y5, yA, yB, yC]
    return y

# Streamlit App
st.title("Elliott-Wellenstruktur (1–5 + A-B-C)")

# Eingabe für Welle 1
wave1_length = st.number_input("Länge der Welle 1", min_value=1, value=100)

# Berechne Wellenpunkte
y = calculate_wave_y(wave1_length)
x = list(range(len(y)))
labels = ["0", "1", "2", "3", "4", "5", "A", "B", "C"]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='Elliott-Wellenstruktur')

# Labels hinzufügen
for xi, yi, label in zip(x, y, labels):
    ax.annotate(label, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

ax.set_title("Elliott-Wellen (Impuls + Korrektur)")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")
ax.grid(True)
ax.legend()

# Plot anzeigen
st.pyplot(fig)

# Punktwerte anzeigen
st.write("**Punkte (Preislevels):**")
for label, value in zip(labels, y):
    st.write(f"Welle {label}: {value:.2f}")
import streamlit as st
import matplotlib.pyplot as plt

def calculate_wave_y(wave1_length, correction_type):
    wave2 = wave1_length * 0.382
    wave3 = wave1_length * 1.618
    wave4 = wave3 * 0.382
    wave5 = wave1_length * 1.0

    y0 = 0
    y1 = y0 + wave1_length
    y2 = y1 - wave2
    y3 = y2 + wave3
    y4 = y3 - wave4
    y5 = y4 + wave5

    if correction_type == "Zigzag":
        waveA = (y5 - y2) * 0.5
        waveB = waveA * 0.618
        waveC = waveA * 1.618
    elif correction_type == "Flat":
        waveA = (y5 - y2) * 0.382
        waveB = waveA * 1.0
        waveC = waveA * 1.0
    else:  # Custom (Default to Zigzag)
        waveA = (y5 - y2) * 0.5
        waveB = waveA * 0.5
        waveC = waveA * 1.0

    yA = y5 - waveA
    yB = yA + waveB
    yC = yB - waveC

    return [y0, y1, y2, y3, y4, y5, yA, yB, yC]

# Streamlit UI
st.title("Elliott-Wellenstruktur (1–5 + A-B-C) mit Korrekturtypen")

# Eingaben
wave1_length = st.number_input("Länge der Welle 1", min_value=1, value=100)
y_offset = st.number_input("Y-Offset (Startpreis)", value=0)
x_offset = st.number_input("X-Offset (Startzeitpunkt)", value=0)
correction_type = st.selectbox("Korrekturtyp", ["Zigzag", "Flat", "Custom"])

# Berechnung + Offset
y = [val + y_offset for val in calculate_wave_y(wave1_length, correction_type)]
x = [i + x_offset for i in range(len(y))]
labels = ["0", "1", "2", "3", "4", "5", "A", "B", "C"]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

# Impulswellen (0–5)
ax.plot(x[:6], y[:6], marker='o', linestyle='-', color='blue', label='Impulswellen (1–5)')

# Korrekturwellen (5–C)
ax.plot(x[5:], y[5:], marker='o', linestyle='--', color='red', label=f'Korrekturwellen (A–C) – {correction_type}')

# Labels
for xi, yi, label in zip(x, y, labels):
    ax.annotate(label, (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')

ax.set_title("Elliott-Wellenstruktur")
ax.set_xlabel("Zeit")
ax.set_ylabel("Preis")
ax.grid(True)
ax.legend()

st.pyplot(fig)

# Trendpunkte anzeigen
st.write("**Punkte (Preislevels):**")
for label, value in zip(labels, y):
    st.write(f"Welle {label}: {value:.2f}")
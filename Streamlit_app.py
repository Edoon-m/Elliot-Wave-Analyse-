import streamlit as st
import matplotlib.pyplot as plt

# Funktion zur Berechnung der Impuls- und Korrekturwellen
def calculate_elliott_waves(wave1_length):
    fib_retracements = [0.236, 0.382, 0.5, 0.618]
    fib_extensions = [1.618, 2.618, 4.236]

    # Impulswellen
    wave2 = wave1_length * fib_retracements[1]  # 38.2% Korrektur
    wave3 = wave1_length * fib_extensions[0]    # 161.8% Extension
    wave4 = wave3 * 0.382                        # 38.2% Korrektur von Welle 3
    wave5 = wave1_length * fib_extensions[0]    # gleich wie Welle 3

    # Preislevels (Y)
    p0 = 0
    p1 = p0 + wave1_length
    p2 = p1 - wave2
    p3 = p2 + wave3
    p4 = p3 - wave4
    p5 = p4 + wave5

    # Korrekturwellen A-B-C (ABC startet nach p5)
    waveA = (p5 - p2) * 0.5   # Korrektur auf halben Weg zurück zu Welle 2
    waveB = waveA * 0.618     # leichte Erholung
    waveC = waveA * 1.618     # tiefer als A

    pA = p5 - waveA
    pB = pA + waveB
    pC = pB - waveC

    # X- und Y-Werte
    x = list(range(9))
    y = [p0, p1, p2, p3, p4, p5, pA, pB, pC]

    labels = ["0", "1", "2", "3", "4", "5", "A", "B", "C"]
    trend_points = dict(zip([f"Welle {l}" for l in labels], y))

    return x, y, labels, trend_points

# Streamlit UI
st.title('Elliott Wave Analyse (1–5 + A-B-C) mit Fibonacci')

wave1_length = st.number_input('Länge von Welle 1 (z.B. 100):', min_value=1, value=100)

# Berechnung
x, y, labels, trend_points = calculate_elliott_waves(wave1_length)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, marker='o', linewidth=2, label='Elliott Wellenstruktur')

# Beschriftung
for i, label in enumerate(labels):
    ax.annotate(f'{label}', (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

ax.set_xlabel('Zeit')
ax.set_ylabel('Preis')
ax.set_title('Elliott Wellen 1–5 + A-B-C')
ax.grid(True)
ax.legend()

# Anzeige in Streamlit
st.pyplot(fig)

# Trendpunkte anzeigen
st.write("**Trendpunkte (Preislevels):**")
for k, v in trend_points.items():
    st.write(f"{k}: {v:.2f}")
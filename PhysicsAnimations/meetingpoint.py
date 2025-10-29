import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# ======================================================
# CRIAR PASTA PARA GIF
# ======================================================
os.makedirs("gifs", exist_ok=True)

# ======================================================
# DADOS DO PROBLEMA
# ======================================================
v_marta = 80 / 60   # km/min
v_pedro = 100 / 60  # km/min
tempo_total = 30  # minutos a partir do instante que Pedro começa (0,5h)

# ======================================================
# VETOR DE TEMPO
# ======================================================
t = np.linspace(0, tempo_total, 300)
t_h = t / 60  # tempo em horas

# ======================================================
# CÁLCULO DAS POSIÇÕES (a partir do instante em que Pedro começa)
# ======================================================
S_marta = 10 + v_marta * t
S_pedro = 0 + v_pedro * t

# ======================================================
# PONTO DE ENCONTRO
# ======================================================
t_encontro = 30  # min = 0,5h
pos_encontro = 10 + v_marta * (t_encontro)  # 50 km

# ======================================================
# CONFIGURAÇÃO DOS GRÁFICOS
# ======================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# -------- Gráfico 1: Estrada --------
ax1.set_xlim(0, 60)
ax1.set_ylim(-2, 2)
ax1.set_xlabel("Posição (km)")
ax1.set_yticks([])
ax1.set_title("Estrada – Encontro de Marta e Pedro")
marta_point, = ax1.plot([], [], 'ro', label="Marta")
pedro_point, = ax1.plot([], [], 'bo', label="Pedro")
linha_encontro = ax1.axvline(pos_encontro, color='green', linestyle='--',
                             label=f"Encontro ({pos_encontro:.1f} km)")
ax1.legend()

# -------- Gráfico 2: Posição × Tempo --------
ax2.set_xlim(0, (tempo_total / 60) + 0.1)
ax2.set_ylim(0, 60)
ax2.set_xlabel("Tempo (h)")
ax2.set_ylabel("Posição (km)")
ax2.set_title("Gráfico S × t (a partir do instante que Pedro inicia)")

linha_marta, = ax2.plot([], [], 'r-', label="Marta")
linha_pedro, = ax2.plot([], [], 'b-', label="Pedro")

# Linha vertical do tempo de encontro
linha_tempo_encontro = ax2.axvline(t_encontro / 60, color='green', linestyle='--',
                                   label=f"Tempo encontro ({t_encontro/60:.2f} h)")
ax2.legend()

# ======================================================
# FUNÇÃO DE ATUALIZAÇÃO
# ======================================================
def update(frame):
    marta_point.set_data([S_marta[frame]], [0.5])
    pedro_point.set_data([S_pedro[frame]], [-0.5])
    linha_marta.set_data(t_h[:frame], S_marta[:frame])
    linha_pedro.set_data(t_h[:frame], S_pedro[:frame])
    return marta_point, pedro_point, linha_marta, linha_pedro

# ======================================================
# CRIA E SALVA ANIMAÇÃO
# ======================================================
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=False)
writer = PillowWriter(fps=15)
ani.save("gifs/encontro_marta_pedro_final.gif", writer=writer)

print("✅ Animação salva como 'gifs/encontro_marta_pedro_final.gif'")

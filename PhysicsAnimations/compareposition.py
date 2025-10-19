import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import time

# =====================
# Dados do problema
# =====================
vA = 3.0      # m/s (corredor A)
vB = 3.5      # m/s (corredor B)
SA0 = -900    # posição inicial de A
SB0 = -1200   # posição inicial de B

# Tempo total da animação (um pouco depois da chegada de B)
t_total = 650  # segundos
dt = 1         # passo de tempo
t = np.arange(1, t_total + dt, dt)

# Posições
SA = SA0 + vA * t
SB = SB0 + vB * t

# =====================
# Configuração do gráfico
# =====================
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlim(0, t_total)
ax.set_ylim(min(SB0, SA0) - 100, max(SA[-1], SB[-1]) + 50)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Posição (m)")
ax.set_title("Corrida: Corredor A vs Corredor B")

# Linha de chegada
ax.axhline(0, color='black', linestyle='--', label='Chegada (S=0)', alpha=0.4)

# Linhas das posições iniciais
#ax.axhline(SA0, color='blue', linestyle=':', alpha=0.5)
#ax.axhline(SB0, color='green', linestyle=':', alpha=0.5)

# Textos das posições iniciais
ax.text(15, SA0 + 1200, f'Sₐ₀ = {SA0} m', color='blue', fontsize=16)
ax.text(15, SB0 + 1400, f'Sᵦ₀ = {SB0} m', color='green', fontsize=16)

# Ticks personalizados no eixo Y (para garantir visibilidade das posições iniciais)
ax.set_yticks(np.arange(SB0 - 100, max(SA[-1], SB[-1]) + 100, 100))

# Pontos e trajetórias
pointA, = ax.plot([], [], 'bo', label='Corredor A')
pointB, = ax.plot([], [], 'go', label='Corredor B')
lineA, = ax.plot([], [], 'b--', alpha=0.9)
lineB, = ax.plot([], [], 'g--', alpha=0.9)

# Texto do tempo
tempo_text = ax.text(0.75, 1.1, '', transform=ax.transAxes, fontsize=12, color='red')

ax.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# =====================
# Função de animação
# =====================
def animate(i):
    i = min(i, len(t) - 1)

    # Atualiza pontos e linhas
    pointA.set_data([t[i]], [SA[i]])
    pointB.set_data([t[i]], [SB[i]])
    lineA.set_data(t[:i+1], SA[:i+1])
    lineB.set_data(t[:i+1], SB[:i+1])

    # Atualiza texto do tempo
    tempo_text.set_text(f"t = {t[i]:.0f}s")

    if t[i] == 301 or t[i] == 601:
        time.sleep(5)

    return pointA, pointB, lineA, lineB, tempo_text

# =====================
# Criação da animação
# =====================
ani = FuncAnimation(fig, animate, frames=len(t), interval=50)
writer = PillowWriter(fps=100)
ax.axhline(-150, color='red', linestyle=':', alpha=0.5)
ax.axhline(900, color='red', linestyle=':', alpha=0.5)
ani.save("gifs/compareposition.gif", writer=writer)

plt.show()
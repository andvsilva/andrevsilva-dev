import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.patches as patches
import os

# ======================================================
# CRIAR PASTA PARA GIF
# ======================================================
os.makedirs("gifs", exist_ok=True)

# ======================================================
# DADOS DO PROBLEMA
# ======================================================
L_t = 34      # comprimento do caminhão (m)
L_c = 4       # comprimento do carro (m)
v_c = 30      # velocidade do carro (m/s)
v_t = 26      # velocidade do caminhão (m/s)
t_total = 12  # tempo total de animação (s)
t_ultrapassagem = 8.5  # momento em que o carro termina de ultrapassar

# ======================================================
# CONFIGURAÇÃO DE ANIMAÇÃO
# ======================================================
fps = 50
frames = int(t_total * fps)
tempos = np.linspace(0, t_total, frames)

# ======================================================
# POSIÇÕES INICIAIS AJUSTADAS
# ======================================================
x_caminhao_0 = 34.0
x_carro_0 = x_caminhao_0 - L_c

x_carro = x_carro_0 + v_c * tempos
x_caminhao = x_caminhao_0 + v_t * tempos

# ======================================================
# FIGURA COM DOIS GRÁFICOS
# ======================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), gridspec_kw={'height_ratios': [2, 1]})
plt.tight_layout(pad=3)

# ======================================================
# ESTRADA E VEÍCULOS
# ======================================================
x_min, x_max = -10, max(x_carro[-1], x_caminhao[-1]) + 10
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(-0.5, 3.5)
ax1.axis('off')

ax1.fill_between([x_min, x_max], 0, 3, color='gray', alpha=0.4)
ax1.plot([x_min, x_max], [1.45, 1.45], 'w--', linewidth=2)

carro = patches.Rectangle((x_carro_0, 0.5), L_c, 0.5, color='blue', label='Carro')
caminhao = patches.Rectangle((x_caminhao_0, 1.5), L_t, 1.0, color='orange', label='Caminhão')
ax1.add_patch(carro)
ax1.add_patch(caminhao)

tempo_texto = ax1.text(0.02, 0.9, '', transform=ax1.transAxes, fontsize=12, color='black')
ax1.legend(loc='upper right')

# ======================================================
# GRÁFICO POSIÇÃO × TEMPO
# ======================================================
ax2.set_xlim(0, t_total)
ax2.set_ylim(0, 600)
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Posição (m)')
ax2.grid(True, linestyle='--', alpha=0.6)

linha_carro, = ax2.plot(tempos, x_carro, color='blue', linewidth=2.5, label='Carro')
linha_caminhao, = ax2.plot(tempos, x_caminhao, color='orange', linewidth=2.5, label='Caminhão')

ax2.fill_between(tempos, x_caminhao, x_carro,
                 where=(x_carro > x_caminhao),
                 color='lightblue', alpha=0.3,
                 label='Carro à frente')

# Linha vertical no momento da ultrapassagem
linha_vertical = ax2.axvline(x=t_ultrapassagem+0.5, color='red', linestyle='--', linewidth=2, label='Fim da ultrapassagem')
linha_vertical_estrada = ax1.plot([300,300], [0,3], color='red', linestyle='--', linewidth=2, label='Fim da ultrapassagem')[0]


ponto_carro, = ax2.plot([], [], 'o', color='blue', markersize=8)
ponto_caminhao, = ax2.plot([], [], 'o', color='orange', markersize=8)

ax2.legend(loc='upper left')

ax2.text(t_total / 2, x_carro[int(frames/2)] + 8,
         "Ultrapassagem concluída", color='blue', fontsize=10, ha='center')

# ======================================================
# FUNÇÃO DE ATUALIZAÇÃO
# ======================================================
def update(frame):
    t = tempos[frame]
    pos_carro_x = x_carro_0 + v_c * t
    pos_caminhao_x = x_caminhao_0 + v_t * t

    carro.set_x(pos_carro_x)
    caminhao.set_x(pos_caminhao_x)

    ponto_carro.set_data([t], [pos_carro_x])
    ponto_caminhao.set_data([t], [pos_caminhao_x])

    tempo_texto.set_text(f"Tempo = {t:.1f} s")
    ax1.set_title("Carro alinhado com a traseira do caminhão no início", fontsize=11)

    return carro, caminhao, tempo_texto, ponto_carro, ponto_caminhao

# ======================================================
# ANIMAÇÃO
# ======================================================
anim = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# ======================================================
# SALVAR COMO GIF
# ======================================================
gif_path = "gifs/ultrapassagem.gif"
writer = PillowWriter(fps=fps)
anim.save(gif_path, writer=writer)

print(f"GIF salvo em: {gif_path}")

plt.show()

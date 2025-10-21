import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# =====================
# Dados do problema
# =====================
x = np.array([0, 2, 4, 6, 10, 12])  # tempo (s)
y = np.array([3, 7, 9.5, 10.5, 15, 16])  # posição (m)

# Ajuste linear (reta)
coef = np.polyfit(x, y, 1)
a, b = coef
y_ajuste = a * x + b

# Impressão da equação
print(f"Equação da reta: y = {a:.2f}x + {b:.2f}")

# =====================
# Criação da figura
# =====================
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(-1, 13)
ax.set_ylim(0, 18)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Posição (m)')
ax.set_title('Ajuste Linear e Estimativa de Velocidade')
ax.grid(True, linestyle='--', alpha=0.5)

# Pontos e linha
line, = ax.plot([], [], 'b-', lw=2, label='Ajuste Linear')
points, = ax.plot([], [], 'ro', label='Dados Experimentais')

# Elementos do triângulo
triangulo, = ax.plot([], [], 'g--', lw=2)
texto_dt = ax.text(0, 0, '', color='g', fontsize=12, ha='center')
texto_ds = ax.text(0, 0, '', color='g', fontsize=12, va='center', rotation=90)
texto_v = ax.text(0, 0, '', color='blue', fontsize=12, fontweight='bold')
angulo_text = ax.text(0, 0, '', color='purple', fontsize=12)

ax.legend()

# =====================
# Função de animação
# =====================
def animate(i):
    if i < len(x):
        # Mostrar pontos um a um
        points.set_data(x[:i+1], y[:i+1])
    else:
        # Mostrar linha de ajuste
        line.set_data(x, y_ajuste)

        # Quando a linha completa, desenhar o triângulo
        x1, x2 = 0, 10
        y1, y2 = a*x1 + b, a*x2 + b

        # Coordenadas do triângulo (ΔS, Δt)
        xt = [x1, x2, x2, x1]
        yt = [y1, y1, y2, y1]
        triangulo.set_data(xt, yt)

        # Rótulos Δt e ΔS
        texto_dt.set_position(((x1 + x2) / 2, y1 - 0.9))
        texto_dt.set_text('Δt')
        texto_ds.set_position((x2 + 0.3, (y1 + y2) / 2))
        texto_ds.set_text('ΔS')

        # Texto velocidade
        texto_v.set_position((x2 -3, (y1 + y2) / 2 - 2))
        texto_v.set_text('v = ΔS/Δt')  # {a:.2f} m/s

        # Ângulo (opcional: θ)
        angulo_text.set_position((x1 + 0.5, y1 + 0.5))
        #angulo_text.set_text('θ')

    return points, line, triangulo, texto_dt, texto_ds, texto_v, angulo_text

# =====================
# Execução da animação
# =====================
ani = FuncAnimation(fig, animate, frames=len(x)+10, interval=500, blit=True)
plt.tight_layout()

# Salvar como GIF
ani.save("gifs/spacextime.gif", writer=PillowWriter(fps=1))
plt.show()

print("✅ GIF gerado com sucesso: spacextime.gif")

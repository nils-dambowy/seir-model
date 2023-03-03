import tkinter as tk
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def deriv(y, t, N, beta, gamma):
    S, I ,R = y
    dS = -beta* S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return dS, dI, dR


def update_plot(canvas, ax, t, S, I, R):
    ax.clear()
    print("update")
    ax.plot(t, S/1000, 'r', alpha=0.5, lw=2, label="Susceptible")
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label="Infected")
    ax.plot(t, R/1000, 'r', alpha=0.5, lw=2, label="Recovered")
    ax.set_xlabel("Time/days")
    ax.set_ylabel("Number (1000s)")
    ax.set_ylim(0, 1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)

    canvas.draw()

def main(x):
    pop = x
    init_infec = 1
    init_recov = 0
    init_suscep = pop - init_infec - init_recov
    beta, gamma = 0.2, 1./10

    t = np.linspace(0, 160, 160)

    y0 = init_suscep, init_infec, init_recov

    ret = odeint(deriv, y0, t, args=(pop, beta, gamma))
    S, I, R = ret.T

    fig =  plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd')
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label="Susceptible")
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label="Infected")
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label="Recovered")
    ax.set_xlabel("Time/days")
    ax.set_ylabel("Number (1000s)")
    ax.set_ylim(0, 1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)

    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)


    
    
    root = tk.Tk()

    root.geometry("1000x400")
    root.resizable(width=False, height=False)

    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    b1 = tk.Button(root, text="Plot", command= lambda:update_plot(canvas, ax, t, S, I, R))
    b1.pack()
    #plt.show()

    root.mainloop()
   



if __name__ == "__main__":
    main(1000)
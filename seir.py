import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def deriv(y, t, N, alpha, beta, gamma):
    S, E, I , R = y
    dS = -beta* S * I / N
    dE = beta * S * I / N - alpha * E
    dI = alpha * E - gamma * I
    dR = gamma * I
    return dS, dE, dI, dR

def update_plot(canvas, ax, t, entries, S, E, I, R):
    ax.clear()
    pop,  init_exposed, init_infec, init_recov, alpha, beta, gamma = entries
    y0 = int(pop.get()), int(init_exposed.get()), int(init_infec.get()), int(init_recov.get())
    ret = odeint(deriv, y0, t, args= (int(pop.get()), float(alpha.get()), float(beta.get()), float(gamma.get())))
    S, E, I, R = ret.T

    ax.plot(t, S/int(pop.get()), 'b', alpha=0.5, lw=2, label="Susceptible")
    ax.plot(t, E/int(pop.get()), 'y', alpha=0.5, lw=2, label="Exposed")
    ax.plot(t, I/int(pop.get()), 'r', alpha=0.5, lw=2, label="Infected")
    ax.plot(t, R/int(pop.get()), 'g', alpha=0.5, lw=2, label="Recovered")
    ax.set_xlabel("Time/days")
    ax.set_ylabel("Number ({}s)".format(str(pop.get())))
    ax.set_ylim(0, 1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    legend=ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)

    canvas.draw()

def on_closing(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"): 
        root.quit()
        root.destroy()

def main(x):
    pop          = x
    init_infec   = 1
    init_recov   = 0
    init_exposed = 0
    init_suscep  = pop - init_infec - init_recov
    alpha, beta, gamma = 0.3, 0.2, 1./10

    t = np.linspace(0, 160, 160)

    y0 = init_suscep, init_exposed, init_infec, init_recov

    ret = odeint(deriv, y0, t, args= (pop, alpha, beta, gamma))
    S, E, I, R = ret.T

    fig =  plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd')
    ax.plot(t, S/pop, 'b', alpha=0.5, lw=2, label="Susceptible")
    ax.plot(t, E/pop, 'y', alpha=0.5, lw=2, label="Exposed")
    ax.plot(t, I/pop, 'r', alpha=0.5, lw=2, label="Infected")
    ax.plot(t, R/pop, 'g', alpha=0.5, lw=2, label="Recovered")
    ax.set_xlabel("Time/days")
    ax.set_ylabel("Number ({}s)".format(str(pop)))
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
     
    l1 = tk.Label(root, text="Population: ").pack()
    e1 = tk.Entry(root)
    e1.pack()

    test2 = ""
    l2 = tk.Label(root, text="Initial amount of infected people: ").pack()
    e2 = tk.Entry(root)
    e2.pack()

    test3 = ""
    l3 = tk.Label(root, text="Init amount exposed: ").pack()
    e3 = tk.Entry(root)
    e3.pack()

    test4 = ""
    l4 = tk.Label(root, text="Init amount recovered: ").pack()
    e4 = tk.Entry(root)
    e4.pack()

    test5 = ""
    l5 = tk.Label(root, text="Alpha: ").pack()
    e5 = tk.Entry(root)
    e5.pack()

    test6 = ""
    l6 = tk.Label(root, text="Beta: ").pack()
    e6 = tk.Entry(root)
    e6.pack()

    test7 = ""
    l7 = tk.Label(root, text="Gamma: ").pack()
    e7 = tk.Entry(root)
    e7.pack()

    entries = e1, e2, e3, e4, e5, e6, e7

    b1 = tk.Button(root, text="Plot", command= lambda:update_plot(canvas, ax, t, entries,S, E, I, R))
    b1.pack()




    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

    root.mainloop()

if __name__ == "__main__":
    main(1000)
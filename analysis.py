import solvers
import matplotlib.pyplot as plt

def stability_warmup_f(t: float, y: float) -> float:
    a1 = 1
    return -1 * a1 * y

def stability_warmup() -> None:
    yi = 1
    ti = 0
    tf = 10
    nSteps1 = 4
    nSteps2 = 10
    nSteps3 = 20
    t1, y1 = solvers.euler(stability_warmup_f, yi, ti, tf, nSteps1)
    t2, y2 = solvers.euler(stability_warmup_f, yi, ti, tf, nSteps2)
    t3, y3 = solvers.euler(stability_warmup_f, yi, ti, tf, nSteps3)
    plt.plot(t1, y1, label="h = 2.5")
    plt.plot(t2, y2, label="h = 1.0")
    plt.plot(t3, y3, label="h = 0.5")
    plt.xlabel("Time")
    plt.ylabel("y(t)")
    plt.legend()
    plt.show()

stability_warmup()
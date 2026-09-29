import numpy as np
from typing import Callable
def validation(y_i: float | list | tuple, t_i: float, t_f: float, n_steps: int) -> None:
    if n_steps < 1 or not isinstance(n_steps, int):
        raise ValueError("Number of steps must be a positive integer")
    elif t_f <= t_i:
        raise ValueError("Final time must be greater than initial time")
    elif np.asarray(y_i).ndim > 1:
        raise ValueError("Y_i must be one-dimensional")
    
def euler(f: Callable, y_i: float | list | tuple, t_i: float, t_f: float, n_steps: int) -> tuple[list, list]:
    validation(y_i, t_i, t_f, n_steps)
    h = (t_f - t_i) / (n_steps)
    t  = []
    y = []
    y.append(np.asarray(y_i, dtype = float))
    t.append(t_i)
    for i in range(n_steps):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)

    return t, y

def euler_cromer(f: Callable, y_i: tuple[float, float], t_i: float, t_f: float, n_steps: int) -> tuple[list, list]:
    validation(y_i, t_i, t_f, n_steps)
    h = (t_f - t_i) / (n_steps)
    t  = []
    y = []
    x = y_i[0]
    v = y_i[1]
    y.append([x,v])
    t.append(t_i)
    for i in range(n_steps):
        v = y[-1][1] + h * f(t[-1], [y[-1][0],y[-1][1]])[1]
        x = y[-1][0] + h * v
        t.append(t[-1] + h)
        y.append([x,v])
    return t, y


def rk4(f: Callable, y_i: float | list | tuple, t_i: float, t_f: float, n_steps: int) -> tuple[list, list]:
    validation(y_i, t_i, t_f, n_steps)
    h = (t_f - t_i) / n_steps
    t = []
    y = []
    y.append(np.asarray(y_i, dtype=float))
    t.append(t_i)
    for i in range(n_steps):
        k1 = np.asarray(f(t[-1], y[-1]))
        k2 = np.asarray(f(t[-1] + h/2, y[-1] + (h/2) * k1))
        k3 = np.asarray(f(t[-1] + h/2, y[-1] + (h/2) * k2))
        k4 = np.asarray(f(t[-1] + h, y[-1] + h * k3))
        y.append(y[-1] + (h/6) * (k1 + 2*k2 + 2*k3 + k4))
        t.append(t[-1] + h)

    return t, y
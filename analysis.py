def euler(f, y_i, t_i, t_f, n_steps):
    h = (t_f - t_i) / (n_steps + 1)
    t  = []
    y = []
    y.append(y_i)
    t.append(t_i)
    for i in range(1, n_steps):
        y.append(y[-1] + h * f(t[-1], y[-1]))
        t.append(t[-1] + h)
        i+=1
    return t, y

def euler_cromer(f, y_i: tuple[float, float], t_i, t_f, n_steps):
    h = (t_f - t_i) / (n_steps + 1)
    t  = []
    y = []
    v = []
    y.append(y_i[0])
    v.append(y_i[1])
    t.append(t_i)
    for i in range(1, n_steps):
        v.append(v[-1] + h * f(t[-1], v[-1]))
        y.append(y[-1] + h * v[-1])
        i+=1
    return t, y


def rk4(f, y_i, t_i, t_f, n_steps):
    h = (t_f - t_i) / (n_steps + 1)
    t  = []
    y = []
    y.append(y_i)
    t.append(t_i)
    for i in range(1, n_steps):
        k1 = f(t[-1], y[-1])
        k2 = f(t[-1] + h/2, y[-1] + (h/2) * k1)
        k3 = f(t[-1] + h/2, y[-1] + (h/2) * k2)
        k4 = f(t[-1] + h, y[-1] + h * k3)
        y.append(y[-1] + (h/6) * (k1 + 2*k2 + 2*k3 + k4))
        t.append(t[-1] + h)
                
                
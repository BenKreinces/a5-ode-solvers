import solvers
import matplotlib.pyplot as plt
import numpy as np

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
    plt.xlabel("Time (s)")
    plt.ylabel("Position")
    plt.legend()
    plt.show()

def sho_helper(t: float, y: np.ndarray) -> np.ndarray:
    w = 1
    x = y[0]
    v = y[1]
    return np.array([v, -(w**2) * x])

def simple_harmonic_oscillator() -> None:
    yi = (1, 0)
    ti = 0
    tf = 30
    nSteps = 300
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1,3,1)
    ax2 = fig1.add_subplot(1,3,2)
    ax3 = fig1.add_subplot(1,3,3)
    fig1.subplots_adjust(left=0.08, right=0.98, bottom=0.12, top=0.92, wspace=.48)
    
    t1, y1 = solvers.euler(sho_helper, yi, ti, tf, nSteps)
    t2, y2 = solvers.euler_cromer(sho_helper, yi, ti, tf, nSteps)
    t3, y3 = solvers.rk4(sho_helper, yi, ti, tf, nSteps)
    y1 = np.array(y1)
    y2 = np.array(y2)
    y3 = np.array(y3)
    ax1.plot(t1, y1[:,0], label="Euler")
    ax1.plot(t2, y2[:,0], label="Euler-Cromer")
    ax1.plot(t3, y3[:,0], label="RK4")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Position")
    ax1.legend()
    ax2.plot(y1[:,0], y1[:,1], label="Euler")
    ax2.plot(y2[:,0], y2[:,1], label="Euler-Cromer")
    ax2.plot(y3[:,0], y3[:,1], label="RK4")
    ax2.set_xlabel("Position")
    ax2.set_ylabel("Velocity")
    ax2.legend()
    w = 1
    E1 = 0.5 * y1[:,1]**2 + 0.5 * w**2 * y1[:,0]**2
    E2 = 0.5 * y2[:,1]**2 + 0.5 * w**2 * y2[:,0]**2
    E3 = 0.5 * y3[:,1]**2 + 0.5 * w**2 * y3[:,0]**2
    ax3.plot(t1, E1, label="Euler")
    ax3.plot(t2, E2, label="Euler-Cromer")
    ax3.plot(t3, E3, label="RK4")
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Energy")
    ax3.legend()
    plt.show()



def dho_helper_under(t: float, y: np.ndarray) -> np.ndarray:
    beta = 0.2
    w = 1
    x = y[0]
    v = y[1]
    return np.array([v, -2 * beta * v - w**2 * x])

def dho_helper_crit(t: float, y: np.ndarray) -> np.ndarray:
    beta = 1.0
    w = 1
    x = y[0]
    v = y[1]
    return np.array([v, -2 * beta * v - w**2 * x])

def dho_helper_over(t: float, y: np.ndarray) -> np.ndarray:
    beta = 2.0
    w = 1
    x = y[0]
    v = y[1]
    return np.array([v, -2 * beta * v - w**2 * x])

def damped_harmonic_oscillator() -> None:
    yi = (1, 0)
    ti = 0
    tf = 30
    nSteps = 300
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1,2,1)
    ax3 = fig1.add_subplot(1,2,2)
    fig1.subplots_adjust(left=0.08, right=0.98, bottom=0.12, top=0.92, wspace=.48)
    t1, y1 = solvers.rk4(dho_helper_under, yi, ti, tf, nSteps)
    t2, y2 = solvers.rk4(dho_helper_crit, yi, ti, tf, nSteps)
    t3, y3 = solvers.rk4(dho_helper_over, yi, ti, tf, nSteps)
    y1 = np.array(y1)
    y2 = np.array(y2)
    y3 = np.array(y3)
    ax1.plot(t1, y1[:,0], label="Underdamped")
    ax1.plot(t2, y2[:,0], label="Critically Damped")
    ax1.plot(t3, y3[:,0], label="Overdamped")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Position")
    ax1.legend()
    w = 1
    E1 = 0.5 * y1[:,1]**2 + 0.5 * w**2 * y1[:,0]**2
    E2 = 0.5 * y2[:,1]**2 + 0.5 * w**2 * y2[:,0]**2
    E3 = 0.5 * y3[:,1]**2 + 0.5 * w**2 * y3[:,0]**2
    ax3.plot(t1, E1, label="Underdamped")
    ax3.plot(t2, E2, label="Critically Damped")
    ax3.plot(t3, E3, label="Overdamped")
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Energy")
    ax3.legend()
    plt.show()

damped_harmonic_oscillator()
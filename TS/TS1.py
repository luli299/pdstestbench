# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:30:06 2026

@author: suare
"""
import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig

#%%definiciones
N=1000
f0=2000#(Hz)frecuencia de la señal
Puntos_Per=10
fs=Puntos_Per*f0
#%%1.Señal sinusoidal de 2KHz que tenga al menos 10 puntos por periodo.
def mi_funcion_sen( vmax = 1, dc = 0, ff = 1, ph=0, nn = N, fs = fs):
    
    tt=np.arange(N)/fs #se mide en segundos
    xx = vmax * np.sin( 2 * np.pi * ff * tt + ph ) #valores de la senoidal
    #tt=np.arange(N)/fs #se mide en segundos
    
    return(tt, xx)
def modulo_Trans_Fourrier(signal, N, fs):
    frec = np.fft.fftfreq(N, 1/fs) #asigna a cada muestra de la FFT su valor de frecuencia real en Hz
    fft_total = np.fft.fft(signal)
    frec = np.fft.fftshift(frec) #ordena los N asignados a cada frecuencia de menor a mayor
    mod=np.fft.fftshift(np.abs(fft_total)/N)
    
    return (frec,mod)
    
vmax=1 #mi amplitud max
dc=0
ph=0
nn=np.arange(N)
tt, x1 = mi_funcion_sen( vmax = vmax, dc = dc, ff = f0, nn=N, fs=fs)
frec, mod1 = modulo_Trans_Fourrier(x1, N, fs)

plt.figure(figsize=(8, 4))
plt.plot(frec, mod1, 'b')
plt.title("Punto 1")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.show()

#%%2.Misma señal con 2W de potencia media y desfasada en π/2.
tt, x2 = mi_funcion_sen( vmax = 2, dc = dc, ff = f0, ph=np.pi/2, nn=N, fs=fs)
frec, mod2 = modulo_Trans_Fourrier(x2, N, fs)

plt.figure(figsize=(8, 4))
plt.plot(frec, mod2, 'b')
plt.title("Punto 2")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.show()

#%%3.Una secuencia aleatoria de ruido normalmente distribuido con DC (valor medio) 0V y varianza 0.1 W.
DC=0#V, esparnza o valor medio 
v=0.1#(W)varianza
dv=np.sqrt(v)#desvio estandar 
nq=np.random.normal(DC,dv, N)#(ruido)
frec, mod3 = modulo_Trans_Fourrier(nq, N, fs)

plt.figure(figsize=(8, 4))
plt.plot(frec, mod3, 'b')
plt.title("Punto 3")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.show()

#%%4.Una secuencia aleatoria de ruido uniformemente distribuido con DC (valor medio) 0V y varianza 0.1 W.
DC=0#V, esparnza o valor medio 
v=0.1#(W)varianza
a=np.sqrt(3*v)
nq=np.random.uniform(-a,a,N)#(ruido) seria la amplitud limite, es el pico maximo que alcanzara el ruido uniforme
frec, mod4 = modulo_Trans_Fourrier(nq, N, fs)

plt.figure(figsize=(8, 4))
plt.plot(frec, mod4, 'b')
plt.title("Punto 4")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.show()

#%%5.Un pulso rectangular de la misma frecuencia, 1 W de potencia y ciclo de actividad del 50%.
amp5=1#(V)amplitud del pico de onda
tt=np.arange(N)/fs#crea el vector de tiempos en segundos. Define el instante exacto de cadda muestra temporal
x5=amp5*sig.square(2*np.pi*f0*tt, duty=0.5)#genera la onda cuadrada en el tiempo
frec, mod5 = modulo_Trans_Fourrier(x5, N, fs)

plt.figure(figsize=(8, 4))
plt.plot(frec, mod5, 'b')
plt.title("Punto 5")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.grid(True)
plt.show()
















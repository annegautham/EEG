from select import POLLWRNORM
from cv2 import threshold
import scipy
import serial
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack, signal
import time
from statistics import mean
ser = serial.Serial('COM4', 9600, timeout=1)
ser.close()
ser.open()
time.sleep(2)

data = []
N = 800
T = 1.0/800.0
x=np.linspace(0.0,N*T,N)

def spectrogram(x):
    plt.specgram(x,cmap = 'plasma')

#for i in range(2):

for i in range(N):
    line=ser.readline()
    if line:
        string = line.decode()
        num = float(string)
        data.append(num)

ser.close()
m = mean(data)
data = [x-m for x in data]
plt.figure(1)
plt.plot(data, linestyle = '-', color = 'black')
plt.xlabel('Time')
plt.ylabel('Voltage')


fig, ax = plt.subplots(1)
f_data = fftpack.fft(data)

# Power Spectrum
f_x = np.linspace(0.0,1/(2*T),N//2)
plt.figure(2)
plt.plot(f_x, 2.0/N *np.abs(f_data[:N//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

threshold = 29
sample_freq = fftpack.fftfreq(len(data), d=T)
#Filtered Power Spectrum
f_data[np.abs(sample_freq) > threshold] = 0
plt.figure(3)
plt.plot(f_x, 2.0/N *np.abs(f_data[:N//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

# Filtered Signal
filter_data = fftpack.ifft(f_data)
plt.figure(4)
plt.plot(filter_data, linestyle = '-', color = 'black')
plt.xlabel('Time')
plt.ylabel('Voltage')

plt.figure(5)
plt.specgram(filter_data, cmap = 'plasma')
plt.show()

if (figN, Ff = ax.plt(POLLWRNORM(

#print(*data, sep = ", ") 

import numpy as np
import matplotlib.pyplot as plt





###########################################
# generate subcarrier positions
###########################################
payload_sc = [-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -6, -5, -4, -3, -2, -1,  1, 2, 3, 4, 5, 6,  8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  22, 23, 24, 25, 26];
payload_sc = [-26, -25, -24, -23, -22, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -6, -5, -4, -3, 3, 4, 5, 6,  8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  22, 23, 24, 25];



###########################################
# preamble data (given)
###########################################
freq_preamble = [
[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 
[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [-1.472, -1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [1.472, 1.472], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 
[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 0], [0, -1], [-1, 0], [0, 1], [0, 0], [0, -1], [1, 0], [0, -1], [1, 0], [0, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 0], [0, -1], [-1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, 0], [0, -1], [-1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 
[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [-1, 0], [-1, 0], [1, 0], [1, 0], [-1, 0], [1, 0], [-1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [-1, 0], [-1, 0], [1, 0], [1, 0], [-1, 0], [1, 0], [-1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [1, 0], [-1, 0], [-1, 0], [1, 0], [1, 0], [-1, 0], [1, 0], [-1, 0], [1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [-1, 0], [1, 0], [1, 0], [-1, 0], [-1, 0], [1, 0], [-1, 0], [1, 0], [-1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
];

freq_pilot = [[1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [1, 1, 1, -1], [1, 1, 1, -1], [1, 1, 1, -1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1], [-1, -1, -1, 1]];




filename = "rx_signal.dat"
count = 0
with open(filename, 'rb') as f:
    count = count+1
    data = np.fromfile(f, dtype=np.float32)


rx_signal = data[:20000:2] + 1j*data[1:20000:2]
print(rx_signal)
print(len(rx_signal))

plt.figure(1)
plt.plot(abs(rx_signal))
plt.xlabel('sample index')
plt.ylabel('real part of signal')
plt.show()


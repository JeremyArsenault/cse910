close all;
clc;
clear;

fileID = fopen(['C:\Users\hzeng.CSE182\Desktop\upload\rx_signal.dat'], 'rb');
if (fileID < 0)
    disp('Error: fail to open files!');
    pause;
end
frewind(fileID);
num_sample_shift = 10000;
num_sample_process = 10000;
fseek(fileID, num_sample_shift, 'bof');
data_ant_f = fread(fileID, 2*num_sample_process, 'float');
rx_signal = transpose(data_ant_f(1:2:end) + 1i*data_ant_f(2:2:end));

figure; 
plot(abs(rx_signal),'*-');

a = 1;
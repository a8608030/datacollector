%%
clc; clear all; close all;
[data_ecg_B] = textread('Nordic_BMD_ECG_2020_06_24_15_00_10.TXT', '%n')
lim= [5000 : 12000];

[cfs,f] = cwt(data_ecgB(lim),500);

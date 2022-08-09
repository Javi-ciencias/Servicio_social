import pandas as pd
import numpy as np
import scipy as sp
import mne
import seaborn as sns
from scipy.signal import welch, butter,lfilter, filtfilt, freqs

chan= ['Fp1', 'A2', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T3', 'C3', 'Cz', 'C4', 'T4', 'T5', 'P3', 'Pz', 'P4', 'T6', 'O1', 'A1', 'O2', 'T1', 'T2']

der_bi_chan=["Fp1-Fp2","F7-F3","F3-Fz","Fz-F4","F4-F8","A1-T3","T3-C3","C3-Cz","Cz-C4","C4-T4","T4-A2","T5-P3","P3-Pz","Pz-P4","P4-T6","O1-O2"]

chan_lobe=["Fp1","Fp2","F3","F4","F7","F8","Fz","T1","T3","T5","T2","T4","T6", "C3","Cz","C4","P3","Pz","P4","O1","O2"]

der_lobe=np.zeros(len(chan_lobe),dtype=int)
for i in range(0,len(der_lobe)):
    der_lobe[i]=int(chan.index(chan_lobe[i]))

der_bi_ind=np.zeros([len(der_bi_chan),2],dtype=int)
for i in range(0,len(der_bi_chan)):
    der_bi_ind[i,0]=int(chan.index(der_bi_chan[i].split("-")[0]))
    der_bi_ind[i,1]=int(chan.index(der_bi_chan[i].split("-")[1]))

def segments(sub):
    fs=1024
    inter_c=pd.DataFrame({"StartInd":[],"EndInd":[],"SleepStage":[]})
    intervals=pd.read_csv("derivatives/sub-"+sub+"/ses-01/eeg/DataIntervals.tsv",sep="\t")
    start=intervals.iloc[0]["StartInd"]
    stage=intervals.iloc[0]["SleepStage"]
    for i in range(1,len(intervals)):
        if stage!=intervals.iloc[i]["SleepStage"]:
            if intervals.iloc[i-1]["EndInd"]-start>5*60*fs:
                   inter_c.loc[len(inter_c)]=[int(start-150*fs+(intervals.iloc[i-1]["EndInd"]-start)/2),int(start+150*fs+(intervals.iloc[i-1]["EndInd"]-start)/2),stage]
            #inter_c.loc[len(inter_c)]=[int(start),int(intervals.iloc[i-1]["EndInd"]),stage]
            start=intervals.iloc[i]["StartInd"]
            stage=intervals.iloc[i]["SleepStage"]
    if stage==intervals.iloc[-1]["SleepStage"]:
        if intervals.iloc[-1]["EndInd"]-start>5*60*fs:
            inter_c.loc[len(inter_c)]=[int(start-150*fs+(intervals.iloc[-1]["EndInd"]-start)/2),int(start+150*fs+(intervals.iloc[-1]["EndInd"]-start)/2),stage]
            
    return inter_c

def monopolar(sub,lobes=False):
    raw=mne.io.read_raw_edf("sub-"+sub+"/ses-01/eeg/sub-"+sub+"_ses-01_task-hfo_eeg.edf", preload=True, verbose=0)
    raw.filter(0.4, 80)
    raw.notch_filter(50)
    data = raw._data
    
    data_lobes=np.zeros([len(chan_lobe),len(data[0])])
    if lobes==True:
        for i in range(0,len(chan_lobe)):
            data_lobes[i]=data[der_lobe[i]]
        return data_lobes
    else:
        return data

def bipolar_der(sub):
    raw=mne.io.read_raw_edf("sub-"+sub+"/ses-01/eeg/sub-"+sub+"_ses-01_task-hfo_eeg.edf", preload=True, verbose=0)
    raw.filter(0.4, 80)
    raw.notch_filter(50)

    data = raw._data
    
    data_bi=np.zeros([len(der_bi_chan),len(data[0])])
    for i in range(0,len(der_bi_chan)):
        data_bi[i]=data[der_bi_ind[i,0]]-data[der_bi_ind[i,1]]
    return data_bi

# data_bi is an array with dimentions of: [bipolar channels, n]
# start is the index in which the segment to be analyzed starts. 
# end is the index in which the segment to be analyzed ends. 
def f_waves(data,start,end):
    fs=1024
    start=int(start)
    end=int(end)
    #We establish windows of 10s
    window_l=10
    windows=int(np.ceil((end-start)/(window_l*fs)))
    waves=np.zeros([len(data),windows,5,3])
    for i in range(0,windows):
        for j in range(0,len(data)):
            if i==windows-1:
                data_fft=np.absolute(np.fft.rfftn(data[j,start+i*window_l*fs:]))
            else:
                data_fft=np.absolute(np.fft.rfftn(data[j,start+i*window_l*fs:start+(i+1)*window_l*fs]))

            #Delta waves: 0.2-4 Hz
            waves[j,i,0,0]=sum(data_fft[:4*window_l])
            waves[j,i,0,1]=np.mean(data_fft[:4*window_l])
            k=0
            temp=0
            while temp<waves[j,i,0,0]/2:
                temp+=data_fft[k]
                k+=1
            waves[j,i,0,2]=k/window_l

            # Theta waves: 4-8 Hz
            waves[j,i,1,0]=sum(data_fft[4*window_l:8*window_l])
            waves[j,i,1,1]=np.mean(data_fft[4*window_l:8*window_l])
            k=0
            temp=0
            while temp<waves[j,i,1,0]/2:
                temp+=data_fft[k]
                k+=1
            waves[j,i,1,2]=4+k/window_l

            # Alpha waves: 8-12 Hz
            waves[j,i,2,0]=sum(data_fft[8*window_l:12*window_l])
            waves[j,i,2,1]=np.mean(data_fft[8*window_l:12*window_l])
            k=0
            temp=0
            while temp<waves[j,i,2,0]/2:
                temp+=data_fft[k]
                k+=1
            waves[j,i,2,2]=8+k/window_l

            # Beta waves: 12-30 Hz
            waves[j,i,3,0]=sum(data_fft[12*window_l:30*window_l])
            waves[j,i,3,1]=np.mean(data_fft[12*window_l:30*window_l])
            k=0
            temp=0
            while temp<waves[j,i,3,0]/2:
                temp+=data_fft[k]
                k+=1
            waves[j,i,3,2]=12+k/window_l

            # Gamma: 30-90 Hz
            waves[j,i,4,0]=sum(data_fft[30*window_l:90*window_l])
            waves[j,i,4,1]=np.mean(data_fft[30*window_l:90*window_l])
            k=0
            temp=0
            while temp<waves[j,i,4,0]/2:
                temp+=data_fft[k]
                k+=1
            waves[j,i,4,2]=30+k/window_l
    
    waves_avg=np.zeros([5,5])
    waves_avg[0]=np.std(waves[:7,:,:,2],axis=(0,1))
    waves_avg[1]=np.std(waves[7:13,:,:,2],axis=(0,1))
    waves_avg[2]=np.std(waves[13:16,:,:,2],axis=(0,1))
    waves_avg[3]=np.std(waves[16:19,:,:,2],axis=(0,1))
    waves_avg[4]=np.std(waves[19,:,:,2],axis=(0,1))
    return waves_avg

medians=np.zeros([])
for i in range(1,31):
    print("Sujeto  "+str(i))
    sub="0"+str(i)
    sub=sub[-2:]
    
    # Load the data
    data=monopolar(sub,lobes=True)
    
    #load the segments
    seg=segments(sub)
    
    #Analyze each segment
    for j in range(0,len(seg)):
        print("Segment: "+str(j+1)+"/"+str(len(seg)))
        waves=f_waves(data,seg["StartInd"][j],seg["EndInd"][j])
        if i==1:
            medians=np.array([np.append(waves,[seg["SleepStage"][j]])])
        else:
            medians=np.append(medians,[np.append(waves,[seg["SleepStage"][j]])],axis=0)
    del seg
    del data
    del sub
    
medians_csv=pd.DataFrame(medians) 
medians_csv.to_csv("Data_medians_lobe_STD.csv")
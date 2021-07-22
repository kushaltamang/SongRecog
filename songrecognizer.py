# Mohit Tamang 
#Song Recognizer
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import operator
import glob


# returns the signature of a song i.e, the array containing 
# highest frequency value at each time interval
def signature(name):
    data, fs = sf.read(name) # reading the original songs, one at a time
    f, t, Sxx = spectrogram(data, fs=fs, nperseg=fs//2)
    return 2*np.argmax(Sxx,axis=0)

# s = signature of song from our database
# t = signature of testSong
# shorter the distance, higher the song matching percentage
def taxicab_distance(s,t):
    return np.sum(abs(np.subtract(s,t)))

# given a testSong, and a database with original songs, 
# the function identifies the best matched songs                 
def classifyMusic():
    i=0
    database = {} # dictionary that stores [name: signature] pair for each original songs
    results = {} # stores [name: distance] for each original song compared to the testSong
    test_signature = signature('testSong.wav')
    # process to store the [name:signature] pair of all songs into our database
    for name in glob.glob('song-*.wav'):
        database[name] = signature(name)
        
    # stores [name:distance] pair of our test result in results dictionary
    # less distance = bettter matches with testSong
    for name in glob.glob('song-*.wav'):
        results[name] = taxicab_distance(database[name],test_signature)
        
    # sorting the results dictionary by value
    # now we can easily print the n-best matches, which would be the first n-values
    results = sorted(results.items(), key=operator.itemgetter(1))
    #printing the 5-best matches 
    while(i<5):
        print(results[i][1],' ',results[i][0])
        i = i + 1
    #plotting the spectrogram of testSong and its 2 best matches
    x,fs = sf.read('testSong.wav')
    plt.specgram(x,Fs=fs)
    plt.title('spectrogram of testSong.wav')
    plt.show()
    x,fs = sf.read(results[0][0])
    plt.specgram(x,Fs=fs)
    plt.title("spectrogram of the best matched song (%s)"% (results[0][0]))
    plt.show()
    x,fs = sf.read(results[1][0])
    plt.specgram(x,Fs=fs)
    plt.title("spectrogram of the second best matched song (%s)"% (results[1][0]))
    plt.show()
    return 0
    

###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()

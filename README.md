The music identification service Shazam can recognize a song by “listening” to a short piece of it with a user’s mobile phone. While the underlying algorithm is more complex than I am describing here, the basic idea is that a spectrogram of the song being played is generated, then the peaks within the spectrogram are used to generate a signature representing the song. This signature is compared to a database of existing song signatures to identify the song being played.

This project is a Shazam like song-recognizer program prototype. 

Instructions:

There is a file 'music wav.zip'. It contains:
- A README.txt file.
- 8 files of the form song-*.wav; these are the original songs that you will build a
database of signatures from.
- 8 files of the form test-*.wav; these are the corrupted versions of the songs that
your program should be able to identify.
- testSong.wav is a sample test file. To change the test song, copy one of the other
test-*.wav files to this filename.

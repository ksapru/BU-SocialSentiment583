import os

for filename in os.listdir('.'):
    if(filename[0] == '.'):      # to avoid hidden files such as .DS_Store
        continue
    os.system('ffmpeg -i {} -acodec pcm_s16le -ar 22050 {}.wav'.format(filename, filename))
        

import cv2
import numpy as np
import os, sys

slides = []
slides_sum = []
new_frame = []
output_stream = sys.stdout

if len(sys.argv)<3 :
    print("Incorrect number of arguments!")
    exit(0)

slides_folder = sys.argv[2]
frames_folder = sys.argv[1]

# load_slides
for file in os.listdir(slides_folder):
    img = cv2.imread(os.path.join(slides_folder, file),cv2.IMREAD_GRAYSCALE)
    if img is not None:
        m = img.mean()
        new_img = img - m
        slides.append([new_img, file])
        slides_sum.append(np.linalg.norm(new_img))

print("dataset read")
print("Now please wait while the code is Running....")

def calc_xcorr(frame_norm, s):
    minh = min(slides[s][0].shape[0], new_frame.shape[0])
    minw = min(slides[s][0].shape[1], new_frame.shape[1])
    im = np.multiply(slides[s][0][:minh,:minw], new_frame[:minh,:minw])
    norm = slides_sum[s]*frame_norm
    res = im.sum()
    res = res/norm
    return res

# used for printing running accuracy
total = 0
correct = 0
frames_len = len(os.listdir(frames_folder)) 

f = open("results.txt","w+")

# finding answer for all frames
for file in os.listdir(frames_folder):
    frame_img = cv2.imread(os.path.join(frames_folder, file),cv2.IMREAD_GRAYSCALE)
    if frame_img is not None:
        mx_corr = -10000000
        idx = -1
        m = frame_img.mean()
        new_frame = frame_img - m
        frame_norm = np.linalg.norm(new_frame)
        for i in range(len(slides)):
            corr_val = calc_xcorr(frame_norm,i)
            if corr_val > mx_corr:
                idx = i
                mx_corr = corr_val
        string  = str(file) + " " + str(slides[idx][1]) + "\n"
        f.write(string)
          
        a = file.split('_')[0:2]
        b = slides[idx][1].split('.')[0]
        b = b.split('_')[0:2]
        if a[0]==b[0] and a[1]==b[1]:
            correct += 1
        total+=1
        accuracy = 100*(correct/total)
        console_op = "Total frames done: "+str(total)+"/"+str(frames_len)+", "+"Running Accuracy = "+str(accuracy)+"\r" 
        output_stream.flush()
        output_stream.write(console_op)

print("Done!")
f.close()
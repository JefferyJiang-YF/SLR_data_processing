import json
import math
import os
import random
import cv2
import numpy as np
import os,sys,shutil


            

def mkdir_actions(actions):
    DATA_PATH = os.path.join('NP_Data\pre_processing') 
    for action in actions:
        for root, dirs, files in os.walk(r"C:\deep-learning\HKMU\Extrat_keypoints\data\WLASL_train\{}".format(action)):
            for sequence in range (len(files)):
                try:
                    os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
                except:
                    pass

def rand_start_sampling(frame_start, frame_end, num_samples):
    """Randomly select a starting point and return the continuous ${num_samples} frames."""
    num_frames = frame_end - frame_start + 1

    if num_frames > num_samples:
        select_from = range(frame_start, frame_end - num_samples + 1)
        sample_start = random.choice(select_from)
        frames_to_sample = list(range(sample_start, sample_start + num_samples))
    else:
        frames_to_sample = list(range(frame_start, frame_end + 1))

    return frames_to_sample


def k_copies_fixed_length_sequential_sampling(frame_start, frame_end, num_samples, num_copies):
    num_frames = frame_end - frame_start + 1

    frames_to_sample = []

    if num_frames <= num_samples:
        num_pads = num_samples - num_frames

        frames_to_sample = list(range(frame_start, frame_end + 1))
        frames_to_sample.extend([frame_end] * num_pads)

        frames_to_sample *= num_copies

    elif num_samples * num_copies < num_frames:
        mid = (frame_start + frame_end) // 2
        half = num_samples * num_copies // 2

        frame_start = mid - half

        for i in range(num_copies):
            frames_to_sample.extend(list(range(frame_start + i * num_samples,
                                               frame_start + i * num_samples + num_samples)))

    else:
        stride = math.floor((num_frames - num_samples) / (num_copies - 1))
        for i in range(num_copies):
            frames_to_sample.extend(list(range(frame_start + i * stride,
                                               frame_start + i * stride + num_samples)))

    return frames_to_sample

def sequential_sampling(frame_start, frame_end, num_samples):
    """Keep sequentially ${num_samples} frames from the whole video sequence by uniformly skipping frames."""
    num_frames = frame_end - frame_start + 1

    frames_to_sample = []
    if num_frames > num_samples:
        frames_skip = set()

        num_skips = num_frames - num_samples
        interval = num_frames // num_skips

        for i in range(frame_start, frame_end + 1):
            if i % interval == 0 and len(frames_skip) <= num_skips:
                frames_skip.add(i)

        for i in range(frame_start, frame_end + 1):
            if i not in frames_skip:
                frames_to_sample.append(i)
    else:
        frames_to_sample = list(range(frame_start, frame_end + 1))

    return frames_to_sample

#print(k_copies_fixed_length_sequential_sampling(0, 18, 15, num_copies=2))
# print(len(sequential_sampling(0, 42, 21)))
def normalize_video(source_folder,new_path):
    leng = len(os.listdir(source_folder))
    for i in range(1):
        process_path = os.path.join(source_folder + '{}'.format(i))
        pre_process_path = os.path.join(new_path + '{}'.format(i))
        file_list = os.listdir(process_path)
        frame_start = 0
        frame_end = len(file_list) - 1
        num = 0
        # print("-"*8)
        # print(frame_end)
        if len(file_list) < 30:
            no_frame = k_copies_fixed_length_sequential_sampling(frame_start, frame_end, 15, num_copies=2)
        elif len(file_list)>30 and len(file_list)<=60:
            no_frame = rand_start_sampling(frame_start, frame_end, 30)
        elif len(file_list)> 60:
            no_frame = sequential_sampling(frame_start, frame_end, 31)
        else:
            no_frame = [ i for i in range(30)]
        print(process_path)
        print(pre_process_path)
        print(no_frame)
        for file_obj in file_list:
            file_path=os.path.join(process_path,file_obj)
            file_name,file_extend=os.path.splitext(file_obj)
                    
            for j in range(len(no_frame)):
                #print(no_frame)
               # print(file_name)
                if file_name == str(no_frame[j]):
                    print(j)
                    new_name = str(num) + file_extend
                    num += 1
                    newfile_path = os.path.join(pre_process_path, new_name)
                    shutil.copyfile(file_path,newfile_path)
                    print("Done")
                else:
                    continue
            
if __name__ == '__main__':
    mkdir_actions(actions = np.array(['bed','thank you','book']))
    source_folder=r'NP_Data/raw/book/'
    new_path = r'NP_Data/pre_processing/book/'
    normalize_video(source_folder, new_path)
import numpy as np
import os
import read_seq
import cv2

video_list = 'video_Olympic.list'
dataset_root = '/home/datasets/Olympic'
dataset_converted_root = '/home/datasets/Olympic_converted'

if not os.path.exists(dataset_converted_root):
    print('Creating new folder for converted dataset')
    os.mkdir(dataset_converted_root)

cnt = 0
file = open(video_list, 'r')
for line_raw in file:
    video_name = line_raw.rstrip('\n')
    video_class = video_name.split('/')[0]
    video_filename = video_name.split('/')[-1]
    video_path = os.path.join(dataset_root, video_name)
    video_name_wo_ext = os.path.join(* video_name.split('.')[:-1])
    converted_video_path = os.path.join(dataset_converted_root, video_name_wo_ext + '_converted.avi')
    
    dest_class_folder = os.path.join(dataset_converted_root, video_class)
    if not os.path.exists(dest_class_folder):
        os.mkdir(dest_class_folder)
    
    print('#{:04d} \t| Reading video {}'.format(cnt+1, video_name))
    image_npy_list = read_seq.read_seq(video_path)
    print('Found {:04d} images'.format(len(image_npy_list)))
    sample_img = image_npy_list[0]
    h = sample_img.shape[0]
    w = sample_img.shape[1]
    
    video = np.array(image_npy_list, dtype=np.float32)
    writer = cv2.VideoWriter(converted_video_path, cv2.VideoWriter_fourcc(*'PIM1'), 25, (w, h), True)
    for img in image_npy_list:
        img = img[:,:,[2, 1, 0]]
        writer.write(img)
    print('')
    cnt+= 1

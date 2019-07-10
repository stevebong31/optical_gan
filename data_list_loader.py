import os, glob, cv2, math, csv, tqdm, random
import numpy as np

def MPI_dataset_list_loader(mpi_path):
    image_path = mpi_path + '/training/clean'
    lab_path = mpi_path + '/training/flow_png'
    dir_lists = sorted(os.listdir(image_path))
    total = []
    for i in dir_lists:
        paths = sorted(glob.glob(image_path+'/%s/*.png'%i))
        x = [[paths[i], paths[i+1]] for i in range(len(paths)-1)]
        for j in x:
            total.append(j)    
    dir_lists_lab = sorted(os.listdir(lab_path))
    total_lab = []
    for i in dir_lists_lab:
        paths_lab = sorted(glob.glob(lab_path+'/%s/*.png'%i))
        x = [[paths_lab[i]] for i in range(len(paths_lab))]
        for j in x:
            total_lab.append(j)            
    return total, total_lab

def kitti_dataset_list_loader(kitti_path):
    image_path = kitti_path + '/flow/training/colored_0/'
    lab_path = kitti_path + '/flow/training/flow_noc/'
    image_lists = sorted(os.listdir(image_path))
    total = []
    x = [[image_path+image_lists[i], image_path+image_lists[i+1]] for i in range(0,len(image_lists)-1,2)]
    for j in x:
        total.append(j)    
    lab_lists = sorted(os.listdir(lab_path))
    total_lab = []
    x = [[lab_path+lab_lists[i]] for i in range(len(lab_lists))]
    for j in x:
        total_lab.append(j)
    return total, total_lab

def flying_dataset_list_loader(flying_path):
    image_path = flying_path + '/data/'
    lab_path = flying_path + '/labels/'
    image_lists = sorted(os.listdir(image_path))
    total = []
    x = [[image_path+image_lists[i], image_path+image_lists[i+1]] for i in range(0,len(image_lists)-1,2)]
    for j in x:
        total.append(j)    
    lab_lists = sorted(os.listdir(lab_path))
    total_lab = []
    x = [[lab_path+lab_lists[i]] for i in range(len(lab_lists))]
    for j in x:
        total_lab.append(j)
    return total, total_lab

def driving_dataset_list_loader(root):
    image_path = root + '/driving/images'
    lab_path = root + '/driving/flows'
    dir_lists = sorted(os.listdir(image_path))
    total = []
    for i in dir_lists:
        paths = sorted(glob.glob(image_path+'/%s/*.png'%i))
        x = [[paths[i], paths[i+1]] for i in range(len(paths)-1)]
        for j in x:
            total.append(j)    
    dir_lists_lab = sorted(os.listdir(lab_path))
    total_lab = []
    for i in dir_lists_lab:
        paths_lab = sorted(glob.glob(lab_path+'/%s/*.pfm'%i))
        x = [[paths_lab[i]] for i in range(1,len(paths_lab))]
        for j in x:
            total_lab.append(j)            
    return total, total_lab
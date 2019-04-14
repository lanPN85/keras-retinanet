import os
import shutil
import csv
import json
import random


def read_annot(path):
    with open(path, 'rt') as f:
        d = json.load(f)
    annots = []
    if 'AddressWordCoors' in d.keys():
        for coor in d['AddressWordCoors']:
            annots.append([
                coor[0][0], coor[0][1],
                coor[1][0], coor[1][1],
                'address'
            ])

    if 'HometownWordCoors' in d.keys():
        for coor in d['HometownWordCoors']:
            annots.append([
                coor[0][0], coor[0][1],
                coor[1][0], coor[1][1],
                'hometown'
            ])

    if 'NameWordCoors' in d.keys():
        for coor in d['NameWordCoors']:
            annots.append([
                coor[0][0], coor[0][1],
                coor[1][0], coor[1][1],
                'name'
            ])

    if 'BirthdateCoor' in d.keys():
        coor = d['BirthdateCoor']
        annots.append([
            coor[0][0], coor[0][1],
            coor[1][0], coor[1][1],
            'dob'
        ])
    
    if 'id_rect' in d.keys():
        coor = d['id_rect']
        annots.append([
            coor[0][0], coor[0][1],
            coor[1][0], coor[1][1],
            'id'
        ])
    
    return annots

DIR = './data/crop_5-2'
VAL_RATIO = 0.2

sub_dirs = ['batch_001', 'batch_002', 'batch_003', 'batch_004',
    'batch_005', 'batch_101', 'batch_102']
sub_dirs = filter(lambda x: x.startswith('batch_'), sub_dirs)
sub_dirs = map(lambda x: os.path.join(DIR, x), sub_dirs)
sub_dirs = list(sub_dirs)

img_paths = []
for sd in sub_dirs:
    files = os.listdir(sd)
    files = map(lambda x: os.path.join(sd, x), files)
    files = map(lambda x: os.path.abspath(x), files)
    files = list(files)
    img_paths.extend(files)

random.shuffle(img_paths)
val_size = int(len(img_paths) * VAL_RATIO)
train_paths, val_paths = img_paths[val_size:], img_paths[:val_size]
train_len, val_len = 0, 0

with open(os.path.join(DIR, 'train.csv'), 'wt', newline='') as f:
    writer = csv.writer(f)
    for path in train_paths:
        txt_path = path[:-3] + 'txt'
        if not os.path.exists(txt_path):
            continue
        annot_rows = read_annot(txt_path)
        for arow in annot_rows:
            row = [path] + arow
            print(row)
            writer.writerow(row)
        train_len += 1

with open(os.path.join(DIR, 'val.csv'), 'wt', newline='') as f:
    writer = csv.writer(f)
    for path in val_paths:
        txt_path = path[:-3] + 'txt'
        if not os.path.exists(txt_path):
            continue
        annot_rows = read_annot(txt_path)
        for arow in annot_rows:
            row = [path] + arow
            print(row)
            writer.writerow(row)
        val_len += 1

print('Train set size: %d' % train_len)
print('Val set size: %d' % val_len)

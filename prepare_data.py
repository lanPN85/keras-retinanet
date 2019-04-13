import csv

SKIP = True

DIR = '/content/gdrive/My Drive/TrainingData/idcard/full_label/full'
TRAIN_SOURCE = os.path.join(DIR, 'train.txt')
VAL_SOURCE = os.path.join(DIR, 'val.txt')
TRAIN_TARGET = os.path.join(DIR, 'train.csv')
VAL_TARGET = os.path.join(DIR, 'val.csv')

if not SKIP:
    for source, target in zip([TRAIN_SOURCE, VAL_SOURCE], [TRAIN_TARGET, VAL_TARGET]):
        with open(source, 'rt') as sf, open(target, 'wt', newline='') as tf_:
            writer = csv.writer(tf_)
            for line in sf:
                parts = line.strip().split()
                name = os.path.split(parts[0])[-1]
                img_path = os.path.join(DIR, 'transform', name)

                for i in range(2, len(parts), 5):
                    cid = 'id' if int(parts[i+4]) == 0 else 'name'
                    writer.writerow([img_path, parts[i], parts[i+1], parts[i+2], parts[i+3], cid])
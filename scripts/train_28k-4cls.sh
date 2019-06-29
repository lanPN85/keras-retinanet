BACKBONE=resnet101
EXP=${BACKBONE}-4cls-LR1e4-anc8s-imgnet

rm -r logs/$EXP

mkdir snapshots/$EXP
mkdir export/$EXP
mkdir logs/$EXP

python3 keras_retinanet/bin/train.py --gpu 0\
    --backbone ${BACKBONE} --batch-size 4\
    --epochs 50 --steps 7000 --lr 1e-4\
    --snapshot-path snapshots/$EXP\
    --export-path export/$EXP\
    --tensorboard-dir logs/$EXP --config configs/id-config-v8-Sangdv.ini\
    --random-transform --workers 12\
    --image-min-side 400 --image-max-side 1300\
    csv data/crop_28k/train_4cls.csv data/crop_28k/class_names_4cls.csv\
        --val-annotations data/crop_28k/val_4cls.csv

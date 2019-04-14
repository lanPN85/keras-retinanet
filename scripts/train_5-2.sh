python3 keras_retinanet/bin/train.py\
    --backbone resnet50 --batch-size 12\
    --epochs 25 --steps 20000 --lr 1e-4\
    --snapshot-path snapshots/resnet50-LR1e4\
    --export-path exports/resnet50-LR1e4\
    --tensorboard-dir logs/resnet50-LR1e4\
    --random-transform --workers 8\
    --image-min-side 400 --image-max-side 1300\
    csv data/crop_5-2/train.csv data/crop_5-2/class_names.csv\
        --val-annotations data/crop_5-2/val.csv\
    > logs/resnet50-LR1e4/train.log

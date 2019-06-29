EXP=resnet101-4cls-LR1e5-anc3-imgnet
EP=49

mkdir results/$EXP

python3 keras_retinanet/bin/evaluate.py\
    --backbone resnet50 --score-threshold 0.5\
    --iou-threshold 0.60 --max-detections 60\
    --save-path results/$EXP\
    --image-min-side 600 --image-max-side 1300 --convert-model\
    --config configs/id-config-v3.ini\
    csv data/crop_28k/val_4cls.csv data/crop_28k/class_names_4cls.csv\
    snapshots/$EXP/resnet101_csv_$EP.h5\
    > logs/$EXP/eval_$EP.log

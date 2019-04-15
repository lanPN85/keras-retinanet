python3 keras_retinanet/bin/evaluate.py\
    --backbone resnet50 --score-threshold 0.5\
    --iou-threshold 0.8 --max-detections 40\
    --save-path results/resnet50-LR1e4\
    --image-min-side 400 --image-max-side 1300\
    csv data/crop_5-2/val.csv data/crop_5-2/class_names.csv\
    export/resnet50-LR1e4/model.h5

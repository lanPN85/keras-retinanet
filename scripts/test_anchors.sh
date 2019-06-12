python3 keras_retinanet/bin/debug.py\
	--image-min-side 600 --image-max-side 1300\
	--anchors --annotations --config configs/id-config-v6.ini\
	csv data/crop_5-2/val.csv data/crop_5-2/class_names.csv

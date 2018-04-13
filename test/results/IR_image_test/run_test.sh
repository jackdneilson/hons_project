#!/bin/sh
python3 run.py ./test/SCface/SCface_database/surveillance_cameras_IR_cam8/001_cam8.jpg test_IR_images --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/IR_image_test;
python3 run.py ./test/SCface/SCface_database/surveillance_cameras_IR_cam8/012_cam8.jpg test_IR_images --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/IR_image_test;
python3 run.py ./test/SCface/SCface_database/surveillance_cameras_IR_cam8/018_cam8.jpg test_IR_images --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/IR_image_test;
python3 run.py ./test/SCface/SCface_database/surveillance_cameras_IR_cam8/050_cam8.jpg test_IR_images --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/IR_image_test;
python3 run.py ./test/SCface/SCface_database/surveillance_cameras_IR_cam8/123_cam8.jpg test_IR_images --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/IR_image_test;

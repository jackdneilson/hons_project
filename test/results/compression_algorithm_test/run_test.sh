#!/bin/sh

python3 run.py ./test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg test_image_compression --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/compression_algorithm_test;

python3 run.py ./test/lfw/Doc_Rivers/Doc_Rivers_0001.jpg test_image_compression --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/compression_algorithm_test;

python3 run.py ./test/lfw/George_HW_Bush/George_HW_Bush_0003.jpg test_image_compression --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/compression_algorithm_test;

python3 run.py ./test/lfw/Joseph_Blatter/Joseph_Blatter_0002.jpg test_image_compression --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/compression_algorithm_test;

python3 run.py ./test/lfw/Tony_Blair/Tony_Blair_0006.jpg test_image_compression --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/compression_algorithm_test;

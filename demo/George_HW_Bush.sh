#!/bin/bash
python3 ../run.py ../test/lfw/George_HW_Bush/George_HW_Bush_0001.jpg test --pthreads=2 --cthreads=2 --maxload=500 --name="George_H*" --output_location="."

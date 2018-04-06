#!/bin/sh
python3 run.py ./test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --name="Aaron*" --output_location=./test/results/multiple_dataset_test;

python3 run.py ./test/essex_cswww/faces94/male/cjsake/cjsake.1.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/multiple_dataset_test;

python3 run.py ./test/essex_cswww/faces95/adhast/adhast.1.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/multiple_dataset_test;

python3 run.py ./test/essex_cswww/faces96/cjhewi/cjhewi.1.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/multiple_dataset_test;

python3 run.py ./test/essex_cswww/grimace/glen/glen_exp.16.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/multiple_dataset_test;

python3 run.py ./test/lfw/Aaron_Peirsol/Aaron_Peirsol_0001.jpg test_multiple_db --pthreads=2 --cthreads=2 --maxload=200 --output_location=./test/results/multiple_dataset_test;

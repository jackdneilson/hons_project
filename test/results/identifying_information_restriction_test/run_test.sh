#!/bin/sh
python3 run.py ./test/lfw/George_HW_Bush/George_HW_Bush_0003.jpg test --pthreads=2 --cthreads=2 --maxload=200 --name="George*" --output_location=./test/results/identifying_information_restriction_test;
python3 run.py ./test/essex_cswww/faces94/male/cjsake/cjsake.1.jpg test --pthreads=2 --cthreads=2 --maxload=200 --name="cj*" --output_location=./test/results/identifying_information_restriction_test;
python3 run.py ./test/essex_cswww/faces95/adhast/adhast.1.jpg test --pthreads=2 --cthreads=2 --maxload=200 --name="ad*" --output_location=./test/results/identifying_information_restriction_test;
python3 run.py ./test/essex_cswww/faces96/cjhewi/cjhewi.1.jpg test --pthreads=2 --cthreads=2 --maxload=200 --name="cj*" --output_location=./test/results/identifying_information_restriction_test;
python3 run.py ./test/essex_cswww/grimace/glen/glen_exp.16.jpg test --pthreads=2 --cthreads=2 --maxload=200 --name="glen*" --output_location=./test/results/identifying_information_restriction_test;

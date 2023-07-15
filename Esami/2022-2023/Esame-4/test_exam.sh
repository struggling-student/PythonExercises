#!/bin/bash
rm -f testexam.txt
for sol in `ls program.*`;
do
    echo ">> testing solution:" $sol "..."
    echo $sol >> testexam.txt
    ln -sf $sol program.py;
    score=`python grade.py | grep "Total score"`
    echo $score
    echo $score >> testexam.txt
    echo ">> tested solution:" $sol "!"
done

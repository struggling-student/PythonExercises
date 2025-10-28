#!/bin/bash
rm -f testexam.txt
for sol in vuoto iac andrea hide;
do
    echo ">> testing solution:" $sol "..."
    echo $sol >> testexam.txt
    ln -sf program.$sol.py program.py;
    score=`python grade.py | grep "\[TOTAL SCORE\]"`
    echo $score
    echo $score >> testexam.txt
    echo ">> tested solution:" $sol "!"
done

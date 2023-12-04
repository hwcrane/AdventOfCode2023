mkdir day_$1

cd day_$1

curl --cookie session=$AOCSESSION https://adventofcode.com/2023/day/$1/input > input

cp ../template.py part_1.py
cp ../template.py part_2.py
touch test

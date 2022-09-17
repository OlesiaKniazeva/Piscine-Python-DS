#!/bin/sh

directory="split"
rm -rf $directory
mkdir "$directory"

echo 'Enter file for partition'
read -r input_file

if [ -f "$input_file" ];
then
  echo
else
  echo "Entered file doesn't exist. File \"../ex03/hh_positions.csv\" will be used"
  input_file="../ex03/hh_positions.csv"
fi


echo 'proccessing in directory '$directory

    header=$(head -n1 $input_file);
    tail -n+2 $input_file |
    awk -F ',' '{
      idx = match($2, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)
      ss = substr($2, idx, 10)
      print ss }' |
    uniq |
    awk -v directory="$directory" -v var="$header" '{
      print var > directory"/"$0".csv"
    }';

    tail -n+2 $input_file | awk -v directory="$directory" -F ',' '{
      idx = match($2, /[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/)
      ss = substr($2, idx, 10)
      print >> directory"/"ss".csv"
    }';

    echo 'finised'


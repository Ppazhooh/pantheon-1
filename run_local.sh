result_directory="/d1"
#rm tmp/*

for all_log_name in /proj/CC4NGN/5G/clb_traces/*
do
  log_name=$(basename "$all_log_name")
  src/experiments/test.py local --schemes "reminis" -f 0 -t 5 --start-run-id 1 --buffer-size 3300 --mm-delay 10 --downlink-trace /proj/CC4NGN/5G/traces/480mb --uplink-trace /proj/CC4NGN/5G/clb_traces/$log_name --data-dir $result_directory
  rm $result_directory/*acklink*
  rm $result_directory/*stats*
  rm $result_directory/*init*
  rm $result_directory/*.json

  for i in $result_directory/*mm*_run*.log
  do
    mv "$i" "$i"_"$log_name"
  done
 # /proj/CC4NGN/5G/anal.sh
 # mv $result_directory/*mm* $result_directory/logs2

done

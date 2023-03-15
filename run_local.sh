result_directory="logs"

for all_log_name in ~/Reminis/5G_traces/*
do
  log_name=$(basename "$all_log_name")
  src/experiments/test.py local --schemes "reminis" -f 0 -t 60 --start-run-id 1 --buffer-size 3300 --mm-delay 10 --downlink-trace ~/Reminis/wired_traces/480mb --uplink-trace ~/Reminis/5G_traces/$log_name --data-dir $result_directory
  rm $result_directory/*acklink*
  rm $result_directory/*stats*
  rm $result_directory/*init*
  rm $result_directory/*.json

  for i in $result_directory/*mm*_run*.log
  do
    mv "$i" "$i"_"$log_name"
  done
done

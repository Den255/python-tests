# Linux Count and List Open Files for Nginx Process #
SEARCH="python3 main.py"
for (( ; ; ))
do
	for i in $(pgrep -f "${SEARCH}" )
	do
     		echo "$(ps -p ${i} -o command)"
     		echo "PID # ${i} open files count : $(sudo ls -l /proc/${i}/fd | wc -l)"
	done
sleep 1
clear
done


start_ide:
	-pkill -f spyder
	sleep 1
	if [ -e ~/examPY/program.py ] ; then \
		PATH=/opt/miniconda3/envs/F21/bin:$(PATH) spyder -w ~/examPY ~/examPY/grade.py ~/examPY/program.py ; \
	else  \
		PATH=/opt/miniconda3/envs/F21/bin:$(PATH) spyder -w ~/examPY ~/examPY/grade.py ~/examPY/program*.py ; \
	fi

run_tests:
	make -C examPY test_results

show_tests:
	-pkill -f firefox
	sleep 1
	firefox examPY/test_results.html

browser:
	-pkill -f firefox
	sleep 1
	firefox

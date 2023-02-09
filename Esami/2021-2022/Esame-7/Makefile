
start_ide:
	-pkill -f spyder
	sleep 1
	PATH=/opt/miniconda3/envs/F21/bin:$(PATH) spyder

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

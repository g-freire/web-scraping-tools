PYTHON = python3
PIP = pip3

.PHONY : all env modules filter csv xpath clean test help

lxml:
	@time "$(PYTHON)" extract.py lxml
	@echo "--------------------------------";

bs4:
	@time "$(PYTHON)" extract.py bs4
	@echo "--------------------------------";

p_lxml:
	@time "$(PYTHON)" extract-parallel.py lxml
	@echo "--------------------------------";

p_bs4:
	@time "$(PYTHON)" extract-parallel.py bs4
	@echo "--------------------------------";


test:
	@time "$(PYTHON)" -m pytest test_parser.py
	@echo "--------------------------------";

modules: requirements.txt
	@echo "%% Downloading Python Modules";
	@echo "--------------------------------";
	@time "$(PIP)" install -r requirements.txt
	@echo""

schedule:
	bash scheduler.sh


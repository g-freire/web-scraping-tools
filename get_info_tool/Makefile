PYTHON = python3
PIP = pip3
URL =  https://www.epocacosmeticos.com.br/


.PHONY : all modules info container build run robot pid echo

all: build_run robot sitemap

modules: requirements.txt
	@echo "%% Downloading Python Modules";
	@echo "--------------------------------";
	@time "$(PIP)" install -r requirements.txt
	@echo""

info: echo info.py 
	@"$(PYTHON)" info.py 

container:help-docker build run

build: help-docker
	@docker build -t info .

run:help-docker
	@docker run --rm -it --name info info:latest >> info.txt

robot:
	@echo "%% getting robot.txt from "$(URL)" "
	@curl "$(URL)"/robots.txt > robot.txt

pid:
	@echo "--------------------------------";
	@echo "%% Process ID (PID):" $$$$ 
	@echo "--------------------------------";

echo: 
	@echo "--------------------------------";
	@echo "%%  Starting info script";
	@echo "--------------------------------";


define HELP_TEXT

                  ##         	   
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""___/ ===
          {                       /  ===-
           ______ O           __/
                          __/
              ___________/

Usage:  make prune	
	make build 
	make compose 

endef
export HELP_TEXT
help-docker: ## This help target
	@echo "$$HELP_TEXT"
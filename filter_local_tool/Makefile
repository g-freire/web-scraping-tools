PYTHON = python3
PIP = pip3

.PHONY : all filter test container build run

filter: echo filter_tool.py
	@"$(PYTHON)" filter_tool.py 

test:
	@py.test -v

container: help-docker build run 

build: help-docker
	@docker build -t filter .

run: help-docker
	@docker run --rm -it --name filter filter:latest > filtered_urls.txt

modules: requirements.txt
	@echo "%% Downloading Python Modules";
	@echo "--------------------------------";
	@time "$(PIP)" install -r requirements.txt
	@echo""

clean :
	-@rm pip-self*
	-@rm -rf __pycache*

echo: 
	@echo "--------------------------------";
	@echo "%%  Starting filter script";
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
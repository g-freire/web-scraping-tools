PYTHON = python3
PIP = pip3

.PHONY : modules report test container build compose prune echo

modules: requirements.txt
	@echo "%% Downloading Python Modules";
	@echo "--------------------------------";
	@time "$(PIP)" install -r requirements.txt
	@echo""

report: echo
	@time "$(PYTHON)" parser.py 
	@echo "--------------------------------";

test:
	@cd test/ && py.test -v
	@echo "--------------------------------";

container: help-docker build compose

build: help-docker
	@docker-compose build

compose: help-docker
	@docker-compose up 

prune: help-docker
	@docker image prune

git-deploy:
	@git status 
	@git add .
	@git commit -m "human deploy"
	@git push -u origin master

clean :
	-@rm pip-self*
	-@rm -rf __pycache*

echo: 
	@echo "--------------------------------";
	@echo "%%  Starting main script";
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

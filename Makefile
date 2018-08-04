# $ make at root will deploy all repos to github
git-deploy:
	@git status 
	@git add .
	@git commit -m ""
	@git push -f origin master
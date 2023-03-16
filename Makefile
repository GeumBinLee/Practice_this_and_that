commit :
	git add .pre-commit-config.yaml
	git add .
	pre-commit run
	git commit -m "Use Makefile, pre-commit, black and isort"
	git push origin main
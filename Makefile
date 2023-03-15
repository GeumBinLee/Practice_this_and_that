commit :
	git add .pre-commit-config.yaml
	git add .
	pre-commit run
	git commit -m "Use Makefile, pre-commit and black"
	git push origin +main
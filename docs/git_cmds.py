C_date = 20180109

#Finding your username in the URL of remote repositories
git remote -v
#Finding your username in your user.name configuration
git config user.name
YOUR_USERNAME


Cmds:
	-Task:Finding your username in the URL of remote repositories
		-Command:git remote -v
		-Output:origin  https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git (fetch)
				origin	https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git (push)
	-Task:Finding your username in your user.name configuratio
		-Command:git config user.name
		-Output:YOUR_USERNAME
import git
import os

print("*"*50)
print("*"*20+"SAIFEDDIN"+"*"*21+"\n")

r = git.Repo.init()
basepath = os.getcwd()

dirs = os.listdir(basepath)
dirs.remove('.git')

r.index.add(dirs)

r.index.commit("Initial commit")

remote = r.create_remote('origin', url=input("Paste the url of the remote : "))	

print("Remote added successfuly")
print("Don't forget to run 'git push origin master' !")
print('Finallizing ...done !')



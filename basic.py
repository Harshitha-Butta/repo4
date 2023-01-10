import git
import json
from git import Repo
import os

g = git.cmd.Git('https://github.com//Harshitha-Butta//repo4')




def add_version(data, filename='versions_hyd_host2.json'):
    with open(filename,'w') as f:
        json.dump(data, f,indent=4)
        
repo = Repo('C:\\git practice\\repo4')
g.pull()
#version=input()

version = '21.9.0.41'

#version=os.environ['version']

with open('versions_hyd_host2.json') as f:
    data=json.load(f)
    data['configuration']['cfc_versions'][version]=True
    data['configuration']['standalone_latest_general_release']=version
    data['configuration']['standalone_latest_controlled_release']=version
    data['configuration']['hosted_installers_latest']=version
    data['configuration']['aem_host_last_version']=version
    f.seek(0)

add_version(data)

#g.add('--all')
repo.remote().add('.')
repo.remote().commit()
#g.commit('-m', 'commit message from python script', author='harshitha.butta@gmail.com')
origin = repo.remote(name='origin')
origin.push()

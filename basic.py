
import json
from git import Repo
import os


def add_version(data, filename='versions_hyd_host2.json'):
    with open(filename,'w') as f:
        json.dump(data, f,indent=4)
        

repopath = os.getenv('location')
repo = Repo(repopath)
repo.git.pull()

version=os.environ['version']

print("New version is : ",version)
with open('versions_hyd_host2.json') as f:
    data=json.load(f)
    data['configuration']['cfc_versions'][version]=True
    data['configuration']['standalone_latest_general_release']=version
    data['configuration']['standalone_latest_controlled_release']=version
    data['configuration']['hosted_installers_latest']=version
    data['configuration']['aem_host_last_version']=version
    f.seek(0)

add_version(data)

commit_message = 'Added CFC version - '+version+ ' to HYD HOST2'
repo.index.add('versions_hyd_host2.json')
repo.index.commit(commit_message)
repo.git.push("--set-upstream","origin","master")

import os
import subprocess
import sys

from dataclasses import dataclass
### gen common.properties
from jinja2 import Template
# Generate folder
from pathlib import Path
from shutil import copytree, ignore_patterns,rmtree

import argparse
import yaml

@dataclass
class Node():
    id: int
    host: str
    privatekey: str
    pubkey: str
    schema: str

class PostchainGenerator(object):
    def __init__(self,config,num_nodes,project_dir):
        self.config = config
        self.num_nodes = num_nodes
        self.project_dir = project_dir
        self.node_data = self._build_nodes()
    def _build_nodes(self):
        nodes = []
        for inode in range(self.num_nodes):
            print('---- private/public key for node', inode)
            try:
                r = subprocess.run([self.config.get('POSTCHAIN_CLI'),
                                    self.config.get('POSTCHAIN_KEYGEN_CMD')],
                                    stdout=subprocess.PIPE)
                r = r.stdout.decode('utf-8').strip().replace(' ', '').split('\n')
            except FileNotFoundError:
                raise Exception("""The postchain cli command: {} not found!
                Either export it to PATH such as `export PATH=$PATH:/path/to/postchain-node`
                or add PATH to ~/.bashrc""".format(self.config.get('POSTCHAIN_CLI')))
            else:
                privatekey = r[2].strip("privatekey:")  # remove `privkey:`
                pubkey = r[3].strip("pubkey:")  # remove `pubkey:`
                nodes.append(Node(inode,"node{}".format(inode), privatekey,pubkey,schema="node_app_{}".format(inode)))
        return nodes    

    def gen_manifests(self):

        # Directory 
        directory = "_build"
        config_template_dir = self.config.get('CONFIG_TEMPLATE_DIR')
        docker_image = self.config.get('DOCKER_IMAGE')        
            
        # Path 
        build_dir = os.path.join(self.project_dir, directory)
        kube_dir = os.path.join(build_dir,'kubernetes')

        try:
            rmtree(build_dir)       
        except Exception: 
            pass
        Path(build_dir).mkdir(parents=True, exist_ok=True)
        Path(kube_dir).mkdir(parents=True, exist_ok=True)
        copytree(os.path.join(self.project_dir,"rell"), os.path.join(build_dir,'rell'), ignore=ignore_patterns('*.pyc', 'tmp*'))

        for inode in range(len(self.node_data)):
            config_dir = os.path.join(build_dir,"config{}".format(inode))
            Path(config_dir).mkdir(parents=True, exist_ok=True)
            with open(os.path.join(config_dir,'common.properties'),'w') as f:
                t = Template(open(r"{}/common.properties".format(config_template_dir)).read())
                f.write(t.render(nodes=self.node_data))
            with open(os.path.join(config_dir,'node-config.properties'),'w') as f:
                t = Template(open(r"{}/node-config.properties".format(config_template_dir)).read())
                f.write(t.render(node=self.node_data[inode]))

            with open(os.path.join(config_dir,'run.xml'),'w') as f:
                t = Template(open(r"{}/run.xml".format(config_template_dir)).read())
                f.write(
                        t.render(signers=self.node_data,
                                module_name=self.config.get("postchain",{}).get('module_name'),
                        )
                )


            with open(os.path.join(build_dir,'Dockerfile{}'.format(inode)),'w') as f:
                t = Template(open(r"{}/Dockerfile".format(config_template_dir)).read())
                f.write(t.render(inode=inode))
            with open(os.path.join(build_dir,"run{}.sh".format(inode)), 'w', newline='\n') as f:
                t = Template(open(r"{}/run.sh".format(config_template_dir)).read())
                f.write(t.render(inode=inode))

            with open(os.path.join(build_dir,".env"),'w') as f:
                t = Template(open(r"{}/.env".format(config_template_dir)).read())
                f.write(t.render())
            with open(os.path.join(build_dir,"docker-compose.yaml"),'w') as f:
                t = Template(open(r"{}/docker-compose.yml".format(config_template_dir)).read())
                f.write(t.render(nodes=self.node_data,docker_image=docker_image))
            # generate kubernetes
            # gen deployment
            with open(os.path.join(kube_dir,'node{}-deployment.yaml'.format(inode)),'w') as f:
                t = Template(open(r"{}/kubernetes/node-deployment.yaml".format(config_template_dir)).read())
                f.write(t.render(node=self.node_data[inode],docker_image=docker_image))
        # copy postgres deployment
        with open(os.path.join(kube_dir,'postgres-deployment.yaml'),'w') as f:
            t = Template(open(r"{}/kubernetes/postgres-deployment.yaml".format(config_template_dir)).read())
            f.write(t.render())        
        with open(os.path.join(kube_dir,'postchain-configmap.yaml'),'w') as f:
            t = Template(open(r"{}/kubernetes/postchain-configmap.yaml".format(config_template_dir)).read())
            f.write(t.render())            


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', required=True, type=str)        
    parser.add_argument('-n', '--num', required=True, type=int,default=1)
    parser.add_argument('-d', '--dir', required=True)
    # parser.add_argument('-D', '--debug', action='store_true')

    args, unknown = parser.parse_known_args()    

    with open(args.config, "r") as ymlfile:
        config = yaml.load(ymlfile)    
    generator = PostchainGenerator(config,num_nodes=args.num,project_dir=args.dir)
    generator.gen_manifests()

if __name__ == '__main__':
    main()    
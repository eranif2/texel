import docker
import pytest
import yaml
import  requests



with open('./properties.yaml', 'r') as f:
    Properties = yaml.safe_load(f)

Docker_Client =  docker.from_env()

try:
    x = Docker_Client.containers.run(Properties['image_name'],detach=True,ports={f"{Properties['continer_port']}/tcp" : "8099" }).id
except:
    print(f"Error: failed to start continer from image: {Properties['image_name']}")  
    exit(1)

contianer = Docker_Client.containers.get(x)


def test_contianer_is_runing():
    assert contianer.status == 'running'

def test_nginx_is_running():
   response = requests.get('http://127.0.0.1:8099')
   assert response.status_code == '200'



test_nginx_is_running()

contianer.stop()



from invoke import task
import yaml
import os


def load_properties():
    with open('./properties.yaml', 'r') as f:
        return yaml.safe_load(f)

@task
def build(ctx):
    Properties = load_properties()
    ctx.run(f"docker build . --tag {Properties['image_name']}")
    

@task
def test(ctx):
    ctx.run('pytest -q tests.py')

@task
def push(ctx):
    Properties = load_properties()
    username = os.environ['HUB_USERNAME']
    password = os.environ['HUB_PASSWORD']

    print (username, password)
    try:
        ctx.run(f'docker login --username={username} --password={password}')
    except:
        print ('Error: login to docker hub')
    
    ctx.run(f"docker tag {Properties['image_name']}  {username}/{Properties['image_name']}")
    ctx.run(f"docker push {username}/{Properties['image_name']}")

@task
def deploy(ctx):
    ctx.run(f'kubctl apply -f deployment.yaml')
import docker

client = docker.from_env()
containers = client.containers.list(all=True)
for container in containers:
  print(container)

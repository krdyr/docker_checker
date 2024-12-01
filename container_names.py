import docker

client = docker.from.env()
containers = client.containers.list(all=True)
for container in containers:
  print(container)

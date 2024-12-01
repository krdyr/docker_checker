import docker

containers = client.containers.list(all=True)
for container in containers:
  print(container)

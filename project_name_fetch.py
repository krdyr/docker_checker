import docker

def get_compose_project_name():
    client = docker.from_env()
    try:
        # List all containers
        containers = client.containers.list(all=True)
        for container in containers:
            # Check if the label exists
            project_label = container.labels.get("com.docker.compose.project")
            if project_label:
                return project_label
    except Exception as e:
        print(f"Error retrieving project name: {e}")
    finally:
        client.close()
    return None


project_name = get_compose_project_name()
if project_name:
    print(f"Current Docker Compose project name: {project_name}")
else:
    print("No Compose project found.")

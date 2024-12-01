import docker

def restart_inactive_containers(project_name):
    # Connect to the Docker client
    client = docker.from_env()

    try:
        # Get all containers
        containers = client.containers.list(all=True)
        for container in containers:
            if container.attrs['Config']['Labels'].get('com.docker.compose.project') == project_name:
                # Check container status
                if container.status != 'running':
                    print(f"Starting container: {container.name} (Status: {container.status})")
                    container.start()
                else:
                    print(f"Container is already running: {container.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    restart_inactive_containers()

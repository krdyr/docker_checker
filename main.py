import time
from project_name_fetch import get_compose_project_name
from container_checker import restart_inactive_containers
def main():
  project_name = get_compose_project_name()
  restart_inactive_containers(project_name)
  time.sleep(3600)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error starting main function: {e}")

from data.load_projects import load_projects


def main():
    projects=load_projects()
    projects.lies_projects()
   


if __name__ == "__main__":
    main()

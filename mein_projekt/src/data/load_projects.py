from dotenv import load_dotenv
import os

class load_projects:

    def __init__(self):
        load_dotenv()
        self.path=os.getenv("PROJECTS_PATH")
        self.all_projects={}

    def test(self):
        print(self.path)

    def lies_projects(self):
        for i in os.listdir(self.path):
            self.split_auto(i)

    
    def split_auto(self,s:str):
        nummer = ""
        name = ""
        for i, c in enumerate(s):
            if not c.isdigit() and c!='-':  
                nummer = s[:i]
                name = s[i:].lstrip("_- ")
                break
        self.all_projects[nummer]=name
        print(f"name:{nummer}\nname:{name}")

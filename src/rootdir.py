from buildable import Buildable
from debugger import * 
from config import config

class RootDir(Buildable):
    def __init__(self, name):
        self.name = name
        config.name = name
        self.rcfilesetup = RcFileSetup()
        pass

    def make_folder(self, path):
        debug(f"Creating folder at {path}")
        if not config.isdry:
            pass # create thing here


    def create_folders(self):
        folder_definition = config.assetdir + "folders.txt"
        if not os.path.isfile(folder_definition):
            debug(f"File not found: {folder_definition}")
            exit() 

        self.make_folder(f"~/{self.name}")

        with open(folder_definition, 'r') as ffile:
            for line in ffile:
                self.make_folder(f"~/{self.name}/{line.strip()}")

    def build(self):
        self.create_folders()
        self.rcfilesetup.build()
        pass

    def teardown(self):
        print(f"Tearing down {self.name}")
        self.rcfilesetup.teardown()
        pass


class RcFileSetup(Buildable):
    def __init__(self):
        pass

# make .setup directory, have .software_setup in it and .aliases in it etc.
#software_rc_file = os.path.expanduser(f"~/{self.name}/.software")
    def build(self):
        shell = os.environ.get('SHELL')
        rc_file = f".{os.path.basename(shell)}rc"

        user_rc_file = os.path.expanduser(f"~/{config.name}/{rc_file}")
        debug(f"Writing lines to: {user_rc_file}")
        if not config.dryrun:
            with open(user_rc_file, "w") as file:
                file.write("# This is some content for the new file.\n")
                file.write("# You can write multiple lines if needed.\n")
            
            with open(os.path.expanduser(f"~/{rc_file}"), "a") as file:
                file.write(f"\n# Tony Bash Customization Enter Point\n")
                file.write(f"source {user_rc_file}")
        pass

    def teardown(self):
        debug("Tearing down rc file setup")
        pass

import os
import sys
from debugger import Debugger
from pathlib import Path

class SetupScript:
    def __init__(self):
        self._debugger = Debugger()
        self.debug = self._debugger.debug
        self.clear = self._debugger.clear
        self.dryrun = "dry-run" in sys.argv or "--dry-run" in sys.argv

    def welcome_message(self):
        print("====================================")
        print("Welcome to Tony's linux setup!")
        if self.dryrun:
            self._debugger.print_red("(Will be a dry-run)...")
        print("====================================")

    def display_program_description(self):
        with open('./assets/program_description.txt', 'r') as desc_file:
            print(desc_file.read())

    def confirm_setup(self):
        print("\nAre you sure you want to set this up? ")
        key = input("Press Enter to continue or any other key to cancel... ")
        return key == ""

    def get_main_folder_name(self):
        print("Please enter your main folder name, your name is a good idea:")
        return input("> ")

    def create_folders(self, folder_name, file_path):
        if not os.path.isfile(file_path):
            self.debug(f"File not found: {file_path}")
            exit() 

        self.debug(f"Creating folder at ~/{folder_name}")
        if not self.dryrun:
            pass # create thing here

        with open(file_path, 'r') as folders_file:
            for line in folders_file:
                line = line.strip()
                path = f"~/{folder_name}/{line}"
                self.debug(f"Create: {path}")
                if not self.dryrun:
                    pass # create thing here

                #self.debug(f"Create: {os.path.expanduser(path)}")

    def setup_bashrc(self):
        shell = os.environ.get('SHELL')
        rc_file = f".{os.path.basename(shell)}rc"
        my_rc = os.path.expanduser(f"~/{self.name}/{rc_file}")
        self.debug(f"Create: {my_rc}")
        if not self.dryrun:
            with open(my_rc, "w") as file:
                file.write("# This is some content for the new file.\n")
                file.write("# You can write multiple lines if needed.\n")
            
            with open(os.path.expanduser(f"~/{rc_file}"), "a") as file:
                file.write(f"\n# Tony Bash Customization Enter Point\n")
                file.write(f"source {my_rc}")


    def run(self):

        # help user understand what they just started
        self.welcome_message()
        self.display_program_description()

        # confirm user really wants to go through with this
        if not self.confirm_setup():
            return

        # get main folder name from them. Must be at least 1 character (not white space)
        self.clear()
        name = self.get_main_folder_name().strip()
        self.name = name
        if len(name) < 1:
            self.debug("Need to provide a proper folder name. sorry :(")
            return

        # create folders, check if file exists
        self.create_folders(name, "assets/folders.txt")
        self.setup_bashrc()


if __name__ == "__main__":
    setup = SetupScript()
    setup.run()

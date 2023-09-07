import os
import sys
from debugger import * 
from config import config
from pathlib import Path
from rootdir import RootDir

class SetupScript:
    def __init__(self):
        config.dryrun = "dry-run" in sys.argv or "--dry-run" in sys.argv
        config.assetdir = "assets/"

    def welcome_message(self):
        print("====================================")
        print("Welcome to Tony's linux setup!")
        if config.dryrun:
            print_red("(Will be a dry-run)...")
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

    def setup_bashrc(self):
        shell = os.environ.get('SHELL')
        rc_file = f".{os.path.basename(shell)}rc"

        user_rc_file = os.path.expanduser(f"~/{self.name}/{rc_file}")
        # make .setup directory, have .software_setup in it and .aliases in it etc.
        #software_rc_file = os.path.expanduser(f"~/{self.name}/.software")
        debug(f"Create: {user_rc_file}")
        if not config.dryrun:
            with open(user_rc_file, "w") as file:
                file.write("# This is some content for the new file.\n")
                file.write("# You can write multiple lines if needed.\n")
            
            with open(os.path.expanduser(f"~/{rc_file}"), "a") as file:
                file.write(f"\n# Tony Bash Customization Enter Point\n")
                file.write(f"source {user_rc_file}")


    def run(self):

        # help user understand what they just started
        self.welcome_message()
        self.display_program_description()

        # confirm user really wants to go through with this
        if not self.confirm_setup():
            return

        # get main folder name from them. Must be at least 1 character (not white space)
        clear()
        name = self.get_main_folder_name().strip()
        self.name = name
        if len(name) < 1:
            debug("Need to provide a proper folder name. sorry :(")
            return

        # create folders, check if file exists
        root = RootDir(name)
        root.build()
        root.teardown()
#         self.create_folders(name, "assets/folders.txt")
#         self.setup_bashrc()


if __name__ == "__main__":
    setup = SetupScript()
    setup.run()

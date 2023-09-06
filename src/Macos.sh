debug_counter=0
debug() {
  ((debug_counter++))
  echo -e "(\033[0;31m$debug_counter\033[0m) $1"
}

echo "Welcome Macos"

# set ~ directory to user specified directory
# make some sort of file that says what the current user directory is
echo "===================================="
echo "Welcome to Tony's linux setup!"
echo "===================================="
echo "Please enter your main folder name, name is a good idea:"
read -p "> " name
echo ""
debug "Creating folder at ~/$name"

# update .zshrc to execute /Tony/.zshrc
# ask user what folders they DONT want to be made (comma seperated list)

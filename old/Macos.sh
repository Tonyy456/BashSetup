debug_counter=0
debug() {
  ((debug_counter++))
  echo -e "(\033[0;31m$debug_counter\033[0m) $1"
}
trim() {
    return $(echo "$1" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
}

echo "Welcome Macos"

# set ~ directory to user specified directory
# make some sort of file that says what the current user directory is
echo "===================================="
echo "Welcome to Tony's linux setup!"
echo "===================================="

cat ./assets/program_description.txt
echo 
echo "Are you sure you want to set this up? "
read -rp "Press Enter to continue or any other key to cancel... " -n 1 key
echo  # Move to the next line for better formatting
if [[ $key != "" ]]; then
    return 0
fi
echo

echo "Please enter your main folder name, your name is a good idea:"
read -p "> " name
echo ""
debug "Creating folder at ~/$name"

file_path="assets/folders.txt"
if [ ! -f "$file_path" ]; then
  debug "File not found: $file_path"
  exit 1
fi
while IFS= read -r line; do
  line= trim $line
  debug "Processing line: $line"
done < "$file_path"

# update .zshrc to execute /Tony/.zshrc
# ask user what folders they DONT want to be made (comma seperated list)

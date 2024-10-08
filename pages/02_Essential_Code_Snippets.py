import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="Essential Code Snippets", page_icon="🌺")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Essential Code Snippets")

st.write("These are some quick copy-and-paste snippets that you might want to use over the course of this workshop. They are specifically for the tools we have discussed.")

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
}
</style>
"""

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)

st.write(font_css, unsafe_allow_html=True)

tablist = ["\u2001  **bash**  \u2001", "\u2001 **conda** \u2001", "\u2001 **git** \u2001", "\u2001 **docs** \u2001", "\u2001 **tests** \u2001",]



tab1, tab2, tab3, tab4, tab5 = st.tabs(tablist)

# Linux Commands

bash_md = """
## Essential linux/bash commands

You will use Linux a lot during your project:
- When you launch the virtual machine in codespaces for this workshop, it
will be running on Ubuntu, a Linux distribution.
- If you use tools such as Anaconda Prompt or MobaXTerm from Windows, these will take
Linux commands.
- Mac commands are Unix-based and so very similar.


```bash
cd # change directory to home
cd /workspaces # return to the /workspaces directory
cd .. # go up a level in the directory structure
ls # list the contents of the current directory
pwd # get the path to the current working directory
```

"""

bash_2 = """

The cheat sheet below is provided by [RehanSaeed](https://github.com/RehanSaeed/Bash-Cheat-Sheet) on GitHub under the [MIT License](https://github.com/RehanSaeed/Bash-Cheat-Sheet/blob/main/LICENSE).

## Command History

```bash
!!            # Run the last command

touch foo.sh
chmod +x !$   # !$ is the last argument of the last command i.e. foo.sh
```

## Navigating Directories

```bash
pwd                       # Print current directory path
ls                        # List directories
ls -a|--all               # List directories including hidden
ls -l                     # List directories in long form
ls -l -h|--human-readable # List directories in long form with human readable sizes
ls -t                     # List directories by modification time, newest first
stat foo.txt              # List size, created and modified timestamps for a file
stat foo                  # List size, created and modified timestamps for a directory
tree                      # List directory and file tree
tree -a                   # List directory and file tree including hidden
tree -d                   # List directory tree
cd foo                    # Go to foo sub-directory
cd                        # Go to home directory
cd ~                      # Go to home directory
cd -                      # Go to last directory
pushd foo                 # Go to foo sub-directory and add previous directory to stack
popd                      # Go back to directory in stack saved by `pushd`
```

## Creating Directories

```bash
mkdir foo                        # Create a directory
mkdir foo bar                    # Create multiple directories
mkdir -p|--parents foo/bar       # Create nested directory
mkdir -p|--parents {foo,bar}/baz # Create multiple nested directories

mktemp -d|--directory            # Create a temporary directory
```

## Moving Directories

```bash
cp -R|--recursive foo bar                               # Copy directory
mv foo bar                                              # Move directory

rsync -z|--compress -v|--verbose /foo /bar              # Copy directory, overwrites destination
rsync -a|--archive -z|--compress -v|--verbose /foo /bar # Copy directory, without overwriting destination
rsync -avz /foo username@hostname:/bar                  # Copy local directory to remote directory
rsync -avz username@hostname:/foo /bar                  # Copy remote directory to local directory
```

## Deleting Directories

```bash
rmdir foo                        # Delete empty directory
rm -r|--recursive foo            # Delete directory including contents
rm -r|--recursive -f|--force foo # Delete directory including contents, ignore nonexistent files and never prompt
```

## Creating Files

```bash
touch foo.txt          # Create file or update existing files modified timestamp
touch foo.txt bar.txt  # Create multiple files
touch {foo,bar}.txt    # Create multiple files
touch test{1..3}       # Create test1, test2 and test3 files
touch test{a..c}       # Create testa, testb and testc files

mktemp                 # Create a temporary file
```

## Standard Output, Standard Error and Standard Input

```bash
echo "foo" > bar.txt       # Overwrite file with content
echo "foo" >> bar.txt      # Append to file with content

ls exists 1> stdout.txt    # Redirect the standard output to a file
ls noexist 2> stderror.txt # Redirect the standard error output to a file
ls 2>&1 > out.txt          # Redirect standard output and error to a file
ls > /dev/null             # Discard standard output and error

read foo                   # Read from standard input and write to the variable foo
```

## Moving Files

```bash
cp foo.txt bar.txt                                # Copy file
mv foo.txt bar.txt                                # Move file

rsync -z|--compress -v|--verbose /foo.txt /bar    # Copy file quickly if not changed
rsync z|--compress -v|--verbose /foo.txt /bar.txt # Copy and rename file quickly if not changed
```

## Deleting Files

```bash
rm foo.txt            # Delete file
rm -f|--force foo.txt # Delete file, ignore nonexistent files and never prompt
```

## Reading Files

```bash
cat foo.txt            # Print all contents
less foo.txt           # Print some contents at a time (g - go to top of file, SHIFT+g, go to bottom of file, /foo to search for 'foo')
head foo.txt           # Print top 10 lines of file
tail foo.txt           # Print bottom 10 lines of file
open foo.txt           # Open file in the default editor
wc foo.txt             # List number of lines words and characters in the file
```

## File Permissions

| # | Permission              | rwx | Binary |
| - | -                       | -   | -      |
| 7 | read, write and execute | rwx | 111    |
| 6 | read and write          | rw- | 110    |
| 5 | read and execute        | r-x | 101    |
| 4 | read only               | r-- | 100    |
| 3 | write and execute       | -wx | 011    |
| 2 | write only              | -w- | 010    |
| 1 | execute only            | --x | 001    |
| 0 | none                    | --- | 000    |

For a directory, execute means you can enter a directory.

| User | Group | Others | Description                                                                                          |
| -    | -     | -      | -                                                                                                    |
| 6    | 4     | 4      | User can read and write, everyone else can read (Default file permissions)                           |
| 7    | 5     | 5      | User can read, write and execute, everyone else can read and execute (Default directory permissions) |

- u - User
- g - Group
- o - Others
- a - All of the above

```bash
ls -l /foo.sh            # List file permissions
chmod +100 foo.sh        # Add 1 to the user permission
chmod -100 foo.sh        # Subtract 1 from the user permission
chmod u+x foo.sh         # Give the user execute permission
chmod g+x foo.sh         # Give the group execute permission
chmod u-x,g-x foo.sh     # Take away the user and group execute permission
chmod u+x,g+x,o+x foo.sh # Give everybody execute permission
chmod a+x foo.sh         # Give everybody execute permission
chmod +x foo.sh          # Give everybody execute permission
```

## Finding Files

Find binary files for a command.

```bash
type wget                                  # Find the binary
which wget                                 # Find the binary
whereis wget                               # Find the binary, source, and manual page files
```

`locate` uses an index and is fast.

```bash
updatedb                                   # Update the index

locate foo.txt                             # Find a file
locate --ignore-case                       # Find a file and ignore case
locate f*.txt                              # Find a text file starting with 'f'
```

`find` doesn't use an index and is slow.

```bash
find /path -name foo.txt                   # Find a file
find /path -iname foo.txt                  # Find a file with case insensitive search
find /path -name "*.txt"                   # Find all text files
find /path -name foo.txt -delete           # Find a file and delete it
find /path -name "*.png" -exec pngquant {} # Find all .png files and execute pngquant on it
find /path -type f -name foo.txt           # Find a file
find /path -type d -name foo               # Find a directory
find /path -type l -name foo.txt           # Find a symbolic link
find /path -type f -mtime +30              # Find files that haven't been modified in 30 days
find /path -type f -mtime +30 -delete      # Delete files that haven't been modified in 30 days
```

## Find in Files

```bash
grep 'foo' /bar.txt                         # Search for 'foo' in file 'bar.txt'
grep 'foo' /bar -r|--recursive              # Search for 'foo' in directory 'bar'
grep 'foo' /bar -R|--dereference-recursive  # Search for 'foo' in directory 'bar' and follow symbolic links
grep 'foo' /bar -l|--files-with-matches     # Show only files that match
grep 'foo' /bar -L|--files-without-match    # Show only files that don't match
grep 'Foo' /bar -i|--ignore-case            # Case insensitive search
grep 'foo' /bar -x|--line-regexp            # Match the entire line
grep 'foo' /bar -C|--context 1              # Add N line of context above and below each search result
grep 'foo' /bar -v|--invert-match           # Show only lines that don't match
grep 'foo' /bar -c|--count                  # Count the number lines that match
grep 'foo' /bar -n|--line-number            # Add line numbers
grep 'foo' /bar --colour                    # Add colour to output
grep 'foo\|bar' /baz -R                     # Search for 'foo' or 'bar' in directory 'baz'
grep --extended-regexp|-E 'foo|bar' /baz -R # Use regular expressions
egrep 'foo|bar' /baz -R                     # Use regular expressions
```

### Replace in Files

```bash
sed 's/fox/bear/g' foo.txt               # Replace fox with bear in foo.txt and output to console
sed 's/fox/bear/gi' foo.txt              # Replace fox (case insensitive) with bear in foo.txt and output to console
sed 's/red fox/blue bear/g' foo.txt      # Replace red with blue and fox with bear in foo.txt and output to console
sed 's/fox/bear/g' foo.txt > bar.txt     # Replace fox with bear in foo.txt and save in bar.txt
sed 's/fox/bear/g' foo.txt -i|--in-place # Replace fox with bear and overwrite foo.txt
```

## Symbolic Links

```bash
ln -s|--symbolic foo bar            # Create a link 'bar' to the 'foo' folder
ln -s|--symbolic -f|--force foo bar # Overwrite an existing symbolic link 'bar'
ls -l                               # Show where symbolic links are pointing
```

## Compressing Files

### zip

Compresses one or more files into *.zip files.

```bash
zip foo.zip /bar.txt                # Compress bar.txt into foo.zip
zip foo.zip /bar.txt /baz.txt       # Compress bar.txt and baz.txt into foo.zip
zip foo.zip /{bar,baz}.txt          # Compress bar.txt and baz.txt into foo.zip
zip -r|--recurse-paths foo.zip /bar # Compress directory bar into foo.zip
```

### gzip

Compresses a single file into *.gz files.

```bash
gzip /bar.txt foo.gz           # Compress bar.txt into foo.gz and then delete bar.txt
gzip -k|--keep /bar.txt foo.gz # Compress bar.txt into foo.gz
```

### tar -c

Compresses (optionally) and combines one or more files into a single *.tar, *.tar.gz, *.tpz or *.tgz file.

```bash
tar -c|--create -z|--gzip -f|--file=foo.tgz /bar.txt /baz.txt # Compress bar.txt and baz.txt into foo.tgz
tar -c|--create -z|--gzip -f|--file=foo.tgz /{bar,baz}.txt    # Compress bar.txt and baz.txt into foo.tgz
tar -c|--create -z|--gzip -f|--file=foo.tgz /bar              # Compress directory bar into foo.tgz
```

## Decompressing Files

### unzip

```bash
unzip foo.zip          # Unzip foo.zip into current directory
```

### gunzip

```bash
gunzip foo.gz           # Unzip foo.gz into current directory and delete foo.gz
gunzip -k|--keep foo.gz # Unzip foo.gz into current directory
```

### tar -x

```bash
tar -x|--extract -z|--gzip -f|--file=foo.tar.gz # Un-compress foo.tar.gz into current directory
tar -x|--extract -f|--file=foo.tar              # Un-combine foo.tar into current directory
```

## Disk Usage

```bash
df                     # List disks, size, used and available space
df -h|--human-readable # List disks, size, used and available space in a human readable format

du                     # List current directory, subdirectories and file sizes
du /foo/bar            # List specified directory, subdirectories and file sizes
du -h|--human-readable # List current directory, subdirectories and file sizes in a human readable format
du -d|--max-depth      # List current directory, subdirectories and file sizes within the max depth
du -d 0                # List current directory size
```

## Memory Usage

```bash
free                   # Show memory usage
free -h|--human        # Show human readable memory usage
free -h|--human --si   # Show human readable memory usage in power of 1000 instead of 1024
free -s|--seconds 5    # Show memory usage and update continuously every five seconds
```

## Packages

```bash
apt update                   # Refreshes repository index
apt search wget              # Search for a package
apt show wget                # List information about the wget package
apt list --all-versions wget # List all versions of the package
apt install wget             # Install the latest version of the wget package
apt install wget=1.2.3       # Install a specific version of the wget package
apt remove wget              # Removes the wget package
apt upgrade                  # Upgrades all upgradable packages
```

## Shutdown and Reboot

```bash
shutdown                     # Shutdown in 1 minute
shutdown now "Cya later"     # Immediately shut down
shutdown +5 "Cya later"      # Shutdown in 5 minutes

shutdown --reboot            # Reboot in 1 minute
shutdown -r now "Cya later"  # Immediately reboot
shutdown -r +5 "Cya later"   # Reboot in 5 minutes

shutdown -c                  # Cancel a shutdown or reboot

reboot                       # Reboot now
reboot -f                    # Force a reboot
```

## Identifying Processes

```bash
top                    # List all processes interactively
htop                   # List all processes interactively
ps all                 # List all processes
pidof foo              # Return the PID of all foo processes

CTRL+Z                 # Suspend a process running in the foreground
bg                     # Resume a suspended process and run in the background
fg                     # Bring the last background process to the foreground
fg 1                   # Bring the background process with the PID to the foreground

sleep 30 &             # Sleep for 30 seconds and move the process into the background
jobs                   # List all background jobs
jobs -p                # List all background jobs with their PID

lsof                   # List all open files and the process using them
lsof -itcp:4000        # Return the process listening on port 4000
```

## Process Priority

Process priorities go from -20 (highest) to 19 (lowest).

```bash
nice -n -20 foo        # Change process priority by name
renice 20 PID          # Change process priority by PID
ps -o ni PID           # Return the process priority of PID
```

## Killing Processes

```bash
CTRL+C                 # Kill a process running in the foreground
kill PID               # Shut down process by PID gracefully. Sends TERM signal.
kill -9 PID            # Force shut down of process by PID. Sends SIGKILL signal.
pkill foo              # Shut down process by name gracefully. Sends TERM signal.
pkill -9 foo           # force shut down process by name. Sends SIGKILL signal.
killall foo            # Kill all process with the specified name gracefully.
```

## Date & Time

```bash
date                   # Print the date and time
date --iso-8601        # Print the ISO8601 date
date --iso-8601=ns     # Print the ISO8601 date and time

time tree              # Time how long the tree command takes to execute
```

## Scheduled Tasks

```pre
   *      *         *         *           *
Minute, Hour, Day of month, Month, Day of the week
```

```bash
crontab -l                 # List cron tab
crontab -e                 # Edit cron tab in Vim
crontab /path/crontab      # Load cron tab from a file
crontab -l > /path/crontab # Save cron tab to a file

* * * * * foo              # Run foo every minute
*/15 * * * * foo           # Run foo every 15 minutes
0 * * * * foo              # Run foo every hour
15 6 * * * foo             # Run foo daily at 6:15 AM
44 4 * * 5 foo             # Run foo every Friday at 4:44 AM
0 0 1 * * foo              # Run foo at midnight on the first of the month
0 0 1 1 * foo              # Run foo at midnight on the first of the year

at -l                      # List scheduled tasks
at -c 1                    # Show task with ID 1
at -r 1                    # Remove task with ID 1
at now + 2 minutes         # Create a task in Vim to execute in 2 minutes
at 12:34 PM next month     # Create a task in Vim to execute at 12:34 PM next month
at tomorrow                # Create a task in Vim to execute tomorrow
```

## HTTP Requests

```bash
curl https://example.com                               # Return response body
curl -i|--include https://example.com                  # Include status code and HTTP headers
curl -L|--location https://example.com                 # Follow redirects
curl -o|--remote-name foo.txt https://example.com      # Output to a text file
curl -H|--header "User-Agent: Foo" https://example.com # Add a HTTP header
curl -X|--request POST -H "Content-Type: application/json" -d|--data '{"foo":"bar"}' https://example.com # POST JSON
curl -X POST -H --data-urlencode foo="bar" http://example.com                           # POST URL Form Encoded

wget https://example.com/file.txt .                            # Download a file to the current directory
wget -O|--output-document foo.txt https://example.com/file.txt # Output to a file with the specified name
```

## Network Troubleshooting

```bash
ping example.com            # Send multiple ping requests using the ICMP protocol
ping -c 10 -i 5 example.com # Make 10 attempts, 5 seconds apart

ip addr                     # List IP addresses on the system
ip route show               # Show IP addresses to router

netstat -i|--interfaces     # List all network interfaces and in/out usage
netstat -l|--listening      # List all open ports

traceroute example.com      # List all servers the network traffic goes through

mtr -w|--report-wide example.com                                    # Continually list all servers the network traffic goes through
mtr -r|--report -w|--report-wide -c|--report-cycles 100 example.com # Output a report that lists network traffic 100 times

nmap 0.0.0.0                # Scan for the 1000 most common open ports on localhost
nmap 0.0.0.0 -p1-65535      # Scan for open ports on localhost between 1 and 65535
nmap 192.168.4.3            # Scan for the 1000 most common open ports on a remote IP address
nmap -sP 192.168.1.1/24     # Discover all machines on the network by ping'ing them
```

## DNS

```bash
host example.com            # Show the IPv4 and IPv6 addresses

dig example.com             # Show complete DNS information

cat /etc/resolv.conf        # resolv.conf lists nameservers
```

## Hardware

```bash
lsusb                  # List USB devices
lspci                  # List PCI hardware
lshw                   # List all hardware
```

## Terminal Multiplexers

Start multiple terminal sessions. Active sessions persist reboots. `tmux` is more modern than `screen`.

```bash
tmux             # Start a new session (CTRL-b + d to detach)
tmux ls          # List all sessions
tmux attach -t 0 # Reattach to a session

screen           # Start a new session (CTRL-a + d to detach)
screen -ls       # List all sessions
screen -R 31166  # Reattach to a session

exit             # Exit a session
```

## Secure Shell Protocol (SSH)

```bash
ssh hostname                 # Connect to hostname using your current user name over the default SSH port 22
ssh -i foo.pem hostname      # Connect to hostname using the identity file
ssh user@hostname            # Connect to hostname using the user over the default SSH port 22
ssh user@hostname -p 8765    # Connect to hostname using the user over a custom port
ssh ssh://user@hostname:8765 # Connect to hostname using the user over a custom port
```

Set default user and port in `~/.ssh/config`, so you can just enter the name next time:

```bash
$ cat ~/.ssh/config
Host name
  User foo
  Hostname 127.0.0.1
  Port 8765
$ ssh name
```

## Secure Copy

```bash
scp foo.txt ubuntu@hostname:/home/ubuntu # Copy foo.txt into the specified remote directory
```

## Bash Profile

- bash - `.bashrc`
- zsh - `.zshrc`

```bash
# Always run ls after cd
function cd {
  builtin cd "$@" && ls
}

# Prompt user before overwriting any files
alias cp='cp --interactive'
alias mv='mv --interactive'
alias rm='rm --interactive'

# Always show disk usage in a human readable format
alias df='df -h'
alias du='du -h'
```

## Bash Script

### Variables

```bash
#!/bin/bash

foo=123                # Initialize variable foo with 123
declare -i foo=123     # Initialize an integer foo with 123
declare -r foo=123     # Initialize readonly variable foo with 123
echo $foo              # Print variable foo
echo ${foo}_'bar'      # Print variable foo followed by _bar
echo ${foo:-'default'} # Print variable foo if it exists otherwise print default

export foo             # Make foo available to child processes
unset foo              # Make foo unavailable to child processes
```

### Environment Variables

```bash
#!/bin/bash

env            # List all environment variables
echo $PATH     # Print PATH environment variable
export FOO=Bar # Set an environment variable
```

### Functions

```bash
#!/bin/bash

greet() {
  local world = "World"
  echo "$1 $world"
  return "$1 $world"
}
greet "Hello"
greeting=$(greet "Hello")
```

### Exit Codes

```bash
#!/bin/bash

exit 0   # Exit the script successfully
exit 1   # Exit the script unsuccessfully
echo $?  # Print the last exit code
```

### Conditional Statements

#### Boolean Operators

- `$foo` - Is true
- `!$foo` - Is false

#### Numeric Operators

- `-eq` - Equals
- `-ne` - Not equals
- `-gt` - Greater than
- `-ge` - Greater than or equal to
- `-lt` - Less than
- `-le` - Less than or equal to
- `-e` foo.txt - Check file exists
- `-z` foo - Check if variable exists

#### String Operators

- `=` - Equals
- `==` - Equals
- `-z` - Is null
- `-n` - Is not null
- `<` - Is less than in ASCII alphabetical order
- `>` - Is greater than in ASCII alphabetical order

#### If Statements

```bash
#!/bin/bash

if [[$foo = 'bar']]; then
  echo 'one'
elif [[$foo = 'bar']] || [[$foo = 'baz']]; then
  echo 'two'
elif [[$foo = 'ban']] && [[$USER = 'bat']]; then
  echo 'three'
else
  echo 'four'
fi
```

#### Inline If Statements

```bash
#!/bin/bash

[[ $USER = 'rehan' ]] && echo 'yes' || echo 'no'
```

#### While Loops

```bash
#!/bin/bash

declare -i counter
counter=10
while [$counter -gt 2]; do
  echo The counter is $counter
  counter=counter-1
done
```

#### For Loops

```bash
#!/bin/bash

for i in {0..10..2}
  do
    echo "Index: $i"
  done

for filename in file1 file2 file3
  do
    echo "Content: " >> $filename
  done

for filename in *;
  do
    echo "Content: " >> $filename
  done
```

#### Case Statements

```bash
#!/bin/bash

echo "What's the weather like tomorrow?"
read weather

case $weather in
  sunny | warm ) echo "Nice weather: " $weather
  ;;
  cloudy | cool ) echo "Not bad weather: " $weather
  ;;
  rainy | cold ) echo "Terrible weather: " $weather
  ;;
  * ) echo "Don't understand"
  ;;
esac
```
"""

bash_3 = """
We are going to use [GitHub Codespaces](https://github.com/features/codespaces)
as a remote development environment. While setting up the Codespace virtual machine,
we will be using a [devcontainer](https://containers.dev/) to install some extensions
and packages that you'll use.

What all of that means is that there's nothing for you to install.
Head over to the [Python project template](https://github.com/ARCTraining/python-project-template)
and log in with your GitHub account which you set up before attending the course. Click the green 
**Use this template**
button and select **Create a new repository**. If you're logged in,
you should now get a prompt that asks you for a name. If you're note logged in,
please log in or sign up using your University of Leeds email!

 ![Screenshot of GitHub repository, highlighting the "Use this template" button.](https://docs.github.com/assets/cb-76823/images/help/repository/use-this-template-button.png)

Use Codespaces as a playground to get familiar with Linux/bash commands.
"""

# Conda commands

conda_md = """
## Essential conda commands

The devcontainer/codespaces virtual machine comes preloaded with `miniforge`, an open source alternative to anaconda with the fast
libmamba solver available. You use this in the same way you would conda from your local machine. Your codespaces machine
comes with a basic Python packaging environment prebuilt.

```bash
# from terminal/outside a conda env
conda env list # list built environments
conda env create --file PATH/TO/A/FILE # build a conda env from a file
conda env create --file .devcontainer/env-files/mkdocs-env.yml # build a conda env from a file
conda activate ENV-NAME  # activate the environment ENV-NAME

# from inside a conda env (after activating the env)
conda list # lists installed packages in the env
conda env export --no-builds > exported-env.yml # exports all packages in the env
conda env export --from-history  > exported-env.yml # exports the packages that were explicitly installed
```

We will look at exporting conda envs in more detail in the
[Project Workflow](Project_Workflow#9-export-record-dev-env-dependencies) section, but
for now, let's look at some of the [basic commands here](https://arctraining.github.io/swd3-dev/sections/package-manager.html#environment-conda-example).
Again, let's use the codespaces virtual machine as a sanbox to practise building (and breaking!)
environments.

Conda is just one of the many options available to manage Python packages and dependencies,
however it is very widely used in scientific research.
See this [cheat-sheet](https://www.datacamp.com/cheat-sheet/conda-cheat-sheet) for other commonly used commands.
"""

# git basics

git_md = """
## Essential git commands

We will use git and a GitHub remote repository to track our changes. You can use git in
the codespaces virtual machine in
 the same way you would from your local machine.
 See [this basic intro to git](https://rogerdudler.github.io/git-guide/).

But first, [what is git and version control?](https://arctraining.github.io/swd3-dev/sections/git.html).

```bash
git status # check on status of current git repo
git branch NAME # create a branch called NAME
git checkout NAME # swap over to the branch called NAME
git add FILE # stage FILE for commit
git commit # commit the staged files (this will open your text editor to create a commit message)
git push origin NAME # push local commits to the remote branch tracking the branch NAME
```

Let's try some [basic git commands](https://arctraining.github.io/swd3-notes/session1/) in our virtual
machine.

### Visualising Git history

The VSCode plugin "GitGraph" is very useful; this is added by default to the codespaces
virtual machine but also can be added to your local VSCode installation.

---

## Making version control work for you

Data scientists love to use Jupyter notebooks as a tool for *literate programming*. While notebooks are a fantastic tool, they are useful mainly *in conjunction with properly formatted Python scripts*. Jupyter notebooks do not
behave well with version control tools due to the extra non-Python code stored in them to allow for the notebook to render.

Ideally, notebooks can be used as part of a development workflow:
- Notebooks are useful when prototyping code and exploring data. Once functions have been developed, they should be moved to a separate `.py` script and
imported into the notebook as a module.
- Notebooks are useful for creating example sets or tutorials for your documentation website.
- Notebooks are useful to display your final results.

Please don't *only* store your code in notebooks.

### Notebooks, repositories and sensitive data

Of course, your data should be stored in a separate folder to your code. Your raw data should remain unedited, untouched, exactly as collected; processed data should be stored in a separate directory (see the section on project layout). This is obviously mandatory and not just "good practise" when it comes to sensitive data. Your code, stored in a repository, should be completely clean of any data.

**This also applies to notebook output.**

It is _vital_ to ensure there is no identifying information stored as output or cached in your Jupyter Notebooks or various cache files before pushing to GitHub.

There are a number of ways around this; some of these options need to be combined or work together:

- Option 1: the easiest, but worst and most likely to fail. Manually clearing output from your notebook (in Jupyter, using `Edit > clear all outputs`). Do this anyway, but **don't rely on this because some day you will forget**.
- Option 2: use a plaintext Jupyter Notebook alternative so output isn't an issue. 
- Option 3: ensure Jupyter Notebook file endings are in your gitignore so you have to specifically add them as an additional manual check. For example, [Jupytext](https://jupytext.readthedocs.io/en/latest/) or [MyST Markdown](https://mystmd.org/) might work well for you.
- Option 4: Use git hooks or pre-commit framework to strip output from Jupyter Notebooks and ensure this is not pushed to the remote repository. See [nbstripout](https://github.com/kynan/nbstripout#using-nbstripout-as-a-pre-commit-hook).
"""

#mkdocs basics

docs_basics = '''
## Writing docs for your code

Good documentation in your code will act like helpful comments
for human users (helping to explain the code and how it works),
but will *also* be machine-readable and can help to generate
documentation webpages.

### Commenting your code

You can add single-line comments to your code using the `#` symbol,
or multiline comments by surrounding the comment in triple quotation marks:

```python
# This is a single line comment

x = 4 * 3  # This is an inline comment

""" 
This is a multiline comment.
All the text included between the quotation
marks is commented out and won't be executed

x = 4 * 3 <- including snippets of code
"""
```

How do we ensure comments in our code are useful? We can keep in mind
these four rules suggested by [Jeff Atwood](https://blog.codinghorror.com/when-good-comments-go-bad/), referenced in this [RealPython tutorial](https://realpython.com/documenting-python-code/):

1. **Keep comments close to the code they are describing.** For example,
use a single line comment immediately before/after the piece of code it
describes, rather than creating a large multiline comment elsewhere in the code.
Inline comments are useful for very brief pointers.
2. **Keep comment formatting as simple as possible.** Using complex formatting
(for example, a markdown-style table) in your comments will make it difficult
to update it and will discourage you from keeping your comments up to date
and relevant.
3. **Don't make pointless comments.** It sounds obvious, but don't comment for the sake of it: for example, including a comment that says `# assign the value 25 to the variable x` near the code `x = 25` is a waste of everyone's time! Use
version control to track changes instead of a "Revision history" comment at the
top of your script. Excess unnecessary comments distract from the actual useful documentation. Assume the person reading understands the basics of the coding language syntax.
4. **Write code that needs as few comments as possible.** You should aim to
write legible, easy to understand code, that is tidy, straightforward, and
follows good coding conventions. Variable names should be descriptive and
not require a comment explanation; functions should be short; algorithms
should be as simple as possible. Lean on documentation standards such as including docstrings and type hints (described below in more detail) to
reduce the need for ad-hoc comments.

These rules are applicable regardless of the language you are using.

> *A quick aside on in-progress commenting: it can be very useful to use
> comments as you write and develop your code, either tagged with labels
> such as `TODO` or `FIXME`, or when writing pseudocode, or when trying 
> to solve a tricky problem. Don't be afraid to use comments as a tool
> when developing your code: you can clean them up as they become obsolete.*

---

### Docstrings

Docstrings are organised snippets of documentation inside
functions that explain what the function does and can
provide context on the function input and output.

Docstrings are always surrounded by triple quotation marks.
A very simple docstring can be a single line after the function call,
while a basic multi-line docstring in a function will look something like this:

```python
def function_name(arg1: type, arg2: type) -> return_type:
    """One line summary

    More detail on the function, with a blank line between the one-
    line summary and this more in-depth text.
    """

    # After another blank line, continue code
    return something
```

---

In the devcontainer, we define a number of extensions for VSCode in the codespaces
virtual machine, including `autodocstring` which will generate a basic
docstring template for you. For example, we can write a function that looks like
this:

```python
def example_function(arg1: str, arg2: float, arg3:int):
    
    # lots of code that does interesting things
    value1 = arg1 + "_result"
    value2 = arg2 * arg3
    
    return value1, value2
```

In this example, we've added in some **type hints** with the function arguments:
`(arg1: str, arg2: float, arg3:int)` which provides guidance to the user as to
the kind of input arguments required.

If we move the cursor to after the colon following the functon definition
(`def example_function(arg1: str, arg2: float, arg3:int):|`) and press enter
to go to a new line, and enter triple quotation marks, you will get the option
to "Generate Docstring". You can click enter and a dcstring template will be
inserted for you:

```python
def example_function(arg1: str, arg2: float, arg3:int):
    """_summary_

    Args:
        arg1 (str): _description_
        arg2 (float): _description_
        arg3 (int): _description_

    Returns:
        _type_: _description_
    """
    
    # lots of code that does interesting things
    value1 = arg1 + "_result"
    value2 = arg2 * arg3
    
    return value1, value2
```

You can then fill this docstring out with details.

> Note: it's best to use the autogenerated docstring feature once you've added in your arguments and their types; otherwise the template will not include these
sections.

---

### Other code documentation

In additional to individual function docstrings, it's a good idea to
include package or module docstrings at the top of your Python scripts.
See the [RealPython: Package and Module Docstring](https://realpython.com/documenting-python-code/#package-and-module-docstrings) section to see examples.

If you're planning on sharing your code more widely, it's a good idea to
take your docstrings and create a user-friendly documentation website with it.
This can be done in an automated fashion with packages such as Sphinx or Mkdocs.
Additionally, it's a good idea to write a more conversational "how-to" guide,
and include some example scripts to get users up and running quickly with your code.


See this in-depth tutorial [for more information on writing documentation](https://realpython.com/documenting-python-code/).

---


'''

mkdocs_md = """
## Essential mkdocs commands

Ensure you are using a conda environment that has mkdocs and the required additional packages installed (you can
install the ready-made `mkdocs-env` in your virtual machine by running `conda env create --file .devcontainer/env-files/mkdocs-env.yml` and then
activating it with `conda activate mkdocs`).

The following commands should be run from the main folder of your repository (where your `pyproject.toml` is).
```bash
mkdocs new . # initialise a new mkdocs project
# You can now edit the mkdocs yml file
TZ=UTC mkdocs serve # serve the mkdocs website without time zone errors
# you may need to set up port forwarding to view the website
TZ=UTC mkdocs build # build your docs files in a /site dir
TZ=UTC mkdocs gh-deploy # deploy the website - change settings on your gh repo to allow writing by actions
```

You should edit your `mkdocs.yml` to contain the following plugins so that it can find your docs:

```yaml
site_name: NAME HERE

theme:
  name: "material"

plugins:
- mkdocstrings:
    handlers:
      python:
        paths: [src]  # search packages in the src folder

nav:
  - FILE NAME HERE: index.md
```

If you have added sensible and well-formatted comments and docstrings to your code, you can use the `mkdocstring`
plugin to automatically build your documentation.

Simply include:

```
::: YOUR_PACKAGE_NAME
```

in one of the markdown files included in your docs (for example, `index.md`) to include any docs you have added to your package `__init__.py` file.

To include function-level documentation, just include:

```
::: YOUR_PACKAGE_NAME.MODULE_NAME
```


For more detail on customising your `mkdocs` set-up and on writing good documentation, please see this [fantastic RealPython tutorial](https://realpython.com/python-project-documentation-with-mkdocs/).
"""

mkdocs_code = """
```yaml
site_name: SWD7 - Introduction to Data Visualisation in Python

repo_url: https://github.com/ARCTraining/swd7-notes
repo_name: SWD7-notes

copyright: By University of Leeds Research Computing Team, Copyright &copy; 2024

theme:
  name: "material"
  custom_dir: overrides
  icon:
    repo: fontawesome/brands/github
  features:
    - content.code.copy
    - navigation.footer
  palette:
    # Palette toggle for light mode
    - scheme: default
      primary: deep purple
      accent: deep purple
      toggle:
        icon: material/brightness-4
        name: Switch to dark mode

    # Palette toggle for dark mode
    - scheme: slate
      primary: deep purple
      accent: deep purple
      toggle:
        icon: material/brightness-7
        name: Switch to light mode

plugins:
- mkdocs-jupyter:
    ignore_h1_titles: True
    include_source: True
  - search
  - toggle-sidebar
  - awesome-pages
  - mermaid2:
      arguments:
        theme: 'base'

markdown_extensions:
  - pymdownx.arithmatex:
        generic: true
        block_tag: 'pre'
  - pymdownx.details
  - pymdownx.tilde
  - pymdownx.snippets
  - admonition
  - pymdownx.blocks.tab
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true


nav:
  - Course content: index.md
  - Delivery guidelines: guidelines.md
  - Introduction: 00-Introduction.md
  - 5 Key Concepts:
    - 1. Audience: 01-Audience.md
    - 2. Story: 02-Story.md
    - 3. Encoding: 03-Encoding.md
    - 4. Composition: 04-Composition.md
    - 5. Simplify: 05-Simplify.md
  - Practical Session:
    - How to use this resource: nbs/00_explanation.md
    - Building gridded plots: nbs/gridded_plots.md
    - 1. Introduction notebook: nbs/01_datavis_solutions.ipynb
    - 2. Other libraries notebook: nbs/02_datavis_solutions.ipynb
    - 3. Composition of multi-panel plots notebook: nbs/03_datavis_solutions.ipynb
    - 4. Exploring heatmaps and legends: nbs/04_datavis_solutions.ipynb
    - 5. Exploring a dataset: nbs/05_datavis_solutions.ipynb
```
"""

# test basics

test_markdown = """

### No tests = not science

A bold statement! But code that does not have tests is straightforwardly
not following the scientific method. You **must** test your code.

We saw in the section on applying **DeReLiCT** to your code how to design tests
([see here](Avoid_DeReLiCT_code#write-initial-tests)), but for quick reference here is a template you can use to build your tests:

```python
def test_example(self):
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 
    test_variable_2 = 
    expected_output = 

    # Act
    output = your_function(test_variable_1, test_variable_2)

    # Assert
    assert output == expected_output

    # Cleanup
```

In your tests directory, remember to include a file called 
`__init__.py` file in your `tests/` directory, containing
the following:

```python
import sys

sys.path.append("src")
```

To run your tests, simply call `pytest` from the project
directory.

This [RealPython testin tutorial](https://realpython.com/python-testing/)
contains a lot more information for you to dig into this topic in more depth.

"""

with tab1:
    
    st.write(bash_md)
    with st.expander("Click here for a full cheat-sheet"):
        st.markdown(bash_2)
    st.markdown(bash_3)

with tab2:

    st.write(conda_md)

with tab3:

    st.write(git_md)

with tab4:
    st.write(docs_basics)

    st.write(mkdocs_md)
    with st.expander("Click here to see an example detailed yml file"):
        st.write(mkdocs_code)

with tab5:
    st.write(test_markdown)


st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)

md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)

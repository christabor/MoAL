# Enable
sudo launchctl load -F /System/Library/LaunchDaemons/telnet.plist
# Disable
sudo launchctl unload -F /System/Library/LaunchDaemons/telnet.plist

# Find network status for telnet
netstat -tcp | ag telnet

# Listen to network traffic
brew install ngrep # (if not installed)
sudo ngrep port 23

# Log in to and use telnet via CLI, instead of python
telnet
# telnet> open
# (to) localhost
# ...
# login: USERNAME
# Password: PASSWORD
# ...

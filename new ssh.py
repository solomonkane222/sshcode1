import re
import pexpect

# Define variables
ip_address = '192.168.56.101'
username = input('Enter Username (e.g., prne): ')
password = input('Enter Password (e.g., cisco123!): ')
password_enable = 'class123!'

# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to create an SSH session for IP address:', ip_address)
    exit()

# Session expecting a password, entering details...
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to enter the password:', password)
    exit()

# Entering enable mode...
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to enter enable mode')
    exit()

# Sending enable password...
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to enter enable mode after sending the password')
    exit()

# Entering configuration mode...
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to enter configuration mode')
    exit()

# Changing hostname to R3...
session.sendline('hostname R3')  # Changing the hostname to R3
result = session.expect([r'R3\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if it exists then display an error and exit
if result != 0:
    print('Failed to set the hostname to R3')

# Exiting configuration mode...
session.sendline('exit')

# Exiting enable mode...
session.sendline('exit')

# Displaying a success message if it works
print('------------------------------------------------------')
print('')
print('Successfully connected to IP address:', ip_address)
print('Username:', username)
print('Password: ********')  # Masking the password for security
print('New Hostname: R3')
print('')
print('------------------------------------------------------')

# Terminating the SSH session
session.close()

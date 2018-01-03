# getInvitePending
Pull all users from Spark Org and find users in invite pending state and write those users to a CSV file

## Requirements:
- Must be run on a Mac or Windows
- Must be run with the authorization token from a Spark Admin user. Authorization token can be found by navigating to https://developer.ciscospark.com > Logging in > Clicking on user avatar picture at the top right. This will show your authorization token. Copy this and use it to run the application. 
- The python requests library must be installed. To do this you must install the package using pip using the command 'pip install requests'
    - Instructions on using pip on Windows: https://python-forum.io/Thread-Basic-Part-1-Python-3-6-and-pip-installation-under-Windows


## Run Instructions:
1) Download the getInvitePendingUsers.py file to your computer.
2) On Mac, launch 'Terminal.app'. For Windows, open your Python interpreter.
3) Issue the following command to run the script:  python getInvitePendingUsers.py
    - Mac Example: python ~/Desktop/getInvitePendingUsers.py
    - Windows Example: C:\>python C:\getInvitePendingUsers

  

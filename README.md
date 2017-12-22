# getInvitePending
Pull all users from Spark Org and find users in invite pending state and write those users to a CSV file

## Requirements:
- Must be run on a Mac or Windows
- Must be run with the authorization token from a Spark Admin user. Authorization token can be found by navigating to https://developer.ciscospark.com > Logging in > Clicking on user avatar picture at the top right. This will show your authorization token. Copy this and use it to run the application. 
- The following python libraries must be installed:
requests
csv
os
time
sys

## Run Instructions:
1) Download the getInvitePendingUsers.py file to your computer.
2) On Mac, launch 'Terminal.app'. For Windows, open your Python interpreter.
3) Issue the following command to run the script:  python <path to script>/getInvitePendingUsers.py (ex. python ~/Desktop/getInvitePending.py)
  

#Add SSH key
import os
import sys
#import paramiko




def USAGE():
    print("\nPlease specify arguments in the following order:\n")
    print("AddSSH.py target_Machine_name Target_account_name target_password sync (if you want it to be synchronous) ")
    print ("The Script was called with " , ( len(sys.argv) - 1 ), "arguments instead of 5" )
    sys.exit(1)

if ( len(sys.argv) != 3 ):
    USAGE()


target_machine = sys.argv[1]
target_account = sys.argv[2]
target_password = sys.argv[3]
#is_synchronous = sys.argv[5]
#print ("[INFO]: Going to execute:", sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5] )


#On target
print(os.path.exists("/home/.ssh"))
print(os.path.exists("/home/.ssh/authorized_keys"))
print(os.path.exists("/home/.ssh/known_hosts"))

#on Source
print(os.path.exists("/home/.ssh"))
print(os.path.exists("/home/.ssh/known_hosts"))
print(os.path.exists("/home/.ssh/id_rsa.pub"))




#ssh=paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(target_machine, port=22, 'pcicrm1', password='Unix11!')

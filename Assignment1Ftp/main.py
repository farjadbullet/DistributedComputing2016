from ftp import Ftp
host = input("Please Enter Host\n")
username = input("Please Enter Username\n")
password = input("Please enter password\n")
ftp = Ftp(host,username,password)
while (True):
    mode = int(input("1.Download \n2.Upload\n"))
    if (mode == 1):
        ftp.listDirectory()
        filename = input("Please enter path of file to download\n")
        ftp.downloadFile(filename)
        
    else:
        filename = input("Please enter path file to upload\n")
        ftp.uploadFile(filename)

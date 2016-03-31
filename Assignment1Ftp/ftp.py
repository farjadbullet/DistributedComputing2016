import ftplib

class Ftp():
    def __init__(self, host, username, password):
        
        self.ftp = ftplib.FTP(host)
        self.ftp.login(username, password)
        self.ftp.dir()
        
    def uploadFile(self, fileName):
        self.ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
        self.ftp.quit()
        print "Success!"

    def downloadFile(self, fileName):
        localfile = open(fileName, 'wb')
        self.ftp.retrbinary('RETR ' + fileName, localfile.write, 1024)
        self.ftp.quit()
        localfile.close()
        print "Success!"
    def listDirectory(self):
        self.ftp.dir()






            

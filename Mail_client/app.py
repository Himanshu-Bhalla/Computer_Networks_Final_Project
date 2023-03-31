from socket import *
import ssl
import base64
import getpass
#import OpenSSL
from flask import Flask
from flask import request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route("/send")

def send_email():
    receiver = request.args.get("receiver")
    Subject = request.args.get("subject")
    Text = request.args.get("body")
    option = request.args.get("option")
    filename = request.args.get("attach")


    endmsg = "\r\n.\r\n"

    if option == "no":

        gooogleSMTPServer = 'smtp.gmail.com'
        gooogleSMTPPort= 465

        print ("creating the socket")
        clientSocket = socket(AF_INET,SOCK_STREAM)
        print ("connecting to the socket")

        wrappedSocket = ssl.wrap_socket(clientSocket,
                        ssl_version=ssl.PROTOCOL_TLSv1,
                        ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5",
                        cert_reqs=ssl.CERT_REQUIRED)

        wrappedSocket.connect((gooogleSMTPServer, gooogleSMTPPort))

        print ("socket is connected")
        recv = wrappedSocket.recv(1024)

        print ("received msg is: %s" % recv)
        if recv[:3] != '220':
            print ('Remote server not responding to 220.')

        Commandhelo = 'HELO Alice\r\n'
        print Commandhelo
        wrappedSocket.send(Commandhelo)
        recv1 = wrappedSocket.recv(1024)
        print "Received msg from recv1 is: %s" % recv1
        if recv1[:3] != '250':
            print 'Remote server not responding to 250.'

        # you can enter your passwords in Username and Password
        Username="gbsir87@gmail.com"
        Password= "qwaszxerdfcv12#$"

        UP=("\000"+Username+"\000"+Password).encode("base64")

        print UP
        UP=UP.strip("\n")
        login = 'AUTH PLAIN '+ UP + '\r\n'
        print login
        wrappedSocket.send(login)
        recv_from_TLS = wrappedSocket.recv(1024)
        print recv_from_TLS

        fromCommand = 'MAIL FROM: <'+ Username+'>\r\n'
        print fromCommand
        wrappedSocket.send(fromCommand)
        recv2 = wrappedSocket.recv(1024)
        print "Received msg from recv1 is: %s" % recv2
        if recv2[:3] != '250':
            print('rcpt2 to 250 reply not received from server, cabron.')

        toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
        print toCommand
        wrappedSocket.send(toCommand)
        recv3 = wrappedSocket.recv(1024)
        print "Reply received from server 3 is : %s" % recv3
        if recv3[:3] != '250':
            print('rcpt3 to 250 reply not received from server, cabron.')

        dataCommand = 'DATA\r\n'
        print dataCommand
        wrappedSocket.send(dataCommand)
        recv4 = wrappedSocket.recv(1024)
        print recv4
        wrappedSocket.send("Subject: "+Subject+"\r\n\r\n"+Text+"\r\n"+ endmsg +"\r\n")
        recv5 = wrappedSocket.recv(1024)
        print recv5

        wrappedSocket.send("QUIT\r\n")
        recv6 = wrappedSocket.recv(1024)
        print recv6
        wrappedSocket.close()

        return "done"
    else:
        # you can enter your username in fromaddr

        fromaddr = "your email"
        toaddr = receiver

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        msg['Subject'] = Subject

        body = Text

        msg.attach(MIMEText(body, 'plain'))


        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
        # you can enter your password in s.login() after fromaddr

        s.login(fromaddr, "Your_Password")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        return "done"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

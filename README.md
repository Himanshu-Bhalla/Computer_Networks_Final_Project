# Email Client
In this project we created an Email client using python and websockets. The additional feature added is that it can also send attachments.

# Steps to run the code
Before following the below steps download the full zip code from github. You can use any compiler but I have shown you the process using pycharm.

## Step1
Open the Pycharm and in the bottom right corner click on add interpreter and then a new window will open there click on new "Inherit global site-packages" and then give name to your virtual environment.
Initially we have given venv but in your machine u will have to add another.
Below are the images of both windows.
![Adding interpreter](https://i.imgur.com/ONiyguo.png)
![Adding interpreter 2](https://i.imgur.com/t8X8MP1.png)

## Step 2
Enter the username and password of the account from which you want to send mail on line 59,60,104,136.
![Username and password](https://i.imgur.com/4L5oauP.png)

## Step 3
Open the pycharm terminal and enter command "pip install flask" to download flask.Given below is the screenshot and the command.
```aidl
pip install flask
```
![installing flask](https://i.imgur.com/0qISAUW.png)

## Step4
Now to run server thpe the command "python -m flask run" to run the deployment server.Given below is the screenshot and the command.
```aidl
python -m flask run
```
![Server](https://i.imgur.com/S5u2t8V.png)

## Step 5
Now open index.html file from the downloaded zip file and open that file using Google Chrome.I have attached the screenshot of the homepage of the mail client. Now 
in the mail client you will have to type whether you want to send attachment or not. Then fill all the details.
![Server](https://i.imgur.com/ZGT22XG.png)

### Below is the screenshot of mail send without attachment
![Server](https://i.imgur.com/KpO5JbA.png)

Screenshot of sent side.
![Server](https://i.imgur.com/vjgfUJB.jpg)

Screenshot of received mail.
![Server](https://i.imgur.com/i7mWIZS.jpg)

### Below is the screenshot of mail send with attachment
![Server](https://i.imgur.com/4vETz76.png)

Screenshot of sent side.
![Server](https://i.imgur.com/RH7xchr.jpg)

Screenshot of received mail.
![Server](https://i.imgur.com/RXFDQVb.jpg)

# Future work and contact details

For now, our mail client has features like it can send emails which allow us to send and read emails all over the globe. It has an interactive GUI which is user-friendly and easy to use. User authentication allows only trusted and authenticated users to send emails so that the unauthorized and spam mails could not be there.
Additionally, in the future, we are planning to add a feature to see whether the mail has reached the receiver or not and whether it has been read or not. This would really help the sender who has some important work and it needs to get transferred as well as read by the user immediately. We are also looking to make it simpler, like having different folders like sent, spam starred, deleted, etc. This would help users to have a more easy way to access the mails. The user can also delete the mail that he has sent in a time gap of 10 minutes prior to the receiver receiving it, so if the mail has been sent mistakenly it can get deleted before getting received.
We are also working on the idea of having a premium option, where users can pay to get some more additional features that are not available in the normal mail client. Setting up a paid subscription option would help us to make it a better one to execute.


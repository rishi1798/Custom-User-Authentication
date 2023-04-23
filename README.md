Steps to run Application:

1.First of all create and activate the virtual environment.

2.After activating the virtual environment install all the dependencies by command pip install -r requirements.txt

3.Run command python manage.py makemigrations and python manage.py migrate

4. Once migrations has been run run the application by python manage.py runserver

5. Now register with your Email id and contact number.After successful registration u can login into account.

6. After login u are redirected to Home page.Where u will see two option first is Logout and second is visit your profile.

7. In your profile section u can update your profile by entering more information about yourself by adding your bio,address and full name.

8. When u click on forget password option. u are redirected to forget password page and their u have to enter your registered mail id.

9. Now check your mail. U should have recieved a change paasword link mail. if u not received that mail u have to generate app password for your google acount.

10.Well, you need to generate a password from your google account (2 factor authentication). It is one time shown.

11.Create & use App Passwords
If you use 2-Step-Verification and get a "password incorrect" error when you sign in, you can try to use an App Password.

1.Go to your Google Account.
2.Select Security.
3.Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
  a. 2-Step Verification is not set up for your account.
  b. 2-Step Verification is only set up for security keys.
  c. Your account is through work, school, or other organization.
  d. You turned on Advanced Protection.
4. At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
5. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
6. Tap Done.

12. Now put your email id and app password in settings.py file of project under EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.

13.Now try again sending mail for changing password.

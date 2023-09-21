import speech_recognition as sr
import pyttsx3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_voice_input():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except Exception as e:
        print(e)
        return None

def speak(text):
  
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def send_email(subject, body, sender_email):
  
    sender_email=''.join(sender_email.split())
    recipient_email = sender_email
    msg = MIMEMultipart()
    msg['From'] = recipient_email
    msg['To'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    username = 'gprasanth60@gmail.com'
    password = 'zxztxhmvqebjkxmy'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

def main_loop():
    
    
    print("Hi! I'm Buddy, your personal email assistant.")
    speak("Hi! I'm Buddy, your personal email assistant.")
    
    speak("What is the subject of your email?")
    subject = get_voice_input()
    while not subject:
        speak("Sorry, I didn't understand that. Please try again.")
        subject = get_voice_input()

 
    speak("What would you like to say in the email?")
    body = get_voice_input()
    while not body:
        speak("Sorry, I didn't understand that. Please try again.")
        body = get_voice_input()

    print("Who is the email provider: A)Gmail B)MUJ C)Outlook ")
    speak("Who is the email provider: A)Gmail B)MUJ C)Outlook ")
    email = get_voice_input()
    if(email=='a'):
        email="@gmail.com"
    elif(email=='b'):
        email="@muj.manipal.edu"
    elif(email=='c'):
        email="@outlook.com"
        
    while not sender_email:
        speak("Sorry, I didn't understand that. Please try again.")
        email = get_voice_input()

    speak("What is the email address you want to send?")
    sender_email = get_voice_input()+email
    while not sender_email:
        speak("Sorry, I didn't understand that. Please try again.")
        sender_email = get_voice_input()

    speak("Here is your email. Please confirm the details.")
    speak(f"Subject: {subject}")
    speak(f"Body: {body}")
    speak(f"Sender email: {sender_email}")
    speak("Do you want to send this email?")
    response = get_voice_input()
    while response not in ['ok', 'no','yes','okay']:
        speak("Sorry, I didn't understand that. Please try again.")
        response = get_voice_input()

    if response == ('ok')or('okay')or('yes'):
        send_email(subject, body, sender_email)
        speak("Email sent successfully.")
    else:
        speak("Email not sent.")
    
    speak("Goodbye!")


if __name__ == '__main__':
    main_loop()

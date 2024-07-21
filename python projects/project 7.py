from plyer import notification
import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
notification.notify(
title = " Notification",
message = "iqbal drink water",
timeout = 10
)
text=" hi good morning iqbal did you drink water today"
time.sleep(5)
speak.Speak(text)

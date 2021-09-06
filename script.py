import speech_recognition as sp
import time
"""
for index, name in enumerate(sp.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
"""

rec = sp.Recognizer()



my_micro = sp.Microphone(device_index=7)

with my_micro as source:
  print("Recognition to start in 3 seconds")
  print('3')
  time.sleep(1)
  print('2')
  time.sleep(1)
  print('1')
  time.sleep(1)
  print('Start Speaking')
  audio = rec.listen(source, phrase_time_limit=10)

  to_text = rec.recognize_google(audio)

print(to_text)

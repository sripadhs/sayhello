import pyttsx3
import streamlit as sl
speaker=pyttsx3.init()
sl.title('Say hello!')
inp=sl.text_input('Enter the text:')
if sl.button('Say hello!'):
    sl.header('hello '+inp)
    speaker.say('hello '+inp)
speaker.runAndWait()
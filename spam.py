import pyautogui
import time
import os

os.system("echo //////////////////////////////////////////////////////////////////////////////////////////")
os.system("echo ///   ::::::::::     :::      :::      ::::::::::::      ::::::::::::      :::         ///")
os.system("echo ///   :::            :::      :::           :::          :::      :::      :::         ///")
os.system("echo ///   :::            :::      :::           :::          :::      :::      :::         ///")
os.system("echo ///   :::::::::      :::      :::           :::          :::      :::      :::         ///")
os.system("echo ///         :::      :::      :::           :::          ::::::::::::      :::         ///")
os.system("echo ///         :::      :::      :::           :::          :::      :::      :::         ///")
os.system("echo ///   :::::::::      ::::::::::::      ::::::::          :::      :::      :::::::::   ///")
os.system("echo //////////////////////////////////////////////////////////////////////////////////////////")
os.system("echo **CREATED THIS MACBETH SPAM!**")
os.system("echo Find some other code here!      https://sujalgoel.ml")

seconds=10

for i in range(seconds):
    print(str(seconds - i) + " seconds remaining to start the script")
    time.sleep(1)

time.sleep(1)
file = open("macbeth.txt", "r")

for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

input("Press enter and exit")
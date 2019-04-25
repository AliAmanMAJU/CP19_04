import pyshark
cap = pyshark.FileCapture('SkypeIRC.cap')

print(cap[0])

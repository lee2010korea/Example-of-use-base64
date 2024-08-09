import base64
while True:
  print("join")
  print("login")
  x = input("--->")
  if x == "join": 
    idd = input("id--->")
    iddb = idd.encode("UTF-8")
    iddc = base64.encodebytes(iddb)
    iddd = iddc.decode("UTF-8")
    pas = input("password--->")
    pasb = pas.encode("UTF-8")
    pasc = base64.encodebytes(pasb) 
    pasd =pasc.decode("UTF-8")
    idd = 0
    iddb = 0
    iddc = 0
    pas = 0
    pasb = 0
    pasc = 0  
  else:
    if x == "login":
      xid = input("id--->")
      xidb = xid.encode("UTF-8")
      xidc = base64.encodebytes(xidb)
      xidd = xidc.decode("UTF-8")
      xpass = input("password--->")
      xpassb = xpass.encode("UTF-8")
      xpassc = base64.encodebytes(xpassb)
      xpassd = xpassc.decode("UTF-8")
      xid = 0
      xidb = 0
      xidc = 0
      xpass = 0
      xpassb = 0
      xpassc = 0
      if xidd != iddd or xpassd != pasd:
        print("fail")
      else:
        print("good")  
from sys import argv
import sys

helpCopyright=""
helpDescription=""
helpExample=""
helpSerial=[]
helpSerialDesc=[]
helpKey=[]
helpKeyNeedValue=[]
helpKeyDesc=[]
paraSerial=[]
paraKey=[]
paraValue=[]
paraHelp=[]
paraName=""


# set help description

def setCopyright(desc):
  global helpCopyright
  helpCopyright=desc

def addDescription(desc):
  global helpDescription
  if helpDescription=="":
    helpDescription=desc
  else:
    helpDescription=helpDescription+"\n"+desc

def addExample(desc):
  global helpExample
  if helpExample=="":
    helpExample=desc
  else:
    helpExample=helpExample+"\n"+desc

# set para

def addSerial(k, desc):
  global paraHelp
  global helpSerial
  global helpSerialDesc
  paraHelp.append(k + " = " + desc)
  helpSerial.append(k)
  helpSerialDesc.append(desc)

def addKey(k, desc, needvalue):
  global paraHelp
  global helpKey
  global helpKeyDesc
  paraHelp.append("/"+ k + " = " + desc)
  helpKey.append(k)
  helpKeyDesc.append(desc)
  helpKeyNeedValue.append(needvalue)


# get para

def serial(i, default):
  if i in range(1,len(paraSerial)):
    return paraSerial[i]
  else:
    return default

def key(k, df):
  if k in paraKey:
    return paraValue[paraKey.index(k)]
  else:
    return df

# utility
# Set text color : "\033["+x+";"+yy+";"+zz"+"m"+text+"\033[m"
#   x = 0 default, 1 Highlight, 4 underline, 5 blink, 7 reverse, 8 hide;
#   yy (x=0/1) = 30 black/darkgray, 31 red/light, 32 green/light, 33 brown/yellow, 34 blue/light, 35 purple/light, 36 cyan/light, 37 lightgray/white
#   zz = 40 black, 41 red, 42 Green, 43 Yellow, 44 Blue, 45 Purple, 46 Cyan, 47 White

def printHelp(num):
  if num.isdigit():
    if int(num)-1 in range(0,len(helpSerial)):
      print("\033[31m[Error "+num+"]\033[m on "+ helpSerial[int(num)-1])
  if num.isalpha():
    if num in helpKey:
      print("\033[31m[Error 201]\033[m on para '" + num + "', " + helpKeyDesc[helpKey.index(num)])

  print("\033[36m" + paraName + "\033[m by ZZX")
  if helpDescription!="":
    print("\033[32m Function:\033[m")
    #print("\033[1;30m"+helpDescription+"\033[m")
    print(helpDescription)
  print("\033[32m Usage:\033[m")
  s = ""
  for i in helpKey:
    if helpKeyNeedValue[helpKey.index(i)]:
      s = s + " /" + i + " " + i
    else:
      s = s + " /" + i
  for i in helpSerial:
    s = s + " " + i
  print("  " + paraName + s)
  print("\033[32m where:\033[m")
  for i in paraHelp:
    print("  " + i)
  if helpExample!="":
    print("\033[32m Example:\033[m")
    print(helpExample)
  print("\033[32m Copyright(C) " + helpCopyright + "\033[m")
  sys.exit()

def printall():
  print("helpSerial:")
  print(helpSerial)
  print("helpSerialDesc:")
  print(helpSerialDesc)
  print("helpKey:")
  print(helpKey)
  print("helpKeyDesc:")
  print(helpKeyDesc)
  print("paraSerial:")
  print(paraSerial)
  print("paraKey:")
  print(paraKey)
  print("paraValue:")
  print(paraValue)
  print("paraHelp:")
  print(paraHelp)
  print("paraName:")
  print(paraName)


# parse

def parse(a):
  global paraName
  global paraSerial
  global paraKey
  global paraValue

  iskey=False
  paraError=False
  k=0
  s=0
  paraName=a[0]
  for i in a:
    if ((i[0:1]=='/') and len(i)>=2):
      if iskey==False:
        paraKey.append(i[1:])
        iskey = True
        if i[1:] in helpKey:
          if helpKeyNeedValue[helpKey.index(i[1:])]==0:
            paraValue.append("True")
            iskey = False
      else:
        print("\033[31m[Error 101]\033[m "+i[1:]+" need value.")
        printHelp("")
    elif iskey==True:
      paraValue.append(i)
      iskey=False
      k=k+1
    else:
      paraSerial.append(i)
      s=s+1
  if iskey==True:
    if i[1:] in helpKey:
      if helpKeyNeedValue[helpKey.index(i[1:])]==0:
        paraValue.append("True")
        iskey = False
      else:
        print("\033[31m[Error 102]\033[m Para '"+i[1:]+"' need value.")
        printHelp("")
    else:
      print("\033[31m[Error 103]\033[m Unknown para '" + i[1:] +"'")
      printHelp("")
  if key("h", "False")=="True":
    printHelp("")
    sys.exit()
  if len(helpSerial) > len(paraSerial):
    print("\033[31m[Error 100]\033[m Need more para.")
    printHelp("")
    sys.exit()



'''

#example
import argument

# set paras
argument.addSerial("ifn", "input file name")
argument.addSerial("ofn", "output file name")
argument.addSerial("page", "output file name")
argument.addKey("i", "input file name",1)
argument.addKey("o", "output file name",1)
argument.addKey("h", "help",0)

# parse
argument.parse(argv)

# get paras
print(argument.serial(1,"f.pdf"))
print(argument.serial(2,"f2.pdf"))
print(int(argument.serial(3, "12")))

# if error, print help
try:
  ...
except IOError as e:
  argument.printHelp("1")

'''

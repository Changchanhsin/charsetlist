import sys
import writefile

start=[0x81,0x30,0x81,0x30]
#end  =[0xFE,0x39,0xFE,0x39]
end  =[0x9A,0x34,0xFE,0x39]
fn   ="GB18030fourBelt.html"
title=""

def checkEqual(s,d,l,v):
  for i in range(0,l):
    if(s[i]!=d[i]):
      return v
  return d[l]

def stringHEX(num):
  ret = ""
  if( type(num)==list):
    for i in num:
      ret= ret+'{:02X}'.format(i)
  else:
    ret = ret+'{:02X}'.format(num)
  return ret

if(len(sys.argv)>=3):
  maxargv=len(sys.argv)
  argStart= writefile.cut(sys.argv[maxargv-2],2)
  argEnd  = writefile.cut(sys.argv[maxargv-1],2)
  for i in range(len(argStart)):
    start[i]=int(argStart[i],16)
  for i in range(len(argEnd)):
    end[i]=int(argEnd[i],16)
  if(maxargv>=4):
    fn=sys.argv[1]
  if(maxargv>=5):
    title=sys.argv[2]
elif(len(sys.argv)>1):
  fn=sys.argv[1]
  if(len(sys.argv)>2):
    title=sys.argv[2]

with open(fn, 'wb')as f:
  writefile.head(f, "gb18030","SimSun");
  writefile.info(f, "GB 18030 four",title, stringHEX(start) + " - " + stringHEX(end))
  i=[0]*4
  for i[0] in range(start[0],end[0]+1):  # 0x81..0xFE

    #print(i[0])
    sHL=checkEqual(i,start,1,0x30)
    eHL=checkEqual(i,end,1,0x39)
    for i[1] in range(sHL,eHL+1): # 0x30..0x39

      #print(i1)
      writefile.arrayBegin(f)
      writefile.arrayTitle(f,11, stringHEX(i[0]) + stringHEX(i[1]))
      writefile.arrayHead(f, 0, range(0x30,0x3A), 0,  stringHEX(i[0]) + stringHEX(i[1]), 256)
      sLH=checkEqual(i,start,2,0x81)
      eLH=checkEqual(i,end,2,0xFE)
      for i[2] in range(sLH, eLH+1): # 0x81..0xFE

        #print(i2)
        sLL=checkEqual(i,start,3,0x30)
        eLL=checkEqual(i,end,3,0x39)
        writefile.arrayCol(f, 0, range(0x30,0x3A), range(sLL,eLL+1), i[0]*256*256+i[1]*256+i[2],i[2], 256)

      writefile.arrayEnd(f)

  writefile.tail(f);
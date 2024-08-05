import struct

def cut(obj, sec):
  return [obj[i:i+sec] for i in range(0, len(obj),sec)]

def stringHEX(num):
  ret = ""
  if( type(num)==list):
    for i in num:
      ret= ret+'{:02X}'.format(i)
  elif(type(num)==range):
    ret= '{:02X}'.format(num[0]) + " - " + '{:02X}'.format(num[len(num)-1])
  else:
    ret = ret+'{:02X}'.format(num)
  return ret

def string(fp, str1):
  a = str1.encode()
  fp.write(a)

def hexnumber(fp, num):
  a = hex(num)[2:].upper().encode()
  fp.write(a)

def singlebyte(fp, fb1):
  a = struct.pack("B",fb1)
  fp.write(a)

def doublebytes(fp, fb1, fb2):
  a = struct.pack("B",fb1)
  fp.write(a)
  a = struct.pack("B",fb2)
  fp.write(a)

def fourbytes(fp, fb1, fb2, fb3, fb4):
  a = struct.pack("B",fb1)
  fp.write(a)
  a = struct.pack("B",fb2)
  fp.write(a)
  a = struct.pack("B",fb3)
  fp.write(a)
  a = struct.pack("B",fb4)
  fp.write(a)

def title(fp, sTitle, sInfo, sDetail):
  string(fp, "<table style='border-radius:10px 10px 0px 0px;background-color:blue;color:white' ><tr><td class=title>&nbsp;&nbsp;")
  string(fp, sTitle)
  string(fp, "&nbsp;&nbsp;</td><td class=info>")
  string(fp, sInfo)
  string(fp, "</td></tr><tr><td colspan=2 class=detail>")
  string(fp, sDetail)
  string(fp, "</td></tr></table>")

def subtitle(fp, sT, sI):
  string(fp, "<table><tr><td><h1 class=title id='"+sT+"'>")
  string(fp, sT)
  string(fp, "&nbsp;&nbsp;</h1></td><td class=info>")
  string(fp, sI)
  string(fp, "</td></tr></table>")

def item(fp, s):
  string(fp, "<p class=info>")
  string(fp, s)
  string(fp, "</p>\n")

def head(fp, codepage, font):
  string(fp, "<html>\n")
  string(fp, "  <meta http-equiv=\"Content-Type\" content=\"text/html; charset="+codepage+"\" />\n")
  string(fp, "  <style>\n")
  string(fp, "    .arrayHeading{background-color:blue;color:white;text-align:center;}\n")
  string(fp, "    .arrayCharacter{background-color:white;color:black;text-align:center;font-family:'"+font+"'}\n")
  string(fp, "    .arrayOutofbound{background-color:lightblue;color:black;}\n")
  string(fp, "    .arrayReserved{background-color:lightblue;color:black;}\n")
  string(fp, "    .arrayUnused{background-color:lightblue;color:black;}\n")
  string(fp, "    .infoTitle{background-color:blue;color:white;text-align:right;font-size:x-small;}\n")
  string(fp, "    .infoText{background-color:white;color:black;text-align:left;font-size:x-small;}\n")
  string(fp, "    .arrayTitle{background-color:white;color:black;text-align:center;font-size:large;}\n")
  string(fp, "    .title{font-size:large;font-weight:bold}\n")
  string(fp, "    .info{font-size:small;}\n")
  string(fp, "    .detail{background:white;color:black;font-size:xx-small;font-family:monospace}\n")
  string(fp, "  </style>\n")
  string(fp, "  <body>\n")

def tail(fp):
  string(fp, "  </body>\n")
  string(fp, "</html>")

def tableB(fp):
  string(fp, "<table width=100% cellpadding=3 border=1 bordercolor=blue style=\"border-collapse:collapse;\" class=arrayHeading>\n")

def tableE(fp):
  string(fp, "</table>\n")

def trB(fp):
  string(fp, "<tr>")

def trE(fp):
  string(fp, "</tr>\n")

def thB(fp):
  string(fp, "<td align=center class=arrayHeading>")

def thE(fp):
  string(fp, "</td>")

def tdB(fp):
  string(fp, "<td bgcolor=white class=arrayCharacter>")

def tdE(fp):
  string(fp, "</td>")

def tdUnused(fp):
  string(fp, "<td bgcolor=white class=arrayUnused>")

def trhB(fp):
  trB(fp)
  thB(fp)

def tablerhB(fp):
  tableB(fp)
  trhB(fp)

def tdrE(fp):
  tdE(fp)
  trE(fp)

# -- info --

def info(fp, codepagename, title, coderange):
  tableB(fp)
  string(fp, "<tr><th nowrap width=10 align=right class=infoTitle>Codepage</th><td class=infoText>"+codepagename+"</td></tr>")
  string(fp, "<tr><th align=right class=infoTitle>Title</th><td class=infoText>"+title+"</td></tr>")
  string(fp, "<tr><th align=right class=infoTitle>Range</th><td class=infoText>"+coderange+"</td></tr>")
  tableE(fp)

# -- array --

def arrayBegin(fp):
  tableB(fp)

def arrayTitle(fp,t,s):
  string(fp, "<tr><td class=arrayTitle align=center colspan="+str(t)+">" +s+"</td><tr>")

def arrayHead(fp, t, rx, ry, cx, power):
  trhB(fp)
  if t>0:
    hexnumber(fp, t)
  else:
    string(fp,cx)
  thE(fp)
  for i1 in rx:
    thB(fp)
    hexnumber(fp, i1)
    thE(fp)
  trE(fp)

# - Print charactre array -
# fp    : opened file pointer
# t     : 
# rx    : full rows range, character's low byte (or low 4bits in 8bites character)
# arx   : used rows range
# i0    : character's high bytes (or high 4bit in 8bites character), character code = i0+rx
# cx    : col name
# power : rx wide (16 or 256)
def arrayCol(fp, t, rx, arx, i0, cx, power):
  trhB(fp)
  hexnumber(fp, cx)
  thE(fp)
  for i1 in rx:
    if i1 in arx:
      tdB(fp)
      if t>0:
        if power==16:
          if t>256:
            fourbytes(fp, t//65536%256, t//256%256, t%256, i0*power+i1)
          else:
            doublebytes(fp, t, i0*power+i1)
        else:
          fourbytes(fp, t//256, t%256, i0, i1)
      else:
        if power==16:
          if i0<256:
            singlebyte(fp, i0*power+i1)
          elif i0<65536:
            doublebytes(fp, (i0*power+i1)//256, (i0*power+i1)%256)
          else:
            fourbytes(fp, (i0*power+i1)%256//256//256//256, (i0*power+i1)%256//256//256%256, (i0*power+i1)//256%256, (i0*power+i1)%256)
        elif power==256:
          if i0<65536:
            doublebytes(fp, i0, i1)
          else:
            fourbytes(fp, i0//256//256, i0//256%256, i0%256, i1)
        else:
          fourbytes(fp, i0//256, i0%256, i1//256, i1%256)
    else:
      tdUnused(fp)
    tdE(fp)
  trE(fp)

def arrayEnd(fp):
  tableE(fp)

def array(fp, t, rx, ry, ar, power):
  tableB(fp)
  trhB(fp)
  if t>0:
    hexnumber(fp, t)
  thE(fp)
  for i1 in rx:
    thB(fp)
    hexnumber(fp, i1)
    thE(fp)
  trE(fp)
  for i0 in ry:
    trhB(fp)
    hexnumber(fp, i0)
    thE(fp)
    for i1 in rx:
      if(i0*power+i1 in ar):
        tdB(fp)
        if t>0:
          if power==16:
            if t>256:
              fourbytes(fp, t//65536%256, t//256%256, t%256, i0*power+i1)
            else:
              doublebytes(fp, t, i0*power+i1)
          else:
            fourbytes(fp, t//256, t%256, i0, i1)
        else:
          if power==16:
            if i0<256:
              singlebyte(fp, i0*power+i1)
            elif i0<65536:
              doublebytes(fp, (i0*power+i1)//256, (i0*power+i1)%256)
            else:
              fourbytes(fp, (i0*power+i1)%256//256//256//256, (i0*power+i1)%256//256//256%256, (i0*power+i1)//256%256, (i0*power+i1)%256)
          elif power==256:
            if i0<65536:
              doublebytes(fp, i0, i1)
            else:
              fourbytes(fp, i0//256//256, i0//256%256, i0%256, i1)
          else:
            fourbytes(fp, i0//256, i0%256, i1//256, i1%256)
      else:
        tdUnused(fp)
      tdE(fp)
    trE(fp)
  tableE(fp)
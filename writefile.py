import struct

isHTML=True
charGap="\t"

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

def linktagBegin(nm):
  if isHTML:
    return ("<a href='#" + nm + "'>")
  else:
    return ""

def linktagEnd():
  if isHTML:
    return ("</a>")
  else:
    return ""

def lineBreak():
  if isHTML:
    return ("<br/>")
  else:
    return ("\r\n")

def string(fp, str1):
  if str1!= "":
    a = str1.encode()
    fp.write(a)

def stringmulti(fp, str1, t):
  a = str1.encode()
  for i in range(t):
    fp.write(a)

def hexnumber(fp, num, w):
  a = hex(num)[2:].zfill(w).upper().encode()
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

def htmlUnicode(fp, code):
  string(fp,"&#%d;"%code)

def utf8(fp, code):
  if code <= 0x7F:
    a = struct.pack("B",code)
    fp.write(a)
  elif code <= 0x07FF:
    b = (0b110<<5) | (code>>6)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | (code & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)
  elif code <= 0xFFFF:
    b = (0b1110<<4) | (code>>12)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | ((code>>6) & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | (code & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)
  else:
    b = (0b11110<<3) | ((code>>18) & 0b111)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | ((code>>12) & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | ((code>>6) & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)
    b = (0b10<<6) | (code & 0b111111)
    a = struct.pack("B",b)
    fp.write(a)

def title(fp, sTitle, sInfo, sDetail,sDetail2):
  if isHTML:
    string(fp, "<table style='border-radius:10px 10px 0px 0px;background-color:blue;color:white' ><tr><td class=title>&nbsp;&nbsp;")
    string(fp, sTitle)
    string(fp, "&nbsp;&nbsp;</td><td class=info>")
    string(fp, sInfo)
    if sDetail!="":
      string(fp, "</td></tr><tr><td colspan=2 class=detail>")
      string(fp, sDetail)
    if sDetail2!="":
      string(fp, "</td></tr><tr><td colspan=2 class=detail>")
      string(fp, sDetail2)
    string(fp, "</td></tr></table>")
  else:
    string(fp, "[  " + sTitle + "  ]\r\n")
    string(fp, sInfo + "\r\n")
    if sDetail!="":
      string(fp, "--------------------------------\r\n")
      string(fp, sDetail)
    if sDetail2!="":
      string(fp, "--------------------------------\r\n")
      string(fp, sDetail2)
    string(fp, "--------------------------------\r\n")

def subtitle(fp, sT, sI):
  if isHTML:
    string(fp, "<br>\n<table><tr><td class=title id='"+sT+"'>")
    string(fp, sT)
    string(fp, "&nbsp;&nbsp;</td><td class=info>")
    string(fp, sI)
    string(fp, "</td></tr></table>")
  else:
    string(fp, "\r\n[" + sT + charGap)
    string(fp, sI + "]\r\n")

def item(fp, s):
  if isHTML:
    string(fp, "<p class=info>")
    string(fp, s)
    string(fp, "</p>\n")
  else:
    string(fp, s + "\r\n")

def breakline(fp):
  if isHTML:
    string(fp, "<br/>")
  else:
    string(fp, "\r\n")

def head(fp, codepage, font):
  if isHTML:
    string(fp, "<html>\n")
    string(fp, "  <meta http-equiv=\"Content-Type\" content=\"text/html; charset="+codepage+"\" />\n")
    string(fp, "  <style>\n")
    string(fp, "    #control{border: 1px solid #000;  border-bottom-right-radius:14px;  border-top--right-radius:14px;  background:black;  color:white;  padding:2px;  position:fixed;  top:0px;left:0px;  box-shadow:4px 4px 16px #000  }\n")
    string(fp, "    .arrayHeading{background-color:blue;color:white;text-align:center;min-width:32px}\n")
    string(fp, "    .arrayCharacter{background-color:white;color:black;text-align:center;font-family:'"+font+"';font-size:24px;}\n")
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
    string(fp, " <script>\n")
    string(fp, "function changeFont(){\n")
    string(fp, "  for(styleRule of document.styleSheets[0].cssRules){\n")
    string(fp, "    if(styleRule.selectorText==\".arrayCharacter\"){\n")
    string(fp, "      styleRule.style.fontFamily = document.getElementById('fontfamily').value;\n")
    string(fp, "      console.log(styleRule.style.fontFamily);\n")
    string(fp, "    }\n")
    string(fp, "  }\n")
    string(fp, "}\n")
    string(fp, " </script>\n")
    string(fp, "  <body>\n")
    string(fp, "<div id=control style=\"transition:all1s linear;\">\n")
    string(fp, "  <input alt='Fangsong,Kaiti,SimHei' type=text id=\"fontfamily\" value=\""+font+"\"><input type=button value=\"Refresh Font\" onclick=\"changeFont();\">\n")
    string(fp, "  <input type=button style=\"border-top--right-radius:15px;border-bottom-right-radius:15px;\" id=actcontrol onclick=\"if(document.getElementById('control').offsetLeft==0){document.getElementById('control').style.left=-document.getElementById('control').offsetWidth+document.getElementById('actcontrol').offsetWidth+6+'px';document.getElementById('actcontrol').value='>';}else{document.getElementById('control').style.left='0px';document.getElementById('actcontrol').value='<';}\" value='<'>")
    string(fp, "</div>\n<br/><br/>\n")

def tail(fp):
  if isHTML:
    string(fp, "  </body>\n")
    string(fp, "</html>")

def tableB(fp):
  if isHTML:
    string(fp, "<table cellpadding=3 border=1 bordercolor=blue style=\"border-collapse:collapse;\" class=arrayHeading>\n")
#  else:
#    string(fp, "\r\n")

def tableE(fp):
  if isHTML:
    string(fp, "</table>\n")
  else:
    string(fp, "\r\n")

def trB(fp):
  if isHTML:
    string(fp, "<tr>")
  else:
    string(fp, "\r\n")

def trE(fp):
  if isHTML:
    string(fp, "</tr>\n")

def thB(fp):
  if isHTML:
    string(fp, "<td align=center class=arrayHeading>")

def thE(fp):
  if isHTML:
    string(fp, "</td>")
  else:
    string(fp, charGap)

def tdB(fp):
  if isHTML:
    string(fp, "<td bgcolor=white class=arrayCharacter>")

def tdE(fp):
  if isHTML:
    string(fp, "</td>")
  else:
    string(fp, charGap)

def tdUnused(fp):
  if isHTML:
    string(fp, "<td bgcolor=white class=arrayUnused>")
  else:
    string(fp, "  ")

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
  if isHTML:
    tableB(fp)
    string(fp, "<tr><th nowrap width=10 align=right class=infoTitle>Codepage</th><td class=infoText>"+codepagename+"</td></tr>")
    string(fp, "<tr><th align=right class=infoTitle>Title</th><td class=infoText>"+title+"</td></tr>")
    string(fp, "<tr><th align=right class=infoTitle>Range</th><td class=infoText>"+coderange+"</td></tr>")
    tableE(fp)
  else:
    string(fp, " Codepage "+codepagename+"\n")
    string(fp, " Title    "+title+"\n")
    string(fp, " Range    "+coderange+"\n")

# -- array --

def arrayBegin(fp):
  tableB(fp)

def arrayTitle(fp,t,s):
  if isHTML:
    string(fp, "<tr><td class=arrayTitle align=center colspan="+str(t)+">" +s+"</td><tr>")
  else:
    string(fp, s + "\r\n")

def arrayHead(fp, t, rx, ry, cx, power):
  trhB(fp)
  if t>0:
    if power==16:
      hexnumber(fp, t, 1)
    else:
      hexnumber(fp, t, 2)
  else:
    string(fp,cx)
  thE(fp)
  for i1 in rx:
    thB(fp)
    if power==16:
      hexnumber(fp, i1, 1)
    else:
      hexnumber(fp, i1, 2)
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
  if power==16:
    hexnumber(fp, cx, 1)
  else:
    hexnumber(fp, cx, 2)
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

def arrayUnicode(fp, u, ry, x):
  tableB(fp)
  trhB(fp)
  stringmulti(fp, " ",len(str('{:02X}'.format(ry[0]))))
   #string(fp, charGap)
  thE(fp)
  for i1 in range(0,1<<x):
    thB(fp)
    hexnumber(fp, i1, 1)
    #string(fp, charGap)
    #string(fp, " ")
    thE(fp)
  trE(fp)
  for i0 in ry:
    trhB(fp)
    hexnumber(fp, ((u<<12)>>x) + i0,2)
    thE(fp)
    for i1 in range(0,1<<x):
      tdB(fp)
      if isHTML:
        htmlUnicode(fp, (u<<16) + (i0<<x) + i1)
      else:
        utf8(fp, (u<<16) + (i0<<x) + i1)
      tdE(fp)
    trE(fp)
  tableE(fp)

def array(fp, t, rx, ry, ar, power):
  tableB(fp)
  trhB(fp)
  if t>0:
    if power==16:
      hexnumber(fp, t, 1)
    else:
      hexnumber(fp, t, 2)
  else:
    string(fp," ")
  thE(fp)
  for i1 in rx:
    thB(fp)
    if power==16:
      hexnumber(fp, i1, 1)
      if t>0:
        string(fp, " ")
    else:
      hexnumber(fp, i1, 2)
    thE(fp)
  trE(fp)
  for i0 in ry:
    trhB(fp)
    if power==16:
      hexnumber(fp, i0, 1)
    else:
      hexnumber(fp, i0, 2)
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


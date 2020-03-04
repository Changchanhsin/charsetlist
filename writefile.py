import struct

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

def title(fp, s):
  string(fp, "<p><b>")
  string(fp, s)
  string(fp, "</b></p>\n")

def item(fp, s):
  string(fp, "<i>")
  string(fp, s)
  string(fp, "</i><br>\n")

def tableB(fp):
  string(fp, "<table cellpadding=3 border=1 bordercolor=blue style=\"border-collapse:collapse;\" bgcolor=blue>\n")

def tableE(fp):
  string(fp, "</table>\n")

def trB(fp):
  string(fp, "<tr>")

def trE(fp):
  string(fp, "</tr>\n")

def thB(fp):
  string(fp, "<td align=center><font color=white>")

def thE(fp):
  string(fp, "</font></td>")

def tdB(fp):
  string(fp, "<td bgcolor=white align=center>")

def tdE(fp):
  string(fp, "</td>")

def trhB(fp):
  trB(fp)
  thB(fp)

def tablerhB(fp):
  tableB(fp)
  trhB(fp)

def tdrE(fp):
  tdE(fp)
  trE(fp)

def arrayHead(fp, t, rx, ry, power):
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

def arrayMid(fp, t, rx, i0, power):
  trhB(fp)
  hexnumber(fp, i0)
  thE(fp)
  for i1 in rx:
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
    tdE(fp)
  trE(fp)

def arrayEnd(fp):
  tableE(fp)

def array(fp, t, rx, ry, power):
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
      tdE(fp)
    trE(fp)
  tableE(fp)
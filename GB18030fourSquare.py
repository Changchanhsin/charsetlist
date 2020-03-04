import struct

def write_string(fp, str1):
  a = str1.encode()
  fp.write(a)

def write_hexnumber(fp, num):
  a = hex(num)[-2:].encode()
  fp.write(a)

def write_fourbytes(fp, fb1, fb2, fb3, fb4):
  a = struct.pack("B",fb1)
  fp.write(a)
  a = struct.pack("B",fb2)
  fp.write(a)
  a = struct.pack("B",fb3)
  fp.write(a)
  a = struct.pack("B",fb4)
  fp.write(a)


with open('GB18030fourSquare.html', 'wb')as f:
  write_string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb18030\" /><body>\n")
  write_string(f, "<table cellpadding=3 border=1 bordercolor=blue style=\"border-collapse:collapse;\" bgcolor=blue>\n")
  write_string(f, "<td align=center><font color=white></font></td>")
  for i2 in range(0x81,0xFF):
    for i3 in range(0x30,0x3A):
      write_string (f, "<td align=center><font color=white>")
      write_hexnumber(f, i2)
      write_hexnumber(f, i3)
      write_string (f, "</font></td>")
  for i0 in range(0x81,0xFF):
    for i1 in range(0x30,0x3A):
      write_string (f, "</tr>\n<tr><td align=center><font color=white>")
      write_hexnumber(f, i0)
      write_hexnumber(f, i1)
      write_string (f, "</font></td>")
      for i2 in range(0x81,0xFF):
        write_string (f, "\n")
        for i3 in range(0x30,0x3A):
          write_string (f, "<td bgcolor=white align=center>")
          write_fourbytes(f, i0, i1, i2, i3)
          write_string (f, "</td>")
  write_string(f, "</tr>\n</table>\n")
  write_string(f, "</body></html>")

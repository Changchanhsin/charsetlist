import writefile

with open('GB18030fourBelt.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb18030\" /><body>\n")

  writefile.string(f, "GB 18030 four")
  writefile.arrayHead(f, 0, range(0x30,0x3A), 0, 256)
  for i0 in range(0x81,0xFF):
    for i1 in range(0x30,0x3A):
      for i2 in range(0x81,0xFF):
        writefile.arrayMid(f, 0,
                           range(0x30,0x3A),
                           i0*256*256+i1*256+i2, 256)
  writefile.arrayEnd(f)

  writefile.string(f, "</body></html>")

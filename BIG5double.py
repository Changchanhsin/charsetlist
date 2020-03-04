import writefile

with open('BIG5double.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=big5\" />\n<body>\n")

  writefile.title(f, "BIG-5 single")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x02,0x08), 16)

  writefile.title(f, "BIG-5 double")
  writefile.array(f, 0,
                  list(range(0x40,0x7F))+list(range(0xA1,0xFF)),
                  range(0x81,0xFF), 256)

  writefile.string(f, "</body></html>")

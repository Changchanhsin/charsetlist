import writefile

with open('GB18030double.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb18030\" />\n<body>\n")

  writefile.title(f, "GB 18030 single")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x02,0x08), 16)

  writefile.title(f, "GB 18030 double")
  writefile.array(f, 0,
                  list(range(0x40,0x7F))+list(range(0x80,0xFF)),
                  range(0x81,0xFF), 256)

  writefile.string(f, "</body></html>")

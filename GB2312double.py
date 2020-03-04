import writefile

with open('GB2312double.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb2312\" />\n<body>\n")

  writefile.title(f, "GB 2312 single")
  writefile.item(f, " control : 0x00-0x1F, 0x7F")
  writefile.item(f, " ASCII : 0x20-0x7E")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x02,0x08), 16)

  writefile.title(f, "GB 2312 double")
  writefile.item(f, "double 1 : 0xA1-0xA9 : 0xA1-0xFE")
  writefile.item(f, "double 2 : 0xB0-0xF7 : 0xA1-0xFE")
  writefile.item(f, "user 1 : 0xAA-0xAF : 0xA1-0xFE")
  writefile.item(f, "user 2 : 0xF8-0xFE : 0xA1-0xFE")
  writefile.array(f, 0,
                  range(0xA1,0xFF),
                  range(0xA1,0xFF), 256)

  writefile.string(f, "</body></html>")

import writefile

with open('SJISdouble.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=sjis\" />\n<body>\n")

  writefile.title(f, "Shift-JIS single")
  writefile.item(f, " control : 0x00-0x1F, 0x7F")
  writefile.item(f, " ASCII : 0x20-0x7E")
  writefile.item(f, " hirakana : 0xA1-0xDF")
  writefile.array(f, "",
                  range(0x00,0x10),
                  list(range(0x2,0x8))+list(range(0xA,0xE)),
                  16)

  writefile.title(f, "Shift-JIS double")
  writefile.item(f, "JIS X 0208 : 0x81-0x9F, 0xE0-0xEF : 0x40-0x7E, 0x80-0xFC")
  writefile.item(f, "User defined : 0xF0-0xFC : 0x40-0x7E, 0x80-0xFC")
  writefile.array(f, "",
                  list(range(0x40,0x7F))+list(range(0x80,0xFD)),
                  list(range(0x81,0xA0))+list(range(0xE0,0xFD)),
                  256)

  writefile.string(f, "</body></html>")

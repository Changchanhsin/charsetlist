import writefile

with open('BIG5double.html', 'wb')as f:
  writefile.head(f, "big5","MS Gothic");
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=big5\" />\n<body>\n")

  writefile.title(f, "BIG-5 single")
  writefile.array(f, 0, range(0x00,0x10), range(0x02,0x08), range(0x20,0x7F), 16)

  writefile.title(f, "BIG-5 double")
  writefile.array(f, 0,
                  list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1)),
                  range(0x81,0xFE+1),range(0x8140,0xFEFF), 256)

  writefile.tail(f)

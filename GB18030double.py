import writefile

with open('GB18030double.html', 'wb')as f:
  writefile.head(f, "gb18030","SimSun");

  writefile.subtitle(f, "GB 18030 single","")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x02,0x08),range(0x00,0xFF+1), 16)
  writefile.string(f, "<br>")
  writefile.subtitle(f, "GB 18030 double","")
  writefile.array(f, 0,
                  list(range(0x40,0x7F))+list(range(0x80,0xFF)),
                  range(0x81,0xFF), range(0x0000,0xFFFF+1), 256)

  writefile.tail(f);
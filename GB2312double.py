import writefile

with open('GB2312double.html', 'wb')as f:
  writefile.head(f, "gb2312","SimSun");

  writefile.subtitle(f, "GB 2312 single",
                    "control : 0x00-0x1F, 0x7F<br>\
                     ASCII : 0x20-0x7E")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x02,0x08),range(0x00,0xFF+1), 16)
  writefile.string(f,"<br>")
  writefile.subtitle(f, "GB 2312 double",
                    "double 1 : 0xA1-0xA9 : 0xA1-0xFE<br>\
                     double 2 : 0xB0-0xF7 : 0xA1-0xFE<br>\
                     user 1 : 0xAA-0xAF : 0xA1-0xFE<br>\
                     user 2 : 0xF8-0xFE : 0xA1-0xFE")
  writefile.array(f, 0,
                  range(0xA1,0xFF),
                  range(0xA1,0xFF), range(0x0000,0xFFFF+1),256)

  writefile.tail(f);
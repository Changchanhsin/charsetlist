import writefile

with open('SJISdouble.html', 'wb')as f:
  writefile.head(f, "sjis","MS Gothic");

  writefile.subtitle(f, "Shift-JIS","")

  writefile.info(f, "Shift-JIS (JIS X 0201)", "Single", "control : 0x00-0x1F, 0x7F<br>ASCII : 0x20-0x7E<br>hirakana : 0xA1-0xDF")
#  writefile.item(f, " control : 0x00-0x1F, 0x7F")
#  writefile.item(f, " ASCII : 0x20-0x7E")
#  writefile.item(f, " hirakana : 0xA1-0xDF")
  writefile.array(f, 0,
                  range(0x0,0xF+1),
                  list(range(0x2,0x8))+list(range(0xA,0xE)),
                  list(range(0x20,0x7F+1))+list(range(0xA1,0xDE+1)), 16)

  writefile.string(f,"\n<br/>\n")
  writefile.info(f, "Shift-JIS (JIS X 0208)", "Double", "JIS X 0208 : 0x81-0x9F, 0xE0-0xEF : 0x40-0x7E, 0x80-0xFC<br>User defined : 0xF0-0xFC : 0x40-0x7E, 0x80-0xFC")
#  writefile.title(f, "Shift-JIS double")
#  writefile.item(f, "JIS X 0208 : 0x81-0x9F, 0xE0-0xEF : 0x40-0x7E, 0x80-0xFC")
#  writefile.item(f, "User defined : 0xF0-0xFC : 0x40-0x7E, 0x80-0xFC")
  writefile.array(f, 0,
                  list(range(0x40,0x7E+1))+list(range(0x80,0xFC+1)),
                  list(range(0x81,0x9F+1))+list(range(0xE0,0xEF+1))+list(range(0xF0,0xFC+1)),
                  range(0x8140,0xFCFC+1), 256)

  writefile.tail(f);

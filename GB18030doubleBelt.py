import writefile

with open('GB18030doubleBelt.html', 'wb')as f:
  writefile.string(f, "<html>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb18030\" />\n<body>\n")

  writefile.title(f, "GB 18030 single")
  writefile.array(f, 0,
                  range(0x00,0x10),
                  range(0x2,0x8),
                  16)

  writefile.title(f, "GB 18030 double")
  for i0 in range(0x81,0xFF):
    writefile.array(f, i0,
                    range(0x0,0x10),
                    range(0x4,0x10),
                    16)
    writefile.string(f, "<br/>")

  writefile.string(f, "</body></html>")

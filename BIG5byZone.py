import writefile

def checkEqual(s,d,l,v):
  for i in range(0,l):
    if(s[i]!=d[i]):
      return v
  return d[l]

def stringHEX(num):
  ret = ""
  if( type(num)==list):
    for i in num:
      ret= ret+'{:02X}'.format(i)
  else:
    ret = ret+'{:02X}'.format(num)
  return ret

def writeDouble(f, nm, ri0, r):
  writefile.subtitle(f, nm, "Code: " + stringHEX(r[0])+ " - " +stringHEX(r[len(r)-1]))
  for i0 in ri0:
    if(i0==ri0[len(ri0)-1]):
      maxLow = int('{:04X}'.format(r[len(r)-1])[2:4],16)
      maxLowHigh = int('{:04X}'.format(r[len(r)-1])[2:3],16)
      writefile.array(f, i0,
                      range(0x0,0xF+1),list(range(0x4,0x7+1))+list(range(0xA,maxLowHigh+1)),
                      list(range(0x40,0x7E+1))+list(range(0xA1,maxLow+1)), 16)
    else:
      writefile.array(f, i0,
                      range(0x0,0xF+1),list(range(0x4,0x7+1))+list(range(0xA,0xF+1)),
                      list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1)), 16)
    writefile.string(f, "<br/>")


with open('BIG5doubleBelt.html', 'wb')as f:
  writefile.head(f, "big5","MingLiU");

  writefile.title(f, "BIG-5",
                  "Codepage : 950<br>Language : Chinese (Traditional)<br>Range : 0x8140 - 0xFEFE",
                  "High Byte : 0x81 - 0xFE<br>Low Byte  : 0x40 - 0x7E, 0xA1 - 0xFE<br>\
                   0x8140 - 0xA0FE : PUA<br>\
                   0xA140 - 0xA3BF : Symbols<br>\
                   0xA3C0 - 0xA3FE : <i>Reserved</i><br>\
                   0xA440 - 0xC67E : Chinese Level 1, order by stroke<br>\
                   0xC6A1 - 0xC8FE : PUA<br>\
                   0xC940 - 0xF9D5 : Chinese Level 2, order by stroke<br>\
                   0xF9D6 - 0xFEFE : PUA")

  writefile.string(f, "<br>")
  writefile.subtitle(f, "BIG-5 single","")
  writefile.array(f, 0, range(0x00,0x10), range(0x02,0x08), range(0x20,0x7F), 16)

  writefile.string(f, "<br>")
#  writeDouble(f, "BIG-5 Double : PUA 1",      range(0x81,0xA0+1), range(0x8140,0xA0FE+1))
  writeDouble(f, "BIG-5 Double : Symbols",    range(0xA1,0xA3+1), range(0xA140,0xA3BF+1))
  writeDouble(f, "BIG-5 Double : Chinese L1", range(0xA4,0xC6+1), range(0xA440,0xC67E+1))
  writeDouble(f, "BIG-5 Double : Chinese L2", range(0xC9,0xF9+1), range(0xC940,0xF9D5+1))

  writefile.subtitle(f, "BIG-5 Double","")
  writefile.array(f, 0,
                  list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1)),
                  range(0x81,0xFE+1),range(0x8140,0xFEFF), 256)

  writefile.tail(f)

#“高位字节”使用了 0x81-0xFE，“低位字节”使用了 0x40-0x7E 和 0xA1-0xFE。
# 0x8140-0xA0FE：保留给用户自定义字符（造字区）
# 0xA140-0xA3BF：标点符号、希腊字母及特殊符号，包括在 0xA259-0xA261，安放了九个计量用汉字：兙兛兞兝兡兣嗧瓩糎
# 0xA3C0-0xA3FE：保留。此区没有开放作造字区用
# 0xA440-0xC67E：常用汉字，先按笔划再按部首排序
# 0xC6A1-0xC8FE：保留给用户自定义字符（造字区）
# 0xC940-0xF9D5：次常用汉字，亦是先按笔划再按部首排序
# 0xF9D6-0xFEFE：保留给用户自定义字符（造字区）
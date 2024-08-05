import writefile

range2312y  = range(0xA,0xF+1)
range2312   = range(0xA1,0xFE+1)
rangeGBKy   = range(0x4,0xA+1)
rangeGBK    = list(range(0x40,0x7E+1))+list(range(0x80,0xA0+1))
range18030y = range(0x4,0xF+1)
range18030  = list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1))
start=[0x81,0x30,0x81,0x30]
#end  =[0xFE,0x39,0xFE,0x39]
end  =[0x9A,0x34,0xFE,0x39]

zone=[["Single", 0x00, 0xFF, 128, 128]
     ,["Double 1 - Symbols", 0xA1A1, 0xA9FE, 728,  846 , range2312y,  range2312 ]
     ,["Double 5 - Symbols", 0xA840, 0xA9A0, 166,  192 , rangeGBKy,   rangeGBK  ]
     ,["Double 2 - Chinese", 0xB0A1, 0xF7FE, 6763, 6768, range2312y,  range2312 ]
     ,["Double 3 - Chinese", 0x8140, 0xA0FE, 6080, 6080, range18030y, range18030]
     ,["Double 4 - Chinese", 0xAA40, 0xFE80, 8145, 8160, rangeGBKy,   rangeGBK  ]
     ,["Double PUA 1",       0xAAA1, 0xAFFE, 564,  564 , range2312y,  range2312 ]
     ,["Double PUA 2",       0xF8A1, 0xFEFE, 658,  658 , range2312y,  range2312 ]
     ,["Double PUA 3",       0xA140, 0xA780, 672,  672 , rangeGBKy,   rangeGBK  ]
     ,["Quad - Uyghur, Kazakh, Kyrgyz (1)",         0x81318132, 0x81319934, 42,    243  ]
     ,["Quad - Uyghur, Kazakh, Kyrgyz (2)",         0x8430BA32, 0x8430FE35, 59,    684  ]
     ,["Quad - Uyghur, Kazakh, Kyrgyz (3)",         0x84318730, 0x84319530, 84,    141  ]
     ,["Quad - Tibetan",                            0x8132E834, 0x8132FD31, 193,   208  ]
     ,["Quad - Mongolian (Include Manchu, Todo, Sibo, Ali Gali)", 0x8134D238, 0x8134E337, 149, 170]
     ,["Quad - Mongolian BIRGA",                    0x9034C538, 0x9034C730, 13,    13   ]
     ,["Quad - Dehong Dai",                         0x8134F434, 0x8134F830, 35,    37   ]
     ,["Quad - Xishuangbanna New Dai",              0x8134F932, 0x81358437, 83,    96   ]
     ,["Quad - Xishuangbanna Old Dai",              0x81358B32, 0x81359935, 127,   144  ]
     ,["Quad - Yi Syllables and Radicals",          0x82359833, 0x82369435, 1215,  1223 ]
     ,["Quad - Lisu",                               0x82369535, 0x82369A32, 48,    48   ]
     ,["Quad - Hangul Jamo",                        0x81339D36, 0x8133B635, 69,    250  ]
     ,["Quad - Hangul Compatibility Ideographs",    0x8139A933, 0x8139B734, 51,    142  ]
     ,["Quad - Hangul Syllables",                   0x8237CF35, 0x8336BE36, 3431,  11172]
     ,["Quad - Diandong Miao",                      0x9232C636, 0x9232D635, 133,   160  ]
     ,["Quad - Kangxi Radicals",                    0x81398B32, 0x8139A135, 214,   224  ]
     ,["Quad - CJK Unified Ideographs Extension A", 0x8139EE39, 0x82358738, 6530,  6530 ]
     ,["Quad - CJK Unified Ideographs",             0x82358F33, 0x82359636, 66,    74   ]
     ,["Quad - CJK Unified Ideographs Extension B", 0x95328236, 0x9835F336, 42711, 42711]
     ,["Quad - CJK Unified Ideographs Extension C", 0x9835F738, 0x98399E36, 4149,  4149 ]
     ,["Quad - CJK Unified Ideographs Extension D", 0x98399F38, 0x9839B539, 222,   222  ]
     ,["Quad - CJK Unified Ideographs Extension E", 0x9839B632, 0x9933FE33, 5762,  5762 ]
     ,["Quad - CJK Unified Ideographs Extension F", 0x99348138, 0x9939F730, 7473,  7473 ]
      ]

def checkEqual(s,d,l,v):
  for i in range(0,l):
    if(s[i]!=d[i]):
      return v
  return d[l]

def writeDouble(f, nm, ri0, ry, ra):
  writefile.subtitle(f, nm, writefile.stringHEX(ri0))
  for i0 in ri0:
    writefile.array(f, i0, range(0x0,0xF+1), ry, ra, 16) 
    writefile.string(f, "<br/>")

def writeQuad(f, nm, st, ed):
  writefile.subtitle(f, nm, writefile.stringHEX(st) + " - " + writefile.stringHEX(ed))
  s=[0]*4
  s[0] = st>>24 & 0xFF
  s[1] = st>>16 & 0xFF
  s[2] = st>>8  & 0xFF
  s[3] = st     & 0xFF
  e=[0]*4
  e[0] = ed>>24 & 0xFF
  e[1] = ed>>16 & 0xFF
  e[2] = ed>>8  & 0xFF
  e[3] = ed     & 0xFF

  i=[0]*4
  for i[0] in range(s[0],e[0]+1):  # 0x81..0xFE
    sHL=checkEqual(i,s,1,0x30)
    eHL=checkEqual(i,e,1,0x39)
    for i[1] in range(sHL,eHL+1): # 0x30..0x39
      writefile.arrayBegin(f)
      writefile.arrayTitle(f,11, writefile.stringHEX(i[0]) + writefile.stringHEX(i[1]))
      writefile.arrayHead(f, 0, range(0x30,0x3A), 0,  writefile.stringHEX(i[0]) + writefile.stringHEX(i[1]), 256)
      sLH=checkEqual(i,s,2,0x81)
      eLH=checkEqual(i,e,2,0xFE)
      for i[2] in range(sLH, eLH+1): # 0x81..0xFE
        sLL=checkEqual(i,s,3,0x30)
        eLL=checkEqual(i,e,3,0x39)
        writefile.arrayCol(f, 0, range(0x30,0x3A), range(sLL,eLL+1), i[0]*256*256+i[1]*256+i[2],i[2], 256)
      writefile.arrayEnd(f)
    writefile.string(f, "<br/>")

def zonelist():
  ret = ""
  for i in zone:
    ret = ret + "<br/><a href='#" + i[0] + "'>" + writefile.stringHEX(i[1]) + " - " + writefile.stringHEX(i[2]) + " " + i[0] + " (" + str(i[3]) + "/" + str(i[4]) + ")</a>"
  return ret

with open('GB18030ByZone.html', 'wb')as f:
  writefile.head(f, "gb18030","SimSun");

  writefile.title(f, "GB 18030",
                  "Codepage : 936(GB2312/GBK), 54936(GB18030)<br>\
                   Language : Chinese (Simplified), Chinese, Multilingual<br>\
                   Range : 0x20 - 0x7E, 0x8140 - 0xFEFE, 0x81308130 - 0xFE39FE39",
                  "GB 18030-2022"+zonelist() )
  writefile.string(f, "<br/>")

  writefile.subtitle(f, "Single","")
  writefile.array(f, 0, range(0x00,0x10),  range(0x0,0x8), range(0x20,0x7F+1), 16)

  writefile.string(f, "<br/>")
  for i in zone:
    if "Double " in i[0]:
      writeDouble(f, i[0], range((i[1]>>8) & 0xFF, ((i[2]>>8) & 0xFF) + 1), i[5], i[6])

  for i in zone:
    if "Quad " in i[0]:
      writeQuad(f, i[0], i[1], i[2])
  writefile.tail(f);
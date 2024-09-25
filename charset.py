#!/usr/bin/env python

from sys import argv
import argument
import writefile
import sys


argument.setCopyright("2016-2024, Chanhsin")
argument.addDescription("  Create character set array")
argument.addSerial("codepage_name", "Character set: 'gb2312', 'gbk', 'gb18030', 'big5', 'sjis', 'utf-8'")
argument.addSerial("file_name", "Output file name (html), default is charset+'.html' or '.txt' if /t is selected")
argument.addKey("list", "List zone/array id of charaset", 0)
argument.addKey("block", "Show by block", 0)
argument.addKey("zone", "Zone id of block when /b is selected, e.g. 'symbols,chinese', split with ',' no spacing", 1)
argument.addKey("m", "Show as matrix", 0)
argument.addKey("array", "Array id set when /m is selected, e.g. 'single,double', split with ',' no spacing", 1)
argument.addKey("strip", "Show array as strip, for utf-8 only", 0)
argument.addKey("txt", "Output as TXT file", 0)
#argument.addKey("c", "Specify the start code, in HEX without '0x' prefix", 1)
#argument.addKey("e", "Specify the end code, default is start code", 1)
argument.addKey("gap", "Characters gap (in TXT file) with space('s'/'2s'), tabulation('t'), or no space('n'), default is 't'", 1)
argument.addKey("version", "Select version year, 'YYYY' for single, '-YYYY' for before, 'YYYY-' for later, 'YYYY-YYYY' for between", 1)
argument.addKey("debug", "show debug message", 0)
argument.addKey("help", "help", 0)
argument.addExample("  %file% gbk gbk.html /b")

argument.parse(argv)
if argument.key("t", "False" ) == "True":
  writefile.isHTML = False
else:
  writefile.isHTML = True

fileext = ""

verrange = argument.key("v","")
vermin = 0
vermax = 9999

if len(verrange)==5:
  if verrange[0:1]=="-":
    if verrange[1:5].isdigit():
      vermax=int(verrange[1:])
  elif verrange[4:5]=="-":
    if verrange[0:4].isdigit():
      vermin=int(verrange[0:4])
elif len(verrange)==4:
  if verrange.isdigit():
    vermax=int(verrange)
    vermin=int(verrange)
elif len(verrange)==9:
  if verrange[0:4].isdigit():
    vermin=int(verrange[0:4])
  if verrange[5:9].isdigit():
    vermax=int(verrange[5:9])

if (vermax != 9999):
  if (vermin != 0):
    if (vermin == vermax):
      fileext = fileext + "." + str(vermin)
    else:
      fileext = fileext + "." + str(vermin) + "-" + str(vermax)
  else:
    fileext = fileext + ".-" + str(vermax)
else:
  if (vermin != 0):
    if (vermin == vermax):
      fileext = fileext + "." + str(vermin)
    else:
      fileext = fileext + "." + str(vermin) + "-"

charset   = argument.serial(1,"unknown")
listZone  = argument.key("l", "False")
byBlock   = argument.key("b", "False")
oneArray  = argument.key("m", "False")
showZones = argument.key("z", ""     )
showFulls = argument.key("a", "")
showStrip = argument.key("s", "False")

if showZones!="":
  fileext = fileext + "." + showZones

if showFulls!="":
  fileext = fileext + "." + showFulls

if writefile.isHTML == True:
  fn1 = argument.serial(2, charset + fileext + ".html")
else:
  fn1 = argument.serial(2, charset + fileext + ".txt")

specifyStart = argument.key("s", "")
specifyEnd   = argument.key("e", "")

gap = argument.key("g", "t")
if gap=="s":
  writefile.charGap=" "
if gap=="2s":
  writefile.charGap="  "
if gap=="n":
  writefile.charGap=""

if argument.key("d", "False")=="True":
  argument.printall()

charsetindex=["gb2312","gbk","gb18030","big5","sjis","utf-8"]

try:
  currset=charsetindex.index(charset)
except Exception as e:
  argument.printHelp("1")
  sys.exit()


CHARSET_GB2312  = 0
CHARSET_GBK     = 1
CHARSET_GB18030 = 2
CHARSET_BIG5    = 3
CHARSET_SJIS    = 4
CHARSET_UNICODE = 5

INFO_CHARSET  = 0
INFO_FONT     = 1
INFO_NAME     = 2
INFO_CODEPAGE = 3
INFO_LANGUAGE = 4
INFO_RANGE    = 5
INFO_VERSION  = 6
charsetinfo=[["gb2312",  "SimSun",    "GB 2312",  "936",   "Chinese (Simplified)",                        "0x20-0x7E, 0x8181-0xFEFE", "GB/T 2312-1980(1980)"]
            ,["gbk",     "SimSun",    "GBK",      "936",   "Chinese (Simplified), Chinese, Multilingual", "0x20-0x7E, 0x8140-0xFEFE", "GBK (1995)"]
            ,["gb18030", "SimSun",    "GB 18030", "54936", "Chinese (Simplified), Chinese, Multilingual", "0x20-0x7E, 0x8140-0xFEFE, 0x81308130-0xFE39FE39", "GB 18030-2000(2000),GB 18030-2005(2005),GB 18030-2022(2022)"]
            ,["big5",    "MingLiU",   "BIG-5",    "950",   "Chinese (Traditional)",                       "0x81-0xFE : 0x40-0x7E, 0xA1-0xFE", ""]
            ,["sjis",    "MS Mincho", "Shift JIS","932",   "Kanji",                                       "0x81-0x9F, 0xE0-0xEF : 0x40-0x7E, 0x80-0xFC", ""]
            ,["utf-8",   "Tahoma",    "UNICODE",  "0",     "Multilingual",                                "0x000000-0x10FFFF", "1.1/ISO/IEC 10646-1:1993 (1993), 2.0 (1996), 2.1, 3.0/ISO/IEC 10646-1:2000 (1999), 3.1/ISO/IEC 10646-1:2000,ISO/IEC 10646-2:2001 (2001), 3.2 (2002), 4.0/ISO/IEC 10646:2003 (2003), 4.1 (2005), 5.0 (2006), 5.1 (2008), 5.2 (2009), 6.0/ISO/IEC 10646:2011 (2010), 6.1/ISO/IEC 10646:2012 (2012), 7.0 (2014), 8.0/ISO/IEC 10646:2014 (2015), 10.0/ISO/IEC 10646:2017 (2017), 11.0 (2018), 12.0 (2019), 13.0/ISO/IEC 10646:2020 (2020), 14.0 (2021), 15.0 (2022), 15.1 (2023)"]
            ]

rangeControlY  = [0,1,7]
rangeControl   = list(range(0x01,0x1F+1))+list(range(0x7F,0x7F+1))
rangeAsciiY    = range(0x2,0x7+1)
rangeAscii     = range(0x20,0x7E+1)
rangeHiraganaY = range(0xA,0xD+1)
rangeHiraganaL = range(0xA0,0xDF+1)
range8bitY     = range(0x0,0xF+1)
range8bit      = range(0x01,0xFF+1)
range7bitY     = range(0x0,0x7+1)
range7bit      = range(0x01,0x7F+1)
range2312H     = range(0x81,0xFE+1)
range2312Y     = range(0xA,0xF+1)
range2312L     = range(0xA1,0xFE+1)
rangeGbkH      = range(0x81,0xFE+1)
rangeGbkY      = range(0x4,0xA+1)
rangeGbkL      = list(range(0x40,0x7E+1))+list(range(0x80,0xA0+1))
range18030Y    = range(0x4,0xF+1)
range18030L    = list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1))
#start=[0x81,0x30,0x81,0x30]
##end  =[0xFE,0x39,0xFE,0x39]
#end  =[0x9A,0x34,0xFE,0x39]
rangeBIG5Y     = list(range(0x4,0x7+1))+list(range(0xA,0xF+1))
rangeBIG5L     = list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1))
rangeSjisY     = list(range(0x4,0x7+1))+list(range(0x8,0xF+1))
rangeSjisL     = list(range(0x40,0x7E+1))+list(range(0x80,0xFC+1))
rangeUtf8L     = range(0x00,0xFF+1)

FULL_ID         = 0
FULL_BYTE_WIDTH = 1
FULL_NAME       = 2
FULL_HIGH       = 3
FULL_LOW        = 4
             # id        w  name            high                 low
gb2312full =[["single",  1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)]
            ,["double",  2, "Double Bytes", range(0xA1,0xFE+1),  range(0xA1,0xFE+1)] # CHARSET_GB2312  = 0
             ]
gbkfull    =[["single",  1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)]
            ,["double",  2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1)) ] # CHARSET_GBK     = 1
             ]
gb18030full=[["single",  1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)  ]
            ,["double",  2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1)) ] # CHARSET_GB18030 = 2
            ,["quad-bmp",4, "Quad Bytes for BMP",   0x81308130, 0x8431A439]
            ,["quad-smp",4, "Quad Bytes for SMP",   0x8431A530, 0x95328235]
            ,["quad-sip",4, "Quad Bytes for SIP",   0x95328236, 0x9A348431]

             ]
big5full   =[["single",  1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)  ]
            ,["double",  2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1)) ] # CHARSET_BIG5    = 3
             ]
sjisfull   =[["single",  1, "Single Byte",  list(range(0x2,0x7+1))+list(range(0xA,0xD+1)),     range(0x0,0xF+1)]
            ,["double",  2, "Double Bytes", list(range(0x81,0x9F+1))+list(range(0xE0,0xEF+1)), list(range(0x40,0x7E+1))+list(range(0x80,0xFC+1)) ] # CHARSET_SJIS    = 4
             ]
unicodefull=[["single",  1, "Single Bytes",                      range(0x2,0x7+1),     range(0x0,0xF+1)  ]
            ,["bmp",     6, "Basic Multilingual Plane",          range(0x00,0xFF+1),   rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["smp",     6, "Supplementary Multilingual Plane",  range(0x100,0x1FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["sip",     6, "Supplementary Ideographic Plane",   range(0x200,0x2FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["tip",     6, "Tertiary Ideographic Plane",        range(0x300,0x3FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
             ]
fulls=[gb2312full,gbkfull,gb18030full,big5full,sjisfull,unicodefull]

ZONE_ID           = 0
ZONE_BYTE_WIDTH   = 1
ZONE_VERSION      = 2
ZONE_NAME         = 3
ZONE_CODE_START   = 4
ZONE_CODE_END     = 5
ZONE_POINT_CODED  = 6
ZONE_POINT_ALL    = 7
ZONE_CHART_ROWS   = 8
ZONE_CHART_POINTS = 9
            #  0            1 2     3                     4       5       6     7     8            9
            #  id           w ver   name                  start   end     coded all   high 4bit    low
gb2312zone =[["single",     1,1980, "Single",             0x01,   0x7F,   128,  128 , range7bitY,  range7bit  ]
            ,["double1",    2,1980, "Double 1 - Symbols", 0xA1A1, 0xA9FE, 728,  846 , range2312Y,  range2312L ]
            ,["double2",    2,1980, "Double 2 - Chinese", 0xB0A1, 0xF7FE, 6763, 6768, range2312Y,  range2312L ]
            ,["pua1",       2,1980, "Double PUA 1",       0xAAA1, 0xAFFE, 564,  564 , range2312Y,  range2312L ]
            ,["pua2",       2,1980, "Double PUA 2",       0xF8A1, 0xFEFE, 658,  658 , range2312Y,  range2312L ]
             ]
            #  0            1 2     3                     4       5       6     7     8            9
            #  id           w ver   name                  start   end     coded all   high 4bit    low
gbkzone    =[["single",     1,1980, "Single",             0x01,   0x7F,   128,  128 , range7bitY,  range7bit  ]
            ,["double1",    2,1980, "Double 1 - Symbols", 0xA1A1, 0xA9FE, 728,  846 , range2312Y,  range2312L ]
            ,["double5",    2,1995, "Double 5 - Symbols", 0xA840, 0xA9A0, 166,  192 , rangeGbkY,   rangeGbkL  ]
            ,["double2",    2,1980, "Double 2 - Chinese", 0xB0A1, 0xF7FE, 6763, 6768, range2312Y,  range2312L ]
            ,["double3",    2,1995, "Double 3 - Chinese", 0x8140, 0xA0FE, 6080, 6080, range18030Y, range18030L]
            ,["double4",    2,1995, "Double 4 - Chinese", 0xAA40, 0xFE80, 8145, 8160, rangeGbkY,   rangeGbkL  ]
            ,["pua1",       2,1980, "Double PUA 1",       0xAAA1, 0xAFFE, 564,  564 , range2312Y,  range2312L ]
            ,["pua2",       2,1980, "Double PUA 2",       0xF8A1, 0xFEFE, 658,  658 , range2312Y,  range2312L ]
            ,["pua3",       2,1995, "Double PUA 3",       0xA140, 0xA780, 672,  672 , rangeGbkY,   rangeGbkL  ]
             ]
            #  0            1 2     3                     4       5       6     7     8            9
            #  id           w ver   name                  start   end     coded all   high 4bit    low
gb18030zone=[["single",     1,1980, "Single",             0x01,   0x7F,   128,  128 , range7bitY,  range7bit  ]
            ,["double1",    2,1980, "Double 1 - Symbols", 0xA1A1, 0xA9FE, 728,  846 , range2312Y,  range2312L ]
            ,["double5",    2,1995, "Double 5 - Symbols", 0xA840, 0xA9A0, 166,  192 , rangeGbkY,   rangeGbkL  ]
            ,["double2",    2,1980, "Double 2 - Chinese", 0xB0A1, 0xF7FE, 6763, 6768, range2312Y,  range2312L ]
            ,["double3",    2,1995, "Double 3 - Chinese", 0x8140, 0xA0FE, 6080, 6080, range18030Y, range18030L]
            ,["double4",    2,1995, "Double 4 - Chinese", 0xAA40, 0xFE80, 8145, 8160, rangeGbkY,   rangeGbkL  ]
            ,["pua1",       2,1980, "Double PUA 1",       0xAAA1, 0xAFFE, 564,  564 , range2312Y,  range2312L ]
            ,["pua2",       2,1980, "Double PUA 2",       0xF8A1, 0xFEFE, 658,  658 , range2312Y,  range2312L ]
            ,["pua3",       2,1995, "Double PUA 3",       0xA140, 0xA780, 672,  672 , rangeGbkY,   rangeGbkL  ]
            ,["uyghur1",    4,2005, "Quad - Uyghur, Kazakh, Kyrgyz (1)",         0x81318132, 0x81319934, 42,    243  ]
            ,["uyghur2",    4,2005, "Quad - Uyghur, Kazakh, Kyrgyz (2)",         0x8430BA32, 0x8430FE35, 59,    684  ]
            ,["uyghur3",    4,2005, "Quad - Uyghur, Kazakh, Kyrgyz (3)",         0x84318730, 0x84319530, 84,    141  ]
            ,["tibetan",    4,2005, "Quad - Tibetan",                            0x8132E834, 0x8132FD31, 193,   208  ]
            ,["mongolian",  4,2005, "Quad - Mongolian (Including Manchu, Todo, Sibo, Ali Gali)", 0x8134D238, 0x8134E337, 149, 170]
            ,["birga",      4,2020, "Quad - Mongolian BIRGA",                    0x9034C538, 0x9034C730, 13,    13   ]
            ,["dai-dehong", 4,2005, "Quad - Dehong Dai",                         0x8134F434, 0x8134F830, 35,    37   ]
            ,["dai-new",    4,2020, "Quad - Xishuangbanna New Dai",              0x8134F932, 0x81358437, 83,    96   ]
            ,["dai-old",    4,2020, "Quad - Xishuangbanna Old Dai",              0x81358B32, 0x81359935, 127,   144  ]
            ,["yi",         4,2005, "Quad - Yi Syllables and Radicals",          0x82359833, 0x82369435, 1215,  1223 ]
            ,["lisu",       4,2020, "Quad - Lisu",                               0x82369535, 0x82369A32, 48,    48   ]
            ,["hangul-jamo",4,2005, "Quad - Hangul Jamo",                        0x81339D36, 0x8133B635, 69,    250  ]
            ,["hangul",     4,2005, "Quad - Hangul Compatibility Ideographs",    0x8139A933, 0x8139B734, 51,    142  ]
            ,["hangul-syll",4,2005, "Quad - Hangul Syllables",                   0x8237CF35, 0x8336BE36, 3431,  11172]
            ,["miao",       4,2020, "Quad - Diandong Miao",                      0x9232C636, 0x9232D635, 133,   160  ]
            ,["kangxi",     4,2020, "Quad - Kangxi Radicals",                    0x81398B32, 0x8139A135, 214,   224  ]
            ,["cjkexta",    4,2000, "Quad - CJK Unified Ideographs Extension A", 0x8139EE39, 0x82358738, 6530,  6530 ]
            ,["cjk",        4,2005, "Quad - CJK Unified Ideographs",             0x82358F33, 0x82359636, 66,    74   ]
            ,["cjkextb",    4,2005, "Quad - CJK Unified Ideographs Extension B", 0x95328236, 0x9835F336, 42711, 42711]
            ,["cjkextc",    4,2020, "Quad - CJK Unified Ideographs Extension C", 0x9835F738, 0x98399E36, 4149,  4149 ]
            ,["cjkextd",    4,2020, "Quad - CJK Unified Ideographs Extension D", 0x98399F38, 0x9839B539, 222,   222  ]
            ,["cjkexte",    4,2020, "Quad - CJK Unified Ideographs Extension E", 0x9839B632, 0x9933FE33, 5762,  5762 ]
            ,["cjkextf",    4,2020, "Quad - CJK Unified Ideographs Extension F", 0x99348138, 0x9939F730, 7473,  7473 ]
             ]
            #  0            1 2     3                     4       5       6     7     8               9
            #  name         w ver   note                  start   end     used  all   high 4bit       low
sjiszone   =[["control",    1,1980, "Single Control",     0x01,   0x7F,   33,   33,   rangeControlY,  rangeControl  ]
            ,["ascii",      1,1980, "Single ASCII",       0x20,   0x7E,   96,   96,   rangeAsciiY,    rangeAscii    ]
            ,["hiragana",   1,1980, "Single Hiragana",    0xA1,   0xDF,   64,   64,   rangeHiraganaY, rangeHiraganaL]
            ,["symbol",     2,1980, "Symbols",            0x8140, 0x84FC, 64,   64,   rangeSjisY,     rangeSjisL    ]
            ,["kanji1",     2,1980, "Kanji Level 1",      0x889F, 0x9872, 64,   64,   rangeSjisY,     rangeSjisL    ]
            ,["kanji21",    2,1980, "Kanji Level 2(1)",   0x989F, 0x9FFC, 64,   64,   rangeSjisY,     rangeSjisL    ]
            ,["kanji22",    2,1980, "Kanji Level 2(2)",   0xE040, 0xEAA5, 64,   64,   rangeSjisY,     rangeSjisL    ]
            ,["pua",        2,1980, "PUA",                0xF040, 0xFCFC, 64,   64,   rangeSjisY,     rangeSjisL    ]
             ]
            #  0            1 2     3                     4       5       6     7     8            9
            #  name         w ver   note                  start   end     used  all   high 4bit    low
big5zone   =[["single",     1,1992, "Single",             0x01,   0x7F,   128,  128,  range7bitY,  range7bit ]
            ,["symbols",    2,1992, "Symbols",            0xA140, 0xA3BF, 408,  408,  rangeBIG5Y,  rangeBIG5L]
            ,["chinese1",   2,1992, "Chinese Level 1",    0xA440, 0xC67E, 5401, 5401, rangeBIG5Y,  rangeBIG5L]
            ,["chinese2",   2,1992, "Chinese Level 2",    0xC940, 0xF9D5, 9882, 9882, rangeBIG5Y,  rangeBIG5L]
            ,["pua1",       2,1992, "PUA 1",              0x8140, 0xA0FE, 8224, 8224, rangeBIG5Y,  rangeBIG5L]
            ,["pua2",       2,1992, "PUA 2",              0xC6A1, 0xC8FE, 408,  408,  rangeBIG5Y,  rangeBIG5L]
            ,["pua3",       2,1992, "PUA 3",              0xF9D6, 0xFEFE, 1326, 1326, rangeBIG5Y,  rangeBIG5L]
            ,["reserved",   2,1992, "Reserved",           0xA3C0, 0xA3FE, 63,   63,   rangeBIG5Y,  rangeBIG5L]
             ]
            #  0                     1 2     3                                           4         5         6     7     8            9
            #  name                  w ver   note                                        start     end       used  all   high 4bit    used code
unicodezone=[#["controls-0",          6,1993, "C0 Controls",                              0x000001, 0x00001F, 31,  31],
             ["latin",               6,1993, "Basic Latin",                              0x000020, 0x00007F, 95,  95]
            ,["controls-1",          6,1992, "C1 Controls",                              0x000080, 0x00009F, 32,  32]
            ,["latin-1",             6,1993, "Latin-1 Supplement",                       0x0000A0, 0x0000FF, 96,  96]
            ,["latin-ext-a",         6,1993, "Latin Extended-A",                         0x000100, 0x00017F, 128, 128]
            ,["latin-ext-b",         6,1993, "Latin Extended-B",                         0x000180, 0x00024F, 208, 208]
            ,["ipa-ext",             6,1993, "Ipa Extensions",                           0x000250, 0x0002AF, 96,  96]
            ,["spacing",             6,1993, "Spacing Modifier Letters",                 0x0002B0, 0x0002FF, 80,  80]
            ,["diacritical",         6,1993, "Combining Diacritical Marks",              0x000300, 0x00036F, 112, 112]
            ,["greek",               6,1993, "Greek And Coptic",                         0x000370, 0x0003FF, 144, 144]
            ,["cyrillic",            6,1993, "Cyrillic",                                 0x000400, 0x0004FF, 256, 256]
            ,["cyrillic-supp",       6,2002, "Cyrillic Supplement",                      0x000500, 0x00052F, 48,  48]
            ,["armenian",            6,1993, "Armenian",                                 0x000530, 0x00058F, 96,  96]
            ,["hebrew",              6,1993, "Hebrew",                                   0x000590, 0x0005FF, 112, 112]
            ,["arabic",              6,1993, "Arabic",                                   0x000600, 0x0006FF, 256, 256]
            ,["syriac",              6,1999, "Syriac",                                   0x000700, 0x00074F, 80,  80]
            ,["arabic-supp",         6,2005, "Arabic Supplement",                        0x000750, 0x00077F, 48,  48]
            ,["thaana",              6,1999, "Thaana",                                   0x000780, 0x0007BF, 64,  64]
            ,["nko",                 6,2006, "Nko",                                      0x0007C0, 0x0007FF, 64,  64]
            ,["samaritan",           6,2009, "Samaritan",                                0x000800, 0x00083F, 64,  64]
            ,["mandaic",             6,2010, "Mandaic",                                  0x000840, 0x00085F, 32,  32]
            ,["syriac-supp",         6,2017, "Syriac Supplement",                        0x000860, 0x00086F, 16,  16]
            ,["arabic-ext-b",        6,2021, "Arabic Extended-B",                        0x000870, 0x00089F, 48,  48]
            ,["arabic-ext-a",        6,2012, "Arabic Extended-A",                        0x0008A0, 0x0008FF, 96,  96]
            ,["devanagari",          6,1993, "Devanagari",                               0x000900, 0x00097F, 128, 128]
            ,["bengali",             6,1993, "Bengali",                                  0x000980, 0x0009FF, 128, 128]
            ,["gurmukhi",            6,1993, "Gurmukhi",                                 0x000A00, 0x000A7F, 128, 128]
            ,["gujarati",            6,1993, "Gujarati",                                 0x000A80, 0x000AFF, 128, 128]
            ,["oriya",               6,1993, "Oriya",                                    0x000B00, 0x000B7F, 128, 128]
            ,["tamil",               6,1993, "Tamil",                                    0x000B80, 0x000BFF, 128, 128]
            ,["telugu",              6,1993, "Telugu",                                   0x000C00, 0x000C7F, 128, 128]
            ,["kannada",             6,1993, "Kannada",                                  0x000C80, 0x000CFF, 128, 128]
            ,["malayalam",           6,1993, "Malayalam",                                0x000D00, 0x000D7F, 128, 128]
            ,["sinhala",             6,1999, "Sinhala",                                  0x000D80, 0x000DFF, 128, 128]
            ,["thai",                6,1993, "Thai",                                     0x000E00, 0x000E7F, 128, 128]
            ,["lao",                 6,1993, "Lao",                                      0x000E80, 0x000EFF, 128, 128]
            ,["tibetan",             6,1996, "Tibetan",                                  0x000F00, 0x000FFF, 256, 256]
            ,["myanmar",             6,1999, "Myanmar",                                  0x001000, 0x00109F, 160, 160]
            ,["georgian",            6,1993, "Georgian",                                 0x0010A0, 0x0010FF, 96,  96]
            ,["hangul-jamo",         6,1993, "Hangul Jamo",                              0x001100, 0x0011FF, 256, 256]
            ,["ethiopic",            6,1999, "Ethiopic",                                 0x001200, 0x00137F, 384, 384]
            ,["ethiopic-supp",       6,2005, "Ethiopic Supplement",                      0x001380, 0x00139F, 32,  32]
            ,["cherokee",            6,1999, "Cherokee",                                 0x0013A0, 0x0013FF, 96,  96]
            ,["canadian",            6,1999, "Unified Canadian Aboriginal Syllabics",    0x001400, 0x00167F, 640, 640]
            ,["ogham",               6,1999, "Ogham",                                    0x001680, 0x00169F, 32,  32]
            ,["runic",               6,1999, "Runic",                                    0x0016A0, 0x0016FF, 96,  96]
            ,["tagalog",             6,2002, "Tagalog",                                  0x001700, 0x00171F, 32,  32]
            ,["hanunoo",             6,2002, "Hanunoo",                                  0x001720, 0x00173F, 32,  32]
            ,["buhid",               6,2002, "Buhid",                                    0x001740, 0x00175F, 32,  32]
            ,["tagbanwa",            6,2002, "Tagbanwa",                                 0x001760, 0x00177F, 32,  32]
            ,["khmer",               6,1999, "Khmer",                                    0x001780, 0x0017FF, 128, 128]
            ,["mongolian",           6,1999, "Mongolian",                                0x001800, 0x0018AF, 176, 176]
            ,["canadian-ext",        6,2009, "Unified Canadian Aboriginal Syllabics Extended", 0x0018B0, 0x0018FF, 80, 80]
            ,["limbu",               6,2003, "Limbu",                                    0x001900, 0x00194F, 80, 80]
            ,["taile",               6,2003, "Tai Le",                                   0x001950, 0x00197F, 48, 48]
            ,["newtailue",           6,2005, "New Tai Lue (Xishuang Banna Dai)",         0x001980, 0x0019DF, 96, 96]
            ,["khmer-symbols",       6,2003, "Khmer Symbols",                            0x0019E0, 0x0019FF, 32, 32]
            ,["buginese",            6,2005, "Buginese",                                 0x001A00, 0x001A1F, 32, 32]
            ,["taitham",             6,2009, "Tai Tham",                                 0x001A20, 0x001AAF, 144, 144]
            ,["diacritical-ext",     6,2014, "Combining Diacritical Marks Extended",     0x001AB0, 0x001AFF, 80, 80]
            ,["balinese",            6,2006, "Balinese",                                 0x001B00, 0x001B7F, 128, 128]
            ,["sundanese",           6,2008, "Sundanese",                                0x001B80, 0x001BBF, 64, 64]
            ,["batak",               6,2010, "Batak",                                    0x001BC0, 0x001BFF, 64, 64]
            ,["lepcha",              6,2008, "Lepcha",                                   0x001C00, 0x001C4F, 80, 80]
            ,["olchiki",             6,2008, "Ol Chiki",                                 0x001C50, 0x001C7F, 48, 48]
            ,["cyrillic-ext",        6,2016, "Cyrillic Extended",                        0x001C80, 0x001C8F, 16, 16]
            ,["georgian-ext",        6,2018, "Georgian Extended",                        0x001C90, 0x001CBF, 48, 48]
            ,["sundanese-supp",      6,2016, "Sundanese Supplement",                     0x001CC0, 0x001CCF, 16, 16]
            ,["vedic-ext",           6,2009, "Vedic Extensions",                         0x001CD0, 0x001CFF, 48, 48]
            ,["phonetic-ext",        6,2003, "Phonetic Extensions",                      0x001D00, 0x001D7F, 128, 128]
            ,["phonetic-ext-supp",   6,2005, "Phonetic Extensions Supplement",           0x001D80, 0x001DBF, 64, 64]
            ,["diacritical-supp",    6,2005, "Combining Diacritical Marks Supplement",   0x001DC0, 0x001DFF, 64, 64]
            ,["latin-ext-add",       6,1993, "Latin Extended Additional",                0x001E00, 0x001EFF, 256, 256]
            ,["greek-ext",           6,1993, "Greek Extended",                           0x001F00, 0x001FFF, 256, 256]
            ,["punctuation",         6,1993, "General Punctuation",                      0x002000, 0x00206F, 112, 112]
            ,["sup-sub",             6,1993, "Superscripts And Subscripts",              0x002070, 0x00209F, 48, 48]
            ,["currency",            6,1993, "Currency Symbols",                         0x0020A0, 0x0020CF, 48, 48]
            ,["diacritical-symbols", 6,1993, "Combining Diacritical Marks For Symbols",  0x0020D0, 0x0020FF, 48, 48]
            ,["letterlike",          6,1993, "Letterlike Symbols",                       0x002100, 0x00214F, 80, 80]
            ,["number",              6,1993, "Number Forms",                             0x002150, 0x00218F, 64, 64]
            ,["arrows",              6,1993, "Arrows",                                   0x002190, 0x0021FF, 112, 112]
            ,["mathematical",        6,1993, "Mathematical Operators",                   0x002200, 0x0022FF, 256, 256]
            ,["technical",           6,1993, "Miscellaneous Technical",                  0x002300, 0x0023FF, 256, 256]
            ,["control",             6,1993, "Control Pictures",                         0x002400, 0x00243F, 64, 64]
            ,["optical",             6,1993, "Optical Character Recognition",            0x002440, 0x00245F, 32, 32]
            ,["enclosed",            6,1993, "Enclosed Alphanumerics",                   0x002460, 0x0024FF, 160, 160]
            ,["box",                 6,1993, "Box Drawing",                              0x002500, 0x00257F, 128, 128]
            ,["block",               6,1993, "Block Elements",                           0x002580, 0x00259F, 32, 32]
            ,["geometric",           6,1993, "Geometric Shapes",                         0x0025A0, 0x0025FF, 96, 96]
            ,["symbols",             6,1993, "Miscellaneous Symbols",                    0x002600, 0x0026FF, 256, 256]
            ,["dingbats",            6,1993, "Dingbats",                                 0x002700, 0x0027BF, 192, 192]
            ,["mathematical-a",      6,2002, "Miscellaneous Mathematical Symbols-A",     0x0027C0, 0x0027EF, 48, 48]
            ,["arrows-a",            6,2002, "Supplemental Arrows-A",                    0x0027F0, 0x0027FF, 16, 16]
            ,["braille",             6,1999, "Braille Patterns",                         0x002800, 0x0028FF, 256, 256]
            ,["arrows-b",            6,2002, "Supplemental Arrows-B",                    0x002900, 0x00297F, 128, 128]
            ,["mathematical-b",      6,2002, "Miscellaneous Mathematical Symbols-B",     0x002980, 0x0029FF, 128, 128]
            ,["mathematical-o",      6,2002, "Supplemental Mathematical Operators",      0x002A00, 0x002AFF, 256, 256]
            ,["symbols-arrows",      6,2003, "Miscellaneous Symbols And Arrows",         0x002B00, 0x002BFF, 256, 256]
            ,["glagolitic",          6,2005, "Glagolitic",                               0x002C00, 0x002C5F, 96, 96]
            ,["latin-ext-c",         6,2006, "Latin Extended-C",                         0x002C60, 0x002C7F, 32, 32]
            ,["coptic",              6,2005, "Coptic",                                   0x002C80, 0x002CFF, 128, 128]
            ,["georgian-supp",       6,2005, "Georgian Supplement",                      0x002D00, 0x002D2F, 48, 48]
            ,["tifinagh",            6,2005, "Tifinagh",                                 0x002D30, 0x002D7F, 80, 80]
            ,["ethiopic-ext",        6,2005, "Ethiopic Extended",                        0x002D80, 0x002DDF, 96, 96]
            ,["cyrillic-ext-a",      6,2008, "Cyrillic Extended-A",                      0x002DE0, 0x002DFF, 32, 32]
            ,["punctuation-supp",    6,2005, "Supplemental Punctuation",                 0x002E00, 0x002E7F, 128, 128]
            ,["cjk-radicals-supp",   6,1999, "CJK Radicals Supplement",                  0x002E80, 0x002EFF, 128, 128]
            ,["kangxi",              6,1999, "Kangxi Radicals",                          0x002F00, 0x002FDF, 224, 224]
            ,["ideographic",         6,1999, "Ideographic Description Characters",       0x002FF0, 0x002FFF, 16, 16]
            ,["cjk-symbols",         6,1993, "CJK Symbols And Punctuation",              0x003000, 0x00303F, 64, 64]
            ,["hiragana",            6,1993, "Hiragana",                                 0x003040, 0x00309F, 96, 96]
            ,["katakana",            6,1993, "Katakana",                                 0x0030A0, 0x0030FF, 96, 96]
            ,["bopomofo",            6,1993, "Bopomofo",                                 0x003100, 0x00312F, 48, 48]
            ,["hangul-comp-jamo",    6,1993, "Hangul Compatibility Jamo",                0x003130, 0x00318F, 96, 96]
            ,["kanbun",              6,1993, "Kanbun (CJK Miscellaneous)",               0x003190, 0x00319F, 16, 16]
            ,["bopomofo-ext",        6,1999, "Bopomofo Extended",                        0x0031A0, 0x0031BF, 32, 32]
            ,["cjk-strokes",         6,2005, "CJK Strokes",                              0x0031C0, 0x0031EF, 48, 48]
            ,["katakana-ext",        6,2002, "Katakana Phonetic Extensions",             0x0031F0, 0x0031FF, 16, 16]
            ,["enclosed-cjk",        6,1993, "Enclosed CJK Letters And Months",          0x003200, 0x0032FF, 256, 256]
            ,["cjk-comp",            6,1993, "CJK Compatibility",                        0x003300, 0x0033FF, 256, 256]
            ,["cjk-ext-a",           6,1999, "CJK Unified Ideographs Extension A",       0x003400, 0x004DBF, 6592, 6592]
            ,["yijing",              6,2003, "Yijing Hexagram Symbols",                  0x004DC0, 0x004DFF, 64, 64]
            ,["cjk",                 6,1993, "CJK Unified Ideographs",                   0x004E00, 0x009FFF, 20992, 20992]
            ,["yi",                  6,1999, "Yi Syllables",                             0x00A000, 0x00A48F, 1168, 1168]
            ,["yi-radicals",         6,1999, "Yi Radicals",                              0x00A490, 0x00A4CF, 64, 64]
            ,["lisu",                6,2009, "Lisu",                                     0x00A4D0, 0x00A4FF, 48, 48]
            ,["vai",                 6,2008, "Vai",                                      0x00A500, 0x00A63F, 320, 320]
            ,["cyrillic-ext-b",      6,2008, "Cyrillic Extended-B",                      0x00A640, 0x00A69F, 96, 96]
            ,["bamum",               6,2009, "Bamum",                                    0x00A6A0, 0x00A6FF, 96, 96]
            ,["tone",                6,2005, "Modifier Tone Letters",                    0x00A700, 0x00A71F, 32, 32]
            ,["latin-ext-d",         6,2006, "Latin Extended-D",                         0x00A720, 0x00A7FF, 224, 224]
            ,["sylotinagri",         6,2005, "Syloti Nagri",                             0x00A800, 0x00A82F, 48, 48]
            ,["indicnumber",         6,2009, "Common Indic Number Forms",                0x00A830, 0x00A83F, 16, 16]
            ,["phags-pa",            6,2006, "Phags-Pa",                                 0x00A840, 0x00A87F, 64, 64]
            ,["saurashtra",          6,2008, "Saurashtra",                               0x00A880, 0x00A8DF, 96, 96]
            ,["devanagari-ext",      6,2009, "Devanagari Extended",                      0x00A8E0, 0x00A8FF, 32, 32]
            ,["kayahli",             6,2008, "Kayah Li",                                 0x00A900, 0x00A92F, 48, 48]
            ,["rejang",              6,2008, "Rejang",                                   0x00A930, 0x00A95F, 48, 48]
            ,["hangul-jamo-ext-a",   6,2009, "Hangul Jamo Extended-A",                   0x00A960, 0x00A97F, 32, 32]
            ,["javanese",            6,2009, "Javanese",                                 0x00A980, 0x00A9DF, 96, 96]
            ,["myanmar-ext-b",       6,2014, "Myanmar Extended-B",                       0x00A9E0, 0x00A9FF, 32, 32]
            ,["cham",                6,2008, "Cham",                                     0x00AA00, 0x00AA5F, 96, 96]
            ,["myanmar-ext-a",       6,2009, "Myanmar Extended-A",                       0x00AA60, 0x00AA7F, 32, 32]
            ,["taiviet",             6,2009, "Tai Viet",                                 0x00AA80, 0x00AADF, 96, 96]
            ,["meeteimayek-ext",     6,2012, "Meetei Mayek Extensions",                  0x00AAE0, 0x00AAFF, 32, 32]
            ,["ethiopic-ext-a",      6,2010, "Ethiopic Extended-A",                      0x00AB00, 0x00AB2F, 48, 48]
            ,["latin-ext-e",         6,2014, "Latin Extended-E",                         0x00AB30, 0x00AB6F, 64, 64]
            ,["cherokee-s",          6,2015, "Cherokee Supplement",                      0x00AB70, 0x00ABBF, 80, 80]
            ,["meeteimayek",         6,2009, "Meetei Mayek",                             0x00ABC0, 0x00ABFF, 64, 64]
            ,["hangul-syllables",    6,1996, "Hangul Syllables",                         0x00AC00, 0x00D7A3, 11172, 11172]
            ,["hangul-jamo-ext-b",   6,2009, "Hangul Jamo Extended-B",                   0x00D7B0, 0x00D7FF, 80, 80]
            ,["high-surrogates",     6,1991, "High Surrogates",                          0x00D800, 0x00DB7F, 0, 23424]
            ,["pua-surrogates",      6,1991, "High Private Use Surrogates",              0x00DB80, 0x00DBFF, 0, 128]
            ,["low-surrogates",      6,1991, "Low Surrogates",                           0x00DC00, 0x00DFFF, 0, 1024]
            ,["pua",                 6,1991, "Private Use Area",                         0x00E000, 0x00F8FF, 0, 6400]
            ,["cjk-comp-ideo",       6,1993, "CJK Compatibility Ideographs",             0x00F900, 0x00FAFF, 472, 512]
            ,["alphabetic",          6,1993, "Alphabetic Presentation Forms",            0x00FB00, 0x00FB4F, 58, 80]
            ,["arbic-pfa",           6,1993, "Arabic Presentation Forms-A",              0x00FB50, 0x00FDFF, 663, 688]
            ,["selectors",           6,2002, "Variation Selectors",                      0x00FE00, 0x00FE0F, 16, 16]
            ,["vertical",            6,2005, "Vertical Forms",                           0x00FE10, 0x00FE1F, 10, 16]
            ,["half",                6,1993, "Combining Half Marks",                     0x00FE20, 0x00FE2F, 16, 16]
            ,["cjk-comp-form",       6,1993, "CJK Compatibility Forms",                  0x00FE30, 0x00FE4F, 32, 32]
            ,["smallform",           6,1993, "Small Form Variants",                      0x00FE50, 0x00FE6F, 32, 32]
            ,["arabic-pfb",          6,1993, "Arabic Presentation Forms-B",              0x00FE70, 0x00FEFE, 141, 143]
            ,["half-full",           6,1993, "Halfwidth And Fullwidth Forms",            0x00FF00, 0x00FFEF, 225, 240]
            ,["specials",            6,1993, "Specials",                                 0x00FFF0, 0x00FFFD, 7, 14]
            ,["linear-b-syllabary",  6,2003, "Linear B Syllabary",                       0x010000, 0x01007F, 88, 128]
            ,["linear-b-ideograms",  6,2003, "Linear B Ideograms",                       0x010080, 0x0100FF, 123, 128]
            ,["aegean",              6,2003, "Aegean Numbers",                           0x010100, 0x01013F, 57, 64]
            ,["greek-numbers",       6,2005, "Ancient Greek Numbers",                    0x010140, 0x01018F, 79, 80]
            ,["ancient-symbols",     6,2008, "Ancient Symbols",                          0x010190, 0x0101CF, 14, 64]
            ,["phaistos",            6,2008, "Phaistos Disc",                            0x0101D0, 0x0101FF, 46, 48]
            ,["lycian",              6,2008, "Lycian",                                   0x010280, 0x01029F, 29, 32]
            ,["carian",              6,2008, "Carian",                                   0x0102A0, 0x0102DF, 49, 64]
            ,["coptic-epact",        6,2014, "Coptic Epact Numbers",                     0x0102E0, 0x0102FF, 28, 32]
            ,["old-italic",          6,2001, "Old Italic",                               0x010300, 0x01032F, 39, 48]
            ,["gothic",              6,2001, "Gothic",                                   0x010330, 0x01034F, 27, 32]
            ,["old-permic",          6,2014, "Old Permic",                               0x010350, 0x01037F, 43, 48]
            ,["ugaritic",            6,2003, "Ugaritic",                                 0x010380, 0x01039F, 31, 32]
            ,["old-persian",         6,2005, "Old Persian",                              0x0103A0, 0x0103DF, 50, 64]
            ,["deseret",             6,2001, "Deseret",                                  0x010400, 0x01044F, 80, 80]
            ,["shavian",             6,2003, "Shavian",                                  0x010450, 0x01047F, 48, 48]
            ,["osmanya",             6,2003, "Osmanya",                                  0x010480, 0x0104AF, 40, 48]
            ,["osage",               6,2016, "Osage",                                    0x0104B0, 0x0104FF, 72, 80]
            ,["elbasan",             6,2014, "Elbasan",                                  0x010500, 0x01052F, 40, 48]
            ,["vithkuqi",            6,2021, "Vithkuqi",                                 0x010570, 0x0105BF, 70, 80]
            ,["linear-a",            6,2014, "Linear A",                                 0x010600, 0x01077F, 341, 384]
            ,["latin-ext-f",         6,2021, "Latin Extended-F",                         0x010780, 0x0107BF, 57, 64]
            ,["cypriot",             6,2003, "Cypriot Syllabary",                        0x010800, 0x01083F, 55, 64]
            ,["aramaic",             6,2009, "Imperial Aramaic",                         0x010840, 0x01085F, 31, 32]
            ,["palmyrene",           6,2014, "Palmyrene",                                0x010860, 0x01087F, 32, 32]
            ,["nabataean",           6,2014, "Nabataean",                                0x010880, 0x0108AF, 40, 48]
            ,["hatran",              6,2015, "Hatran",                                   0x0108E0, 0x0108FF, 26, 32]
            ,["phoenician",          6,2006, "Phoenician",                               0x010900, 0x01091F, 29, 32]
            ,["lydian",              6,2008, "Lydian",                                   0x010920, 0x01093F, 27, 32]
            ,["meroitic-h",          6,2012, "Meroitic Hieroglyphs",                     0x010980, 0x01099F, 32, 32]
            ,["meroitic-c",          6,2012, "Meroitic Cursive",                         0x0109A0, 0x0109FF, 90, 96]
            ,["kharoshthi",          6,2005, "Kharoshthi",                               0x010A00, 0x010A5F, 68, 96]
            ,["old-s-arabian",       6,2009, "Old South Arabian",                        0x010A60, 0x010A7F, 32, 32]
            ,["old-n-arabian",       6,2014, "Old North Arabian",                        0x010A80, 0x010A9F, 32, 32]
            ,["manichaean",          6,2014, "Manichaean",                               0x010AC0, 0x010AFF, 51, 64]
            ,["avestan",             6,2009, "Avestan",                                  0x010B00, 0x010B3F, 61, 64]
            ,["parthian",            6,2009, "Inscriptional Parthian",                   0x010B40, 0x010B5F, 30, 32]
            ,["pahlavi",             6,2009, "Inscriptional Pahlavi",                    0x010B60, 0x010B7F, 27, 32]
            ,["psalter",             6,2014, "Psalter Pahlavi",                          0x010B80, 0x010BAF, 29, 48]
            ,["old-turkic",          6,2009, "Old Turkic",                               0x010C00, 0x010C4F, 73, 80]
            ,["old-hungarian",       6,2015, "Old Hungarian",                            0x010C80, 0x010CFF, 108, 128]
            ,["hanifi-rohingya",     6,2018, "Hanifi Rohingya",                          0x010D00, 0x010D3F, 50, 64]
            ,["rumi",                6,2009, "Rumi Numeral Symbols",                     0x010E60, 0x010E7F, 31, 32]
            ,["yezidi",              6,2020, "Yezidi",                                   0x010E80, 0x010EBF, 47, 64]
            ,["arabic-ext-c",        6,2022, "Arabic Extended-C",                        0x010EC0, 0x010EFF, 3, 64]
            ,["old-sogdian",         6,2018, "Old Sogdian",                              0x010F00, 0x010F2F, 40, 48]
            ,["sogdian",             6,2018, "Sogdian",                                  0x010F30, 0x010F6F, 42, 64]
            ,["old-uyghur",          6,2021, "Old Uyghur",                               0x010F70, 0x010FAF, 26, 64]
            ,["chorasmian",          6,2020, "Chorasmian",                               0x010FB0, 0x010FDF, 28, 48]
            ,["elymaic",             6,2019, "Elymaic",                                  0x010FE0, 0x010FFF, 23, 32]
            ,["brahmi",              6,2010, "Brahmi",                                   0x011000, 0x01107F, 115, 128]
            ,["kaithi",              6,2009, "Kaithi",                                   0x011080, 0x0110CF, 68, 80]
            ,["sora-sompeng",        6,2012, "Sora Sompeng",                             0x0110D0, 0x0110FF, 35, 48]
            ,["chakma",              6,2012, "Chakma",                                   0x011100, 0x01114F, 71, 80]
            ,["mahajani",            6,2014, "Mahajani",                                 0x011150, 0x01117F, 39, 48]
            ,["sharada",             6,2012, "Sharada",                                  0x011180, 0x0111DF, 96, 96]
            ,["sinhala-archaic",     6,2014, "Sinhala Archaic Numbers",                  0x0111E0, 0x0111FF, 20, 32]
            ,["khojki",              6,2014, "Khojki",                                   0x011200, 0x01124F, 65, 80]
            ,["multani",             6,2015, "Multani",                                  0x011280, 0x0112AF, 38, 48]
            ,["khudawadi",           6,2014, "Khudawadi",                                0x0112B0, 0x0112FF, 69, 80]
            ,["grantha",             6,2014, "Grantha",                                  0x011300, 0x01137F, 86, 128]
            ,["newa",                6,2016, "Newa",                                     0x011400, 0x01147F, 97, 128]
            ,["tirhuta",             6,2014, "Tirhuta",                                  0x011480, 0x0114DF, 92, 96]
            ,["siddham",             6,2014, "Siddham",                                  0x011580, 0x0115FF, 92, 128]
            ,["modi",                6,2014, "Modi",                                     0x011600, 0x01165F, 79, 96]
            ,["mongolian-supp",      6,2016, "Mongolian Supplement",                     0x011660, 0x01167F, 13, 32]
            ,["takai",               6,2012, "Takri",                                    0x011680, 0x0116CF, 68, 80]
            ,["ahom",                6,2015, "Ahom",                                     0x011700, 0x01174F, 65, 80]
            ,["dogra",               6,2018, "Dogra",                                    0x011800, 0x01184F, 60, 80]
            ,["warang",              6,2014, "Warang Citi",                              0x0118A0, 0x0118FF, 84, 96]
            ,["dives",               6,2020, "Dives Akuru",                              0x011900, 0x01195F, 72, 96]
            ,["nandinagari",         6,2019, "Nandinagari",                              0x0119A0, 0x0119FF, 65, 96]
            ,["zanabazar",           6,2017, "Zanabazar Square",                         0x011A00, 0x011A4F, 72, 80]
            ,["soyombo",             6,2017, "Soyombo",                                  0x011A50, 0x011AAF, 83, 96]
            ,["canadian-ext-a",      6,2021, "Unified Canadian Aboriginal Syllabics Extended-A", 0x011AB0, 0x011ABF, 16, 16]
            ,["paucinhau",           6,2014, "Pau Cin Hau",                              0x011AC0, 0x011AFF, 57, 64]
            ,["devanagari-ext-a",    6,2022, "Devanagari Extended-A",                    0x011B00, 0x011B5F, 10, 96]
            ,["bhaiksuki",           6,2016, "Bhaiksuki",                                0x011C00, 0x011C6F, 97, 112]
            ,["marchen",             6,2016, "Marchen",                                  0x011C70, 0x011CBF, 68, 80]
            ,["masaram",             6,2017, "Masaram Gondi",                            0x011D00, 0x011D5F, 75, 96]
            ,["gunjala",             6,2018, "Gunjala Gondi",                            0x011D60, 0x011DAF, 63, 80]
            ,["makasar",             6,2018, "Makasar",                                  0x011EE0, 0x011EFF, 25, 32]
            ,["kawi",                6,2022, "Kawi",                                     0x011F00, 0x011F5F, 82, 96]
            ,["lisu-supp",           6,2010, "Lisu Supplement",                          0x011FB0, 0x011FBF, 1, 16]
            ,["tamil-supp",          6,2019, "Tamil Supplement",                         0x011FC0, 0x011FFF, 51, 64]
            ,["cuneiform",           6,2006, "Cuneiform",                                0x012000, 0x0123FF, 992, 1024]
            ,["cuneiform-num-punc",  6,2006, "Cuneiform Numbers And Punctuation",        0x012400, 0x01247F, 116, 128]
            ,["early",               6,2015, "Early Dynastic Cuneiform",                 0x012480, 0x01254F, 196, 208]
            ,["cypro-minoan",        6,2021, "Cypro-Minoan",                             0x012F90, 0x012FFF, 99, 112]
            ,["egyptian",            6,2009, "Egyptian Hieroglyphs",                     0x013000, 0x01342F, 1072, 1072]
            ,["egyptian-format",     6,2019, "Egyptian Hieroglyphs Format Controls",     0x013430, 0x01345F, 38, 48]
            ,["anatolian",           6,2015, "Anatolian Hieroglyphs",                    0x014400, 0x01467F, 538, 640]
            ,["bamum-supp",          6,2010, "Bamum Supplement",                         0x016800, 0x016A3F, 569, 576]
            ,["mro",                 6,2014, "Mro",                                      0x016A40, 0x016A6F, 43, 48]
            ,["tangsa",              6,2021, "Tangsa",                                   0x016A70, 0x016ACF, 89, 96]
            ,["bassavah",            6,2014, "Bassa Vah",                                0x016AD0, 0x016AFF, 36, 48]
            ,["pahawh",              6,2014, "Pahawh Hmong",                             0x016B00, 0x016B8F, 127, 144]
            ,["medefaidrin",         6,2018, "Medefaidrin",                              0x016E40, 0x016E9F, 91, 96]
            ,["miao",                6,2012, "Miao",                                     0x016F00, 0x016F9F, 149, 160]
            ,["ideo-symbols-punc",   6,2016, "Ideographic Symbols And Punctuation",      0x016FE0, 0x016FFF, 7, 32]
            ,["tangut",              6,2016, "Tangut",                                   0x017000, 0x0187FF, 6136, 6144]
            ,["tangut-comp",         6,2016, "Tangut Components",                        0x018800, 0x018AFF, 768, 768]
            ,["khitan-small",        6,2020, "Khitan Small Script",                      0x018B00, 0x018CFF, 470, 512]
            ,["tangut-supp",         6,2020, "Tangut Supplement",                        0x018D00, 0x018D7F, 9, 128]
            ,["kana-ext-b",          6,2021, "Kana Extended-B",                          0x01AFF0, 0x01AFFF, 13, 16]
            ,["kana-supp",           6,2020, "Kana Supplement",                          0x01B000, 0x01B0FF, 256, 256]
            ,["kana-ext-a",          6,2017, "Kana Extended-A",                          0x01B100, 0x01B12F, 35, 48]
            ,["small-kana-ext",      6,2019, "Small Kana Extension",                     0x01B130, 0x01B16F, 9, 64]
            ,["nushu",               6,2017, "Nushu",                                    0x01B170, 0x01B2FF, 396, 400]
            ,["duployan",            6,2014, "Duployan",                                 0x01BC00, 0x01BC9F, 143, 160]
            ,["shorthand",           6,2014, "Shorthand Format Control",                 0x01BCA0, 0x01BCAF, 4, 16]
            ,["znamenny",            6,2021, "Znamenny Musical Symbols",                 0x01CF00, 0x01CFCF, 185, 208]
            ,["byzantine",           6,2001, "Byzantine Musical Symbols",                0x01D000, 0x01D0FF, 246, 256]
            ,["musical",             6,2001, "Musical Symbols",                          0x01D100, 0x01D1FF, 233, 256]
            ,["ancient-greek",       6,2005, "Ancient Greek Musical Notation",           0x01D200, 0x01D24F, 70, 80]
            ,["kaktovik-num",        6,2022, "Kaktovik Numerals",                        0x01D2C0, 0x01D2DF, 20, 32]
            ,["mayan-num",           6,2018, "Mayan Numerals",                           0x01D2E0, 0x01D2FF, 20, 32]
            ,["taixuanjing",         6,2003, "Tai Xuan Jing Symbols",                    0x01D300, 0x01D35F, 87, 96]
            ,["conunting-rod",       6,2006, "Counting Rod Numerals",                    0x01D360, 0x01D37F, 25, 32]
            ,["math-alpha-symbols",  6,2001, "Mathematical Alphanumeric Symbols",        0x01D400, 0x01D7FF, 996, 1024]
            ,["sutton",              6,2015, "Sutton Signwriting",                       0x01D800, 0x01DAAF, 672, 688]
            ,["latin-ext-g",         6,2021, "Latin Extended-G",                         0x01DF00, 0x01DFFF, 37, 256]
            ,["glagolitic-supp",     6,2016, "Glagolitic Supplement",                    0x01E000, 0x01E02F, 38, 48]
            ,["cyrillic-ext-d",      6,2022, "Cyrillic Extended-D",                      0x01E030, 0x01E08F, 63, 96]
            ,["nyiakeng",            6,2019, "Nyiakeng Puachue Hmong",                   0x01E100, 0x01E14F, 71, 80]
            ,["toto",                6,2021, "Toto",                                     0x01E290, 0x01E2BF, 31, 48]
            ,["wangcho",             6,2019, "Wancho",                                   0x01E2C0, 0x01E2FF, 59, 64]
            ,["nag-mundari",         6,2022, "Nag Mundari",                              0x01E4D0, 0x01E4FF, 42, 48]
            ,["ethiopic-ext-b",      6,2022, "Ethiopic Extended-B",                      0x01E7E0, 0x01E7FF, 28, 32]
            ,["mende",               6,2014, "Mende Kikakui",                            0x01E800, 0x01E8DF, 213,   224]
            ,["adlam",               6,2016, "Adlam",                                    0x01E900, 0x01E95F, 88,    96   ]
            ,["indic-siyaq-num",     6,2018, "Indic Siyaq Numbers",                      0x01EC70, 0x01ECBF, 66,    80   ]
            ,["ottoman-siyaq-num",   6,2019, "Ottoman Siyaq Numbers",                    0x01ED00, 0x01ED4F, 61,    80   ]
            ,["arabic-math",         6,2012, "Arabic Mathematical Alphabetical Symbols", 0x01EE00, 0x01EEFF, 143,   256  ]
            ,["mahjong",             6,2008, "Mahjong Tiles",                            0x01F000, 0x01F02F, 44,    48   ]
            ,["domino",              6,2008, "Domino Tiles",                             0x01F030, 0x01F09F, 100,   112  ]
            ,["cards",               6,2010, "Playing Cards",                            0x01F0A0, 0x01F0FF, 82,    96   ]
            ,["enclosed-alpha-supp", 6,2009, "Enclosed Alphanumeric Supplement",         0x01F100, 0x01F1FF, 200,   256  ]
            ,["enclosed-ideo-supp",  6,2009, "Enclosed Ideographic Supplement",          0x01F200, 0x01F2FF, 64,    256  ]
            ,["symbols-pict",        6,2010, "Miscellaneous Symbols And Pictographs",    0x01F300, 0x01F5FF, 768,   768  ]
            ,["emoticons",           6,2010, "Emoticons",                                0x01F600, 0x01F64F, 80,    80   ]
            ,["ornamental",          6,2014, "Ornamental Dingbats",                      0x01F650, 0x01F67F, 48,    48   ]
            ,["transport",           6,2010, "Transport And Map Symbols",                0x01F680, 0x01F6FF, 118,   128  ]
            ,["alchemical",          6,2010, "Alchemical Symbols",                       0x01F700, 0x01F77F, 124,   128  ]
            ,["geometric-ext",       6,2014, "Geometric Shapes Extended",                0x01F780, 0x01F7FF, 103,   128  ]
            ,["arrows-c-supp",       6,2014, "Supplemental Arrows-C",                    0x01F800, 0x01F8FF, 150,   256  ]
            ,["symbols-pict-supp",   6,2015, "Supplemental Symbols And Pictographs",     0x01F900, 0x01F9FF, 256,   256  ]
            ,["chess",               6,2018, "Chess Symbols",                            0x01FA00, 0x01FA6F, 98,    112  ]
            ,["symbols-pict-ext-a",  6,2019, "Symbols And Pictographs Extended-A",       0x01FA70, 0x01FAFF, 107,   144  ]
            ,["legacycomputing",     6,2020, "Symbols For Legacy Computing",             0x01FB00, 0x01FBFF, 212,   256  ]
            ,["cjk-ext-b",           6,2001, "CJK Unified Ideographs Extension B",       0x020000, 0x02A6DF, 42720, 42720]
            ,["cjk-ext-c",           6,2009, "CJK Unified Ideographs Extension C",       0x02A700, 0x02B73F, 4154,  4160 ]
            ,["cjk-ext-d",           6,2010, "CJK Unified Ideographs Extension D",       0x02B740, 0x02B81F, 222,   224  ]
            ,["cjk-ext-e",           6,2015, "CJK Unified Ideographs Extension E",       0x02B820, 0x02CEAF, 5762,  5776 ]
            ,["cjk-ext-f",           6,2017, "CJK Unified Ideographs Extension F",       0x02CEB0, 0x02EBEF, 7473,  7488 ]
            ,["cjk-ext-i",           6,2023, "CJK Unified Ideographs Extension I",       0x02EBF0, 0x02EE5F, 622,   624  ]
            ,["cjk-comp-ideo-supp",  6,2001, "CJK Compatibility Ideographs Supplement",  0x02F800, 0x02FA1F, 542,   544  ]
            ,["cjk-ext-g",           6,2020, "CJK Unified Ideographs Extension G",       0x030000, 0x03134F, 4939,  4944 ]
            ,["cjk-ext-h",           6,2022, "CJK Unified Ideographs Extension H",       0x031350, 0x0323AF, 4192,  4192 ]
            ,["tags",                6,2001, "Tags",                                     0x0E0000, 0x0E007F, 97,    128  ]
            ,["selectors-supp",      6,2003, "Variation Selectors Supplement",           0x0E0100, 0x0E01EF, 240,   240  ]
             ]
zones=[gb2312zone,gbkzone,gb18030zone,big5zone,sjiszone,unicodezone]

def checkEqual(s,d,l,v):
  for i in range(0,l):
    if(s[i]!=d[i]):
      return v
  return d[l]

def removeUnused(ru, ra):
  rb=[]
  for i in ra:
    if i not in ru:
      rb.append(i)
  return rb

def writeSingle(f, nm, ry, ra):
  writefile.subtitle(f, nm, writefile.stringHEX(ry))
  writefile.array(f, 0, range(0x00,0x10), ry, ra, 16)

def writeDouble(f, z):
  nm = z[ZONE_NAME]
  st = z[ZONE_CODE_START]
  ed = z[ZONE_CODE_END]
  ry = z[ZONE_CHART_ROWS]
  ra = z[ZONE_CHART_POINTS]
  writefile.subtitle(f, nm, writefile.stringHEX(st)+"-"+writefile.stringHEX(ed))
  s = range(0,((st>>4)&0xF))
  rs = range(0,(st&0xFF))
  e = range(((ed>>4)&0xF)+1, 0xFF+1)
  re = range((ed&0xFF)+1, 0xFF+1)
  r0 = range(st>>8, (ed>>8) + 1)
  for i in range(0, len(r0)):
    if i==0:
      writefile.array(f, r0[i], range(0x0,0xF+1), removeUnused(s,ry), removeUnused(rs,ra), 16)
    elif i==len(r0)-1:
      writefile.array(f, r0[i], range(0x0,0xF+1), removeUnused(e,ry), removeUnused(re,ra), 16)
    else:
      writefile.array(f, r0[i], range(0x0,0xF+1), ry, ra, 16)
    writefile.breakline(f)

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
    writefile.breakline(f)

def writeUnicode(f, nm, st, ed):
  writefile.subtitle(f, nm, writefile.stringHEX(st)+"-"+writefile.stringHEX(ed))
  writefile.arrayUnicode(f, 0, range(st>>4,(ed>>4)+1), 4) 

def writeZones(f, zone, checkedZoneList):
  for i in range(len(zone)):
    if (    (checkedZoneList=="" or isInList(zone[i][ZONE_NAME], checkedZoneList) or isInList(zone[i][ZONE_ID], checkedZoneList))
        and ((zone[i][ZONE_VERSION] >= vermin) and (zone[i][ZONE_VERSION] <= vermax))
       ):
      if zone[i][ZONE_BYTE_WIDTH]==1:
        writeSingle(f, zone[i][ZONE_NAME], zone[i][ZONE_CHART_ROWS], zone[i][ZONE_CHART_POINTS])
      if zone[i][ZONE_BYTE_WIDTH]==2:
        writeDouble(f, zone[i])
      if zone[i][ZONE_BYTE_WIDTH]==4:
        writeQuad(f, zone[i][ZONE_NAME], zone[i][ZONE_CODE_START], zone[i][ZONE_CODE_END])
      if zone[i][ZONE_BYTE_WIDTH]==6:
        writeUnicode(f, zone[i][ZONE_NAME], zone[i][ZONE_CODE_START], zone[i][ZONE_CODE_END])

def writeFulls(f, full, checkedFullList):
  for i in range(len(full)):
    if (checkedFullList=="" or full[i][FULL_ID] in checkedFullList):
      writefile.subtitle(f, full[i][FULL_NAME], "")
      if full[i][FULL_BYTE_WIDTH]==1:
        writefile.array(f, 0, full[i][FULL_LOW], full[i][FULL_HIGH], range(0x00,0xFF+1), 16)
      if full[i][FULL_BYTE_WIDTH]==2:
        writefile.array(f, 0, full[i][FULL_LOW], full[i][FULL_HIGH], range(0x00,0xFFFF+1), 256)
      if full[i][FULL_BYTE_WIDTH]==4:
        writeQuad(f, full[i][FULL_NAME], full[i][FULL_HIGH], full[i][FULL_LOW])
      if full[i][FULL_BYTE_WIDTH]==6:
        if showStrip=="False":
          writefile.arrayUnicode(f, 0, full[i][FULL_HIGH], 8)
        else:
          writefile.arrayUnicodeB(f,full[i][FULL_HIGH], 4)
          lastcode=(full[i][FULL_HIGH][0]<<4)-1
          for j in range(0,len(unicodezone)):
            if (unicodezone[j][ZONE_CODE_START]>=(full[i][FULL_HIGH][0]<<8)) and (unicodezone[j][ZONE_CODE_START]<=(full[i][FULL_HIGH][len(full[i][FULL_HIGH])-1]<<8) ):
              if (lastcode+1)!=(unicodezone[j][ZONE_CODE_START]>>4):
                writefile.arrayUnicodeTitle(f, "Reserved", 17, "i")
                writefile.arrayUnicodeData(f, 0, range((lastcode+1),(unicodezone[j][ZONE_CODE_START]>>4)), 4)
              writefile.arrayUnicodeTitle(f, unicodezone[j][ZONE_NAME], 17, "")
              writefile.arrayUnicodeData(f, 0, range(unicodezone[j][ZONE_CODE_START]>>4,(unicodezone[j][ZONE_CODE_END]>>4)+1), 4)
              lastcode = (unicodezone[j][ZONE_CODE_END]>>4)
          writefile.arrayUnicodeE(f)

def writeSpecify(f, z, s, e):
  return ""

def dec2hexstr(d, w, tn, ts):
  s = hex(d)[2:].zfill(w).upper()[:w]
  for i in range(0,tn):
    s = s + ts
  return s

def listZones(z,a):
  print("---------------------------------------------") 
  print("zone id          note") 
  print("----------------+----------------------------")
  for i in range(len(z)):
    print("%-16s %02X-%02X, %s" %(z[i][ZONE_ID],z[i][ZONE_CODE_START],z[i][ZONE_CODE_END],z[i][ZONE_NAME]))
  print("----------------+----------------------------")
  print("array id         note") 
  print("----------------+----------------------------")
  for i in range(len(a)):
    if a[i][FULL_BYTE_WIDTH]==6:
      print("%-16s %s-%s, %s" %(a[i][FULL_ID],dec2hexstr(a[i][FULL_HIGH][0],4,2,"0"),dec2hexstr(a[i][FULL_HIGH][len(a[i][FULL_HIGH])-1],4,2,"F"),a[i][FULL_NAME]))
    elif a[i][FULL_BYTE_WIDTH]==4:
      print("%-16s %s-%s, %s" %(a[i][FULL_ID],dec2hexstr(a[i][FULL_HIGH],8,0,""),dec2hexstr(a[i][FULL_LOW],8,0,""),a[i][FULL_NAME]))
    elif a[i][FULL_BYTE_WIDTH]==2:
      print("%-16s %02X%02X-%02X%02X, %s" %(a[i][FULL_ID],a[i][FULL_HIGH][0],a[i][FULL_LOW][0],a[i][FULL_HIGH][len(a[i][FULL_HIGH])-1],a[i][FULL_LOW][len(a[i][FULL_LOW])-1],a[i][FULL_NAME]))
    else:
      print("%-16s %s-%s, %s" %(a[i][FULL_ID],dec2hexstr(a[i][FULL_HIGH][0],a[i][FULL_BYTE_WIDTH],a[i][FULL_BYTE_WIDTH],"0"),dec2hexstr(a[i][FULL_HIGH][len(a[i][FULL_HIGH])-1],a[i][FULL_BYTE_WIDTH],a[i][FULL_BYTE_WIDTH],"F"),a[i][FULL_NAME]))
  print("---------------------------------------------")
  sys.exit()

def isInList(v, l):
  ck = l.split(",")
  for i in ck:
    if v.find(i) >=0:
      return True
  return False

def zonelist(isshow, zone, checkedZoneList):
  ret = ""
  if isshow=="True":
    for i in range(len(zone)):
      if (    (checkedZoneList=="" or isInList(zone[i][ZONE_NAME], checkedZoneList) or isInList(zone[i][ZONE_ID], checkedZoneList))
          and ((zone[i][ZONE_VERSION] >= vermin) and (zone[i][ZONE_VERSION] <= vermax))
         ):
        ret = ret + writefile.linktagBegin(zone[i][ZONE_NAME])\
                  + writefile.stringHEX(zone[i][ZONE_CODE_START]) + " - " + writefile.stringHEX(zone[i][ZONE_CODE_END])\
                  + " : " + zone[i][ZONE_NAME]\
                  + " (" + str(zone[i][ZONE_POINT_CODED]) + "/" + str(zone[i][ZONE_POINT_ALL]) + ")"\
                  + writefile.linktagEnd()
      else:
        ret = ret + writefile.stringHEX(zone[i][ZONE_CODE_START]) + " - " + writefile.stringHEX(zone[i][ZONE_CODE_END])\
                  + " : " + zone[i][ZONE_NAME]\
                  + " (" + str(zone[i][ZONE_POINT_CODED]) + "/" + str(zone[i][ZONE_POINT_ALL]) + ")"
      ret = ret + writefile.lineBreak()
  return ret

def arraylist(isshow, full, checkedFullList):
  ret = ""
  if isshow=="True":
    for i in full:
      if (checkedFullList=="" or isInList(i[FULL_ID], checkedFullList)):
        ret = ret + writefile.linktagBegin(i[FULL_NAME]) + i[FULL_NAME] + writefile.linktagEnd()
      else:
        ret = ret + i[FULL_NAME]
      ret = ret + writefile.lineBreak()
  return ret


if listZone=="True":
  listZones(zones[currset],fulls[currset])

with open(fn1, 'wb') as f:
  writefile.head(f, charsetinfo[currset][0],charsetinfo[currset][1]);
  writefile.title(f, charsetinfo[currset][2],\
                    "Codepage : "+charsetinfo[currset][INFO_CODEPAGE] + writefile.lineBreak() +\
                    "Language : "+charsetinfo[currset][INFO_LANGUAGE] + writefile.lineBreak() +\
                    "Range : "+ charsetinfo[currset][INFO_RANGE]+ writefile.lineBreak() +\
                    "Version : "+ charsetinfo[currset][INFO_VERSION],\
                     zonelist(byBlock,zones[currset],showZones),\
                     arraylist(oneArray,fulls[currset],showFulls))
  writefile.breakline(f)

  if byBlock=="True":
    writeZones(f, zones[currset], showZones)

  if oneArray=="True":
    writeFulls(f, fulls[currset], showFulls)

  if specifyStart!="":
    writeSpecify(f, zones[currset], specifyStart, specifyEnd)

  writefile.tail(f);

  print("Write file "+fn1+" success.")

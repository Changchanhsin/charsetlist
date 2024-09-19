#!/usr/bin/env python

from sys import argv
import argument
import writefile
import sys


argument.setCopyright("2016-2024, Chanhsin")
argument.addDescription("  Create character set array")
argument.addSerial("charset", "Character set : 'gb', 'gbk', 'gb18030', 'big5', 'sjis'")
argument.addSerial("file", "Output file name (html), default is charset+'.html' or '.txt' if /t is selected")
argument.addKey("l", "List zone/array id of charaset", 0)
argument.addKey("b", "By area block", 0)
argument.addKey("z", "show zone ids, e.g. 'symbols,chinese', split with ',' no spacing", 1)
argument.addKey("a", "One array", 0)
argument.addKey("f", "show array ids, e.g. 'single,double', split with ',' no spacing", 1)
argument.addKey("t", "Output as TXT file", 0)
#argument.addKey("s", "Specify the start code, in HEX without '0x' prefix", 1)
#argument.addKey("e", "Specify the end code, default is start code", 1)
argument.addKey("g", "Characters gap (in TXT file) with space('s'/'2s'), tabulation('t'), or no space('n'), default is 't'", 1)
argument.addKey("d", "show debug message", 0)
argument.addKey("h", "help", 0)
argument.addExample("  %file% gbk gbk.html /b")

argument.parse(argv)
if argument.key("t", "False" ) == "True":
  writefile.isHTML = False
else:
  writefile.isHTML = True

charset   = argument.serial(1,"unknown")
if writefile.isHTML == True:
  fn1       = argument.serial(2, charset+".html")
else:
  fn1       = argument.serial(2, charset+".txt")
listZone  = argument.key("l", "False")
byBlock   = argument.key("b", "False")
showZones = argument.key("z", ""     )
oneArray  = argument.key("a", "False")
specifyStart = argument.key("s", "")
specifyEnd   = argument.key("e", "")
showFulls = argument.key("f", "")

gap = argument.key("g", "t")
if gap=="s":
  writefile.charGap=" "
if gap=="2s":
  writefile.charGap="  "
if gap=="n":
  writefile.charGap=""

if argument.key("d", "False")=="True":
  argument.printall()


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
charsetinfo=[["gb2312",  "SimSun",    "GB 2312",  "936",   "Chinese (Simplified)",                        "0x20-0x7E, 0x8181-0xFEFE"]
            ,["gbk",     "SimSun",    "GBK",      "936",   "Chinese (Simplified), Chinese, Multilingual", "0x20-0x7E, 0x8140-0xFEFE"]
            ,["gb18030", "SimSun",    "GB 18030", "54936", "Chinese (Simplified), Chinese, Multilingual", "0x20-0x7E, 0x8140-0xFEFE, 0x81308130-0xFE39FE39"]
            ,["big5",    "MingLiU",   "BIG-5",    "950",   "Chinese (Traditional)",                       "0x81-0xFE : 0x40-0x7E, 0xA1-0xFE"]
            ,["sjis",    "MS Mincho", "Shift JIS","932",   "Kanji",                                       "0x81-0x9F, 0xE0-0xEF : 0x40-0x7E, 0x80-0xFC"]
            ,["utf-8",   "Tahoma",    "UNICODE",  "0",     "Multilingual",                                "0x000000-0x10FFFF"]
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
             # id       w  name            high                 low
gb2312full =[["single", 1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)]
            ,["double", 2, "Double Bytes", range(0xA1,0xFE+1),  range(0xA1,0xFE+1)] # CHARSET_GB2312  = 0
             ]
gbkfull    =[["single", 1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)]
            ,["double", 2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1)) ] # CHARSET_GBK     = 1
             ]
gb18030full=[["single", 1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)  ]
            ,["double", 2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0x80,0xFE+1)) ] # CHARSET_GB18030 = 2
             ]
big5full   =[["single", 1, "Single Byte",  range(0x2,0x7+1),    range(0x0,0xF+1)  ]
            ,["double", 2, "Double Bytes", range(0x81,0xFE+1),  list(range(0x40,0x7E+1))+list(range(0xA1,0xFE+1)) ] # CHARSET_BIG5    = 3
             ]
sjisfull   =[["single", 1, "Single Byte",  list(range(0x2,0x7+1))+list(range(0xA,0xD+1)),     range(0x0,0xF+1)]
            ,["double", 2, "Double Bytes", list(range(0x81,0x9F+1))+list(range(0xE0,0xEF+1)), list(range(0x40,0x7E+1))+list(range(0x80,0xFC+1)) ] # CHARSET_SJIS    = 4
             ]
unicodefull=[["single", 1, "Single Bytes",                      range(0x2,0x7+1),     range(0x0,0xF+1)  ]
            ,["bmp",    6, "Basic Multilingual Plane",          range(0x01,0xFF+1),   rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["smp",    6, "Supplementary Multilingual Plane",  range(0x100,0x1FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["sip",    6, "Supplementary Ideographic Plane",   range(0x200,0x2FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
            ,["tip",    6, "Tertiary Ideographic Plane",        range(0x300,0x3FF+1), rangeUtf8L        ] # CHARSET_UNICODE = 5
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
            ,["dehong",     4,2005, "Quad - Dehong Dai",                         0x8134F434, 0x8134F830, 35,    37   ]
            ,["newdai",     4,2020, "Quad - Xishuangbanna New Dai",              0x8134F932, 0x81358437, 83,    96   ]
            ,["olddai",     4,2020, "Quad - Xishuangbanna Old Dai",              0x81358B32, 0x81359935, 127,   144  ]
            ,["yi",         4,2005, "Quad - Yi Syllables and Radicals",          0x82359833, 0x82369435, 1215,  1223 ]
            ,["lisu",       4,2020, "Quad - Lisu",                               0x82369535, 0x82369A32, 48,    48   ]
            ,["hjamo",      4,2005, "Quad - Hangul Jamo",                        0x81339D36, 0x8133B635, 69,    250  ]
            ,["hangul",     4,2005, "Quad - Hangul Compatibility Ideographs",    0x8139A933, 0x8139B734, 51,    142  ]
            ,["hsyllables", 4,2005, "Quad - Hangul Syllables",                   0x8237CF35, 0x8336BE36, 3431,  11172]
            ,["dmiao",      4,2020, "Quad - Diandong Miao",                      0x9232C636, 0x9232D635, 133,   160  ]
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
            #  0            1 2     3                                          4       5       6     7     8            9
            #  name         w ver   note                                       start   end     used  all   high 4bit    used code
unicodezone=[#["controls-0",  6,1992, "C0 Controls",      0x0001,   0x001F,   31,  31]
            #,
             ["latin",    6,1992, "Basic Latin",      0x0020,   0x007E,   94,  94]
            ,["controls-1",  6,1992, "C1 Controls",      0x0080,   0x009F,   32,  32]
            ,["latin-1",    6,1992, "Latin-1 Supplement",      0x00A0,   0x00FF,   95,  95]
            ,["latin-ext-a",    6,1992, "Latin Extended-A",      0x0100,   0x017F,   127,  127]
            ,["latin-ext-b",    6,1992, "Latin Extended-B",      0x0180,   0x024F,   207,  207]
            ,["ipa-e",    6,1992, "Ipa Extensions",      0x0250,   0x02AF,   95,  95]
            ,["spacing",    6,1992, "Spacing Modifier Letters",      0x02B0,   0x02FF,   79,  79]
            ,["diacritical",    6,1992, "Combining Diacritical Marks",      0x0300,   0x036F,   111,  111]
            ,["greek",    6,1992, "Greek And Coptic",      0x0370,   0x03FF,   143,  143]
            ,["cyrillic",    6,1992, "Cyrillic",      0x0400,   0x04FF,   255,  255]
            ,["cyrillic-s",    6,1992, "Cyrillic Supplement",      0x0500,   0x052F,   47,  47]
            ,["armenian",    6,1992, "Armenian",      0x0530,   0x058F,   95,  95]
            ,["hebrew",    6,1992, "Hebrew",      0x0590,   0x05FF,   111,  111]
            ,["arabic",    6,1992, "Arabic",      0x0600,   0x06FF,   255,  255]
            ,["syriac",    6,1992, "Syriac",      0x0700,   0x074F,   79,  79]
            ,["arabic-s",    6,1992, "Arabic Supplement",      0x0750,   0x077F,   47,  47]
            ,["thaana",    6,1992, "Thaana",      0x0780,   0x07BF,   63,  63]
            ,["nko",    6,1992, "Nko",      0x07C0,   0x07FF,   63,  63]
            ,["samaritan",    6,1992, "Samaritan",      0x0800,   0x083F,   63,  63]
            ,["mandaic",    6,1992, "Mandaic",      0x0840,   0x085F,   31,  31]
            ,["syriac-s",    6,1992, "Syriac Supplement",      0x0860,   0x086F,   15,  15]
            ,["arabic-a",    6,1992, "Arabic Extended-A",      0x08A0,   0x08FF,   95,  95]
            ,["devanagari",    6,1992, "Devanagari",      0x0900,   0x097F,   127,  127]
            ,["bengali",    6,1992, "Bengali",      0x0980,   0x09FF,   127,  127]
            ,["gurmukhi",    6,1992, "Gurmukhi",      0x0A00,   0x0A7F,   127,  127]
            ,["gujarati",    6,1992, "Gujarati",      0x0A80,   0x0AFF,   127,  127]
            ,["oriya",    6,1992, "Oriya",      0x0B00,   0x0B7F,   127,  127]
            ,["tamil",    6,1992, "Tamil",      0x0B80,   0x0BFF,   127,  127]
            ,["telugu",    6,1992, "Telugu",      0x0C00,   0x0C7F,   127,  127]
            ,["kannada",    6,1992, "Kannada",      0x0C80,   0x0CFF,   127,  127]
            ,["malayalam",    6,1992, "Malayalam",      0x0D00,   0x0D7F,   127,  127]
            ,["sinhala",    6,1992, "Sinhala",      0x0D80,   0x0DFF,   127,  127]
            ,["thai",    6,1992, "Thai",      0x0E00,   0x0E7F,   127,  127]
            ,["lao",    6,1992, "Lao",      0x0E80,   0x0EFF,   127,  127]
            ,["tibetan",    6,1992, "Tibetan",      0x0F00,   0x0FFF,   255,  255]
            ,["myanmar",    6,1992, "Myanmar",      0x1000,   0x109F,   159,  159]
            ,["georgian",    6,1992, "Georgian",      0x10A0,   0x10FF,   95,  95]
            ,["hangul-jamo",    6,1992, "Hangul Jamo",      0x1100,   0x11FF,   255,  255]
            ,["ethiopic",    6,1992, "Ethiopic",      0x1200,   0x137F,   383,  383]
            ,["ethiopic-s",    6,1992, "Ethiopic Supplement",      0x1380,   0x139F,   31,  31]
            ,["cherokee",    6,1992, "Cherokee",      0x13A0,   0x13FF,   95,  95]
            ,["canadian",    6,1992, "Unified Canadian Aboriginal Syllabics",      0x1400,   0x167F,   639,  639]
            ,["ogham",    6,1992, "Ogham",      0x1680,   0x169F,   31,  31]
            ,["runic",    6,1992, "Runic",      0x16A0,   0x16FF,   95,  95]
            ,["tagalog",    6,1992, "Tagalog",      0x1700,   0x171F,   31,  31]
            ,["hanunoo",    6,1992, "Hanunoo",      0x1720,   0x173F,   31,  31]
            ,["buhid",    6,1992, "Buhid",      0x1740,   0x175F,   31,  31]
            ,["tagbanwa",    6,1992, "Tagbanwa",      0x1760,   0x177F,   31,  31]
            ,["khmer",    6,1992, "Khmer",      0x1780,   0x17FF,   127,  127]
            ,["mongolian",    6,1992, "Mongolian",      0x1800,   0x18AF,   175,  175]
            ,["canadian-e",    6,1992, "Unified Canadian Aboriginal Syllabics Extended",      0x18B0,   0x18FF,   79,  79]
            ,["limbu",    6,1992, "Limbu",      0x1900,   0x194F,   79,  79]
            ,["taile",    6,1992, "Tai Le",      0x1950,   0x197F,   47,  47]
            ,["newtailue",    6,1992, "New Tai Lue (Xishuang Banna Dai)",      0x1980,   0x19DF,   95,  95]
            ,["khmer-symbols",    6,1992, "Khmer Symbols",      0x19E0,   0x19FF,   31,  31]
            ,["buginese",    6,1992, "Buginese",      0x1A00,   0x1A1F,   31,  31]
            ,["taitham",    6,1992, "Tai Tham",      0x1A20,   0x1AAF,   143,  143]
            ,["diacritical-e",    6,1992, "Combining Diacritical Marks Extended",      0x1AB0,   0x1AFF,   79,  79]
            ,["balinese",    6,1992, "Balinese",      0x1B00,   0x1B7F,   127,  127]
            ,["sundanese",    6,1992, "Sundanese",      0x1B80,   0x1BBF,   63,  63]
            ,["batak",    6,1992, "Batak",      0x1BC0,   0x1BFF,   63,  63]
            ,["lepcha",    6,1992, "Lepcha",      0x1C00,   0x1C4F,   79,  79]
            ,["olchiki",    6,1992, "Ol Chiki",      0x1C50,   0x1C7F,   47,  47]
            ,["cyrillic-e",    6,1992, "Cyrillic Extended",      0x1C80,   0x1C8F,   15,  15]
            ,["georgian-e",    6,1992, "Georgian Extended",      0x1C90,   0x1CBF,   47,  47]
            ,["sundanese-s",    6,1992, "Sundanese Supplement",      0x1CC0,   0x1CCF,   15,  15]
            ,["vedic-e",    6,1992, "Vedic Extensions",      0x1CD0,   0x1CFF,   47,  47]
            ,["phonetic-e",    6,1992, "Phonetic Extensions",      0x1D00,   0x1D7F,   127,  127]
            ,["phonetic-ext-s",    6,1992, "Phonetic Extensions Supplement",      0x1D80,   0x1DBF,   63,  63]
            ,["diacritical-s",    6,1992, "Combining Diacritical Marks Supplement",      0x1DC0,   0x1DFF,   63,  63]
            ,["latin-ext-add",    6,1992, "Latin Extended Additional",      0x1E00,   0x1EFF,   255,  255]
            ,["greek-e",    6,1992, "Greek Extended",      0x1F00,   0x1FFF,   255,  255]
            ,["punctuation",    6,1992, "General Punctuation",      0x2000,   0x206F,   111,  111]
            ,["sup-sub",    6,1992, "Superscripts And Subscripts",      0x2070,   0x209F,   47,  47]
            ,["currency",    6,1992, "Currency Symbols",      0x20A0,   0x20CF,   47,  47]
            ,["diacritical-symbols",    6,1992, "Combining Diacritical Marks For Symbols",      0x20D0,   0x20FF,   47,  47]
            ,["letterlike",    6,1992, "Letterlike Symbols",      0x2100,   0x214F,   79,  79]
            ,["number",    6,1992, "Number Forms",      0x2150,   0x218F,   63,  63]
            ,["arrows",    6,1992, "Arrows",      0x2190,   0x21FF,   111,  111]
            ,["mathematical",    6,1992, "Mathematical Operators",      0x2200,   0x22FF,   255,  255]
            ,["technical",    6,1992, "Miscellaneous Technical",      0x2300,   0x23FF,   255,  255]
            ,["control",    6,1992, "Control Pictures",      0x2400,   0x243F,   63,  63]
            ,["optical",    6,1992, "Optical Character Recognition",      0x2440,   0x245F,   31,  31]
            ,["enclosed",    6,1992, "Enclosed Alphanumerics",      0x2460,   0x24FF,   159,  159]
            ,["box",    6,1992, "Box Drawing",      0x2500,   0x257F,   127,  127]
            ,["block",    6,1992, "Block Elements",      0x2580,   0x259F,   31,  31]
            ,["geometric",    6,1992, "Geometric Shapes",      0x25A0,   0x25FF,   95,  95]
            ,["symbols",    6,1992, "Miscellaneous Symbols",      0x2600,   0x26FF,   255,  255]
            ,["dingbats",    6,1992, "Dingbats",      0x2700,   0x27BF,   191,  191]
            ,["mathematical-a",    6,1992, "Miscellaneous Mathematical Symbols-A",      0x27C0,   0x27EF,   47,  47]
            ,["arrows-a",    6,1992, "Supplemental Arrows-A",      0x27F0,   0x27FF,   15,  15]
            ,["braille",    6,1992, "Braille Patterns",      0x2800,   0x28FF,   255,  255]
            ,["arrows-b",    6,1992, "Supplemental Arrows-B",      0x2900,   0x297F,   127,  127]
            ,["mathematical-b",    6,1992, "Miscellaneous Mathematical Symbols-B",      0x2980,   0x29FF,   127,  127]
            ,["mathematical-o",    6,1992, "Supplemental Mathematical Operators",      0x2A00,   0x2AFF,   255,  255]
            ,["symbols-arrows",    6,1992, "Miscellaneous Symbols And Arrows",      0x2B00,   0x2BFF,   255,  255]
            ,["glagolitic",    6,1992, "Glagolitic",      0x2C00,   0x2C5F,   95,  95]
            ,["latin-ext-c",    6,1992, "Latin Extended-C",      0x2C60,   0x2C7F,   31,  31]
            ,["coptic",    6,1992, "Coptic",      0x2C80,   0x2CFF,   127,  127]
            ,["georgian-s",    6,1992, "Georgian Supplement",      0x2D00,   0x2D2F,   47,  47]
            ,["tifinagh",    6,1992, "Tifinagh",      0x2D30,   0x2D7F,   79,  79]
            ,["ethiopic-e",    6,1992, "Ethiopic Extended",      0x2D80,   0x2DDF,   95,  95]
            ,["cyrillic-ea",    6,1992, "Cyrillic Extended-A",      0x2DE0,   0x2DFF,   31,  31]
            ,["punctuation-s",    6,1992, "Supplemental Punctuation",      0x2E00,   0x2E7F,   127,  127]
            ,["cjk-radicals-s",    6,1992, "CJK Radicals Supplement",      0x2E80,   0x2EFF,   127,  127]
            ,["kangxi",    6,1992, "Kangxi Radicals",      0x2F00,   0x2FDF,   223,  223]
            ,["ideographic",    6,1992, "Ideographic Description Characters",      0x2FF0,   0x2FFF,   15,  15]
            ,["cjk-symbols",    6,1992, "CJK Symbols And Punctuation",      0x3000,   0x303F,   63,  63]
            ,["hiragana",    6,1992, "Hiragana",      0x3040,   0x309F,   95,  95]
            ,["katakana",    6,1992, "Katakana",      0x30A0,   0x30FF,   95,  95]
            ,["bopomofo",    6,1992, "Bopomofo",      0x3100,   0x312F,   47,  47]
            ,["hangul-comp-jamo",    6,1992, "Hangul Compatibility Jamo",      0x3130,   0x318F,   95,  95]
            ,["kanbun",    6,1992, "Kanbun (CJK Miscellaneous)",      0x3190,   0x319F,   15,  15]
            ,["bopomofo-e",    6,1992, "Bopomofo Extended",      0x31A0,   0x31BF,   31,  31]
            ,["cjk-strokes",    6,1992, "CJK Strokes",      0x31C0,   0x31EF,   47,  47]
            ,["katakana-pe",    6,1992, "Katakana Phonetic Extensions",      0x31F0,   0x31FF,   15,  15]
            ,["enclosed-cjk",    6,1992, "Enclosed CJK Letters And Months",      0x3200,   0x32FF,   255,  255]
            ,["cjk-comp",    6,1992, "CJK Compatibility",      0x3300,   0x33FF,   255,  255]
            ,["cjk-a",    6,1992, "CJK Unified Ideographs Extension A",      0x3400,   0x4DBF,   6591,  6591]
            ,["yijing",    6,1992, "Yijing Hexagram Symbols",      0x4DC0,   0x4DFF,   63,  63]
            ,["cjk",    6,1992, "CJK Unified Ideographs",      0x4E00,   0x9FFF,   20991,  20991]
            ,["yi",    6,1992, "Yi Syllables",      0xA000,   0xA48F,   1167,  1167]
            ,["yi-r",    6,1992, "Yi Radicals",      0xA490,   0xA4CF,   63,  63]
            ,["lisu",    6,1992, "Lisu",      0xA4D0,   0xA4FF,   47,  47]
            ,["vai",    6,1992, "Vai",      0xA500,   0xA63F,   319,  319]
            ,["cyrillic-eb",    6,1992, "Cyrillic Extended-B",      0xA640,   0xA69F,   95,  95]
            ,["bamum",    6,1992, "Bamum",      0xA6A0,   0xA6FF,   95,  95]
            ,["tone",    6,1992, "Modifier Tone Letters",      0xA700,   0xA71F,   31,  31]
            ,["latin-ext-d",    6,1992, "Latin Extended-D",      0xA720,   0xA7FF,   223,  223]
            ,["sylotinagri",    6,1992, "Syloti Nagri",      0xA800,   0xA82F,   47,  47]
            ,["indicnumber",    6,1992, "Common Indic Number Forms",      0xA830,   0xA83F,   15,  15]
            ,["phags-pa",    6,1992, "Phags-Pa",      0xA840,   0xA87F,   63,  63]
            ,["saurashtra",    6,1992, "Saurashtra",      0xA880,   0xA8DF,   95,  95]
            ,["devanagari-e",    6,1992, "Devanagari Extended",      0xA8E0,   0xA8FF,   31,  31]
            ,["kayahli",    6,1992, "Kayah Li",      0xA900,   0xA92F,   47,  47]
            ,["rejang",    6,1992, "Rejang",      0xA930,   0xA95F,   47,  47]
            ,["hangul-jamo-ext-a",    6,1992, "Hangul Jamo Extended-A",      0xA960,   0xA97F,   31,  31]
            ,["javanese",    6,1992, "Javanese",      0xA980,   0xA9DF,   95,  95]
            ,["myanmar-eb",    6,1992, "Myanmar Extended-B",      0xA9E0,   0xA9FF,   31,  31]
            ,["cham",    6,1992, "Cham",      0xAA00,   0xAA5F,   95,  95]
            ,["myanmar-ea",    6,1992, "Myanmar Extended-A",      0xAA60,   0xAA7F,   31,  31]
            ,["taiviet",    6,1992, "Tai Viet",      0xAA80,   0xAADF,   95,  95]
            ,["meeteimayek-e",    6,1992, "Meetei Mayek Extensions",      0xAAE0,   0xAAFF,   31,  31]
            ,["ethiopic-ea",    6,1992, "Ethiopic Extended-A",      0xAB00,   0xAB2F,   47,  47]
            ,["latin-ext-e",    6,1992, "Latin Extended-E",      0xAB30,   0xAB6F,   63,  63]
            ,["cherokee-s",    6,1992, "Cherokee Supplement",      0xAB70,   0xABBF,   79,  79]
            ,["meeteimayek",    6,1992, "Meetei Mayek",      0xABC0,   0xABFF,   63,  63]
            ,["hangul-syllables",    6,1992, "Hangul Syllables",      0xAC00,   0xD7A3,   11171,  11171]
            ,["hangul-jamo-ext-b",    6,1992, "Hangul Jamo Extended-B",      0xD7B0,   0xD7FF,   79,  79]
            ,["pua",    6,1992, "Private Use Area",      0xE000,   0xF8FF,   6399,  6399]
            ,["cjk-comp-ideo",    6,1992, "CJK Compatibility Ideographs",      0xF900,   0xFAFF,   511,  511]
            ,["alphabetic",    6,1992, "Alphabetic Presentation Forms",      0xFB00,   0xFB4F,   79,  79]
            ,["arbic-pfa",    6,1992, "Arabic Presentation Forms-A",      0xFB50,   0xFDFF,   687,  687]
            ,["selectors",    6,1992, "Variation Selectors",      0xFE00,   0xFE0F,   15,  15]
            ,["vertical",    6,1992, "Vertical Forms",      0xFE10,   0xFE1F,   15,  15]
            ,["half",    6,1992, "Combining Half Marks",      0xFE20,   0xFE2F,   15,  15]
            ,["cjk-comp-form",    6,1992, "CJK Compatibility Forms",      0xFE30,   0xFE4F,   31,  31]
            ,["smallform",    6,1992, "Small Form Variants",      0xFE50,   0xFE6F,   31,  31]
            ,["arabic-pfb",    6,1992, "Arabic Presentation Forms-B",      0xFE70,   0xFEFE,   142,  142]
            ,["half-full",    6,1992, "Halfwidth And Fullwidth Forms",      0xFF00,   0xFFEF,   239,  239]
            ,["specials",    6,1992, "Specials",      0xFFF0,   0xFFFD,   13,  13]
            ,["linear-b-s",    6,1992, "Linear B Syllabary",      0x10000,   0x1007F,   127,  127]
            ,["linear-b-i",    6,1992, "Linear B Ideograms",      0x10080,   0x100FF,   127,  127]
            ,["aegean",    6,1992, "Aegean Numbers",      0x10100,   0x1013F,   63,  63]
            ,["greek-numbers",    6,1992, "Ancient Greek Numbers",      0x10140,   0x1018F,   79,  79]
            ,["ancient-symbols",    6,1992, "Ancient Symbols",      0x10190,   0x101CF,   63,  63]
            ,["phaistos",    6,1992, "Phaistos Disc",      0x101D0,   0x101FF,   47,  47]
            ,["lycian",    6,1992, "Lycian",      0x10280,   0x1029F,   31,  31]
            ,["carian",    6,1992, "Carian",      0x102A0,   0x102DF,   63,  63]
            ,["coptic-epact",    6,1992, "Coptic Epact Numbers",      0x102E0,   0x102FF,   31,  31]
            ,["old-italic",    6,1992, "Old Italic",      0x10300,   0x1032F,   47,  47]
            ,["gothic",    6,1992, "Gothic",      0x10330,   0x1034F,   31,  31]
            ,["old-permic",    6,1992, "Old Permic",      0x10350,   0x1037F,   47,  47]
            ,["ugaritic",    6,1992, "Ugaritic",      0x10380,   0x1039F,   31,  31]
            ,["old-persian",    6,1992, "Old Persian",      0x103A0,   0x103DF,   63,  63]
            ,["deseret",    6,1992, "Deseret",      0x10400,   0x1044F,   79,  79]
            ,["shavian",    6,1992, "Shavian",      0x10450,   0x1047F,   47,  47]
            ,["osmanya",    6,1992, "Osmanya",      0x10480,   0x104AF,   47,  47]
            ,["osage",    6,1992, "Osage",      0x104B0,   0x104FF,   79,  79]
            ,["elbasan",    6,1992, "Elbasan",      0x10500,   0x1052F,   47,  47]
            ,["caucasian",    6,1992, "Caucasian Albanian",      0x10530,   0x1056F,   63,  63]
            ,["linear-a",    6,1992, "Linear A",      0x10600,   0x1077F,   383,  383]
            ,["cypriot",    6,1992, "Cypriot Syllabary",      0x10800,   0x1083F,   63,  63]
            ,["aramaic",    6,1992, "Imperial Aramaic",      0x10840,   0x1085F,   31,  31]
            ,["palmyrene",    6,1992, "Palmyrene",      0x10860,   0x1087F,   31,  31]
            ,["nabataean",    6,1992, "Nabataean",      0x10880,   0x108AF,   47,  47]
            ,["hatran",    6,1992, "Hatran",      0x108E0,   0x108FF,   31,  31]
            ,["phoenician",    6,1992, "Phoenician",      0x10900,   0x1091F,   31,  31]
            ,["lydian",    6,1992, "Lydian",      0x10920,   0x1093F,   31,  31]
            ,["meroitic-h",    6,1992, "Meroitic Hieroglyphs",      0x10980,   0x1099F,   31,  31]
            ,["meroitic-c",    6,1992, "Meroitic Cursive",      0x109A0,   0x109FF,   95,  95]
            ,["kharoshthi",    6,1992, "Kharoshthi",      0x10A00,   0x10A5F,   95,  95]
            ,["old-s-arabian",    6,1992, "Old South Arabian",      0x10A60,   0x10A7F,   31,  31]
            ,["old-n-arabian",    6,1992, "Old North Arabian",      0x10A80,   0x10A9F,   31,  31]
            ,["manichaean",    6,1992, "Manichaean",      0x10AC0,   0x10AFF,   63,  63]
            ,["avestan",    6,1992, "Avestan",      0x10B00,   0x10B3F,   63,  63]
            ,["parthian",    6,1992, "Inscriptional Parthian",      0x10B40,   0x10B5F,   31,  31]
            ,["pahlavi",    6,1992, "Inscriptional Pahlavi",      0x10B60,   0x10B7F,   31,  31]
            ,["psalter",    6,1992, "Psalter Pahlavi",      0x10B80,   0x10BAF,   47,  47]
            ,["old-turkic",    6,1992, "Old Turkic",      0x10C00,   0x10C4F,   79,  79]
            ,["old-hungarian",    6,1992, "Old Hungarian",      0x10C80,   0x10CFF,   127,  127]
            ,["hanifi-rohingya",    6,1992, "Hanifi Rohingya",      0x10D00,   0x10D3F,   63,  63]
            ,["rumi",    6,1992, "Rumi Numeral Symbols",      0x10E60,   0x10E7F,   31,  31]
            ,["yezidi",    6,1992, "Yezidi",      0x10E80,   0x10EBF,   63,  63]
            ,["old-sogdian",    6,1992, "Old Sogdian",      0x10F00,   0x10F2F,   47,  47]
            ,["sogdian",    6,1992, "Sogdian",      0x10F30,   0x10F6F,   63,  63]
            ,["chorasmian",    6,1992, "Chorasmian",      0x10FB0,   0x10FDF,   47,  47]
            ,["elymaic",    6,1992, "Elymaic",      0x10FE0,   0x10FFF,   31,  31]
            ,["brahmi",    6,1992, "Brahmi",      0x11000,   0x1107F,   127,  127]
            ,["kaithi",    6,1992, "Kaithi",      0x11080,   0x110CF,   79,  79]
            ,["sora-sompeng",    6,1992, "Sora Sompeng",      0x110D0,   0x110FF,   47,  47]
            ,["chakma",    6,1992, "Chakma",      0x11100,   0x1114F,   79,  79]
            ,["mahajani",    6,1992, "Mahajani",      0x11150,   0x1117F,   47,  47]
            ,["sharada",    6,1992, "Sharada",      0x11180,   0x111DF,   95,  95]
            ,["sinhala-archaic",    6,1992, "Sinhala Archaic Numbers",      0x111E0,   0x111FF,   31,  31]
            ,["khojki",    6,1992, "Khojki",      0x11200,   0x1124F,   79,  79]
            ,["multani",    6,1992, "Multani",      0x11280,   0x112AF,   47,  47]
            ,["khudawadi",    6,1992, "Khudawadi",      0x112B0,   0x112FF,   79,  79]
            ,["grantha",    6,1992, "Grantha",      0x11300,   0x1137F,   127,  127]
            ,["newa",    6,1992, "Newa",      0x11400,   0x1147F,   127,  127]
            ,["tirhuta",    6,1992, "Tirhuta",      0x11480,   0x114DF,   95,  95]
            ,["siddham",    6,1992, "Siddham",      0x11580,   0x115FF,   127,  127]
            ,["modi",    6,1992, "Modi",      0x11600,   0x1165F,   95,  95]
            ,["mongolian-s",    6,1992, "Mongolian Supplement",      0x11660,   0x1167F,   31,  31]
            ,["takai",    6,1992, "Takri",      0x11680,   0x116CF,   79,  79]
            ,["ahom",    6,1992, "Ahom",      0x11700,   0x1173F,   63,  63]
            ,["dogra",    6,1992, "Dogra",      0x11800,   0x1184F,   79,  79]
            ,["warang",    6,1992, "Warang Citi",      0x118A0,   0x118FF,   95,  95]
            ,["dives",    6,1992, "Dives Akuru",      0x11900,   0x1195F,   95,  95]
            ,["nandinagari",    6,1992, "Nandinagari",      0x119A0,   0x119FF,   95,  95]
            ,["zanabazar",    6,1992, "Zanabazar Square",      0x11A00,   0x11A4F,   79,  79]
            ,["soyombo",    6,1992, "Soyombo",      0x11A50,   0x11AAF,   95,  95]
            ,["paucinhau",    6,1992, "Pau Cin Hau",      0x11AC0,   0x11AFF,   63,  63]
            ,["bhaiksuki",    6,1992, "Bhaiksuki",      0x11C00,   0x11C6F,   111,  111]
            ,["marchen",    6,1992, "Marchen",      0x11C70,   0x11CBF,   79,  79]
            ,["masaram",    6,1992, "Masaram Gondi",      0x11D00,   0x11D5F,   95,  95]
            ,["gunjala",    6,1992, "Gunjala Gondi",      0x11D60,   0x11DAF,   79,  79]
            ,["makasar",    6,1992, "Makasar",      0x11EE0,   0x11EFF,   31,  31]
            ,["lisu-s",    6,1992, "Lisu Supplement",      0x11FB0,   0x11FBF,   15,  15]
            ,["tamil-s",    6,1992, "Tamil Supplement",      0x11FC0,   0x11FFF,   63,  63]
            ,["cuneiform",    6,1992, "Cuneiform",      0x12000,   0x123FF,   1023,  1023]
            ,["cuneiform-np",    6,1992, "Cuneiform Numbers And Punctuation",      0x12400,   0x1247F,   127,  127]
            ,["early",    6,1992, "Early Dynastic Cuneiform",      0x12480,   0x1254F,   207,  207]
            ,["egyptian",    6,1992, "Egyptian Hieroglyphs",      0x13000,   0x1342F,   1071,  1071]
            ,["egyptian-fc",    6,1992, "Egyptian Hieroglyphs Format Controls",      0x13430,   0x1343F,   15,  15]
            ,["anatolian",    6,1992, "Anatolian Hieroglyphs",      0x14400,   0x1467F,   639,  639]
            ,["bamum-s",    6,1992, "Bamum Supplement",      0x16800,   0x16A3F,   575,  575]
            ,["mro",    6,1992, "Mro",      0x16A40,   0x16A6F,   47,  47]
            ,["bassavah",    6,1992, "Bassa Vah",      0x16AD0,   0x16AFF,   47,  47]
            ,["pahawh",    6,1992, "Pahawh Hmong",      0x16B00,   0x16B8F,   143,  143]
            ,["medefaidrin",    6,1992, "Medefaidrin",      0x16E40,   0x16E9F,   95,  95]
            ,["miao",    6,1992, "Miao",      0x16F00,   0x16F9F,   159,  159]
            ,["ideo-symbols-punc",    6,1992, "Ideographic Symbols And Punctuation",      0x16FE0,   0x16FFF,   31,  31]
            ,["tangut",    6,1992, "Tangut",      0x17000,   0x187FF,   6143,  6143]
            ,["tangut-comp",    6,1992, "Tangut Components",      0x18800,   0x18AFF,   767,  767]
            ,["khitan-small",    6,1992, "Khitan Small Script",      0x18B00,   0x18CFF,   511,  511]
            ,["tangut-s",    6,1992, "Tangut Supplement",      0x18D00,   0x18D7F,   127,  127]
            ,["kana-s",    6,1992, "Kana Supplement",      0x1B000,   0x1B0FF,   255,  255]
            ,["kana-ea",    6,1992, "Kana Extended-A",      0x1B100,   0x1B12F,   47,  47]
            ,["small-kana-e",    6,1992, "Small Kana Extension",      0x1B130,   0x1B16F,   63,  63]
            ,["nushu",    6,1992, "Nushu",      0x1B170,   0x1B2FF,   399,  399]
            ,["duployan",    6,1992, "Duployan",      0x1BC00,   0x1BC9F,   159,  159]
            ,["shorthand",    6,1992, "Shorthand Format Control",      0x1BCA0,   0x1BCAF,   15,  15]
            ,["byzantine",    6,1992, "Byzantine Musical Symbols",      0x1D000,   0x1D0FF,   255,  255]
            ,["musical",    6,1992, "Musical Symbols",      0x1D100,   0x1D1FF,   255,  255]
            ,["ancient-greek",    6,1992, "Ancient Greek Musical Notation",      0x1D200,   0x1D24F,   79,  79]
            ,["mayan-num",    6,1992, "Mayan Numerals",      0x1D2E0,   0x1D2FF,   31,  31]
            ,["taixuanjing",    6,1992, "Tai Xuan Jing Symbols",      0x1D300,   0x1D35F,   95,  95]
            ,["conunting-rod",    6,1992, "Counting Rod Numerals",      0x1D360,   0x1D37F,   31,  31]
            ,["math-alpha-symbols",    6,1992, "Mathematical Alphanumeric Symbols",      0x1D400,   0x1D7FF,   1023,  1023]
            ,["sutton",    6,1992, "Sutton Signwriting",      0x1D800,   0x1DAAF,   687,  687]
            ,["glagolitic-s",    6,1992, "Glagolitic Supplement",      0x1E000,   0x1E02F,   47,  47]
            ,["nyiakeng",    6,1992, "Nyiakeng Puachue Hmong",      0x1E100,   0x1E14F,   79,  79]
            ,["wangcho",    6,1992, "Wancho",      0x1E2C0,   0x1E2FF,   63,  63]
            ,["mende",    6,1992, "Mende Kikakui",      0x1E800,   0x1E8DF,   223,  223]
            ,["adlam",    6,1992, "Adlam",      0x1E900,   0x1E95F,   95,  95]
            ,["indic-siyaq-num",    6,1992, "Indic Siyaq Numbers",      0x1EC70,   0x1ECBF,   79,  79]
            ,["ottoman-siyaq-num",    6,1992, "Ottoman Siyaq Numbers",      0x1ED00,   0x1ED4F,   79,  79]
            ,["arabic-math",    6,1992, "Arabic Mathematical Alphabetical Symbols",      0x1EE00,   0x1EEFF,   255,  255]
            ,["mahjong",    6,1992, "Mahjong Tiles",      0x1F000,   0x1F02F,   47,  47]
            ,["domino",    6,1992, "Domino Tiles",      0x1F030,   0x1F09F,   111,  111]
            ,["cards",    6,1992, "Playing Cards",      0x1F0A0,   0x1F0FF,   95,  95]
            ,["enclosed-alpha-s",    6,1992, "Enclosed Alphanumeric Supplement",      0x1F100,   0x1F1FF,   255,  255]
            ,["enclosed-ideo-s",    6,1992, "Enclosed Ideographic Supplement",      0x1F200,   0x1F2FF,   255,  255]
            ,["symbols-pict",    6,1992, "Miscellaneous Symbols And Pictographs",      0x1F300,   0x1F5FF,   767,  767]
            ,["emoticons",    6,1992, "Emoticons",      0x1F600,   0x1F64F,   79,  79]
            ,["ornamental-db",    6,1992, "Ornamental Dingbats",      0x1F650,   0x1F67F,   47,  47]
            ,["transport",    6,1992, "Transport And Map Symbols",      0x1F680,   0x1F6FF,   127,  127]
            ,["alchemical",    6,1992, "Alchemical Symbols",      0x1F700,   0x1F77F,   127,  127]
            ,["geometric-se",    6,1992, "Geometric Shapes Extended",      0x1F780,   0x1F7FF,   127,  127]
            ,["arrows-c",    6,1992, "Supplemental Arrows-C",      0x1F800,   0x1F8FF,   255,  255]
            ,["symbols-pict-s",    6,1992, "Supplemental Symbols And Pictographs",      0x1F900,   0x1F9FF,   255,  255]
            ,["chess",    6,1992, "Chess Symbols",      0x1FA00,   0x1FA6F,   111,  111]
            ,["symbols-pict-ext-a",    6,1992, "Symbols And Pictographs Extended-A",      0x1FA70,   0x1FAFF,   143,  143]
            ,["legacycomputing",    6,1992, "Symbols For Legacy Computing",      0x1FB00,   0x1FBFF,   255,  255]
            ,["cjk-ext-b",    6,1992, "CJK Unified Ideographs Extension B",      0x20000,   0x2A6DF,   42719,  42719]
            ,["cjk-ext-c",    6,1992, "CJK Unified Ideographs Extension C",      0x2A700,   0x2B73F,   4159,  4159]
            ,["cjk-ext-d",    6,1992, "CJK Unified Ideographs Extension D",      0x2B740,   0x2B81F,   223,  223]
            ,["cjk-ext-e",    6,1992, "CJK Unified Ideographs Extension E",      0x2B820,   0x2CEAF,   5775,  5775]
            ,["cjk-ext-f",    6,1992, "CJK Unified Ideographs Extension F",      0x2CEB0,   0x2EBEF,   7487,  7487]
            ,["cjk-comp-ideo-s",    6,1992, "CJK Compatibility Ideographs Supplement",      0x2F800,   0x2FA1F,   543,  543]
            ,["cjk-ext-g",    6,1992, "CJK Unified Ideographs Extension G",      0x30000,   0x3134F,   4943,  4943]
            ,["tags",    6,1992, "Tags",      0xE0000,   0xE007F,   127,  127]
            ,["selectors-s",    6,1992, "Variation Selectors Supplement",      0xE0100,   0xE01EF,   239,  239]
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
    if (checkedZoneList=="" or isInList(zone[i][ZONE_NAME], checkedZoneList) or isInList(zone[i][ZONE_ID], checkedZoneList)):
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
      if full[i][FULL_BYTE_WIDTH]==6:
        writefile.arrayUnicode(f, 0, full[i][FULL_HIGH], 8)

def writeSpecify(f, s, e):
  return ""

def listZones(z):
  print("zone id          note") 
  print("----------------+--------------------") 
  for i in range(len(z)):
    print("%-16s %02X-%02X, %s" %(z[i][ZONE_ID],z[i][ZONE_CODE_START],z[i][ZONE_CODE_END],z[i][ZONE_NAME]))
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
    for i in zone:
      if (checkedZoneList=="" or isInList(i[ZONE_NAME], checkedZoneList) or isInList(i[ZONE_ID], checkedZoneList)):
        ret = ret + writefile.linktagBegin(i[ZONE_NAME])\
                  + writefile.stringHEX(i[ZONE_CODE_START]) + " - " + writefile.stringHEX(i[ZONE_CODE_END])\
                  + " : " + i[ZONE_NAME]\
                  + " (" + str(i[ZONE_POINT_CODED]) + "/" + str(i[ZONE_POINT_ALL]) + ")"\
                  + writefile.linktagEnd()
      else:
        ret = ret + writefile.stringHEX(i[ZONE_CODE_START]) + " - " + writefile.stringHEX(i[ZONE_CODE_END])\
                  + " : " + i[ZONE_NAME]\
                  + " (" + str(i[ZONE_POINT_CODED]) + "/" + str(i[ZONE_POINT_ALL]) + ")"
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

if charset=="gb2312":
  currset=0
if charset=="gbk":
  currset=1
if charset=="gb18030":
  currset=2
if charset=="big5":
  currset=3
if charset=="sjis":
  currset=4
if charset=="utf-8":
  currset=5

if listZone=="True":
  listZones(zones[currset])

with open(fn1, 'wb') as f:
  writefile.head(f, charsetinfo[currset][0],charsetinfo[currset][1]);
#  writefile.actChangeFont(f)
  writefile.title(f, charsetinfo[currset][2],\
                    "Codepage : "+charsetinfo[currset][3] + writefile.lineBreak() +\
                    "Language : "+charsetinfo[currset][4] + writefile.lineBreak() +\
                    "Range : "+charsetinfo[currset][5],\
                     zonelist(byBlock,zones[currset],showZones),\
                     arraylist(oneArray,fulls[currset],showFulls))
  writefile.breakline(f)

  if byBlock=="True":
    writeZones(f, zones[currset], showZones)

  if oneArray=="True":
    writeFulls(f, fulls[currset], showFulls)

  if specifyStart!="":
    writeSpecify(f, specifyStart, specifyEnd)

  writefile.tail(f);
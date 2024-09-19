# charsetlist

charset.py by ZZX
 Function:
  Create character set array
 Usage:
  charset.py /l /b /z z /a /f f /t /g g /d /h charset file
 where:
  charset = Character set : 'gb', 'gbk', 'gb18030', 'big5', 'sjis'
  file = Output file name (html)
  /l = List zone/array id of charaset
  /b = By area block
  /z = show zone ids, e.g. 'symbols,chinese', split with ',' no spacing
  /a = One array
  /f = show array ids, e.g. 'single,double', split with ',' no spacing
  /t = Output as TXT file
  /g = Characters gap with space('s'/'2s'), tabulation('t'), or no space('n'), default is 't'
  /d = show debug message
  /h = help
 Example:
  charset.py gbk gbk.html /b
 Copyright(C) 2016-2024, Chanhsin

# charsetlist

charset.py by ZZX

## Function:
  Create character set array
  
## Usage:
  charset.py /l /b /z zone /m /a array /s /t /g gap /v version /d /h codepage_name file_name
  
## where:

  codepage_name = Character set: 'gb2312', 'gbk', 'gb18030', 'big5', 'sjis', 'utf-8'
  
  file_name = Output file name (html), default is charset+'.html' or '.txt' if /t is selected
  
  /l = List zone/array id of charaset
  
  /b = Show by block
  
  /z = Zone id of block when /b is selected, e.g. 'symbols,chinese', split with ',' no spacing
  
  /m = Show as matrix
  
  /a = Array id set when /m is selected, e.g. 'single,double', split with ',' no spacing
  
  /s = Show array as strip, for utf-8 only
  
  /t = Output as TXT file
  
  /g = Characters gap (in TXT file) with space('s'/'2s'), tabulation('t'), or no space('n'), default is 't'
  
  /v = Select version year, 'YYYY' for single, '-YYYY' for before, 'YYYY-' for later, 'YYYY-YYYY' for between
  
  /d = show debug message
  
  /h = help
  
## Example:
  charset.py gbk /b
  
## Copyright(C) 2016-2024, Chanhsin
···

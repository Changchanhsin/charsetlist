print ("<html><body>")
print ("<table cellpadding=3 cellspacing=1 bgcolor=red><tr>")
for i in range(0,200704):
  if( i%16 ==0):
    print("</tr>\n<tr><td align=center><font color=white>%04X</font></td>"%i,end='')
  print ("<td bgcolor=white align=center>",end='')
  print ("&#%d;"%i,end='')
  print ("</td>",end='')
print ("</table>")
print ("</body></html>")
from xml.dom.minidom import parse
import sys
i=1
dom = parse("C:\\input.xml")
out = open("C:\\output.srt", 'wb', )
body = dom.getElementsByTagName("timedtext")[0]
paras = body.getElementsByTagName("text")
for para in paras:
    out.write((str(i) + "\r\n").encode("utf-8"))
    sub = para.attributes['t'].value;
    t = int(sub)
    sub1 = str(t%1000).zfill(3)
    sub2 = str(int(t/1000)%60).zfill(2)
    sub3 = str(int(t/60000)%60).zfill(2)
    sub4 = str(int(t/3600000)%60).zfill(2)
    start = sub4 + ':' + sub3 + ':' + sub2+ ',' + sub1
             
    sub = para.attributes['d'].value;
    d = int(sub) + t
    sub1 = str(d%1000).zfill(3)
    sub2 = str(int(d/1000)%60).zfill(2)
    sub3 = str(int(d/60000)%60).zfill(2)
    sub4 = str(int(d/3600000)%60).zfill(2)
    end = sub4 + ':' + sub3 + ':' + sub2+ ',' + sub1
    out.write((start + ' --> ' + end + '\r\n').encode("utf8"))
    for child in para.childNodes:
        if child.nodeName == '#text':
            out.write(child.data.encode("utf8"))
    out.write(("\r\n\r\n").encode("utf8"))
    i += 1
out.close()
from FileHelper import Loader, Writer

example = Loader("a_example.txt")
k=Writer("a_example.out")
count = 0
vertical=[]
horizontal=[]
for x in example.photos:
    if 'V'in x:
        vertical.append(count)
    if 'H'in x:
        horizontal.append(count)
    count = count+1
length = int(len(vertical)/2+len(horizontal))
k.writeSlidesLength(length)
k.writeVerticalsAndHorizontals(vertical,horizontal)
k.close()
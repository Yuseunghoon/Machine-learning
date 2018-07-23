f=open('aaaa.jpg','rb')
bin=f.read()
print(bin)
f.close()

f_dest = open('python_copy.jpg','wb')
f_dest.write(bin)
f_dest.close()

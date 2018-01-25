import docx2txt

# extract text
text = docx2txt.process("input")

# extract text and write images in /tmp/img_dir
#text = docx2txt.process("file.docx", "/tmp/img_dir") 


# file-output.py
f = open('output.txt','w')
f.write(text.encode("utf-8"))
f.close()

#print(text)
print('DONE')
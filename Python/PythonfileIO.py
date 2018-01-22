'''
从一个文件复制到另一个文件
'''
old_file_name = input('please input a file name')

f_read = open(old_file_name,'r+')

position = old_file_name.rfind('.')
new_file_name = old_file_name[0:position] + '[复件]' + old_file_name[position:]

f_write = open(new_file_name,'w')

content = f_read.read()
f_write.write(content)

f_read.close()
f_write.close()


import pickle


a = [1, 2, 'apple']
# 只能写入二进制或字符串类型
fh.write(str(a))
fh = open('temp.txt', 'r')
a2 = fh.read()
# 读取的是字符串，无法存储类型

# 如果既想存储内容又想存储类型用腌制

# 腌制到内存中
a2 = pickle.dumps(a) # 存储
a3 = pickle.loads(a2) # 加载成a3
# 腌制到文件中 结尾都没有s
fh= open('temp.txt', 'wb') # 以二进制形式打开
pickle.dump(a, fh) # 
fh.close()
fh = open('temp.txt', 'rb')
a4 = pickle.load(fh) # 此时的a4是个列表，不是字符串，既保存了内容又保存了类型


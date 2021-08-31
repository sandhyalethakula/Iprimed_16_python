'''2.print string output using string slicing
'''

msg = 'Hello world, Python people!'
print("'"+msg[6:11]+"'")
print("'"+msg[13:26]+"'") 
print("'"+msg[13:20]+msg[6:11]+"'") 
print("'"+msg[0:6]+msg[20:26]+"'") 		
print("'"+msg[0:6]+msg[20:26]+' who belong to '+msg[13:20]+msg[6:11]+"'") 
print("'"+msg[:26]+"'")
print("'"+msg[-2::-1]+"'")
print("'"+msg[-23::-1]+"'")
print("'"+msg[-2:-8:-1]+"'")
rev= msg[6:11] +""+msg[12:19]              
print("'"+rev[::-1]+"'") 

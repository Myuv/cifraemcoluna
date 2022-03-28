import math
  
key = str (input("Chave: "))
  
def criptografrarMensagem(msg):
    cifra = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
    col = len(key)
      
    row = int(math.ceil(msg_len / col))
  
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
   
    matriz = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cifra += ''.join([row[curr_idx] 
                          for row in matriz])
        k_indx += 1
  
    return cifra
  
msg = "fujam todos fomos descobertos"
  
cifra = criptografrarMensagem(msg)
print("Mensagem criptografada: {}". format(cifra))
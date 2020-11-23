#encapsulation / fonksiyon içinde fonksiyon örneği
def outher(num1):
  print('outher')
  def inner_incerement(num1):
    print('inner')
    return num1+1
  num2=inner_incerement(num1)
  print(num1,num2)

outher(10)


# bir diğer örnek
 
def islem(islem_adi):
 def toplam(*args):
    toplam=0
    for i in args:
      toplam+=i
      return toplam

 def carpma(*args):
   carpma=1
   for i in args:
      carpma*=i
      return carpma
 

 if islem_adi == "toplama":
  return toplam
 else:
  return carpma


toplama=islem("toplama")
print(toplama(9,8,7,9,6))
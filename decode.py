#-*-coding:cp1254-*-
import sys
sys.path

print """Dosya okutmayacaksan bo� b�rak. """

def decode():
    sy = raw_input("okunacak dosya :")
    if sy is "":
        msg =raw_input("�ifre :")
        sifreli_msg="""%s"""%(msg)
    else:
        
        sifreli_msg="""%s"""%(sy)
    

    
    

    sozluk = {"z":"a", "v":"b" , "w":"c" ,
              "l":"d", "n":"e" , "i":"f" ,
              "h":"g", "s":"�" , "a":"�" ,
              "g":"h", "f":"i" , "�":"�" ,
              "d":"j", "j":"k" , "k":"l" ,
              "t":"m", "b":"n" , "e":"o" ,
              "m":"�", "j":"p" , "p":"r" ,
              "�":"s", "s":"�" , "c":"t" ,
              "�":"u", "�":"�" , "k":"v" ,
              "o":"y", "r":"z"}

    sifresiz_msg = ""
    for harf in sifreli_msg:
         sifresiz_msg += sozluk.get(harf,harf)

    print sifresiz_msg
    global sifresiz_msg
    
def yaz():
    asg = raw_input("dosya ad� :")
    sg = open(asg,"a")
    sg.write(":%s"%(sifresiz_msg))

decode()
yaz()

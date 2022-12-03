# turkhackteam.org/net
# Coded By Connec

from termcolor import colored
import os

menu = (colored('''
                                               
             (`)..                                    ,.-')
              (',.)-..                            ,.-(..`)         
               (,.' ,.)-..                    ,.-(. `.. )                    
                (,.' ..' .)-..            ,.-( `.. `.. )                     
                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                   ( ,.' ,.'    _== ==_     `.. `.. )                        
                    ( ,.'   _==' ~  ~  `==_    `.. )                     
                     \  _=='   ----..----  `==_   )                     
                  ,.-:    ,----___.  .___----.    -..                        
              ,.-'   (   _--====_  \/  _====--_   )  `-..                 
          ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
      ,.-'.'   .'      (          |  |          )      `.   `.-..  
  ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..      
-'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-     
                            \ . _  __  _ . /                               
                             \ `V-'  `-V' |                                 
                              | \ \ | /  /                                 
                               V \ ~| ~/V                                   
                                |  \  /|                                    
                                 \~ | V                            
                                  \  |                                        
                                   VV
                                        tak30w3r| coded by connec | turkhackteam.org

\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32m\033[1mSubdomain Çekme
\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32m\033[1mTakeover Tespit (subjack)
\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32m\033[1mTakeover Tespit (subzy)
\033[0;31m[\033[0;33mm\033[0;31m]> \033[0;32m\033[1mMenü
''','red'))

print(menu)

try:
    while True:
        islem = input("\033[0;31mtak30w3r>")

        if (islem == "1"):
            site = input("\033[0;31m[\033[0;33m*\033[0;31m]> \033[0;32m\033[1mSite (site.com): ")
            dosya = input("\033[0;31m[\033[0;33m*\033[0;31m]> \033[0;32m\033[1mDosya İsmi: ")

            os.system("subfinder -d {} -o {}".format(site,dosya))
        
        elif (islem == "2"):
            dosya = input("\033[0;31m[\033[0;33m*\033[0;31m]> \033[0;32m\033[1mDosya İsmi: ")

            os.system("subjack -w {} -v --ssl".format(dosya))

        elif (islem == "3"):
            dosya = input("\033[0;31m[\033[0;33m*\033[0;31m]> \033[0;32m\033[1mDosya İsmi: ")

            os.system("subzy --targets {}".format(dosya))
        elif (islem == "m"):
            print(menu)
        else:
            print("\033[0;31m[\033[0;33m!\033[0;31m]> \033[0;32m\033[1mGeçerli Bir İşlem Giriniz!")
except KeyboardInterrupt:
     print("""
Çıkış Yapılıyor...
                """)
     exit()




    


    
   

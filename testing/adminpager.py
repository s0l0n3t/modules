#-*-coding:cp1254-*-
#!/usr/bin/env python
#github.com/s0l0n3t/modules

import httplib
import sys
import socket
import time

print """
        Admin page founder v1.0"""
__Author__ = "s0l0n3t"
__date__ = "07.05.2016"

print "Date:",__date__
print

lib = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

def deneme():
  try:
    var1=0
    var2=0


    site = raw_input("Link :")    
    site = site.replace("http://","")
    print "[!] Checking "+site+ "..."
    print
    sslcon = httplib.HTTPConnection(site)
    sslcon.connect()
    print "[+] Connection succes"
  except(httplib.HTTPResponse):
    raw_input("[!] Server is unavaible ,enter anyone[key]")
    exit()

  analys = raw_input(">[Enter a key] ")
 
  if analys != "exit":
     for i in lib:
         i =i.replace("\n","")
         i = "/" + i
         hosting = site + i
         print "[#]Checking" , hosting + "..."
         sslcon1 = httplib.HTTPConnection(site)
         sslcon1.request("GET",i)
         recv = sslcon1.getresponse()
         var1 = var1 + 1
         if recv.status == 200:
             var2 = var2 + 1
             print "\n[+]Admin page was found %s"%(hosting)
             time.sleep(1)
         elif recv.status == 404:
             var2 = var2

         elif recv.status == 302:
             var2 =var2

         else:
             print "[??]Redirected Error :",recv.status,"%s"%(hosting)

         sslcon1.close()
     print "tamamlandı"
     print var2,":Admin pages"
     print var1,":Agains"

     raw_input("[!!] Testing was finish [anykey]")
  else:
     exit()

    
while True:
  try:
    deneme()
  except(KeyboardInterrupt):
      
      print "\n\n[!!] Returning ..."
      

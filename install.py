#!/bin/python

import os,sys,time

def menu():
        os.system("clear")
        os.system("figlet Update")
        print "\t \033[36;1mTools \033[35;1mBy \033[33;1mReza \033[32;1mAlfauzan\n"
        print("\033[32;1m1. \033[36;1mWajib update ya!!!")
        print("\033[32;1m2. \033[36;1mInfo Script.")
        print("\033[35;1m3. \033[33;1mKeluar\033[31;1m/\033[35;1mexit")
        # input
        pilih = input("\033[35;1m==> \033[36;1mMasukkan \033[32;1mpilihan : ")
        if pilih ==1:
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg update && pkg upgrade")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg install nano")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg install figlet")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg install toilet")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg install ruby")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("gem install lolcat")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pkg install python")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip install requests")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip install mechanize")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip install futures")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip install --upgrade pip")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip2 install requests")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip2 install mechanize")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip2 install futures")
                os.system("clear")
                os.system("figlet Tunggu / Wait")
                os.system("pip2 install --upgrade pip")
                os.system("clear")
                os.system("figlet Sukses!")
                logo = """
                \033[32;1m======================================================
                \033[32;1m=+=>(+) \033[36;1mAuthor : Reza Alfauzan                 \033[32;1m(+)<=+=
                \033[31;1m=+=>(+) \033[36;1mGithub : GRCR4K3R                      \033[34;1m(+)<=+=
                \033[36;1m=+=>(+) \033[32;1mJangan recode bang entar error         \033[36;1m(+)<=+=
                \033[36;1m=+=>(+) \033[36;1mMaaf Ya Gua masih noob:)               (+)<=+=
                ======================================================
                \033[36;1m**********************\033[32;1m*****************\033[36;1m***************"""
                print logo
                
        if pilih ==2:
                os.system("figlet Rzaa Ajaa")
                logo = """
                      \033[32;1m===============================================
                      \033[32;1m= (+) \033[36;1mReza Yang Buat Scriptnya             \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mGithub Gua :GRCR4K3R                 \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mFacebook   :Rzaa Ajaa                \033[32;1m(+)=
                      \033[32;1m= (+) \033[36;1mProfil     :Stiker Pentol Itu gua!!  \033[32;1m(+)=
                      ==============================================="""
                print logo
        if pilih ==3:
                os.system("figlet Update Exit..")
                os.system("figlet Good Byee...")
                time.sleep(5)
menu()

import os
import socket
import time
import webbrowser

def mac():
    os.system("clear")
    print("""
1. Wlan0 
2. Eth0 
0. Geri         
        """)
    select=input("select:")
    if select=="1":
        os.system("clear")
        os.system("macchanger -r wlan0")
        time.sleep(1)
        os.system("clear")
        anapg()

    elif select=="2":
        os.system("clear")
        os.system("macchanger -r eth0")
        print("The MAC address has been changed.")
        time.sleep(1)
        os.system("clear")
        anapg()
    elif select=="0":
        os.system("clear")
        
        
        anapg()
    else:
        os.system("clear")
        print("you typed wrong")
        time.sleep(1)
        os.system("clear")
        mac()


######################################################################


def bilgi():
    print("""
1. Whois Query
2.TheHarvester Scan
3. DNSenum
4. Directory Scan
5. Nmap Tools
0. back""")
    select=input("select:")
    
    
    if select=="1":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"dmitry -winsep {ip}")
        
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif select=="2":
        os.system("clear")
        
        ip=input(str("Enter the URL address of the target site:"))
        os.system(f"theHarvester -d {ip} -l 500 -b all")
        
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif select=="3":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"dnsenum {ip}")
        
        print("0. back ")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif select=="4":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"wafw00f -a {ip}")
        
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            bilgi()
        else :
            os.system("clear")
            bilgi()

    elif select=="5":
        os.system("clear")
        nmap_aktif()



    elif select=="0":
        os.system("clear")
        anapg()
    
    else:
        os.system("clear")
        print("you typed wrong")
        time.sleep(1)
        bilgi()


    
######################################################################

def nmap_aktif():
    os.system("clear")
    print("""
1. TCP SYN Scan
2. UDP scan
3. Service Versions and Operating System Detection
4. Script Scanning
5. Scripts (7 Most Used Scripts)
6. Simple Scan (2-3 minutes
7. Advanced Scan (15 minutes)
0. Back
""")
    tikla=input("select: ")
    if tikla=="1":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -sT {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()
    if tikla=="2":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -sU {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()
    if tikla=="3":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -v -O -sV -T4 {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()

    if tikla=="4":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -sC {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()

    if tikla=="5":
        print("""
http-title

Gets title information from the target web server. It is particularly useful for identifying web applications and determining their versions.

-> nmap --script http-title target.com

ssl-enum-ciphers

Lists the SSL/TLS encryption algorithms supported by the target server. This is useful for detecting security vulnerabilities.

-> nmap --script ssl-enum-ciphers target.com

smb-vuln-ms17-010

Scans target systems for a significant Windows SMB vulnerability named MS17-010 (EternalBlue).

-> map --script smb-vuln-ms17-010 target.com

vulners

Used to detect security vulnerabilities related to CVE (Common Vulnerabilities and Exposures) numbers using the Vulners.com database.

-> nmap --script vulners target.com

ftp-anon

Checks whether anonymous access is allowed on the target FTP server.

-> nmap --script ftp-anon target.com

dns-zone-transfer

Used to attempt a zone transfer from the target DNS server. This is useful for detecting misconfigurations in DNS servers.

-> nmap --script dns-zone-transfer target.com

smtp-enum-users

Used to discover email addresses by listing valid email accounts on the target SMTP server.

-> nmap --script smtp-enum-users target.com

""")
        script=input(str("kulanmak istediginiz script adını yazın: "))
        ip=input(str("Enter the URL address of the target site: "))
        
        os.system(f"nmap --script {script} {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()

    if tikla=="6":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -vvv -sT -T4 -A {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()

    if tikla=="7":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site: "))
        os.system(f"nmap -vvv -sT -T2 -A {ip}")
        print("0. back")
        tikla=input("select: ")

        if tikla=="0":
            os.system("clear")
            nmap_aktif()
        else : 
            os.system("clear")
            nmap_aktif()

    if tikla=="0":
        os.system("clear")
        bilgi()
    else :
        os.system("clear")
        bilgi()




def nmap():
    os.system("clear")
    print("""
1. Learn the Target Site's IP Address
2. Discover Open IP Addresses of the Target Site
3. Learn Open Ports of the Target Site
4. Service Version Scanning of the Target Site
5. UDP Scan
6. Determine OS Fingerprint
7. Spoofing
0. Back 
""")
    select=input("select:")
    if select=="1":
        os.system("clear")
        url=input(str("Enter the URL address of the target site:  "))
        b=socket.gethostbyname(url)
        print(b)
        
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="2":
        os.system("clear")
        ip=input(str("Enter the IP address of the target site: "))
        os.system(f"nmap -sn -n -v --open {ip}/24")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="3":
        os.system("clear")
        ip=input(str("Enter the IP address of the target site: "))
        os.system(f"sudo nmap -Pn -sS -n -v --reason --open {ip}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="4":
        os.system("clear")
        ip=input(str("Enter the IP address of the target site: "))
        os.system(f"sudo nmap -sS -sV -sC -n -v -p 21,53,80,139,445,1001,1900 {ip}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    
    elif select=="5":
        os.system("clear")
        ip=input(str("Enter the IP address of the target site: "))
        os.system(f"nmap -sU -v {ip}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="6":
        os.system("clear")
        ip=input(str("Enter the IP address of the target site: "))
        os.system(f"nmap {ip} -O -n ")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="7":
       
        
        os.system("clear")   
        Spoofed_ip=input("Spoofed_ip")
        Target_IP=input("Target_IP")
        os.system(f"nmap -S {Spoofed_ip} -e eth 0 -sS -sV -v -n -PN {Target_IP}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            nmap()
        else :
            os.system("clear")
            nmap()
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        nmap()

######################################################################   
    
def wppres():
    print("""
1. Change MAC Address
2. Passive and Active Information Gathering
3. Network Scanning
4. WordPress Vulnerability Scan
5. SQL and XSS Vulnerability Scan
6. Vulnerability Detection on Local Machine
7. FTP and SSH Attack
8. Photo Analysis
9. Skipfish Scan
10. Android
11. Create Custom Wordlist
0. Exit
    """)
    select=input("select:")

    if select=="1":
        os.system("clear")
        os.system("wpscan --update")
        os.system("clear")
        wppres()

    if select=="2":
        os.system("clear")
        os.system("wpscan --version")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
        

    if select=="3":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com):"))
        os.system(f" wpscan --url {ip}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if select=="4":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com): "))
        os.system(f" wpscan --url {ip} --enumerate u")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if select=="5":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com):"))
        os.system(f" wpscan --url {ip} --enumerate p")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if select=="6":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com):"))
        os.system(f" wpscan --url {ip} --enumerate ap")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if select=="7":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com):"))
        os.system(f"wpscan --url {ip} –enumerate t ")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
        
    if select=="8":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com):"))
        os.system(f"wpscan --url {ip} –enumerate at ")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()
    if select=="9":
        os.system("clear")
        ip=input(str("Enter the URL address of the target site (www.domainname.com): "))
        kulad=input(str("Enter the username information:"))
        wordlist=input(str("Enter the path of the wordlist:"))
        os.system(f"wpscan --url {ip} –wordlist {wordlist} --username {kulad}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            wppres()
        else :
            os.system("clear")
            wppres()



    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        time.sleep(2)
        nmap()

######################################################################

def sqlxss():
    os.system("clear")
    print("""
1. Web Standard Scan
2. SQL Injection Scan
3. XSS Scan
0. Back""")
    
    select=input("select: ")
    
    if select == "1":
        os.system("clear")
        url=input(str("Enter the URL of the target site"))

        os.system(f"nikto -h {url}")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
            
                
    elif select == "2":
        os.system("clear")
        url=input(str("Enter the URL of the target site"))

        os.system(f"nikto -h {url} -Cgidirs none -Tuning 9")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
                
    elif select =="3":
        os.system("clear")
        url=input(str("Enter the URL of the target site"))

        os.system(f"nikto -h {url} -Cgidirs none -Tuning 4")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            sqlxss()
        else :
            os.system("clear")
            sqlxss()
    
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        time.sleep(2)
        nmap()

######################################################################

def lynis():
    print("""
1. Lynis Version
2. Lynis Commands
3. Lynis System Scan
4. If Lynis is Not Installed
0. Back
    
    """

    )
    
    select=input("select: ")
    if select=="1":
        os.system("clear")
        os.system("lynis show version")
        time.sleep(2)
        lynis()
    elif select=="2":
        os.system("clear")
        os.system("lynis show commands")
        time.sleep(2)

        lynis()
    elif select=="3":
        os.system("clear")
        os.system("lynis audit system")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            lynis()
        else :
            os.system("clear")
            lynis()
        
    elif select=="4":
        os.system("clear")
        os.system("sudo apt install lynis")
        time.sleep(2)

        lynis()
    
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        time.sleep(2)

        lynis()
        

######################################################################

def hydra():
    print("""
1. FTP Attack with Hydra (Brute Force)
2. SSH Attack with Hydra (Brute Force)
0. Back   
    """)
    select=input("select: ")
    if select=="1":
        os.system("clear")
        ftp=input(str("Enter the target FTP address: "))

        os.system(f"""
hydra -l admin -p password ftp://{ftp}
hydra -L /usr/share/wordlists/rockyou.txt.gz -P /usr/share/wordlists/rockyou.txt.gz ftp://{ftp}""")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            hydra()
        else :
            os.system("clear")
            hydra()
        
    elif select=="2":
        os.system("clear")
        ssh=input(str("Enter the target SSH address: "))
        os.system(f"""hydra -l admin -p password {ssh} -t 4 ssh
hydra -L /usr/share/wordlists/rockyou.txt.gz -P /usr/share/wordlists/rockyou.txt.gz {ssh} -t 4 ssh""")
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            hydra()
        else :
            os.system("clear")
            hydra()
    
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        time.sleep(2)

        hydra()
######################################################################

def exiftool():
    print("""
1. Scan Photo
0. Back  
""")   
    select=input("select: ")
    if select=="1":
        os.system("clear")
        yol=input(str("Enter the path of the photo or you can drag and drop it: "))
        os.system(f"exiftool {yol}")
        
        print("0. back")
        tikla=input("select: ")
        if tikla=="0":
            os.system("clear")
            exiftool()
        else :
            os.system("clear")
            exiftool()
    
    
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        
        time.sleep(2)
        exiftool()
######################################################################
def skipfish():
    print(""""
1. Simple Scan
2. Medium Scale Scan
3. Deep Scan
0. Back """)
    select=input("select: ")
    
    if select=="1":
        os.system("clear")
        url=input(str("Enter the URL of the target site"))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 2 {url}")
        os.system(f"open {sinifla}/index.html")       
        os.system("clear")
        skipfish()
        
        
    elif select=="2":
        
        os.system("clear")
        url=input(str("Enter the URL of the target site"))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 8 {url}")
        os.system(f"open {sinifla}/index.html")
        os.system("clear")
        skipfish()
    
    elif select=="3":
        
        os.system("clear")
        url=input(str("Enter the URL of the target site"))
        sinifla=url.split("/")
        sinifla=str(sinifla[2])
        os.system(f"rm -r {sinifla}")
        os.system(f"skipfish -o {sinifla} -d 16 {url}")
        os.system(f"open {sinifla}/index.html")
        os.system("clear")
        skipfish()
    
    
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        
        time.sleep(2)
        skipfish()
#####################################################################

def apktool():
    print("""
1. Install Apk Tool
2. Decompile Apk File
0. Back""")
    select=input("select: ")
    if select=="1":
        os.system("clear")
        os.system("sudo apt install apktool")
        os.system("clear")
        apktool()
    elif select=="2":
        os.system("clear")
        print("It is found in the apk file, you should move it to your religion.")
        ad=input("Enter the name of the apk file (e.g., test.apk):")
        
        os.system(f"apktool d -f -r {ad}")        
        apktool()
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        
        time.sleep(2)
        apktool()

#####################################################################
def cupp():
    print("""
1. Install Wordlist Generation Tool
2. Create Wordlist
0. Back """)
    select=input("select: ")
    if select=="1":
        os.system("clear")
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("The tool has been installed.")
        time.sleep(2)
        os.system("clear")
        cupp()
    elif select=="2":
        os.system("clear")
        
        os.system("python3 ./cupp/cupp.py -i")
        os.system("clear")
        cupp()
    elif select=="0":
        os.system("clear")
        anapg()


    else:
        print("incorrect repetition error when typing incorrectly")
        
        time.sleep(2)
        cupp()

   
######################################################################
def anapg():
    
    print("""
1. Change MAC Address
2. Passive and Active Information Gathering
3. Network Scanning
4. WordPress Vulnerability Scan
5. SQL and XSS Vulnerability Scan
6. Vulnerability Detection on Local Machine
7. FTP and SSH Attack
8. Photo Analysis
9. Skipfish Scan
10. Android
11. Create Custom Wordlist
0. Exit""")

    islem=input("select:")
    
    if islem=="1":
        os.system("clear")
        mac()
    elif islem=="2":
        os.system("clear")
        bilgi()
    elif islem=="3":
        os.system("clear")
        nmap()
    elif islem=="4":
        os.system("clear")
        wppres()
    elif islem=="5":
        os.system("clear")
        sqlxss()
    elif islem=="6":
        os.system("clear")
        lynis()
    elif islem=="7":
        os.system("clear")
        hydra()
    elif islem=="8":
        os.system("clear")
        exiftool()
    elif islem=="9":
        os.system("clear")
        skipfish()
    elif islem=="10":
        os.system("clear")
        apktool()
    elif islem=="11":
        os.system("clear")
        cupp()
    elif islem=="0":
        os.system("clear")
        exit()
    else:
        os.system("clear")
        print("you wrote wrong")
        time.sleep(1)
        os.system("clear")
        anapg()
        


anapg()
        


   
    


    

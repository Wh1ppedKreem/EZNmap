import os

print("""

╭━━━┳━━━━╮╭━╮╱╭┳━╮╭━┳━━━┳━━━╮
┃╭━━┻━━╮━┃┃┃╰╮┃┃┃╰╯┃┃╭━╮┃╭━╮┃
┃╰━━╮╱╭╯╭╯┃╭╮╰╯┃╭╮╭╮┃┃╱┃┃╰━╯┃
┃╭━━╯╭╯╭╯╱┃┃╰╮┃┃┃┃┃┃┃╰━╯┃╭━━╯
┃╰━━┳╯━╰━╮┃┃╱┃┃┃┃┃┃┃┃╭━╮┃┃
╰━━━┻━━━━╯╰╯╱╰━┻╯╰╯╰┻╯╱╰┻╯
=============================================
!DISCLAIMER! YOU NEED TO HAVE NMAP INSTALLED
=============================================
MADE BY KAREEM 0_0
=============================================
""")

print("Select what type of scan you want to perform: ")

print("(1) Stealth Scan (may take longer than light)")
print("(2) Light Scan")
print("(3) Moderate Scan")
print("(4) Intense Scan")
print("(5) Super Scan")

choice = int(input("Enter a choice (1-5) >>> "))

while True:
    if choice == 1:
        ip_address = input("Enter the IP address you would like to scan >>> ")
        os.system(f"sudo nmap -T0 {ip_address}")
    elif choice == 2:
        ip_address = input("Enter the IP address you would like to scan >>> ")
        os.system(f"sudo nmap -T3 {ip_address}")
    elif choice == 3:
        ip_address = input("Enter the IP address you would like to scan >>> ")
        os.system(f"sudo nmap -sC -sV -O {ip_address}")
    elif choice == 4:
        ip_address = input("Enter the IP address you would like to scan >>> ")
        os.system(f"sudo nmap -sC -sV -O --script vuln {ip_address}")
    elif choice == 5:
        ip_address = input("Enter the IP address you would like to scan >>> ")
        verbosity_level = input("Select verbosity level (how much info you want to show) (1/2/3) >>> ")
        if verbosity_level == 1:
            os.system(f"sudo nmap -sC -sV -O --script vuln -T5 -v {ip_address}")
        elif verbosity_level == 2:
            os.system(f"sudo nmap -sC -sV -O --script vuln -T5 -vv {ip_address}")
        else:
            os.system(f"sudo nmap -sC -sV -O --script vuln -T5 -vvv {ip_address}")

    else:
        break
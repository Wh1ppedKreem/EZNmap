import os
import re
import subprocess

# This class contains the colour codes for text in the linux terminal.
class tc:  #tc stands for terminal colours
    BLACK = "\u001b[30m" 
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"

SPLASH = f"""\
{tc.MAGENTA}
╭━━━┳━━━━╮╭━╮╱╭┳━╮╭━┳━━━┳━━━╮
┃╭━━┻━━╮━┃┃┃╰╮┃┃┃╰╯┃┃╭━╮┃╭━╮┃
┃╰━━╮╱╭╯╭╯┃╭╮╰╯┃╭╮╭╮┃┃╱┃┃╰━╯┃
┃╭━━╯╭╯╭╯╱┃┃╰╮┃┃┃┃┃┃┃╰━╯┃╭━━╯
┃╰━━┳╯━╰━╮┃┃╱┃┃┃┃┃┃┃┃╭━╮┃┃
╰━━━┻━━━━╯╰╯╱╰━┻╯╰╯╰┻╯╱╰┻╯{tc.RED}
=============================================
!DISCLAIMER! {tc.YELLOW}YOU NEED TO HAVE NMAP INSTALLED!{tc.RESET}{tc.RED}
============================================={tc.CYAN}
=============================================
[MADE BY {tc.GREEN}KAREEM BALABLE{tc.RESET}{tc.CYAN}]     |\/\/\|
[{tc.GREEN}Wh1ppedKreem{tc.RESET} {tc.CYAN}on {tc.BLUE}Github]{tc.RESET}  {tc.CYAN}¯\_( ͡❛ ͜ʖ ͡❛)_/¯
============================================={tc.RESET}
"""

OPTIONS = f"""
Select what type of scan you want to perform:
{tc.GREEN}[1] Stealth Scan (may take longer than light)
{tc.YELLOW}[2] Light Scan
{tc.CYAN}[3] Moderate Scan
{tc.BLUE}[4] Intense Scan
{tc.MAGENTA}[5] Super Scan
{tc.RED}[6] Quit
{tc.RED}[7] Help{tc.RESET}
"""

# This variable contains the regular expression pattern for an IP address.
ip_regex_pattern = (r"^(\d{1,3}\.){3}\d{1,3}$")

# This function checks if the IP address given is valid, 
# using a regular expression pattern.
def is_ip_address(ip_address):
    return bool(re.match(ip_regex_pattern, ip_address))

# This function returns a valid option from the user.
def get_user_choice(is_valid_option, prompt, invalid_message=None):
    option = input(prompt).strip()
    while not is_valid_option(option):
        if invalid_message is None:
            print(f"Invalid option: {option}")
        else:
            print(invalid_message.format(option=option))
        option = input(prompt).strip()
    return option

print(SPLASH, OPTIONS)
# Main Function.
def main():
    while True:
        choice = int(input("Enter a choice (1-7) >>> "))
        
        # Checks if the user entered a valid choice.
        if choice > 7 or choice == '':
            print(f"{tc.RED}Invalid choice, try again")
            return main()
        
        if choice == 7:
            print(f"""
            {tc.GREEN}Stealth Scan{tc.RESET} utilises the -T0 switch in nmap to make your  
            scan almost undetectable however it is slow and and may not return 
            much information compared to the next commands.

            {tc.YELLOW}Light Scan{tc.RESET} utilises the -T3 switch which is the default 
            switch in nmap and this command will output the open ports on the IP address scanned + 
            what type of ports they are.

            {tc.CYAN}Moderate Scan{tc.RESET} utilises the -sC -sV -O switches to show the the operating 
            system and service on each open port and uses the default scripts in nmap (which are safe) 
            to give you more information.

            {tc.BLUE}Intense Scan{tc.RESET} is similar to moderate scan but also adds the utilisation of 
            vulnerability-scanning scripts to show you potential vulnerabilities of the services on each 
            open port by giving you links to websites and CVEs corresponding to the vulnerable service.

            {tc.MAGENTA}Super Scan{tc.RESET} is like Intense Scan howver you get the added option of 
            selecting a verbosity option to decide how much information you want to show e.g. verbosity 
            3 will show you much more information than Intense Scan whereas verbosity 1 will show you 
            a little more information than Intense Scan and verbosity 2 in-between verbosity 1 & 2.
            """)
        
        # Quit
        if choice == 6:
            print("Quitting...")
            quit()
        ip_address = get_user_choice(
            is_ip_address,
            f"{tc.GREEN}Enter the IP address you would like to scan >>> {tc.RESET}",
            f"{tc.RED}Invalid IP address, try again{tc.RESET}"
        )
        if choice == 1:
            # Stealth Scan
            os.system(f"sudo nmap -T0 {ip_address}")
        elif choice == 2:
            # Light Scan
            os.system(f"sudo nmap -T3 {ip_address}")
        elif choice == 3:
            # Moderate Scan
            os.system(f"sudo nmap -sC -sV -O {ip_address}")
        elif choice == 4:
            # Intense Scan
            os.system(f"sudo nmap -sC -sV -O --script vuln {ip_address}")
        elif choice == 5:
            # Super Scan
            verbosity_level = int(input(f"{tc.MAGENTA}Select verbosity level (how much info you want to show) (1/2/3) >>> {tc.RESET}"))
            verbosity_arg = f"-{'v'*verbosity_level}"
            os.system(f"sudo nmap -sC -sV -O --script vuln {verbosity_arg} {ip_address}")
        else:
            # Returns to the beginning of the main function when complete.
            return main()

if __name__ == "__main__":
    main()

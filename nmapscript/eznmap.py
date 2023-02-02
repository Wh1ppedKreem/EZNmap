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
{tc.RESET}
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
        choice = int(input("Enter a choice (1-6) >>> "))
        
        # Checks if the user entered a valid choice.
        if choice > 6 or choice == '':
            print(f"{tc.RED}Invalid choice, try again")
            return main()
        
        # Quit
        if choice == 6:
            print("Quitting...")
            quit()
        ip_address = get_user_choice(
            is_ip_address,
            f"{tc.GREEN}Enter the IP address you would like to scan >>> ",
            f"{tc.RED}Invalid IP address, try again"
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
            verbosity_level = input("Select verbosity level (how much info you want to show) (1/2/3) >>> ")
            verbosity_arg = f"-{'v'*verbosity_level}"
            os.system(f"sudo nmap -sC -sV -O --script vuln {verbosity_arg}", ip_address)
        else:
            # Returns to the beginning of the main function when complete.
            return main()

if __name__ == "__main__":
    main()

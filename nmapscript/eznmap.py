import os
import re
import subprocess

SPLASH = """\
╭━━━┳━━━━╮╭━╮╱╭┳━╮╭━┳━━━┳━━━╮
┃╭━━┻━━╮━┃┃┃╰╮┃┃┃╰╯┃┃╭━╮┃╭━╮┃
┃╰━━╮╱╭╯╭╯┃╭╮╰╯┃╭╮╭╮┃┃╱┃┃╰━╯┃
┃╭━━╯╭╯╭╯╱┃┃╰╮┃┃┃┃┃┃┃╰━╯┃╭━━╯
┃╰━━┳╯━╰━╮┃┃╱┃┃┃┃┃┃┃┃╭━╮┃┃
╰━━━┻━━━━╯╰╯╱╰━┻╯╰╯╰┻╯╱╰┻╯
=============================================
!DISCLAIMER! YOU NEED TO HAVE NMAP INSTALLED
=============================================
MADE BY KAREEM
[Wh1ppedKreem on Github]
=============================================
"""

OPTIONS = """
Select what type of scan you want to perform:
[1] Stealth Scan (may take longer than light)
[2] Light Scan
[3] Moderate Scan
[4] Intense Scan
[5] Super Scan
[6] Quit
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
            print("Invalid choice, try again")
            return main()
        ip_address = get_user_choice(
            is_ip_address,
            "Enter the IP address you would like to scan >>> ",
            "Invalid IP address, try again"
        )
        if choice == 6:
            print("Quitting...")
            quit()
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

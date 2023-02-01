import re
import subprocess

# For
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
MADE BY KAREEM 0_0
=============================================
"""

OPTIONS = """\
Select what type of scan you want to perform:
(1) Stealth Scan (may take longer than light)
(2) Light Scan
(3) Moderate Scan
(4) Intense Scan
(5) Super Scan
(6) Exit
"""

ip_regex_pattern = (r"^(\d{1,3}\.){3}\d{1,3}$")

def is_ip_address(text):
    """Determines if text is a valid IP address.
    
    This uses something called a regular expression to check if the text is a 
    valid IP address. Regular expressions are a powerful tool for matching
    strings. Regular expressions can be a bit complicated, but they're very
    useful, and used throughout computing (not just Python). For example,
    the `grep` command uses regular expressions to match lines in files.
    
    https://en.wikipedia.org/wiki/Regular_expression
    
    To mess around with regular expressions, you can use this website - it 
    has a really nice playground + cheatsheet:
    https://regexr.com/

    Args:
        text (string): The text to check.
        
    Returns:
        bool: True if text is a valid IP address, False otherwise.
    """
    # re.match() checks if the text matches the regular expression.
    # The regular expression is r"^(?:\d{1,3}\.){3}\d{1,3}$"
    # This means:
    #   - ^ matches the start of the string
    #   - (\d{1,3}\.){3} matches 3 groups of 1-3 digits (\d means digits) 
    #     followed by a period
    #   - \d{1,3} matches 1-3 digits
    #   - $ matches the end of the string
    # The parentheses around (\d{1,3}\.) are used to group the expression.
    return bool(re.match(ip_regex_pattern, text))


def get_user_choice(is_valid_option, prompt, invalid_message=None):
    """Returns a valid option from the user.
    
    is_valid_option (function): Function that takes a string and returns True 
        if it is a valid option.
    prompt (string): The prompt to display to the user.
    invalid_message (string): The message to display if the user enters an
        invalid option. This can be a format string that takes a single
        keyword argument "option" which is the user's input.
        Default: "Invalid option: {option}"

    Returns:
        string: The user's choice.
    """
    # str.strip() strips leading / trailing whitespace. e.g "  1 " -> "1"
    option = input(prompt).strip()
    while not is_valid_option(option):
        if invalid_message is None:
            print(f"Invalid option: {option}")
        else:
            print(invalid_message.format(option=option))
        option = input(prompt).strip()
    return option

def main():
    print(SPLASH, OPTIONS)
    while True:
        # Lambda functions allow you to define a function inline (within an expression,
        # on one line).
        # The format of a lambda function is:
        # lambda <arguments>: <expression>
        # The expression is evaluated and the result is returned.
        #
        # For example:
        #   f = lambda x: x + 1
        #   f(1) == 2 -> True
        #
        # This would be equivalent to:
        #   def f(x):
        #       return x + 1
        #   f(1) == 2 -> True
        check_valid_choice = lambda choice: choice.isdigit() and 1 <= int(choice) <= 6

        choice = int(get_user_choice(check_valid_choice, "Enter a choice (1-6) >>> "))
        command = ["sudo", "nmap"]
        if choice == 6:
            print("Exiting...")
            break

        ip_address = get_user_choice(
            is_ip_address,
            "Enter the IP address you would like to scan >>> ",
            "Invalid IP address: {option}"
        )    
        if choice == 1:
            command += ["-T0", ip_address]
        elif choice == 2:
            command += ["-T3", ip_address]
        elif choice == 3:
            command += ["-sC", "-sV", "-O", ip_address]
        elif choice == 4:
            command += ["-sC", "-sV", "-O", "--script", "vuln", ip_address]
        elif choice == 5:
            verbosity_level = input(
                "Select verbosity level (how much info you want to show) (1/2/3) >>> "
            )
            verbosity_level = max(3, verbosity_level)
            verbosity_argument = f"-{'v'*verbosity_level}"
            command += [
                "-sC","-sV","-O","--script","vuln","-T5", verbosity_argument, ip_address
            ]
        
        # Example: "-".join(["a", "b", "c"]) -> "a-b-c"
        print("Running command: ", " ".join(command))
        return_code = subprocess.call(command)
        # In linux, all commands return a return code. A return code of 0 means
        # that the command ran successfully. Non-zero return codes often mean
        # that the command failed.
        # subprocess.call() returns the return code of the command.
        print(f"Command finished with return code {return_code}.\n")


# __name__ is a special variable that is set to the name of the current module.
# When a module is run directly, __name__ is set to "__main__".
# When a module is imported, __name__ is set to the name of the module:
# 
# >>> sys.__name__
# 'sys'
# 
# It's good practice to use the  `if __name__ == "__main__":` to run any code
# that's only meant to be run when the module is run directly, as it means that 
# if we choose to import this module in another script (for example, if we want 
# to use the is_ip_address function somewhere else), then this code won't run.
# 
# It's convention to put all of your code inside a function called main(), and
# then call main() within this if statement.
if __name__ == "__main__":
    main()
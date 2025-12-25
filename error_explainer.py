#!/usr/bin/env python3
import sys
import re

ERROR_DB = {
    # dumbo dpkg errors
    r"Could not get lock /var/lib/dpkg/lock": 
        "🔒 APT LOCK ERROR: Another process is using the package manager.\n"
        "   -> EXPLANATION: You are probably running an update in the background.\n"
        "   -> SOLUTION: Wait 5 minutes. If it persists, reboot. DO NOT forcibly remove lock files unless necessary.",
    
    r"dpkg: error processing package": 
        "📦 BROKEN PACKAGE: A package installation failed halfway.\n"
        "   -> SOLUTION: Run 'sudo dpkg --configure -a' to fix the broken install.",
    
    r"Unable to locate package": 
        "❓ UNKNOWN PACKAGE: Apt cannot find the software you are trying to install.\n"
        "   -> SOLUTION: Check the spelling. You might also need to add a repository (PPA) or run 'sudo apt update'.",

    # permission errors [use sudo hehehe]
    r"Permission denied": 
        "🚫 ACCESS DENIED: You do not have permission to touch this file.\n"
        "   -> SOLUTION: Add 'sudo' before your command to run as administrator.\n"
        "   -> ALTERNATIVE: Check file ownership with 'ls -l' and fix with 'chown'.",
    
    r"No space left on device": 
        "💾 DISK FULL: Your hard drive has 0 bytes remaining.\n"
        "   -> EXPLANATION: Services like MySQL or Docker will crash immediately.\n"
        "   -> SOLUTION: Check usage with 'df -h'. Clear /var/log or old backups.",

    # systemd errors[COMMON IDK WHY]
    r"Job for (.+) failed because the control process exited with error code": 
        "⚙️ SERVICE CRASH: A background service (like nginx or mysql) failed to start.\n"
        "   -> SOLUTION: Run 'journalctl -xe' or 'systemctl status <service_name>' to see the actual error log.",

    # network errors [ALSO too common lmao]
    r"Connection refused": 
        "🔌 CONNECTION REFUSED: The target server is active, but not listening on that port.\n"
        "   -> EXPLANATION: The service might be down, or a firewall (UFW) is blocking it.\n"
        "   -> SOLUTION: Check if the service is running ('systemctl status'). Check firewall ('sudo ufw status').",
    
    r"Temporary failure in name resolution": 
        "🌐 DNS ERROR: Your server cannot translate domain names to IPs.\n"
        "   -> SOLUTION: Check your internet connection. Edit /etc/resolv.conf and add 'nameserver 8.8.8.8'.",

    # php [mid language]
    r"Allowed memory size of (\d+) bytes exhausted": 
        "🧠 PHP OOM (Out Of Memory): A script tried to eat too much RAM.\n"
        "   -> SOLUTION: Edit 'php.ini' (usually in /etc/php/7.x/fpm/php.ini) and increase 'memory_limit'. Restart PHP-FPM.",
    
    r"syntax error, unexpected": 
        "📝 PHP SYNTAX ERROR: You missed a semicolon ';' or a bracket '}' in your code.\n"
        "   -> SOLUTION: The error message usually tells you the exact line number. Go fix the typo.",

   # ptero [best panel]
    r"bind: address already in use": 
        "🚧 PORT CONFLICT: The server cannot start because the port is taken.\n"
        "   -> SOLUTION: You are likely running two servers on the same port. Kill the old one or change the port in config.",
    
    r"context deadline exceeded": 
        "⏱️ WINGS TIMEOUT: The daemon (Wings) couldn't finish the task in time.\n"
        "   -> SOLUTION: Common when transferring large servers. Check your network speed or disk I/O.",
    
    r"x509: certificate has expired":
        "📜 SSL EXPIRED: Your security certificate is dead.\n"
        "   -> SOLUTION: Run 'certbot renew' or restart your webserver if you auto-renewed but didn't reload.",
}

def explain_error(error_text):
    print("\n🔎 ANALYZING ERROR SIGNATURE...\n")
    found_count = 0
    
    for pattern, explanation in ERROR_DB.items():
        if re.search(pattern, error_text, re.IGNORECASE):
            print(f"Match #{found_count+1}:")
            print(explanation)
            print("-" * 50)
            found_count += 1
            
    if found_count == 0:
        print("🤷 UNKNOWN ERROR.")
        print("   LMAFAO, UR ERROR SO CURSED, I couldn't match this text to my database.")
        print("   TIP: Make sure you pasted the English error message. [obv]")

def main():
    if len(sys.argv) > 1:
        
        user_input = " ".join(sys.argv[1:])
        explain_error(user_input)
    else:
        
        print("========================================")
        print("   UBUNTU ERROR IDENTIFIER (er-iden)    ")
        print("========================================")
        print("Paste your error below and hit ENTER:")
        try:
            user_input = input(">> ")
            if user_input.strip():
                explain_error(user_input)
            else:
                print("Exiting: No input provided.")
        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()

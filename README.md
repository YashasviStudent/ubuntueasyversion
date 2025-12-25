# Ubuntu/Linux Error Identifier (er-iden)

### Tired of cryptic Linux errors?
Ever used Ubuntu Server and got hit with `Could not get lock /var/lib/dpkg/lock` or `bind: address already in use` and had no idea what to do?

**er-iden** (Error Identifier) simplifies complex terminal errors into plain English without needing to search the internet. It works entirely offline!

Compatible with:
* **Ubuntu System Errors** (APT, Permissions, Systemd)
* **Pterodactyl Panel & Wings**
* **PHP Configuration Errors**
* ...and more added frequently.

---

## 📥 Installation

1.  Download the repository.
2.  Run the installation script:
    ```bash
    sudo bash install.sh
    ```
    *(This will install Python3 if you don't have it, and set up the global commands.)*

---

## 🚀 Usage

You can use the tool in two ways:

### 1. The Short Command (Recommended)
Use the `ei` alias to quickly identify an error.

**Interactive Mode:**
Type `ei`, press enter, then paste your error.
```bash
user@server:~$ ei
>> Permission denied 

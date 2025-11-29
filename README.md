<h2 style="text-align:center;">🔑 KeyDock </h2>
## Local Highly Secure Password Manager

## 🌟 Overview
KeyDock is a highly secure, **local-only** password manager designed to give the user absolute control and protection over their stored credentials. Unlike cloud-based solutions, KeyDock keeps all encrypted data and keys on your local machine, ensuring that a breach only affects your device.

The core principle of KeyDock is simple: **Your Master Password is the single, non-recoverable key to all your data.**

## 💡 Motivation
The digital world demands strong, unique passwords for every service, yet managing them securely remains a challenge. KeyDock was created with the following motivations:

* **Maximum Security Through Local Control:** To eliminate the inherent security risks associated with cloud storage and third-party servers. All encryption and decryption happen locally.
* **Zero-Knowledge Principle:** The system itself cannot recover your Master Password. We never store the master key, only a **cryptographic hash** of it for verification.
* **Simplicity and Reliability:** Using battle-tested, standard Python libraries (`cryptography`'s Fernet and `hashlib`) to ensure the security mechanisms are transparent and robust.

---

## 🔒 Security Architecture
KeyDock employs a multi-layered security approach:

1.  **Master Password Setup:** You set a **Master Password**. by running the `setup_password.py`. This has to be done only once.
    ‼**IMPORTANT NOTE**‼--> All passwords set by your intial master password cannot be accessed if you change your master password. So set up accordingly.
    
2.  **Verification Hash Storage:** A **cryptographic hash** (e.g., using SHA-256) of your Master Password is stored in a local configuration file. This is used *only* for verifying your login attempts and **cannot** be used to reverse-engineer the original password.
   
3.  **Encryption Key Generation:** The **base64 string** of your Master Password is directly used as the **encryption key** (or derived into a Fernet key) to encrypt all your stored credentials. The main takeaway is that, this key is 
generated only on memory and hance cannot be accessed by other people in any way, unless they have a keylogger installed on your computer.
    
4.  **Data Protection:** All other passwords, usernames, and associated metadata are stored in an encrypted vault file.
   
5.  **Access:** To access your vault, you must provide the Master Password.
    * It is first hashed and checked against the stored verification hash.
    * If correct, the Master Password is then used as the key to decrypt the entire vault.

> **⚠️ Critical Security Note:** If you forget your Master Password, **all your stored passwords are lost forever.** This is the core trade-off for this high level of security and local control. There is no "forgot password" feature or backdoor.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **`cryptography` Library** | Provides the **Fernet** symmetric encryption scheme for the vault. |
| **Fernet** | Ensures the data is encrypted using **AES-128** in CBC mode with HMAC for authentication, guaranteeing both **confidentiality** and **integrity**. |
| **`hashlib` Library** | Used to generate the **cryptographic hash** of the Master Password for secure verification. |
| **Python** | The primary language of development. |

---

## 🚀 How to Use KeyDock

### Daily Usage
1.  Easiest way is to add the program to your system Path, which you can then call by your file name:
   ```bash
   keydock
   ```
   We are working on the cross-platform binary, which will be released shortly.

---

## 📈 Future Improvements and Contributions
KeyDock is a project with significant potential for growth. Contributions are highly welcome!

### Core Security & Feature Enhancements
* **Key Derivation Function (KDF):** Implement a robust KDF like **PBKDF2** or **Argon2** to transform the Master Password into the final encryption key. This adds a computational delay (salting and stretching) to the key generation process, making brute-force attacks significantly more expensive, even if the hash is somehow compromised.
    
* **Two-Factor Authentication (2FA):** Explore adding a secondary, local 2FA mechanism (e.g., a time-based code stored securely *outside* the main vault).
* **Platform Compatibility:** Package the application using tools like PyInstaller or similar, to create standalone executables for Windows, macOS, and Linux.

---

## 🤝 Contributing
Feel free to open an issue for bug reports or feature suggestions. If you'd like to contribute code:
---

## 📜 License
This project is licensed under the MIT License.

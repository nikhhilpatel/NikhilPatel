# Active Directory User Onboarding Automation

This PowerShell script automates the creation of a new user in Active Directory. It streamlines the onboarding process by creating the user account, setting a secure initial password, enabling the account, and adding the user to multiple security groups.

## Features

- Creates a new Active Directory user with customizable inputs
- Sets initial password and enforces password change at next login
- Adds the user to specified AD groups
- Provides a clean and reusable structure for IT onboarding tasks

## Technologies Used

- PowerShell
- Active Directory Module for Windows PowerShell

## Prerequisites

- Windows Server or Windows with RSAT tools installed
- PowerShell running as Administrator
- Domain admin privileges (for AD user creation and group modification)

## How to Use

1. Open the script in PowerShell ISE or VS Code.
2. Customize the input variables at the top of the script:
   - `$FirstName`, `$LastName`, `$Groups`, etc.
3. Run the script as an administrator on a domain-joined machine.

## Author

**Nikhil Patel**  
[LinkedIn](https://www.linkedin.com/in/nikhhilpatel/) | patel.npwork@gmail.com
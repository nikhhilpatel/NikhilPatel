# Cisco AnyConnect VPN Profile Deployment Script

This PowerShell script deploys a pre-configured Cisco AnyConnect VPN profile (XML file) to a user's system. It's designed to simplify the process of rolling out secure remote access across a fleet of machines.

## Features

- Automatically creates the required VPN profile directory if it doesn't exist
- Copies the custom VPN profile XML file to the appropriate location
- Ensures users have a consistent VPN setup

## Technologies Used

- PowerShell
- Cisco AnyConnect Secure Mobility Client

## Prerequisites

- Cisco AnyConnect must be installed on the user’s system
- Profile XML file must be prepared and located in the `/Profiles/` directory
- Script should be run with Administrator privileges

## How to Use

1. Place your `.xml` VPN profile in the `Profiles` folder.
2. Run this script as an administrator on the target machine.
3. Verify the VPN profile appears in the AnyConnect client.

## Author

**Nikhil Patel**  
[LinkedIn](https://www.linkedin.com/in/nikhhilpatel/) | patel.npwork@gmail.com
<#
.SYNOPSIS
Deploys a pre-configured Cisco AnyConnect VPN profile to user machines.

.DESCRIPTION
Copies the Cisco AnyConnect XML profile file to the correct directory on user machines and sets basic configurations.

.NOTES
Author: Nikhil Patel
#>

# Define VPN profile path
$ProfileSource = ".\Profiles\vpn_profile.xml"
$ProfileDestination = "C:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\Profile"

# Create directory if it doesn't exist
if (!(Test-Path -Path $ProfileDestination)) {
    New-Item -Path $ProfileDestination -ItemType Directory
}

# Copy VPN profile
Copy-Item -Path $ProfileSource -Destination $ProfileDestination -Force

Write-Host "VPN profile has been deployed successfully."

# Optional: Set VPN as default connection
# You could modify the XML file prior to copying to ensure desired settings are enforced
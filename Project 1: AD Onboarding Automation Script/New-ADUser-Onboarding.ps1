<#
.SYNOPSIS
Automates the onboarding of new Active Directory users.

.DESCRIPTION
Creates a new user in Active Directory, adds them to groups, sets an initial password, and enables the account.

.NOTES
Author: Nikhil Patel
#>

# Input Variables (In real-world use, import from a CSV)
$FirstName = "Nikhil"
$LastName = "Patel"
$Username = "$FirstName.$LastName"
$OU = "OU=Employees,DC=example,DC=com"
$Groups = @("IT_Users", "VPN_Users")
$InitialPassword = "P@ssword123"

# Create New AD User
New-ADUser `
    -Name "$FirstName $LastName" `
    -GivenName $FirstName `
    -Surname $LastName `
    -SamAccountName $Username `
    -UserPrincipalName "$Username@example.com" `
    -AccountPassword (ConvertTo-SecureString $InitialPassword -AsPlainText -Force) `
    -Path $OU `
    -Enabled $true `
    -ChangePasswordAtLogon $true

# Add to groups
foreach ($Group in $Groups) {
    Add-ADGroupMember -Identity $Group -Members $Username
}

Write-Host "User $Username has been created and added to groups."
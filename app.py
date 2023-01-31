
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"    
}

print(monthConversions["Mar"])

# get function return a default answer in case the key is not found in dictionary
print(monthConversions.get("Lol", "Not a valid key"))

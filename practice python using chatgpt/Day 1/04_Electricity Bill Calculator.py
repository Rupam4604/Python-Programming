# Electricity Bill Calculator

# Write a Python program that asks:

# Enter electricity units consumed:

# Calculate the bill according to these slabs:

# Units	Rate
# 0–100	₹5/unit
# 101–200	₹7/unit
# Above 200	₹10/unit
# Example 1
# Enter electricity units consumed: 80

# Electricity Bill: ₹400
# Example 2
# Enter electricity units consumed: 150

# Electricity Bill: ₹850

# For 150 units:

# First 100 × ₹5 = ₹500
# Remaining 50 × ₹7 = ₹350
# Total = ₹850
# Example 3
# Enter electricity units consumed: 250

# Electricity Bill: ₹1300

unit_consumed = int(input("Enter the total unit consumed: "))

if unit_consumed <= 100:
    total = unit_consumed * 5
elif 101<= unit_consumed <= 200:
    total = (100 * 5) + ((unit_consumed-100) * 7) 
else:
    total = (100 * 5) + (100 * 7) + ((unit_consumed - 200) * 10)

print(f"Total unit consumed: {unit_consumed}\nElectricity Bill: {total}")

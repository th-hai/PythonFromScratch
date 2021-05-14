my_name = 'Hai'
my_age = 22 # not a lie
my_height = 70 # inches
my_height_in_centimeters = my_height * 2.54
my_weight = 138 # pounds
my_weight_in_kilograms = my_weight * 0.45359237
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"That equal to {my_height_in_centimeters} centimeter tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"That equal to {my_weight_in_kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
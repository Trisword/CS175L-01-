##CS175L
##AzeezOlapade
##restaurant

vegetarian = False
vegan = False
gluten_free = False

print("Is anyone in your party a vegetarian?")
response = input()
if response.lower() == 'yes':
    vegetarian = True

print("Is anyone in your party a vegan?")
response = input()
if response.lower() == 'yes':
    vegan = True
    
print("Is anyone in your party gluten-free?")
response = input()
if response.lower () == 'yes':
    gluten_free = True

print("Here are your restaurant choices:")

if not vegetarian and not vegan and not gluten_free:
    print(" Joe's Gourmet Burgers")
if not vegan and not gluten_free:
    print(" Mama's Fine Italian")
if not vegan:
    print(" Main Street Pizza Comapany")

print(" Corner Cafe")
print(" Chef's Kitchen")

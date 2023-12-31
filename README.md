# simplecc
simple calorie counter

to run:
```
python simplecc.py myfood myquantity myunitofmeasurement
```
# Adding data
add the data to fooditems.py

# Note for nonlinux users
I did not test it for other environments

# Configuration 
## Food Dictionary

At the top you can define constants for units of measurement, for example OZ, G etc. 

At the bottom, you have the dictionary. Each line follows this format:
"food item name":(measurement,calories)

### Make sure the food item name is lower case. Case insensivity will be coming eventually.

## Location
```
~/.config/simplecc/fooditems.py
```

# Daily logs
```
~/.simplecc/
```

# Removing items
Use your favorite text editor to edit the files in ~/.simplecc directly.

# Download
```
curl https://raw.githubusercontent.com/jmcodebase/simplecc/master/simplecc.py --output simplecc.py
```

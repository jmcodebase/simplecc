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

# Searching food items
Instead of typing things exactly, you can utilize the benefits of the Unix philosophy. 

```
grep --ignore-case "sirl" ~/.config/simplecc/fooditems.py| head -n 1 | cut --delimiter=":" --fields=1
```

This will return the first result that matches sirl, in the case of the default fooditems.py, it will return sirloin.

You can turn this into a reusable command line function or a bash script. I use it with zsh, as a function. Here is the code:

```
scc(){
grep --ignore-case "$1" ~/.config/simplecc/fooditems.py| head -n 1 | cut --delimiter=":" --fields=1
}
```

Keeping things minimalist allows extensibility, you can always come up with your own search.

# Download
```
curl https://raw.githubusercontent.com/jmcodebase/simplecc/master/simplecc.py --output simplecc.py
```

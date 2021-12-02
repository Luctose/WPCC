# WPCC
# basicEx3.py

# Let's take a look at some operations we can do on variables

var1 = 17
var2 = 2

# We created two variables. Let's do some operations and assign the results to
# new variables

add_result = var1 + var2      # 19
sub_result = var1 - var2      # 15
mult_result = var1 * var2     # 34
div_result = var1 / var2      # 8.5
int_div_result = var1 // var2 # 8
mod_result = var1 % var2      # 1 
exp_result = var1**var2       # 289


# Some of these operations are pretty self-explanatory, but some of them are
# maybe things you haven't seen before
# `int_div_result` is the integer division operation. `div_result` gives us the
# result as a floating point number, but integer division will not compute the
# decimals. i.e. `int_div_result` is like `div_result`, but with the decimals chopped off

# `mod_result` will store the remainder of `var1` divided by `var2` (called the modulo
# operator). In this example, "17 % 2 = 1" means: 17/2 is 8 with a remainder of **1**.

# We can print out the values of all these results all at once with print:
print(add_result, sub_result, mult_result, div_result, int_div_result, exp_result)
# This will print all the values with a single space between each one.
# In some languages, printing different variables of different types is not easily
# done easily, but Python is smart.



#########################
# EXERCISE
#########################

# Write program that makes two variables (x and y) and assigns any integer values to them
# Then print their division, integer division, and remainder


# Anonymous Functions
# One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!
# Check out the code at the right. See the lambda bit? Typing
# lambda x: x % 3 == 0
# Is the same as
# def by_three(x):
#     return x % 3 == 0
# Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.
# When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print([x for x in languages if x == "Python"])

squares = [x**2 for x in range(1,11)]
print([a for a in squares if a>=30 and a<=70])


# We've given you another (slightly different) garbled. Sort it out with a filter() and a lambda.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = [x for x in garbled if x != "X"]
print(message)

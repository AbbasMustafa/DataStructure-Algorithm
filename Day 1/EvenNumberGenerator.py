# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

print("********************")
# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

print("********************")
# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
print("********************")
for i in range(100):
    print(next(my_gen))
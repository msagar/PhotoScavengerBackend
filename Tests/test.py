import requests
import random

"""
This test runs against the localhost server and tries permutations of the possible score and the assignment + emoji the user can get back
If there's a error in the json response it might result a failure for the user.

By running a great number of permutations we have assurance that the API works

"""


URL = "http://localhost:8000/v2/newassignment/"

numberoftries = 3000

for i in range (numberoftries):
    j = random.randint(0, 10000)
    j = str(j)
    r = requests.get(url = URL+j)
    data = r.json()
    i = str(i)
    numberoftries = str(numberoftries)
    print("\n##########     " + i + "  out of  " + numberoftries + "     ##########\n")
    print("Tried score:   " + j)
    print(data)

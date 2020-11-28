import math

def hypotenuse (base, height):
    return math.sqrt(base**2 + height**2)

def walking(x,y):
    return x + y + hypotenuse(x,y)

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

def ascending(x,y,z):
    if x <= y <= z:
        return True
    else:
        return False

def f(n):
    if (n > 0):
        print(n)
        n = n-1

def countdown(n):
    while (n > 0):
        print(n)
        n = n - 1

def filter_juniors(employees_list):
    juniors_list = []
    for person in employees_list:
        if (person[1] < 10000):
            juniors_list.append(person)
    return juniors_list


# eureko_compliance_employees_list = [("semih", 10000), ("cincin", 15000), ("beyza", 5000), ("canan", 7000), ("kutay", 10000), ("bilge", 8000)]
#
# print("all employees", eureko_compliance_employees_list)
# print("juniors only", filter_juniors(eureko_compliance_employees_list))
#
# campaigns = ["healthcare campaigns", "smartcare 1", "tech"]
# for campaign in campaigns:
#     print(campaign.capitalize())

eureko_list = [["semih", 10000],
               ["cincin", 15000],
               ["beyza", 5000],
               ["canan", 7000],
               ["kutay", 10000],
               ["bilge", 8000]]

sentence = "I feel jovial today."

sentence.split(" ")

customer_name_1 = "semih"
customer_name_2 = "semih"

customers = ["semih", "ahmet", "mehmet", "semih", "fatma", "mehmet"]
newlist = []
for customer in customers:
    if customer not in newlist:
        newlist.append(customer)

customers_list = ["semih bulut", "özlem aydın", "mehmet bulut", "semih bulut jr.", "fatma bulut", "mehmet yetim"]
customers_list[customers_list.index("özlem aydın")] = "özlem bulut"

customers_data = {
                    101: {"name": "özlem aydın", "age": 32, "salary": 1000},
                    99: {"name": "semih bulut", "age": 35, "salary": 10000}
                  }

customers_data[101]["name"] = "özlem bulut"

story = "A tuple is a sequence of values." \
           " The values can be any type, and they are indexed by integers," \
           " so in that respect tuples are a lot like lists." \
           " The important difference is that tuples are immutable."

# Algorithm
# 1. split long string into tokens; whitespace is the delimiter.
# 2. scan over the list of tokens.
# 3. add the token to a dictionary (K,V) where key K is token and value V is the frequency.
# 4. if the same token is seen again, increment its frequency by 1, otherwise it is a new insert with frequency 1.
# {"apple": 3, "bear": 2, "the": 200, ...}


tokens_list = story.split(" ")

cleaned_token_list = []
for token in tokens_list:
    cleaned_token_list.append(token.lower().strip(".,"))
# print(cleaned_token_list)

word_frequencies = {}
for token in cleaned_token_list:
    if token not in word_frequencies:
        word_frequencies[token] = 1
    else: #token is in word_frequencies
        word_frequencies[token] = word_frequencies[token] + 1

# print(word_frequencies)

f = open("masked_dataset.csv")
print("Header info", f.readline().strip("\n").split("\t"))
d = {}

for line in f.readlines():
    l = line.strip("\n").split("\t")
    campaignId, new_clicks, new_conversions = float(l[2]), float(l[5]), float(l[4])
    if campaignId not in d:
        d[campaignId] = {"clicks": [new_clicks],
                         "conversions": [new_conversions],
                         }
    else:
        d[campaignId]["clicks"].append(new_clicks)
        d[campaignId]["conversions"].append(new_conversions)

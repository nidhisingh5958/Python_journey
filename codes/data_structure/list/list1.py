names = ["allahabad","lucknow","varanasi","kanpur","agra","ghaziabad","mathura","meerut"]
city = input("Enter city to search:")
a = city.lower()
for c in names:
             if c == a:
                          print("City Found")
             else:
                          print("city not found")

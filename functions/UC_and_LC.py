#user defined function that accepts a string and calculates the no. of UC and LC

def string_test(s):
             d={"UPPER_CASE":0,"LOWER_CASE":0}
             for c in s:
                          if c.isupper():
                                       d["UPPER_CASE"]+=1
                          elif c.islower():
                                       d["LOWER_CASE"]+=1
                          else:
                                       pass
             print("Original String:",s)
             print("No. of upper case characters:", d["UPPER_CASE"])
             print("No. of lower case characters:", d["LOWER_CASE"])

string_test("All that we are is the result of what we have thought. Buddha;The most courageous act is still to think for yourself. Aloud. Coco Chanel")

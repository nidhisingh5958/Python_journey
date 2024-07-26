def trafficlight():
             signal=input("Enter the colour of the traffic light:")
             if (signal not in ("RED","YELLOW","GREEN")):
                          print("Please enter a valid Traffic light colour in capital:")
             else:
                          value=light(signal)
                          if (value==0):
                                       print("STOP, Life is more important than speed.")
                          elif (value==1):
                                       print("PLEASE GO SLOW.")
                          else:
                                       print("You may go now.")
def light(colour):
             if (colour=="RED"):
                          return(0)
             elif (colour=="YELLOW"):
                          return(1)
             else:
                          return(2)
trafficlight()
print("Better late than never")
             

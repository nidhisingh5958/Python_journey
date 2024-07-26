def cal_Mean (list1):
             total=0
             count=0
             for i in list1:
                          total=total+i
                          count=count+1
             mean=total/count
             print("The calculated mean is:",mean)
list1=[2.6,3.4,8.5,7.9]
cal_Mean(list1)

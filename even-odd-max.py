values=[2,4,1,-3,-5,7]
negative=max(i for i in values if i<0)
positive=max(j for j in values if j%2==0)
print(negative)
print(positive)

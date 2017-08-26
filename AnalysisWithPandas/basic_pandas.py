import pandas
#pandas basics
df1 = pandas.DataFrame([[2,4,6], [10,20,30]], columns=["page", "value", "price"], index=["time", "place"])
#print(dir(df1)) #get a list of methods attached to the object
print(df1.mean()) #applies mean to item in the data frame,
print(type(df1.mean())) #type: series object
print(df1.mean().mean()) #gets the mean for the entire data frame
df2 = pandas.DataFrame([{"Name":"Dan", "Last" : "Jones"}, {"Name":"Jack", "Last" : "Smith"}]) #passing dictionaries
print(df2)

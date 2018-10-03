#   In this portion of the assignment you should create a more complex heuristic with an accuracy of 80% or more.
#   You are encouraged to use as many of the elements in the csv file as you need.
import pandas

predictions = []

df = pandas.read_csv("titanic_data.csv")
wrong=0

for passenger_index, passenger in df.iterrows():

    if passenger[4]=="male" or passenger[6]>2 or passenger[7]>2:
        predictions.append(0)
    else:
        predictions.append(1)

    if not predictions[passenger_index]==passenger[1]:
        wrong+=1

#print wrong

# Fixed predictions
print "Wrong predictions: "+str(wrong)+", Number of passengers: "+str(passenger_index+1)

accuracy=(891-wrong)/891.0
# The .0 helps us calculate the accuracy as a float number (not integer)
print "The accuracy is "+str(accuracy*100.0)+"%"

# New prediction gives accuracy greater than 80%, better than before.
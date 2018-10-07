#    Here's a simple heuristic to start off:
#       1) If the passenger is female, your heuristic should assume that the
#       passenger survived.
#       2) If the passenger is male, you heuristic should
#       assume that the passenger did not survive.
#  Cross-reference your findings with the passenger["Survived"] column and find an approximate accuracy.


import pandas

wrong=0
df = pandas.read_csv("titanic_data.csv")
survival = {"male": 0, "female": 1}
for passenger_index, passenger in df.iterrows():
    if survival[passenger[4]] <> passenger[1]:
        wrong += 1

print "Wrong predictions: "+str(wrong)+", Number of passengers: "+str(passenger_index+1)
# passenger_index begins from 0 and ends at 890 so all passengers are 890+1

accuracy=(891-wrong)/891.0
# The .0 helps us calculate the accuracy as a float number (not integer)
print "The accuracy is "+str(accuracy*100.0)+"%"

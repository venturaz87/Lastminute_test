import json

#open the json file
with open('order_id_attributions2.json') as data_json:
    data = json.load(data_json)

#create a new file where to store the results
f = open('extraction.txt','w')

#get the length of the sample
d = data["data"]

#loop over the length of the sample to retrieve the variables we need
for i in range(len(d)):

    #v is a vector that allows to enter in the internal category "attributions"
    v = data["data"][i]["attributions"]
    #f.write(d[i]["order_id"]+"\t" +"\n")
    #loop over the internal category "attributions"
    for j in range(len(v)):

        #write to file the variables you need
        print(v[j]["device"])
        f.write(d[j]["attribution_type"]+"\t"+v[j]["ad_id"]+"\t"+v[j]["device"]+"\t" +"\n")

#close the file
f.close()
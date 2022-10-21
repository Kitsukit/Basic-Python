text="Hashem Hashem Hashem Al Al Ghanem 22 # Hashem Hashem"
segments= text.split(" ")
dictionary={"test":1}

for i in range (len(segments)):
    count=0
    for j in range (len(dictionary)):
        if segments[i] != list(dictionary)[j]:
            count=segments.count(segments[i])
            dictionary[segments[i]]=count

            
def show(dic):
    for key, value in dic.items():
        print('Wort:', key, 'Anzahl:', value)
            

def get_value(item):
    return item[1]

sorted_by_value = {k:v for k,v in sorted(dictionary.items(), key = get_value, reverse = True)}


#output
print (sorted_by_value)
show(sorted_by_value)

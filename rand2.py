import random
liste=["köln","koblenz","Düsseldorf","Basel","meinz","manheim","Darmstadt"]
for i in range(4):
    print(random.choices(liste))#wiedeholung sind erlaubt

print(random.choices(liste, k=4)) #mit wiederholung
print(random.sample(liste, 3))#ohne wiederholung
list1=['one','two','three','four','five','six','seven','eight','nine']
list2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
list3=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
n_list1 = []
n_list2 = []
n_list3 = []
for x in list1:
	n_list1.append(len(x))
for x in list2:
	n_list2.append(len(x))
for x in list3:
	n_list3.append(len(x))

deca = 0
for a in n_list3:
	for b in n_list1:
		deca += a+b
	deca +=a
print deca

hundreds = 0
for a in n_list1:
	for d in n_list1:
		hundreds += a+len('hundred')+len('and')+d
	hundreds += a+len('hundred')
	for e in n_list2:
		hundreds += a+len('hundred')+len('and')+e
	for b in n_list3:
		for c in n_list1:
			hundreds += a+len('hundred')+len('and')+b+c
		hundreds += a+len('hundred')+len('and')+b
print hundreds 

total = sum(n_list1) + sum(n_list2) + deca +hundreds +len('onethousand')
print total
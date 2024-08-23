tup1=(1,2,"hello")
tup2=(3,4,5,6,7,8)
tup3=("Got", "it","my", "boy","you","are", "English", "or", "Spanish!!")
tup4=("Who", "ever", "moves", "first", "is", "GAY!!!!")
tup5=("Baby","you","got","something","that","you","know")

l=[tup1,tup2,tup3,tup4,tup5]

max_l=max(l, key=len)

print(max_l,len(tup4))
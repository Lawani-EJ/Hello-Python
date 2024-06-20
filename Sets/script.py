set1 = {"pop","rock","soul","hard rock","rock","R&B","rock","disco"}
print(set1)
album_list = ["Micheal Jackson", "Thriller",1982,"00:42:19","pop, Rock, R&B",46.0,65,"30-Nov-82", None,10.0]
album_set = set(album_list)
print(album_set)
Music_genres = set(["pop","pop","rock","folk rock","hard rock","soul","progressive rock","soft rock","R&B","disco"])
print(Music_genres)

SampleSet = set(["Thriller", "Back in Black", "AC/DC"])
print(SampleSet)
SampleSet.add("NYC")
SampleSet.add("NYC")
SampleSet.add("NYC")
print(SampleSet)
SampleSet.remove("NYC")
print(SampleSet)
"Thriller" in SampleSet
print("Thriller" in SampleSet)

album_set1 = set(["Thriller","AC/DC","Back In Black"])
album_set2 = set(["AC/DC","Back In Black", "The Dark Side of The Moon"])
print(album_set1,album_set2)

FindIntersection = album_set1 & album_set2
print(FindIntersection)

FindDifference = album_set1.difference(album_set2)
print(FindDifference)
# print(album_set1.difference(album_set2))

FindDifference2 = album_set2.difference(album_set1)
print(FindDifference2)
# print(album_set2.difference(album_set1))

FindIntersection2 = album_set1.intersection(album_set2)
print(FindIntersection2)
# print (album_set1.intersection(album_set2))

FindUnion = album_set1.union(album_set2)
print(FindUnion)
# print(album_set1.union(album_set2))

CheckIfSuperSet = album_set1.issuperset(album_set2)
print(CheckIfSuperSet)

CheckIfSubSet = album_set1.issubset(album_set2)
print(CheckIfSubSet)

CheckIfSubSet2 = {"Back In Black","AC/DC"}.issubset(album_set1)
print(CheckIfSubSet2)

CheckIfSuperSet2 = (album_set1).issuperset({"Back In Black","AC/DC"})
print(CheckIfSuperSet2)

# Several Quizzes!
# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print("The sum of A :",sum(A))
print("The sum of B :",sum(B))
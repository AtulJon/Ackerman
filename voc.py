str=(input(""))
if str.isalpha() and len(str)==1:
	if str in ('a','e','i','o','u') or str in ('A','E','I','O','U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Inalid")

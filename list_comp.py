from pprint import pprint as PP
ul=[line.split(":")[0].upper()for line in open("passwd.txt")]
PP(sorted(ul))
PP(sorted(ul,reverse=True))

ul=[ul.split(":")[0].upper() for ul in open("passwd.txt") if ul.startswith("a")]
PP(sorted(ul))
#PP(sorted(ul,reverse=True))
lista = ['Przemek','Arek']
print(type(lista))
print(id(lista))
lista.append('Krysia')
print(id(lista))
print(sorted(lista))


przemek = ('Przemek', 'Domel', 27)

people = list()
people.append(przemek)
print(people)
arek = ('Arek', 'Domel', 25)
krysia = ('Krysia', 'Domel', 62)
people.append(arek)
people.append(krysia)
print(people)
print(sorted(people))


text = """ Kent. I thought the King had more affected the Duke of Albany
than
     Cornwall.
  Glou. It did always seem so to us; but now, in the division of
the
     kingdom, it appears not which of the Dukes he values most,
for
     equalities are so weigh'd that curiosity in neither can make
     choice of either's moiety.
  Kent. Is not this your son, my lord?
  Glou. His breeding, sir, hath been at my charge. I have so
often
     blush'd to acknowledge him that now I am braz'd to't.
  Kent. I cannot conceive you.
  Glou. Sir, this young fellow's mother could; whereupon she grew
     round-womb'd, and had indeed, sir, a son for her cradle ere
she
     had a husband for her bed. Do you smell a fault?
  Kent. I cannot wish the fault undone, the issue of it being so
     proper.
  Glou. But I have, sir, a son by order of law, some year elder
than
     this, who yet is no dearer in my account. Though this knave
came
     something saucily into the world before he was sent for, yet
was
     his mother fair, there was good sport at his making, and the
     whoreson must be acknowledged.- Do you know this noble
gentleman,
     Edmund?"""

text2 = """Good-bye, proud world! I'm going home:
Thou art not my friend, and I'm not thine.
Long through thy weary crowds I roam;
A river-ark on the ocean brine,
Long I've been tossed like the driven foam:
But now, proud world! I'm going home.

Good-bye to Flattery's fawning face;
To Grandeur with his wise grimace;
To upstart Wealth's averted eye;
To supple Office, low and high;
To crowded halls, to court and street;
To frozen hearts and hasting feet;
To those who go, and those who come;
Good-bye, proud world! I'm going home.

I am going to my own hearth-stone,
Bosomed in yon green hills alone,—
secret nook in a pleasant land,
Whose groves the frolic fairies planned;
Where arches green, the livelong day,
Echo the blackbird's roundelay,
And vulgar feet have never trod
A spot that is sacred to thought and God.

O, when I am safe in my sylvan home,
I tread on the pride of Greece and Rome;
And when I am stretched beneath the pines,
Where the evening star so holy shines,
I laugh at the lore and the pride of man,
At the sophist schools and the learned clan;
For what are they all, in their high conceit,
When man in the bush with God may meet?"""

text_1_list = set(text.split())
text_2_list = set(text2.split())
print(text_1_list | text_2_list)
print(text_1_list - text_2_list)
print(text_2_list - text_1_list)
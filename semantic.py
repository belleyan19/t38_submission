"""
Install spacy before running the program
1. pip install spacy
2. python -m spacy download en_core_web_md
3. python -m spacy download en_core_web_sm
"""

# Part 1. Run the code example.py
import spacy
nlp = spacy.load('en_core_web_md')
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]
print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))
recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]
print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))
print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))
"""
Output
======
-------------Complaints similarity---------------
1.0
0.8350770380943701
0.9246800668484182
0.8959758607031337
0.8395325188842946
0.8622109066850939
0.8350770380943701
1.0
0.8906699062993373
0.8145959567773281
0.9506982511773873
0.7946509303034253
0.9246800668484182
0.8906699062993373
1.0
0.8905289515151633
0.8818462415576602
0.869256307461911
0.8959758607031337
0.8145959567773281
0.8905289515151633
1.0
0.8115092735139192
0.8775633198697652
0.8395325188842946
0.9506982511773873
0.8818462415576602
0.8115092735139192
1.0
0.759590996735251
0.8622109066850939
0.7946509303034253
0.869256307461911
0.8775633198697652
0.759590996735251
1.0
-------------Recipes similarity---------------
1.0
0.9058969879808717
0.8761883563680793
0.8921915020817676
0.9362320788371851
0.9077991339554589
0.9058969879808717
1.0
0.8960302632860658
0.8683352787585712
0.9251986105731227
0.909277512798149
0.8761883563680793
0.8960302632860658
1.0
0.8206931822271948
0.923499834067875
0.9066167896089331
0.8921915020817676
0.8683352787585712
0.8206931822271948
1.0
0.843615344994607
0.8890459855149918
0.9362320788371851
0.9251986105731227
0.923499834067875
0.843615344994607
1.0
0.8970581769256016
0.9077991339554589
0.909277512798149
0.9066167896089331
0.8890459855149918
0.8970581769256016
1.0
-------------Recipes similarity---------------
0.7908975726272921
0.6548518295341987
0.7398681679268514
0.7337804972179451
0.6703983067394562
0.7674086724411375
0.7580808759364783
0.5323925552042279
0.7114560945673947
0.7008472217256502
0.5443126469769464
0.7254376103761647
0.7884092498717231
0.5253234387230952
0.7214799557383781
0.6939840662542774
0.5243623425430298
0.7301758500107655
0.6633546838990971
0.4596805000526375
0.5643795549917598
0.6354896259101941
0.4868229640175464
0.6469780435027565
0.8458759758734137
0.6612351139999046
0.7954997963311431
0.7757728611773715
0.6793218010601022
0.7921867919801224
0.7706409888372543
0.5407034497147122
0.6932683919739884
0.7135981756961652
0.549146532488016
0.7118486371023985
"""

# Task 2: Found interesting about the similarities between cat, monkey and banana and think an example of your own
print("=== Task 2 (given) ===")
given_examples = ["cat", "monkey", "banana"]
given_tokens = list()
for example in given_examples:
    example_nlp = nlp(example)
    given_tokens.append(example_nlp)
for token_a in given_tokens:
    for token_b in given_tokens:
        similarity = token_a.similarity(token_b)
        print(token_a.text, token_b.text, similarity)
"""
Notes:
cat and monkey are somehow similar as they are animals.
monkey and banana are somehow similar as their lengths similar.
cat and banana are not similar in terms of nature or word length.
"""
print("=== Task 2 (own) ===")
own_examples = ["apple", "avocado", "apricot"]
own_tokens = list()
for example in own_examples:
    example_nlp = nlp(example)
    own_tokens.append(example_nlp)
for token_a in own_tokens:
    for token_b in own_tokens:
        similarity = token_a.similarity(token_b)
        print(token_a.text, token_b.text, similarity)
"""
Notes:
apple and avocado are somehow similar as they are fruts.
apple and apricot are somehow similar as they are fruts.
avocado and apricot are somehow similar as they are fruts.
"""
"""
Output
======
=== Task 2 (given) ===
cat cat 1.0
cat monkey 0.5929929675536907
cat banana 0.22358827466989753
monkey cat 0.5929929675536907
monkey monkey 1.0
monkey banana 0.4041501317354622
banana cat 0.22358827466989753
banana monkey 0.4041501317354622
banana banana 1.0
=== Task 2 (own) ===
apple apple 1.0
apple avocado 0.5899598824775797
apple apricot 0.687583705688674
avocado apple 0.5899598824775797
avocado avocado 1.0
avocado apricot 0.5434423264659282
apricot apple 0.687583705688674
apricot avocado 0.5434423264659282
apricot apricot 1.0
"""

# Task 3: Run example file with en_core_web_sm
nlp = spacy.load('en_core_web_sm')
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]
print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))
recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]
print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))
print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))
"""
Output
======
-------------Complaints similarity---------------
1.0
/Users/tekichan/Documents/Belle/T38/semantic.py:228: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.5090129538857674
0.7128344367194357
0.7586548020591323
0.5481748320035115
0.5452402277421146
0.5090129538857674
1.0
0.7270419009762081
0.4497374989081487
0.735857044034381
0.5394512424336791
0.7128344367194357
0.7270419009762081
1.0
0.708028182946999
0.7212688150423118
0.6332525252580368
0.7586548020591323
0.4497374989081487
0.708028182946999
1.0
0.5723388623210595
0.5394047273727693
0.5481748320035115
0.735857044034381
0.7212688150423118
0.5723388623210595
1.0
0.49301706778062515
0.5452402277421146
0.5394512424336791
0.6332525252580368
0.5394047273727693
0.49301706778062515
1.0
-------------Recipes similarity---------------
1.0
/Users/tekichan/Documents/Belle/T38/semantic.py:241: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.7084920287496691
0.6028836058675155
0.7353468700623094
0.7425437432011321
0.7203463512361246
0.7084920287496691
1.0
0.6627457990659984
0.6864292226371292
0.7183366474826993
0.7157532895816617
0.6028836058675155
0.6627457990659984
1.0
0.5845283005158871
0.698378425946275
0.7327215292620014
0.7353468700623094
0.6864292226371292
0.5845283005158871
1.0
0.7533078453187548
0.7395232796373041
0.7425437432011321
0.7183366474826993
0.698378425946275
0.7533078453187548
1.0
0.8217725002462082
0.7203463512361246
0.7157532895816617
0.7327215292620014
0.7395232796373041
0.8217725002462082
1.0
-------------Recipes similarity---------------
/Users/tekichan/Documents/Belle/T38/semantic.py:247: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.5966324169014566
0.3016250881950343
0.3826340991569037
0.5629846111969197
0.29655543710447047
0.5637926780487199
0.502491835140449
0.1365426628896247
0.3869489676924255
0.5293672048975042
0.1609466164511931
0.5492882907011589
0.5717307550399429
0.23970945693766119
0.5015129015212759
0.5774550178829511
0.2564426898501645
0.4786500391825245
0.4597122746082667
0.13710947133971688
0.3076859522539867
0.5529147559975695
0.2714134723096019
0.5467640465456629
0.6989334370618809
0.3567423485718211
0.5961972026273806
0.757446761903842
0.5344295408612604
0.5674394173935786
0.6231520617676091
0.10303868880139798
0.47241819225138904
0.6803235933939673
0.3030423951654495
0.43135966164945344
"""
"""
Notes:
The similarity values seem smaller than those of en_core_web_md.
"""

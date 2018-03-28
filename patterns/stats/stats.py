import statistics as statistics
from scipy.stats import mannwhitneyu
import numpy as np

class Stats:
    def __init__:

    def cliff(olds,news):
        gt = lt = 0.0
        for  new in news:
            for old in olds:
                if new > old: gt += 1
                if new < old: lt += 1
        return (gt - lt)/(len(olds) * len(news))

    def fxsize(olds,news):
        ts=[(0.147,'small'),(0.5,'medium'),(0.8,'large')]
        c = cliff(olds,news)
        least,out = 10**32,ts[-1][1]
        for n,txt in ts:
            delta = abs(n-c)
            if delta < least:
                least,out=delta,txt
        return least

    def manwhitneytest(easy, medium, difficult):
        print('\tOn Subjectivity Score\n')
        # # cd = '999'
        toUploaded = []
        # print('\tOn Mean Values\n')
        print('Easy') 
        # print(len(easy['novice']['subjectivity']))
        p = mannwhitneyu(easy['novice']['subjectivity'], easy['beginner']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(easy['novice']['subjectivity'],easy['beginner']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Novice', 'Beginner', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])

        p = mannwhitneyu(easy['novice']['subjectivity'], easy['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['novice']['subjectivity'],easy['intermediate']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Novice', 'Intermediate', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])

        p = mannwhitneyu(easy['novice']['subjectivity'], easy['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(easy['novice']['subjectivity'],easy['experienced']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Novice', 'Experienced', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])

        print('\n')
        p = mannwhitneyu(easy['beginner']['subjectivity'], easy['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity']))
            print(cliffsDelta(easy['beginner']['subjectivity'], easy['intermediate']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Beginner', 'Intermediate', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])

        p = mannwhitneyu(easy['beginner']['subjectivity'], easy['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(easy['beginner']['subjectivity'],easy['experienced']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Beginner', 'Experienced', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])

        print('\n')
        p = mannwhitneyu(easy['intermediate']['subjectivity'], easy['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(easy['intermediate']['subjectivity'],easy['experienced']['subjectivity']))
        toUploaded.append(['Easy', 'Subjectivity', 'Intermediate', 'Experienced', p[1], fxsize(easy['beginner']['subjectivity'],easy['intermediate']['subjectivity'])])


        print('\n\nMedium') 
        p = mannwhitneyu(medium['novice']['subjectivity'], medium['beginner']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(medium['novice']['subjectivity'],medium['beginner']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Novice', 'Beginner', p[1], fxsize(medium['novice']['subjectivity'],medium['beginner']['subjectivity'])])

        p = mannwhitneyu(medium['novice']['subjectivity'], medium['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['novice']['subjectivity'],medium['intermediate']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Novice', 'Intermediate', p[1], fxsize(medium['novice']['subjectivity'],medium['intermediate']['subjectivity'])])

        p = mannwhitneyu(medium['novice']['subjectivity'], medium['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(medium['novice']['subjectivity'],medium['experienced']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Novice', 'Experienced', p[1], fxsize(medium['novice']['subjectivity'],medium['experienced']['subjectivity'])])

        print('\n')
        p = mannwhitneyu(medium['beginner']['subjectivity'], medium['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['beginner']['subjectivity'],medium['intermediate']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Beginner', 'Intermediate', p[1], fxsize(medium['beginner']['subjectivity'],medium['intermediate']['subjectivity'])])

        p = mannwhitneyu(medium['beginner']['subjectivity'], medium['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(medium['beginner']['subjectivity'],medium['experienced']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Beginner', 'Experienced', p[1], fxsize(medium['beginner']['subjectivity'],medium['experienced']['subjectivity'])])

        print('\n')
        p = mannwhitneyu(medium['intermediate']['subjectivity'], medium['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(medium['intermediate']['subjectivity'],medium['experienced']['subjectivity']))
        toUploaded.append(['Medium', 'Subjectivity', 'Intermediate', 'Experienced', p[1], fxsize(medium['intermediate']['subjectivity'],medium['experienced']['subjectivity'])])

        print('\n\nDifficult') 
        p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['beginner']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(difficult['novice']['subjectivity'],difficult['beginner']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Novice', 'Beginner', p[1], fxsize(difficult['novice']['subjectivity'],difficult['beginner']['subjectivity'])])

        p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['novice']['subjectivity'],difficult['intermediate']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Novice', 'Intermediate', p[1], fxsize(difficult['novice']['subjectivity'],difficult['intermediate']['subjectivity'])])

        p = mannwhitneyu(difficult['novice']['subjectivity'], difficult['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['novice']['subjectivity'],difficult['experienced']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Novice', 'Experienced', p[1], fxsize(difficult['novice']['subjectivity'],difficult['experienced']['subjectivity'])])

        print('\n')
        p = mannwhitneyu(difficult['beginner']['subjectivity'], difficult['intermediate']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['beginner']['subjectivity'],difficult['intermediate']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Beginner', 'Intermediate', p[1], fxsize(difficult['beginner']['subjectivity'],difficult['intermediate']['subjectivity'])])

        p = mannwhitneyu(difficult['beginner']['subjectivity'], difficult['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['beginner']['subjectivity'],difficult['experienced']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Beginner', 'Experienced', p[1], fxsize(difficult['beginner']['subjectivity'],difficult['experienced']['subjectivity']) ])

        print('\n')
        p = mannwhitneyu(difficult['intermediate']['subjectivity'], difficult['experienced']['subjectivity'])
        print p
        if(p[1] <= 0.05 and p[1] > -1):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['intermediate']['subjectivity'],medium['experienced']['subjectivity']))
        toUploaded.append(['Difficult', 'Subjectivity', 'Intermediate', 'Experienced', p[1], fxsize(difficult['intermediate']['subjectivity'],medium['experienced']['subjectivity']) ])

        print('\n\t----------------On Polarity Score------------------\n')
        print('Easy') 
        p = mannwhitneyu(easy['novice']['polarity'], easy['beginner']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(easy['novice']['polarity'],easy['beginner']['polarity']))
        p = mannwhitneyu(easy['novice']['polarity'], easy['intermediate']['polarity'])
        print p
        if(p[1] < 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['novice']['polarity'],easy['intermediate']['polarity']))
        p = mannwhitneyu(easy['novice']['polarity'], easy['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(easy['novice']['polarity'],easy['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(easy['beginner']['polarity'], easy['intermediate']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['beginner']['polarity'],easy['intermediate']['polarity']))
        p = mannwhitneyu(easy['beginner']['polarity'], easy['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(easy['beginner']['polarity'],easy['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(easy['intermediate']['polarity'], easy['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(easy['intermediate']['polarity'],easy['experienced']['polarity']))


        print('\n\nMedium') 
        p = mannwhitneyu(medium['novice']['polarity'], medium['beginner']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(medium['novice']['polarity'],medium['beginner']['polarity']))
        p = mannwhitneyu(medium['novice']['polarity'], medium['intermediate']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['novice']['polarity'],medium['intermediate']['polarity']))
        p = mannwhitneyu(medium['novice']['polarity'], medium['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(medium['novice']['polarity'],medium['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(medium['beginner']['polarity'], medium['intermediate']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['beginner']['polarity'],medium['intermediate']['polarity']))
        p = mannwhitneyu(medium['beginner']['polarity'], medium['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(medium['beginner']['polarity'],medium['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(medium['intermediate']['polarity'], medium['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(medium['intermediate']['polarity'],medium['experienced']['polarity']))

        print('\n\nDifficult') 
        # p = mannwhitneyu([np.mean(difficult['novice']['polarity'])], [np.mean(difficult['beginner']['polarity'])])
        # print p
        p = mannwhitneyu(difficult['novice']['polarity'], difficult['beginner']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(difficult['novice']['polarity'],difficult['beginner']['polarity']))
        p = mannwhitneyu(difficult['novice']['polarity'], difficult['intermediate']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['novice']['polarity'],difficult['intermediate']['polarity']))
        p = mannwhitneyu(difficult['novice']['polarity'], difficult['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['novice']['polarity'],difficult['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(difficult['beginner']['polarity'], difficult['intermediate']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['beginner']['polarity'],difficult['intermediate']['polarity']))
        p = mannwhitneyu(difficult['beginner']['polarity'], difficult['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['beginner']['polarity'],difficult['experienced']['polarity']))
        print('\n')
        p = mannwhitneyu(difficult['intermediate']['polarity'], difficult['experienced']['polarity'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['intermediate']['polarity'],difficult['experienced']['polarity']))

        print('\n\t----------------On No of Words---------------------\n')
        print('Easy') 
        p = mannwhitneyu(easy['novice']['word_count'], easy['beginner']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(easy['novice']['word_count'],easy['beginner']['word_count']))
        p = mannwhitneyu(easy['novice']['word_count'], easy['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['novice']['word_count'],easy['intermediate']['word_count']))
        p = mannwhitneyu(easy['novice']['word_count'], easy['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(easy['novice']['word_count'],easy['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(easy['beginner']['word_count'], easy['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(easy['beginner']['word_count'],easy['intermediate']['word_count']))
        p = mannwhitneyu(easy['beginner']['word_count'], easy['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(easy['beginner']['word_count'],easy['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(easy['intermediate']['word_count'], easy['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(easy['intermediate']['word_count'],easy['experienced']['word_count']))


        print('\n\nMedium') 
        p = mannwhitneyu(medium['novice']['word_count'], medium['beginner']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(medium['novice']['word_count'],medium['beginner']['word_count']))
        p = mannwhitneyu(medium['novice']['word_count'], medium['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['novice']['word_count'],medium['intermediate']['word_count']))
        p = mannwhitneyu(medium['novice']['word_count'], medium['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(medium['novice']['word_count'],medium['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(medium['beginner']['word_count'], medium['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(medium['beginner']['word_count'],medium['intermediate']['word_count']))
        p = mannwhitneyu(medium['beginner']['word_count'], medium['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(medium['beginner']['word_count'],medium['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(medium['intermediate']['word_count'], medium['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(medium['intermediate']['word_count'],medium['experienced']['word_count']))

        print('\n\nDifficult') 
        # p = mannwhitneyu([np.mean(difficult['novice']['polarity'])], [np.mean(difficult['beginner']['polarity'])])
        # print p
        p = mannwhitneyu(difficult['novice']['word_count'], difficult['beginner']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Beginner differs significantly ',p[1])
            print(fxsize(difficult['novice']['word_count'],difficult['beginner']['word_count']))
        p = mannwhitneyu(difficult['novice']['word_count'], difficult['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['novice']['word_count'],difficult['intermediate']['word_count']))
        p = mannwhitneyu(difficult['novice']['word_count'], difficult['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Novice vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['novice']['word_count'],difficult['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(difficult['beginner']['word_count'], difficult['intermediate']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Intermediate differs significantly ',p[1])
            print(fxsize(difficult['beginner']['word_count'],difficult['intermediate']['word_count']))
        p = mannwhitneyu(difficult['beginner']['word_count'], difficult['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Beginner vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['beginner']['word_count'],difficult['experienced']['word_count']))
        print('\n')
        p = mannwhitneyu(difficult['intermediate']['word_count'], difficult['experienced']['word_count'])
        print p
        if(p[1] <= 0.05):
            print('Intermediate vs Experienced differs significantly ',p[1])
            print(fxsize(difficult['intermediate']['word_count'],difficult['experienced']['word_count']))
#print fxsize(control,pilot)

# def cliffsDelta(lst1,lst2,
#                 dull = [0.147, # small
#                         0.33,  # medium
#                         0.474 # large
#                         ][0] ): 
#   "Returns true if there are more than 'dull' differences"
#   m, n = len(lst1), len(lst2)
#   lst2 = sorted(lst2)
#   j = more = less = 0
#   for repeats,x in runs(sorted(lst1)):
#     while j <= (n - 1) and lst2[j] <  x: 
#       j += 1
#     more += j*repeats
#     while j <= (n - 1) and lst2[j] == x: 
#       j += 1
#     less += (n - j)*repeats
#   d= (more - less) / (m*n) 
#   return d
#   #return abs(d)  > dull
   
# def runs(lst):
#   "Iterator, chunks repeated values"
#   for j,two in enumerate(lst):
#     if j == 0:
#       one,i = two,0
#     if one!=two:
#       yield j - i,one
#       i = j
#     one=two
#   yield j - i + 1,two
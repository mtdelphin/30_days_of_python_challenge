from functools import reduce 
from collections import Counter
from math import sqrt

class Data:
    def __init__(self, ages=[]):
        self.ages=ages

    def count(self):
        return len(self.ages)
    
    def sum(self):
        return reduce(lambda res, item: res+item, self.ages)
    
    def min(self):
        return min(self.ages)
    
    def max(self):
         return max(self.ages)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        self.ages = sorted(self.ages)
        if self.count() % 2 != 0:
            return self.ages[self.count() // 2]
        else:
            return (self.ages[self.count()/2 - 1] + self.ages[self.count()/2 + 1])/2

    def mode(self):
        mode=Counter(self.ages).most_common(1)[0]
        #print({'mode': mode[0], 'count': mode[1]})
        return mode

    def std(self):
        return sqrt(self.var())
    
    def var(self):
        mean= self.mean()
        sum_squarred_diff=sum([(item-mean)**2 for item in ages])
        return sum_squarred_diff/(self.count()-1)
    
    def freq_dist(self):
        items=Counter(self.ages).items()
        return sorted([(item[1]*4, item[0]) for item in items], reverse=True)

    def describe(self):
        return f'''
            Count: {self.count()}
            Sum: {self.sum()}
            Min: {self.min()}
            Max: {self.max()}
            Range: {self.range()}
            Mean: {self.mean()}
            Median: {self.median()}
            Mode: {self.mode()}
            Variance: {self.var()}
            Standard Deviation: {self.std()}
            Frequency Distribution: {self.freq_dist()}
        '''
    

ages=[31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=Data(ages)

print(data.describe())
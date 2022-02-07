import Digging

data1, itemset1, rules1 = Digging.frequency_and_rules("Homework\Apriori\T3-1.csv", 40, 60)
'''
data2, itemset2, rules2 = Digging.frequency_and_rules("Homework\Apriori\A3-1.csv", 50, 80)
data3, itemset3, rules3 = Digging.frequency_and_rules("Homework\Apriori\A3-2.csv", 40, 60)
'''
print()
print(rules1)
print()
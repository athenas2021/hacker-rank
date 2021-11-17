class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    def computeDifference(self):
        maior = self.__elements[0]
        menor = self.__elements[0]
        for item in self.__elements:
            if item > maior:
                maior = item
            if item < menor:
                menor = item
        
        self.maximumDifference = maior - menor


a = [int(e) for e in input().split(' ')]


d = Difference(a)
d.computeDifference()

print('xpot',d.maximumDifference)
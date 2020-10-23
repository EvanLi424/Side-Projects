#Yes or No Machine

#Takes N factors and how confident you are.

#Your factor is either affirm or neg and it is rated from 1 to 10

Question = input("Should *action*?:")

Factors = []

NumberOfFactors = int(input("Number of factors are you considering:"))

for i in range(1,NumberOfFactors + 1):
    FactorSpec = [input("Aff or Neg:"), int(input("Weight:"))]
    Factors.append(FactorSpec)

print(Factors)

ValuePool = 0
ExtractionPosition = 0
for i in range(1,NumberOfFactors + 1):
    ExtractionType = Factors[ExtractionPosition][0]
    if ExtractionType == 'yes':
        ExtractionWeight = int(Factors[ExtractionPosition][1])
        ValuePool = ValuePool + ExtractionWeight
    if ExtractionType == 'no':
        ExtractionWeight = int(Factors[ExtractionPosition][1]) * -1
        ValuePool = ValuePool + ExtractionWeight
    ExtractionPosition += 1

if ValuePool >= 1 and ValuePool <= 5:
    Answer = 'Maybe'
if ValuePool == 0:
    Answer = 'possibly'
if ValuePool >= 5 and ValuePool <= 10:
    Answer = 'Yes'
if ValuePool <= -1 and ValuePool >= -5:
    Answer = 'Maybe'
if ValuePool <= -5 and ValuePool >= -10:
    Answer = 'No'
    
print(ValuePool)
print('*' * 33)
print(Answer + ", " + Question + ".")
from math import *
#Convolutional Neural Network Mimic

"""
This is for a project about how Convolutional Neural Networks can identify communities that are at risk for 
COVID-19 flare ups. It demonstrates what the inputs and outputs would look like and what type of data that 
would use.
"""

#Input Layer

"""
If you want to change the avg income or population density data, you can edit the following two variables. 
GPD is for gdp per capita $ and PopDen is for population density people/mi^2.
"""

income = int(21000)
PopDen = int(20000) 

def Average_Income():
    LowerIncome_bound = int(0) 
    UpperIncome_bound = int(20000)
    Income_Rating = 5
    while income <= int(100000):
        if income > LowerIncome_bound and income <= UpperIncome_bound:
            return(Income_Rating)
            break 
        LowerIncome_bound += int(20000)
        UpperIncome_bound += int(20000)
        Income_Rating -= int(1)
"""
The GDP Per Capita score is calculated based on intervals that increase by $20,000
"""

def Population_Density():
    def interval_f(x):
        return x**2
    x = int(0)
    PopulationDensity_Rating = 1
    while 1==1:
        LowerPopDen_bound = int(1000) * interval_f(x) 
        UpperPopDen_bound = int(1000) * interval_f(x+1)
        if PopDen > LowerPopDen_bound and PopDen <= UpperPopDen_bound:
            return(PopulationDensity_Rating)
            break 
        PopulationDensity_Rating += 1
        x += 1
"""
The Population Density score is calculated based on intervals that increase exponentially. This tries to 
mimic the effect of actual population density increases; the difference in rate of transition of a disease 
between 1000 and 10000 ppl/mi^2 is much greater than the difference between 40,000 and 50,000 ppl/mi^2
Population Density score increases linearly as the population increases exponentially 
"""

#Output Layer

print("The average income of this community was: $" + str(income) + "\nThe population density of this community was: " + str(PopDen) + "people/square mile" + "\nThe overall rating for this community is:" + str(Population_Density() + Average_Income()))
print('*' * 34)
print("The income score was:" + str(Average_Income()) + "\nThe Population Density score was:" + str(Population_Density()))
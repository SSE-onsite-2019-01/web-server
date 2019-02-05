from stressdetector.estimate.Model import CalcStress

model = CalcStress()

X =[0.026666667, 0.038333333, 0.035, 0.034166667, 3.441666667, 2.605833333, 0.003333333, -9.423516667, 44.066525, 325.55855, 2.166822917, 8.16390625, -11.674375]
v = model.Calc(X)
print(v)

X =[0.026666667, 0.038333333, 0.035, 0.034166667, 3.441666667, 2.605833333, 0.003333333, -9.423516667, 44.066525, 325.55855, 2.166822917, 8.16390625, -11.674375]
v = model.Calc(X)
print(v)
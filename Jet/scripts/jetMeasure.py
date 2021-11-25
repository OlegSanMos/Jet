import jetFunctions as jet

try:
    jet.initStepMotorGpio()
    jet.initSpiAdc()

    measures = []
    for j in range(100):
        measures.append(jet.getMeanAdc(100))
        jet.stepBackward(9)

    jet.save(measures, 9)
finally:
    jet.deinitSpiAdc()
    jet.deinitStepMotorGpio()
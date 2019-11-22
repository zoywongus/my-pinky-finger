import numpy as np
import matplotlib.pyplot as plt
import finger_set, hyperionMeasure

config = {
  hand: 'right'
  auto: true
  flex_rate: 40
  bone_density: 37
}


def sync():
  hyperionMeasure()
  stellarSphere(frontalLobe, kinesis_neurons)
  
def test_sync():
  try:
    movement = 42
    testFlex(movement)
    testMovement(spinalDensity, movement, neurons_enabled)
  except:
    sync()
    
  return result
  

def shutdown():
  turnOfAllNeurons()
  disableCortex()

def enable_finger():
  finger.test(finger_set)
  finger.enable(config)

if __name__ == "__main__":
  sync()
  testResult = test_sync() + 5
  if testResult > 8:
    enable_finger()
  else:
    shutdown()

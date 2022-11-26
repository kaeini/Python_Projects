from abc import ABCMeta, abstractclassmethod

class ICar(meta=ABCMeta):
  @abstractclassmethod
  def print_data():
    """use in child class"""

class CarSingleton(ICar):
  __instance = None
  @staticmethod
  def get_instance():
    if CarSingleton.__instance == False:
      CarSingleton("Tesla Model X", "2016")
    return CarSingleton.__instance


  def __init__(self, car, year):
    if CarSingleton.__instance != None:
      print("Singleton cannot be instansiated more than once")
    else:
      self.car = car
      self.year = year
      CarSingleton.__instance = self

  @staticmethod
  def print_data():
    print(f"Name: {CarSingleton.__instance.name}, Year: {CarSingleton.__instance.year}")
  p = print_data("Ford Focus", 1998)
  print(p)
  p.print_data()
    

  
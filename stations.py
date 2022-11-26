def Stations(stations):
  Station_1 = input("Input your first station: ")
  Station_2 = input("Input your second station: ")
  start_station = stations.index(f'{Station_1}')
  end_station = stations.index(f'{Station_2}')
  substring = stations[start_station+1:end_station]
  print(f"The inbetween stations are {substring}")
  
#Main program
stations = ['Brixton', 'Stockwell', 'Vauxhall', 'Pimlico', 'Victoria', 'Green Park', 'Oxford Circus', 'Warren Street', 'Kings Cross', 'Highbury & Islington', 'Finsbury Park', 'Seven Sisters', 'Tottenham Hale', 'Blackhorse Road', 'Walthamstow Central']
Stations(stations)
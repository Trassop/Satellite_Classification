def load_data():
  file_path = 'Satellite_Data.csv'
  satellite_data = pd.read_csv(file_path)
  return satellite_data

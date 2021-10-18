class ExportCsv:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    
    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result

    
    def write_file(self, filename):
        with open(filename, 'w', encoding='UTF8') as f:
            f.write(self.data)


data = [
  {
    'name': 'Sherlock',
    'surname': 'Holmes',
    'occupation': 'private detective'
  },
  {
    'name': 'John',
    'surname': 'Watson',
    'occupation': 'doctor'
  }
]

exporter = ExportCsv(data)
exporter.write_file('out.csv')
from config import settings

class ConfigTester:
    def __init__(self):
        self.file = settings['FILENAME']['my_file']
        self.url = settings['URL']['example_url']
        self.run_print()
    
    def run_print(self):
        print(f'File name test: {self.file} and URL test: {self.url} ')

def main():
    ct = ConfigTester()

if __name__=='__main__':
    main()

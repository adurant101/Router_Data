# Tested using pyunit unittest
class Router:
    # Get filename, read file, parse data
    def __init__(self,filename):
        self.parse_router_data(self.read_file(filename))

    # Search by interface and print
    def search_router_data(self,search):
        router_dictionary = self.router_data[2]
        if search in router_dictionary:
            for item in self.router_data[1]:
                print(item, end=' ')
            print()
            router_list = router_dictionary[search]
            print(search, end=' ')
            for item in router_list:
                print(item, end = ' ')
        else:
            print("Router interface not found")

        return router_dictionary[search] if search in router_dictionary else None

    # Display router data
    def display_router_data(self):
        print(self.router_data[0])
        for item in self.router_data[1]:
            print(item, end=' ')
        print()
        for key, val in self.router_data[2].items():
            print(key,val)

    # Parse input into list with a dictionary for search
    def parse_router_data(self,data_output):
        codes = data_output[0]
        description = data_output[1].split()
        description_fixed = []
        prev = None
        for word in description:
            if word == 'IP':
                prev = 'IP'
                continue
            elif prev != None:
                word = prev+'-'+word
                prev=None
            description_fixed.append(word)
        self.router_data = [codes,description_fixed]
        temp_router_data = {}
        for i in range(3, len(data_output)):
            temp = data_output[i].split()
            temp_router_data[temp[0]] = temp[1:]
        self.router_data.append(temp_router_data)

    # Read file from filename line by line
    def read_file(self,filename):
        input_file = open(filename, 'r')
        lines = input_file.readlines()
        return lines

# Defining main function
def main():
    filename = 'screen_output.txt'
    router = Router(filename)
    router.search_router_data('dp0p7s0')

if __name__=="__main__":
    main()

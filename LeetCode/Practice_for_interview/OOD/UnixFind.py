'''

find all file >5mb
find all xml
Assume file class
{
get name()
directorylistfile()
getFile()
create a library flexible that is flexible
Design clases,interfaces.



Problem statement:
Design Unix File Search API to search file with different arguments as "extension", "name", "size" ...
The design should be maintainable to add new contraints.


Follow up: How would you handle if some contraints should support AND, OR conditionals.
'''
from collections import deque

# abstract class


class Filter:
    def __init__(self):
        pass
    
    def apply(self):
        pass

class MinSizeFilter (Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension
    
    def apply(self, file):
        return file.extension == self.extension

class File:
    def __init__(self, name, size):
        self.name = name
        self.extension = name.split('.')[1] if '.' in name else ''
        self.size = size
        self.isDirectory = False if '.' in name else True
        self.children = []
    
    def __repr__(self) -> str:
        return self.name



class FileSystem:
    def __init__(self):
        self.filters = []
    
    def addFilter(self, f):
        if isinstance(f, Filter):
            self.filters.append(f)
    

    def applyANDFilter(self, root):
        found_files = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.isDirectory:
                for child in curr.children:
                    queue.append(child)
            else:
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr):
                        is_valid = False
                        break
                
                if is_valid:
                    found_files.append(curr)
                    # print(curr)
        return found_files

    def applyORFilter(self, root):
        found_files = []
        queue = deque([root])
        while queue:
            # print(queue)
            curr = queue.popleft()
            if curr.isDirectory:
                for child in curr.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.apply(curr):
                        found_files.append(curr)
                        # print(curr)
                        break
        return found_files
if __name__ == "__main__":
    f1 = File("root_300", 300)

    f2 = File("fiction_100", 100)
    f3 = File("action_100", 100)
    f4 = File("comedy_100", 100)
    f1.children = [f2, f3, f4]

    f5 = File("StarTrek_4.txt", 4)
    f6 = File("StarWars_10.xml", 10)
    f7 = File("JusticeLeague_15.txt", 15)
    f8 = File("Spock_1.jpg", 1)
    f2.children = [f5, f6, f7, f8]

    f9 = File("IronMan_9.txt", 9)
    f10 = File("MissionImpossible_10.rar", 10)
    f11 = File("TheLordOfRings_3.zip", 3)
    f3.children = [f9, f10, f11]

    f11 = File("BigBangTheory_4.txt", 4)
    f12 = File("AmericanPie_6.mp3", 6)
    f4.children = [f11, f12]


    greater5_filter = MinSizeFilter(5)
    txt_filter = ExtensionFilter("txt")

    my_linux_find = FileSystem()
    my_linux_find.addFilter(greater5_filter)
    my_linux_find.addFilter(txt_filter)

    print(my_linux_find.applyORFilter(f1))
    # print(my_linux_find.applyANDFilter(f1))
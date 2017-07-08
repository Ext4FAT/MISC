import os  

IGNORE = ['.git']

def tree(path):  
    def tree_iter(path, prefix=''):  
        path = os.path.abspath(path)  
        listpath = os.listdir(path)
        listpath.sort()  
        for p in listpath:
            if p in IGNORE:
                continue  
            isLast = listpath.index(p) == len(listpath)-1  
            abspath = os.path.join(path, p)  
            print_tree(p, prefix, isLast)  
            if os.path.isdir(abspath): 
                next_prefix = prefix  
                next_prefix += '    ' if isLast else '│   '  
                tree_iter(abspath, next_prefix)  
  
    def print_tree(path, prefix, isLast):  
        print(prefix, end='')  
        print('└── ' if isLast else '├── ', end='')  
        print(path + '</br>') 
  
    print(path)  
    tree_iter(path)  

def main():  
    tree('..')      

if __name__ == '__main__':  
    main()

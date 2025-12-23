class HashMap:
    def __init__(self,size = 7):
        self.__arr = [[] for _ in range(size)]
        self.size = size

    def add(self,key,value):
        index = self.__hash__(str(key))
        for i in range(len(self.__arr[index])):
            if self.__arr[index][i][0] == key:
                self.__arr[index][i][1] = value
                return
        self.__arr[index].append([key,value])

    def get(self,key,default = None):
        index = self.__hash__(str(key))
        for k,v in self.__arr[index]:
            if k == key: return v
        return default

    def delete(self,key):
        ind = self.__hash__(str(key))
        try:
            if not self.__arr[ind]:
                raise KeyError
            for k,v in self.__arr[ind]:
                if k == key:
                    self.__arr[ind].remove([k,v])
                    return
            raise KeyError
        except KeyError as err:
            print(f"[!] Key '{key}' Not Found")

    def __hash__(self,key):
        ind = 0
        for letter in key:
            ind = (ind + ord(letter) + hash(letter))%self.size
        return  ind

    def keys(self):
        K = []
        for i in range(len(self.__arr)):
            for k,v in self.__arr[i]: K.append(k)
        return K


if __name__ == '__main__':
    MAP = HashMap(10)
    MAP.add(1,2)
    MAP.add(1,3)
    MAP.add(1, 4)
    MAP.add(2,145)
    print(f"Value of 1: {MAP.get(1)}")
    print(f"Value of 2: {MAP.get(2)}")
    MAP.delete(3)
    print(f"Value of 3: {MAP.get(3,'Not Found')}")
    print(f"Key: {MAP.keys()}")
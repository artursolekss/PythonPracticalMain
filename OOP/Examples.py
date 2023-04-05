class MyWrapperList:
    data:list

    def __init__(self,data) -> None:
        self.data = data
    
    def max(self):
        if len(self.data) == 0:
            return

        maxValue = list[0]
        for value in self.data:
            if value > maxValue:
                maxValue = value
        return maxValue

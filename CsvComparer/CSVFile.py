class CSVFile:

    def __init__(self):
        print("Instantiated CSVFile")

    def get_worked_data(self):
        return self.__worked_data

    def set_worked_data(self, worked_data):
        self.__worked_data = worked_data

    def get_used_memory(self):
        return self.__used_memory
    
    def set_used_memory(self, used_memory):
        self.__used_memory = used_memory

    def get_total_memory(self):
        return self.__total_memory

    def set_total_memory(self, total_memory):
        self.__total_memory = total_memory

    def get_cpu_usage(self):
        return self.__cpu_usage

    def set_cpu_usage(self, cpu_usage):
        self.__cpu_usage = cpu_usage

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time
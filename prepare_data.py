class PrepareData:
    """ Подготовка данных для выполнения запросов. """

    @staticmethod
    def handle_data(file_name):
        """ Считывание данных из файлов и их подготовка для запросов. """
        data_list = []
        with open(file_name, 'r') as file:
            words = file.readlines()
        for word in words:
            word = word.split('\n')[0]
            data_list.append(word)

        return data_list

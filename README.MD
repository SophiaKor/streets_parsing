Проект создан для парсинга названий улиц городов в России с помощью selenium.

Адреса веб-страниц, содержащих данные для парсинга, указаны в файле проекта.

Названия улиц записываются в файл - один файл для каждого города. 

Используется драйвер firefox для открытия Firefox на win/linux.


#### Содержание директории

- cities.txt - файл, содержащий названия городов, в которых будут парситься названия улиц
- config.py - переменные окружения
- geckodriver.exe - установочный файл geckodriver для Windows
- main.py - запуск приложения
- parsing.py - основная логика проекта
- prepare_data - подготовка данных для парсинга
- README.MD - данное описание
- refs.txt - файл, содержащий адреса веб-страниц для парсинга
- requirements.txt - зависимости python


#### Требования для запуска

Для корректной работы приложения необходима установка драйвера geckodriver для Firefox Selenium.

https://github.com/mozilla/geckodriver/releases/ - скачать архив для требуемой ОС

Варианты для linux:

- прописание директории для geckodriver

   cd /путь/до/драйвера/

   sudo chmod +x geckodriver
   
   далее в файле parsing.py в функции parsing.py прописать путь до драйвера
   
   Пример: self.driver = webdriver.Firefox('C:/Programs/Python_projects/streets_parsing/geckodriver')

- расположение geckodriver в bin

   wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz

   tar -xvzf geckodriver*
 	
   sudo chmod +x geckodriver
   
   sudo mv geckodriver /usr/local/bin/

Вариант для windows:

   в файле parsing.py в функции parsing.py прописать путь до драйвера
   
   Пример: self.driver = webdriver.Firefox('C:\\Programs\\Python_projects\\streets_parsing\\geckodriver.exe')
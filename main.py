from parsing import Parsing
from prepare_data import PrepareData


def run():
    prepare_data = PrepareData()
    parsing = Parsing()
    parsing.setup_driver()

    cities = prepare_data.handle_data('cities.txt')
    cities.reverse()
    cities_urls = prepare_data.handle_data('refs.txt')
    for i in range(len(cities)):
        inner_urls = parsing.get_urls_for_one_city(cities_urls[i])
        parsing.handle_query(inner_urls, cities[i])

    parsing.close_driver()


if __name__ == "__main__":
    run()

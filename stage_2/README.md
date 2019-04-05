# [CS839 Data Science Project Stage2](https://danish778866.github.io/DataScience/stage_2.html)

## Building and Running

### Clone Repository
```
> git clone https://github.com/danish778866/CS839_Project.git
> cd CS839_Project/stage_2
```

### Install Dependencies
```
> pip install virtualenv
> virtualenv myenv
> source myenv/bin/activate
> pip install Scrapy
> scrapy startproject movies_crawler
> mv src/imdb_spider.py movies_crawler/movies_crawler/spiders
> mv src/tmdb_spider.py movies_crawler/movies_crawler/spiders
> cd movies_crawler/movies_crawler
```

### Run
```
> scrapy crawl IMDb -a num_tuples=5000 -a id=0 -o imdb.csv -t csv
> scrapy crawl TMDb -a num_tuples=5000 -a id=0 -o tmdb.csv -t csv
```

## Organization
The organization of this stage is as follows:
* `README.md`: This README file.
* `src`: The directory containing the spiders written for crawling 
         [IMDb](https://www.imdb.com/) and [TMDb](https://www.themoviedb.org/).
* `data`: CSV files containing the crawled data.

# Analyzing millions of NYC Parking Violations, Part 1: Scripting Parallelized

To run:

```
docker run -v $(pwd):/app -e APP_TOKEN=$(cat .app_token) -it bigdata1:1.0 python main.py
```

This is a simplified version but you see need APP_TOKEN!

Where `.app_token` is a file that contains your `APP_TOKEN`. More details [here](https://docs.google.com/document/d/1jjArRAV462E6N6IcSBxPAtGBoIy3Iqn0KDEgRgaxC8A/edit#heading=h.m494fetmrwxj)

To run other scripts:

```
docker run -v $(pwd):/app -e APP_TOKEN=$(cat .app_token) -it bigdata1:1.0 python main_parallel.py
```

```
docker run -v $(pwd):/app -e APP_TOKEN=$(cat .app_token) -it bigdata1:1.0 python simple_example.py
```

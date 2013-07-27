# notification-tools

a simple notification tool for developers.

## Requirements

```
$ sudo easy_install feedparser
$ sudo easy_install beautifulsoup4
```

## Configuration

```
$ cd destination
$ cp config.py.sample config.py
$ vi config.py
```

## Usage

**Basic Usage**
```
$ python apple_dev_center.py
$ python app_store_ranking.py
```

**Cron**
```
0 * * * * python ~/workspace/notification-tools/apple_dev_center.py
```

## Credits

* [Atrac613](https://github.com/Atrac613)

## License

notification-tools is released under the [MIT License](http://www.opensource.org/licenses/MIT).

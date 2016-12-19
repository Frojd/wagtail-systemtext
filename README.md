# Wagtail System Text

## Requirements

- Python 2.7 / Python 3.5+
- Django 1.8+
- Wagtail 1.7+


## Installation

Install the library with pip:

```
$ pip install wagtailsystemtext
```



## Quick Setup

Make sure wagtail_geo_widget is added to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = (
    # ...
    'wagtailsystemtext',
)
```

Then add SiteSystemTextMiddleware to your middlewares.

```
MIDDLEWARE_CLASSES = (
    # ...
    'wagtailsystemtext.middlewares.SiteSystemTextMiddleware',
)
```

Done!


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).

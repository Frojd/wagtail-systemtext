# Wagtail System Text

Simplified wagtail system text management


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

```python
MIDDLEWARE_CLASSES = (
    # ...
    'wagtailsystemtext.middlewares.SiteSystemTextMiddleware',
)
```

Done!


## Usage

#### Drop in gettext replacement

```python
from wagtailsystemtext.utils import gettext as _

_('my_text')
_('main_label', 'buttons')
```

#### Templatetags

```python
{% load systemtext %}

{% st_trans "my_text" %}
{% st_trans "main_label" group "buttons" %}
```


## Roadmap

- [x] `trans` template tag support
- [x] Wagtail admin view with site permissions
- [x] Cache-rebild on save through admin
- [ ] Default text support (on declaration)
- [ ] Sync command between sites
- [ ] Lazy text transforms
- [ ] Last accessed timestamps
- [ ] `blocktrans` template tag support
- [ ] Automatic tag discovery


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail System Text is released under the [MIT License](http://www.opensource.org/licenses/MIT).

# Wagtail System Text

Simplified Wagtail system text management


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

Make sure wagtailsystemtext is added to your `INSTALLED_APPS`.

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
from wagtailsystemtext.utils import systemtext as _

_('my_text')
_('main_label', group='buttons')
_('main_label', group='buttons', default='My label')
```

#### Templatetags

```python
{% load systemtext %}

{% systemtext "my_text" %}
{% systemtext "main_label" group "buttons" %}
{% systemtext "main_label" group "buttons" default "My label" %}
```


## Roadmap

- [x] `trans` template tag support
- [x] Wagtail admin view with site permissions
- [x] Cache-rebild on save through admin
- [x] Default text support (on declaration)
- [ ] Sync command between sites
- [ ] Lazy text transforms
- [ ] Automatic tag discovery
- [ ] Last accessed timestamps
- [ ] `blocktrans` template tag support


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail System Text is released under the [MIT License](http://www.opensource.org/licenses/MIT).

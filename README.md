# Wagtail System Text

Simplified Wagtail system text management


## Requirements

- Python 2.7
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

### Management commands

- `python manage.py find_and_add_systemtext`: Searches after your .py and .html files after systemtext implementations and adds them to each site.


## Settings

- `SYSTEMTEXT_CACHE_PREFIX`: Cache prefix (`"wagtailsystemtext"` by default)
- `SYSTEMTEXT_CACHE_EXPIRY`: Cache expiry in seconds (10 min by default)
- `SYSTEMTEXT_REBUILD_ON_SAVE`: If cache should be rebuilt on save (`True` by default)
- `SYSTEMTEXT_USE_DEFAULT_ON_EMPTY`: If present, use default value when string is empty (`False` by default)


### Release start

These hooks will automatically bump the application version when using `git flow release ...`

```bash
chmod +x $PWD/git-hooks/bump-version.sh
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-release-start
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-hotfix-start
```



## Roadmap

- [x] `trans` template tag support
- [x] Wagtail admin view with site permissions
- [x] Cache-rebild on save through admin
- [x] Default text support (on declaration)
- [x] Lazy text transforms
- [x] Add setting for fallbacking to default if string is empty
- [x] Automatic tag discovery
- [ ] Sync command between sites
- [ ] Group filter in Wagtail admin
- [ ] Last accessed timestamps
- [ ] `blocktrans` template tag support


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail System Text is released under the [MIT License](http://www.opensource.org/licenses/MIT).

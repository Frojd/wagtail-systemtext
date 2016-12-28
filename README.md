[![Build Status](https://travis-ci.org/Frojd/wagtail-systemtext.svg?branch=master)](https://travis-ci.org/Frojd/wagtail-systemtext)

[![PyPI version](https://badge.fury.io/py/wagtailsystemtext.svg)](https://badge.fury.io/py/wagtailsystemtext)

# Wagtail System Text

This is a library that attempts to simplify the process of updating static text on a Wagtail website. By using identifiers we mark the strings that can be updated by the editor/moderator from the cms.

An template identifier can look like this `{% systemtext "title" %}`. When this identifier are evaluated it will be added to the cms under the section **Settings / System Text** under the name `title`. The entry has a field called `string` that can be updated, this is the text that will be rendered to the website users.

Identifiers can also be grouped, by using the group argument `{% systemtext "title" group "headlines" %}` we can make management easier, identifiers without group will be assigned to the `general` group.

By default identifiers will added in lazy mode, so for instance when a site renders a idenifier it will be added to that sites set of identifiers. The are also management commands that both searches through your code base and finds suiteable identifiers (`find_and_add_systemtext`), syncs then betweeen sites (`sync_systemtext`) and manual add/delete commands (`add_systemtext` / `delete_systemtext`).


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

The implementation closely resembles the default django translaton way of working with text.

### Strings

This is how you work with regular text, supply identifer and group and retrive the systemtext string.

```python
from wagtailsystemtext.utils import systemtext as _st

_st('my_text')
_st('main_label', group='buttons')
_st('main_label', group='buttons', default='My label')
```

### Lazy strings

Lazy strings are run when called upon, when for instance you want to initialize a systemtext retrival before the middleware has run.

```python
from wagtailsystemtext.utils import systemtext_lazy as _st

_st('my_text')
_st('main_label', group='buttons')
_st('main_label', group='buttons', default='My label')
```

### Templates

Systemtext contains a templatetag called systemtext, that behaves in the same way as Djangos `{% trans... %}`

#### Templatetags

```python
{% load systemtext %}

{% systemtext "my_text" %}
{% systemtext "main_label" group "buttons" %}
{% systemtext "main_label" group "buttons" default "My label" %}
```


## Management commands

- `find_and_add_systemtext`: Finds the systemtext identifiers in your applications (by looking for `_st` and `{% systemtext ... %}`) and adds them to each wagtail site).
- `add_systemtext`: Add identifier to site(s)
- `delete_systemtext`: Remove identifiers from site(s)
- `sync_systemtext`: Sync identifiers between sites to make sure they contain the same
- `list_systemtext`: List all active systemtext


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
- [x] Sync command between sites
- [ ] Group filter in Wagtail admin
- [ ] Last accessed timestamps
- [ ] `blocktrans` template tag support


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail System Text is released under the [MIT License](http://www.opensource.org/licenses/MIT).

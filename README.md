# dmenu

A complete python wrapper for dmenu.

```python
>>> from dmenu import Dmenu

>>> dmenu = Dmenu()
>>> dmenu.version
'dmenu-4.5, \xc2\xa9 2006-2012 dmenu engineers, see LICENSE for details'

>>> dmenu.select(['a', 'b', 'c'], prompt='pick a letter:')
>>> # <user selects a>
'a'

>>> dmenu.select(['a', 'b', 'c'])
>>> # <user hits escape>
None

>>> dmenu.select(['a', 'b', 'c'])
>>> # <user types their own selection d>
'd'

>>> dmenu = Dmenu(monitor=2)
>>> # <let's assume the installed version of dmenu does not support the monitor argument>
>>> dmenu.select(['a', 'b', 'c'])
Traceback (most recent call last):
    DmenuUsageError: This version of dmenu does not support your usage: ['dmenu', '-m', '2']

    usage: dmenu [-b] [-f] [-i] [-l lines] [-p prompt] [-fn font]
                 [-nb color] [-nf color] [-sb color] [-sf color] [-v]
```

# ydb - yobibyte's debugger

ydb is a debugger helper that currently can show text and matplotlib figures.
Mental model: each debugging session has a corresponding html page served by a flask app.
You open it and this is your debugging canvas. 

If you want to plot your data, you just do your usual matplotlib thing, and call `ydb.add_figure(fig)`. If you have the page open in the browser, it will autoreload every 3 seconds and your image will be on the refreshed page.

You can also add text to the page by `ydb.add_text(your_text)`. This is probably less useful as you can just print variables in the pdb console, but nothing prevents you from sending any comments/thoughts there and have them in one place.

Right now for this to work, you need to start a flask app locally: `flask --debug run`.

Set `YDB_DIR` env to be used as a storage directory. `.ydb` will be used otherwise.

### Usage

Imagine you got a breakpoing with your usual pdb.
You can do this:

```python
from ydb import ydb
from matplotlib import pyplot as plt

ydb.add_text("Hey you!")

plt.plot([1,2,3])
ydb.add_figure(plt.gcf())

# you'll get smth like
# 'Picture added to /home/yobibyte/.ydb/functional-garnet-flamingo-of-essence/index.html'
```

Run this command to serve files with Flask:

```python
    python -m ydb.app
```

Now nawigate to the functional-garnet-flamingo-of-essence/index.html to get your debugging html page.

# fubuki
**Facebook User-data Beautifikation and Indexer** (Alright, okay, I'm a big Hololive fan so I tried to fit the words in fubuki)
**fubuki** is an open-source indexer for Facebook data *(downloaded information from Facebook in json format)* that is currently being developed

## Great! How does it work?
If you're familiar with command line tools like Metasploit, **fubuki** works in the same fashion. You just use a certain module *(messages, comments, posts, etc.)* and query searches so you can index your chat very effectively.
You are greeted with a very nice banner after running the tool.

*Okay... wait, how do I install it?*
```bash
$ git clone https://github.com/Z34O/fubuki/
```

*Done. Now what?*
```bash
$ cd fubuki
$ python3 main.py
```

Oh wait... did I tell you that you need Python 3.x?

*uh ..no?*

Nevermind, they're installed on most systems anyways

Anyways, **fubuki** is still under development so it can only read messages and comments for now

*Comments what?*

You have to download a copy of ***your OWN information*** from Facebook first.
That information can include messages, posts, comments, your information, etc. depending on what you chose to download

*Okay now I have it downloaded and it's named as facebook-doog, what can I do?*

You can initialize that directory so you can work with the data inside it!
```
[fubuki] init facebook-doog
```

Then you can either choose from this running list of available modules!
- messages
- comments

```
[fubuki] use comments
[comments] search lol

...
```

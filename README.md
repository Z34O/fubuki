# fubuki
**Facebook User-data Beautifikation and Indexer** (Alright, okay, I'm a big Hololive fan so I tried to fit the words in fubuki)
**fubuki** is an open-source indexer for Facebook data *(downloaded information from Facebook in json format)*

## Great! How does it work?
If you're familiar with REPL like Metasploit, **fubuki** works in the same fashion. You just use a certain module *(messages, comments, posts, etc.)* and query searches so you can index your searches very effectively.
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

Oh wait... did I tell you that you need Python 3?

*uh ..no?*

Nevermind, they're installed on most systems anyways

You have to download a copy of your facebook data in json format in... *suprise!* Facebook.
That information can include messages, posts, comments, your information, etc. depending on what you chose to download

*Okay now I have it downloaded and it's named as facebook-doog, what can I do?*

You can initialize that directory so you can work with the data inside it!
```
[fubuki] init facebook-doog
```

Then you can either choose from this running list of available modules!
- messages
- comments
- posts

*Search through comments*

```
[fubuki] use comments
[comments] search lol
... result here
```

*...Or by regex*

```
[comments] search pass(word)?
... result here
```

*Searching through posts*

```
[fubuki] use posts
...
```

You can query more effectively by filtering:

*Filtering by date. Date time format is M(M)/D(D)/YYYY (0:00)* anything in the parentheses are optional

```
[messages] search here is my bank account from 4/12/2011 until 4/15/2011 7:18
... result here
```

*Filter by who sent the message* (it does not have to be an exact match

```
[messages] by Shirakami Fubuki
```

*Filter to whom the message is sent to*

```
[messages] to Himemori Luna
```

*Filter in specific conversations only* (also applies to group chats)

```
[messages] in Natsuiro Matsuri
```

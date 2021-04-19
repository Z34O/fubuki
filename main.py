# FUBUKI
# Facebook User-data Beautifier, Keeper and Intelligence

from datetime import datetime
import readline # Enable arrow key usage in input()
import json
import glob
import os
import re

# Env variables available to all
RED = "\033[31m"
BLUE = "\033[34m"
WHITE = "\033[37m"
ORANGE = "\033[33m"
dt_format = "%m/%d/%Y %H:%M"
datadirectory = ""

def messages():
    os.chdir("messages")

    # Subfunctions
    def beautify(data, jsond):
        print("Sender: "+data["sender_name"])
        print("To: "+jsond["title"])
        print("Content: "+data["content"])
        sentdate = datetime.fromtimestamp(int(data["timestamp_ms"]) / 1000.0)
        print(f"{sentdate.month}/{sentdate.day}/{sentdate.year} {sentdate.hour}:{sentdate.minute}\n")

    # Env variables
    keywords = ["search", "by", "on", "from", "until", "use"]

    while True:
        result = []

        # Default values
        searchkey = r"."
        sender = r"."
        to = r"."
        datefrom = datetime.strptime("1/1/1969 00:00", dt_format)
        dateuntil = datetime.now()
        threadtype = "inbox"

        # Break query into parts
        unsanitized_query = re.split("("+"|".join(keywords)+")", input(f"{BLUE}[messenger] {ORANGE}"))
        print(f"{WHITE}", end="") # Make result color white
        if unsanitized_query[0] == "exit":
            os.chdir("..")
            break
        query = [token.strip() for token in unsanitized_query if token != '']
        if query == []:
            continue
        for count, token in enumerate(query):
            next = query[count + 1] if count != len(query)-1 else None
            if token == "search":
                searchkey = next
            elif token == "by":
                sender = next
            elif token == "on":
                to = next
            elif token == "from":
                next += " 00:00" if ":" not in next else ""
                datefrom = datetime.strptime(next, dt_format)
            elif token == "until":
                next += " 00:00" if ":" not in next else ""
                dateuntil = datetime.strptime(next, dt_format)
            elif token == "use":
                threadtype = next

        # Go to chosen thread type, iterate through directories and look for matches in message_1.json
        try:
            os.chdir(threadtype)
        except FileNotFoundError:
            print(f"{RED}Thread type not found!{WHITE}")
            break
        for conversation in os.listdir():
            try:
                os.chdir(conversation)
                for messages in glob.glob('./*.json'): # Iterate through available messages
                    data = json.load(open(messages, "r"))
                    msgcount = 0
                    while True:
                        try:
                            message = data["messages"][msgcount]
                            conditions = [bool(re.search(searchkey, message["content"])),
                                          bool(re.search(to, data["title"])),
                                          bool(re.search(sender, message["sender_name"])),
                                          datetime.fromtimestamp(int(message["timestamp_ms"]) / 1000.0) > datefrom,
                                          datetime.fromtimestamp(int(message["timestamp_ms"]) / 1000.0) < dateuntil]
                            if all(conditions):
                                result.append((message, data))
                                beautify(message, data)
                        except IndexError:
                            break # Go to next conversation if last message reached
                        except KeyError:
                            pass # Skip conversations without "content"
                        msgcount += 1

            except FileNotFoundError:
                pass # Skip empty conversations
            os.chdir("..")

        os.chdir("..")

def comments():
    os.chdir("comments")

    def beautify(data, jsond):
        print(jsond["title"])
        print("Author: "+data["author"])
        print("Comment: "+data["comment"])
        commentdate = datetime.fromtimestamp(int(data["timestamp"]) / 1000.0)
        print(f"{commentdate.month}/{commentdate.day}/{commentdate.year} {commentdate.hour}:{commentdate.minute}\n")

    while True:
        result = []

        # Default values
        searchkey = r"."
        author = r"."
        datefrom = datetime.strptime("1/1/1969 00:00", dt_format)
        dateuntil = datetime.now()
        on = r"."

        # Reserved keywords \s to make sure it is a keyword and not part of a query value
        keywords = ["search\s", "by\s", "from\s", "until\s", "on\s"]

        # Break query into parts
        unsanitized_query = re.split("("+"|".join(keywords)+")", input(f"{BLUE}[comments] {ORANGE}"))
        query = [token.strip() for token in unsanitized_query if token != '']
        print(f"{WHITE}", end="")
        if unsanitized_query[0] == "exit":
            os.chdir("..")
            break

        for count, token in enumerate(query):
            next = query[count + 1] if count != len(query)-1 else None
            if token == "search":
                searchkey = next
            elif token == "by":
                author = next
            elif token == "on":
                on = next
            elif token == "from":
                next += " 00:00" if ":" not in next else ""
                datefrom = datetime.strptime(next, dt_format)
            elif token == "until":
                next += " 00:00" if ":" not in next else ""
                dateuntil = datetime.strptime(next, dt_format)

        data = json.load(open("comments.json", "r"))
        commentcount = 0
        while True:
            try:
                comment = data["comments"][commentcount]["data"][0]["comment"]
                conditions = [bool(re.search(searchkey, comment["comment"])),
                              bool(re.search(author, comment["author"])),
                              bool(re.search(on, data["comments"][commentcount]["title"].replace(comment["author"], ""))),
                              datetime.fromtimestamp(int(comment["timestamp"]) / 1000.0) > datefrom,
                              datetime.fromtimestamp(int(comment["timestamp"]) / 1000.0) < dateuntil]
                if all(conditions):
                    result.append((comment, data["comments"][commentcount]))
                    beautify(comment, data["comments"][commentcount])
            except IndexError:
                break # Stop if last comment is reached
            except KeyError:
                pass # If no content is found on comment, skip
            commentcount += 1

def posts():
    os.chdir("posts")

    def beautify(data, post):
        print(data["title"])
        print("Post Status: "+post["post"])
        postdate = datetime.fromtimestamp(int(data["timestamp"]) / 1000.0)
        print(f"{postdate.month}/{postdate.day}/{postdate.year} {postdate.hour}:{postdate.minute}\n")

    while True:
        result = []

        searchkey = r"."
        datefrom = datetime.strptime("1/1/1969 00:00", dt_format)
        dateuntil = datetime.now()

        keywords = ["search", "from", "until"]

        unsanitized_query = re.split("("+"|".join(keywords)+")", input(f"{BLUE}[posts] {ORANGE}"))
        query = [token.strip() for token in unsanitized_query if token != '']
        print(f"{WHITE}", end="")
        if unsanitized_query[0] == "exit":
            os.chdir("..")
            break

        for count, token in enumerate(query):
            next = query[count + 1] if count != len(query)-1 else None
            if token == "search":
                searchkey = next
            elif token == "from":
                next += " 00:00" if ":" not in next else ""
                datefrom = datetime.strptime(next, dt_format)
            elif token == "until":
                next += " 00:00" if ":" not in next else ""
                dateuntil = datetime.strptime(next, dt_format)

        for data in glob.glob('./*.json'):
            data = json.load(open("your_posts_1.json", "r"))
            postcount = 0

            while True:
                try:
                    post = data[postcount]["data"][0]
                    conditions = [bool(re.search(searchkey, post["post"])),
                                  bool(re.search(searchkey, data[postcount]["title"])),
                                  datetime.fromtimestamp(int(data[postcount]["timestamp"]) / 1000.0) > datefrom,
                                  datetime.fromtimestamp(int(data[postcount]["timestamp"]) / 1000.0) < dateuntil]
                    if all(conditions):
                        result.append((data, post))
                        beautify(data[postcount], post)
                except IndexError:
                    break
                except KeyError:
                    pass
                postcount += 1

# Starting point for REPL
# If not used as REPL, make sure you are inside the data directory
if __name__ == '__main__':
    os.system("bash banner.sh")

    while True:
        select = input("[fubuki: v.0.2b] ").split(" ")

        if select[0] == "exit":
            exit()
        elif select[0] == "init":
            datadirectory = select[1]
            try:
                os.chdir("../"+datadirectory)
            except FileNotFoundError:
                print(f"{RED}No facebook data file found!{WHITE}")
        elif select[0] == "use":
            try:
                if select[1] == "messages":
                    messages()
                elif select[1] == "comments":
                    comments()
                elif select[1] == "posts":
                    posts()
            except FileNotFoundError:
                print(f"{RED}No file data found for your chosen module")
                print(f"{BLUE}TIP: {ORANGE}Make sure you initialized your facebook information directory by 'init <directory>'{WHITE}")
            except IndexError:
                print(f"{RED}Command 'use' needs 1 valid argument!{WHITE}")
        else:
            print(f"{RED}'{select[0]}' is not a valid command!{WHITE}")

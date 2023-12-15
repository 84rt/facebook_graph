# Your social graph
This repository contains a list of scripts that can help you creat your own own social graph based on your facebook friends list. Fetching this data from facebook is useful to visualize the mutual connecions between our friends. We can create a personal social graph in four steps:
1. Get the list of your facebook friends.
2. For each friend, get a list of their friends.
3. Processing and format the the data.
4. Vusualizing the data as an interative graph.

# How to make your social graph (step-by-step):

### 1. Get a list of your facebook friends

Facebook used to have a API that allowed anyone to fetch their list of facebook friends as well as their mutual friends, ufortunetely this optoins was discontinued and the only way to get a list of *your friends* is to use the website itself. Meta cleary states tha webscrapign their website is agains their policy (which is rather ironic for a website that was created by a guy who hacked his univeristy database in otder to get photos as well as full names of all students to create FaceMash (a site for compring the hotness of two students...)

I am not going to go into detial on how to web scrape facebook (since it's not exactly legal), but there are plenty of free web scrapers you can use. I used a chrome web extension called *Data Scraper* in combination with an open source desktop automation program called *Actiona*, this solution was simple yet extremely slow, if you know how to do proper web scraping I'd advise doing it the standard way. 


### 2. For each friend, get a list of their friends.

The simplest way to fetch the list of mutual friends for all friends is to first go to https://www.facebook.com/friends/list and fetch that and past into an empty spreadsheet and then create a simple alorigthm that goest to each profile i.e. `https://www.facebook.com/your_friends_fb_name` and modifies the URL so that if looks as follows: `https://www.facebook.com/your_friends_fb_name/friends_mutual`
The only thing that you need to keep in mind here is that for all of your firends that didn't change their facebook username (and with that their profile URL) you will need to append the URL with 

### 3. Processing and format the the data.
>Before doing any processing make sure to do a backup in order to avoid repeating scraping in the case of a processing error/mistake. 
1. **Move yourself into the firends list**. My file looked a bit different so I converted it suing the following script:
```python
your_name = "Bart Jaworski"

# Open the csv file and read it as a list of rows
with open(f"{your_name}.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

out_a = []

with open(f"{your_name}.csv", "w") as f:
    for row in rows:
        f.write("[[" + row[1] + "]]\n")
```
Remember that depnding you want to format this file differenlty depending on your chosen visualization type. In this case the above code is formatting the file to suit the *Obsidian Graph View* visualization. 

2. **point two**

### 4. Vusualizing the data as an interative graph.

There are two ways to visulize the social graph: 
1) Using [Obsidian Graph View](https://help.obsidian.md/Plugins/Graph+view): This XXXXXX
2) Using 


The `csv_to_obsidian.py` takes in a CSV file containing a lot of all people `all_feiends.csv` as well as list of CSV files containing either two rows `Name, profile URL` or a single row `Name`. It then converts all off the files into a file structure that can be directly opened using the Obsidian note taking app. Where the social graph then can be viewed using the built-in graph feature.


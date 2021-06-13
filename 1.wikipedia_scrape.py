import wikipedia as wiki

# TO Search for a term in wikipedia search
print(wiki.search("Programming"))

# TO SEARCH ONLY SPECIFIC NUMBER OF RESULTS
print(wiki.search("Programming",results=4))

# SUGGEST - IT RETURNS THE SUGGESTED WIKIPEDIA TITLE FOR THE QUERY 
# OR NONE IF IT DOESN’T FOUND ANY
print(wiki.suggest('Prog'))

# SUMMARY - It prints the summary of an article
print(wiki.summary('Artificial Intelligence'))

# TO PRINT SUMMARY UPTO PARTICULAR NO OF sentences
print(wiki.summary('Artificial Intelligence',sentences=2))

# To Change the Language of the Article
wiki.set_lang("de")    # de is code for German language
print(wiki.summary("Artificial Intelligence"))

# PAGE - TO PRINT CERTAIN INFO FROM PAGE

p = wiki.page('Artificial Intelligence"')

# To Get the URL of the Article
print("URL : ",p.url)

# To Get the Title of the Article
print("TITLE : ",p.title)

# To Get Complete Article
print("CONTENT : \n",p.content)

# To Get the Images Included in Article
print("IMAGES : \n",p.images)

# To Get the Categories of the Article
print("CATEGORIES: \n",p.categories)

# To Get all links in the page
print("LINKS: \n",p.links)

# To Get the page references
print("REFERENCES: \n",p.references)

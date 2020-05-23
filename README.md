# IMBD Autocomplete

IMBD movie title autocomplete functionality. Given a prefix it will return you some movie suggestions.

Testing for prefixes `A`, `The` & `Wh`
```
Movie: A
['Arigo (2020)', 'Arising Circle (2020)', 'Arisen Revelations (2020)', 'Artist Police (2020)', 'Artificial Twins (2020)', 'Arthur Rambo (2020)', 'Art Explosion (2020)', 'Art Saved My Life - An Interview with Composer Orville Stoeber (2020)', 'Art Be Damned! (2020)', 'Art of the Fantastic: A Journey Into Creation (2020)']
Movie: The
['The Prom (2020)', 'The Promise of Perfume (2020)', 'The Protestants (2020)', 'The Protege (2020)', 'The Protectors (2020)', 'The Professionals (2020)', 'The Prophet and the Space Aliens (2020)', 'The Process (2020)', 'The Prodigal Cowboy (2020)', "The Prisoner's Dilemma (2020)"]
Movie: Wh
['Whatever It Takes The Movie: When Blood Runs Cold (2020)', 'What Do I Do Now? (2020)', "What Doesn't Float (2020)", 'What if it Was Me? (2020)', 'What if I Defect? (2020)', 'What Goes Around (2020)', 'What I Meant to Say Was... (2020)', 'What About the Box? (2020)', 'What About Love (2020)', 'What remains (2020)']
Movie:
```

## Quickstart
> :warning: **Never unpickle an unknown pickle file**: Running these commands does JUST THAT!

Make sure you're using Python >=3.6 - it's 2020, let's get it together.
Install packages:
```
python3 -m pip install pandas
```
Run the program:
```
python3 main.py
```

## Additional Info

Movie titles stored in a trie that can be found in `pkl/sample/IMBD_lookup.pkl` The values in the trie are NOT normalized - i.e. I did not run `title.lower()`. This makes getting suggestions case sensitive. (TODO: fix this).

> :warning: **Never unpickle an unknown pickle file**: Be very careful here!

The `get_suggestions` method on the trie also retrieves movie title IDs and not the titles themselves. This is for disambiguation purposes. There are at least 39 movies with the title "Hamlet" for example
```
hamlet_imbd_ids = ['tt0001240', 'tt0002922', 'tt0004049', 'tt0008040', 'tt0012249', 'tt0040416', 'tt0047060', 'tt0058126', 'tt0058174', 'tt0058175', 'tt0058177', 'tt0064400', 'tt0070147', 'tt0074603', 'tt0093138', 'tt0099726', 'tt0116477', 'tt0171359', 'tt0756216', 'tt0818766', 'tt0992971', 'tt10644774', 'tt12057442', 'tt12150208', 'tt1337626', 'tt1964758', 'tt3123390', 'tt3265782', 'tt4047348', 'tt4052786', 'tt4197632', 'tt4431574', 'tt4448876', 'tt4476736', 'tt4888798', 'tt6555348', 'tt6604466', 'tt7798632', 'tt9703966']
```

Once you have the id you can then use it to generate a more descriptive suggestion. Here I simple use `title + year` stored in a dictionary keyed off the movie id. This dictionary is serialized and stored in `pkl/sample/IMBD_lookup.pkl`

> :warning: **Never unpickle an unknown pickle file**: You don't want to catch a computer virus!

`main.py` loads up the trie and the lookup table and then puts the user in a loop. The user is prompted to give a Movie and suggestions are returned. To avoid a recursive nightmare, only 10 suggestions (roughly) are generated per lookup in the trie.


# File Sorter

 Contains scripts to classify files into defined folders (categories) based on extension, sizes and date-modified.

## Scripts

The scripts that are contained in this directory
####  1. Sort-by-Extension.py

Categorizes all files in a directory to different folders based on their respective file extensions.
####  2. Sort-by-Size.py

Categorizes all files in a directory to different folders based on sizes.
```
XXsmall ---> files in the range 0KB to 1MB

Xsmall ---> files in the range 1MB to 25MB

Small ---> files in the range 25MB to 100MB

Medium ---> files in the range 100MB to 500MB

Large ---> files in the range 500MB to 1GB

Xlarge ---> files in the range 1GB to 50GB

XXlarge ---> files greater than 50GB
```

####  3. Deorganizer.py
Extracts all files in a given directory (and sub-directories) and move them to the provided directory. Then deletes all the empty directories  and sub-directories recursively.

> Does not organize files but only does the reverse.
## Author

* **Oshodi Kolapo** :sunglasses:


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

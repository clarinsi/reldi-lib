# Python library for the ReLDI API

If you do not have access rights, register first at http://nl.ijs.si/services/. At the same URL you can also find a nice web interface for testing the available technologies.

The overall most informative file is the ```main.py``` script.

If you need to tag and lemmatise a file or a directory of files (that have to end in ```.txt```), the ```tag_all.py``` script can come in very handy. On the other hand, if you need diacritic restoration, you should use ```restore_all.py``` with the same interface as ```tag_all.py```.

Here are some examples:

```
python restore_all.py hr file
python tag_all.py hr file.redi
python tag_all.py sr directory/subdirectory
```

# hydrogen-renamer
Script to change the name of Gantry 5 theme. Tested under Python 2.7, Linux.

    usage: hydrogen_renamer.py [-h] theme_zipfile old_name new_name
    
    Change all occurrences of old_name to new_name in Wordpress theme_zipfile
    paths and file contents. The new theme will be saved as new_name.zip
    
    positional arguments:
      theme_zipfile  ZIP file containing a theme to be converted
      old_name       Name of the theme to be changed
      new_name       Name of the new theme
    
    optional arguments:
      -h, --help     show this help message and exit

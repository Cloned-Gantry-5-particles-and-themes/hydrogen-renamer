#!/usr/bin/env python

import zipfile
import os
import sys
import argparse

def name_variations(src_name, tgt_name):
    yield (src_name.lower(), tgt_name.lower())
    yield (src_name.upper(), tgt_name.upper())
    yield (src_name.capitalize(), tgt_name.capitalize())

def replace_in_string(s, src_theme_name, tgt_theme_name):
    for (old, new) in name_variations(src_theme_name, tgt_theme_name):
        s = s.replace(old, new)
    return s

rename_path = replace_in_string
replace_in_content = replace_in_string

def rename_theme(src_file_name, tgt_file_name, src_theme_name, tgt_theme_name):
    compression = zipfile.ZIP_DEFLATED
    with zipfile.ZipFile(src_file_name, "r") as src_zip:
        with zipfile.ZipFile(tgt_file_name, "w", compression) as tgt_zip:
            for src_path in src_zip.namelist():
                tgt_path = rename_path(src_path, src_theme_name, tgt_theme_name)
                src_content = src_zip.read(src_path)

                tgt_content = replace_in_content(src_content,
                                src_theme_name,
                                tgt_theme_name)
                tgt_zip.writestr(tgt_path, tgt_content)
        

def main():
    parser = argparse.ArgumentParser(
        description="Change all occurrences of old_name to new_name " +
            "in Wordpress theme_zipfile paths and file contents. " +
            "The new theme will be saved as new_name.zip")
    parser.add_argument("theme_zipfile", type=str,
            help="ZIP file containing a theme to be converted")
    parser.add_argument("old_name", type=str,
            help="Name of the theme to be changed")
    parser.add_argument("new_name", type=str,
            help="Name of the new theme")
    args = parser.parse_args()

    src_file_name = args.theme_zipfile
    src_theme_name = args.old_name

    tgt_theme_name = args.new_name
    tgt_file_name = str(tgt_theme_name) + ".zip"

    if os.path.exists(tgt_file_name):
        print "File named", tgt_file_name, "already exists.",
        print "Delete this file or choose another name."
        sys.exit(1)

    rename_theme(src_file_name, tgt_file_name, src_theme_name, tgt_theme_name)



if __name__ == "__main__":
    main()



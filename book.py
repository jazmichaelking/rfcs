#!/usr/bin/env python3

"""
This auto-generates the mdBook SUMMARY.md file based on the layout on the filesystem.

This generates the `src` directory based on the contents of the `text` directory.

Most RFCs should be kept to a single chapter. However, in some rare cases it
may be necessary to spread across multiple pages. In that case, place them in
a subdirectory with the same name as the RFC. For example:

    0123-my-awesome-feature.md
    0123-my-awesome-feature/extra-material.md

It is recommended that if you have static content like images that you use a similar layout:

    0123-my-awesome-feature.md
    0123-my-awesome-feature/diagram.svg

The chapters are presented in sorted-order.
"""
import sys
import os
import shutil
import subprocess
import signal

def main():
    if len(sys.argv) == 1 or sys.argv[1] == 'generate':
        generate()
    elif sys.argv[1] == 'preview':
        preview()
    elif sys.argv[1] == 'clean':
        clean()
    else:
        print('Unknown command, expected one of: generate, preview, clean')
        exit(1)

def generate():
    checkTools()
    clean()
    createFileLink('README.md', 'src/introduction.md')

    for path in os.listdir('text'):
        if path == ".gitkeep" or path == "README.md":
            continue
        createFileLink(f'text/{path}', f'src/{path}')
    
    with open('src/SUMMARY.md', 'w') as summary:
        summary.write('[Introduction](introduction.md)\n\n')
        collect(summary, 'text', 0)

    subprocess.call(['mdbook', 'build'])

def clean():
    if not os.path.exists('src'):
        return

    for path in os.listdir('src'):
        if path == ".gitignore":
            continue
        elif os.path.isdir(f'src/{path}'):
            shutil.rmtree(f'src/{path}')
        else:
            os.remove(f'src/{path}')

def preview():
    generate()
    checkTools()

    try:
        subprocess.call(['mdbook', 'serve'])
    except KeyboardInterrupt:
        print(" exiting...")

#
# Helpers:
#
def checkTools():
    if not shutil.which('mdbook'):
        print("Could not locate mdbook executable, please see: https://rust-lang.github.io/mdBook/guide/installation.html")
        exit(1)

def collect(summary, path, depth):
    entries = [e for e in os.scandir(path) if e.name.endswith('.md')]
    entries.sort(key=lambda e: e.name)

    for entry in entries:
        indent = '    '*depth
        name = entry.name[:-3]
        link_path = entry.path[5:]
        summary.write(f'{indent}- [{name}]({link_path})\n')
        maybe_subdir = os.path.join(path, name)
        if os.path.isdir(maybe_subdir):
            collect(summary, maybe_subdir, depth+1)

def createFileLink(src, dst):
    if not os.path.exists(dst):
        os.link(os.path.abspath(src), dst)

if __name__ == '__main__':
    main()

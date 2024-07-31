# Über diese Seite

Dies ist der Quellcode um die deutsche Version des Sonic-Pi Tutorials als Offline / Standalone-Version zu generieren.

Hier ist es:
https://tillylab.github.io/sonic-pi-tutorial

Das Original (englische Version) befindet sich hier:
https://sonic-pi.net/tutorial.html

Ich habe die HTML-Seite mit Hilfe von [MkDocs](https://www.mkdocs.org/) aus der (deutschen) Markdown-Version des Tutorials erstellt.

Das Tutorial wurde von Sam Aaron unter der  [CC BY-SA 4.0 Lizenz](LICENSE.md) veröffentlicht.

# About this Page

This is the source code to generate the German version of the Sonic-Pi tutorial as offline / standalone version.

Here it is:
https://tillylab.github.io/sonic-pi-tutorial

The (english language) original can be found here:
https://sonic-pi.net/tutorial.html

I have created the HTML-Page with the help of [MkDocs](https://www.mkdocs.org/) from the (German localized) markdown of the tutorial.

The tutorial is copyright by Sam Aaron and has been released under the [CC BY-SA 4.0 License](LICENSE.md).

# Howto

This is how to do it (in case you want to roll your own localized version ...)

## 1. Get the translated Files.

I used the localized version of the markdown files, generated by Sonic-Pi.
In OSX they can be found at  `/Applications/Sonic Pi.app/Contents/Resources/etc/doc/generated/de`. Where `de` is for German language files. If you want to recreate a version for your own language, look for the appropriate folder.

## 2. Create a single markdown file

I wrote a short python script to create a single file from all the markdown files:

```sh
python ./src/onefile-maker.py
```

## 3. Create a custom_theme folder

I ruthlessly stole all HTML, CSS, JS from https://sonic-pi.net/tutorial.html with the goal of recreating a localized version of this page.

The images are from the docs folder distributed with the current version of Sonic Pi. (On OSX: 
`/Applications/Sonic Pi.app/Contents/Resources/etc/doc/images/tutorial`)

Those files reside in the `src/custom_theme` folder and are copyright Sam Aaron (!).

The previous step also creates a table of contents which I inserted (manually) into `src/custom_theme/main.html`.

## 4. Install mkdocs

I used `mkdocs` to create the page from the costom theme and the markdown. 

First make sure to install mkdocs (possibly inside a python virtual env).

```sh
pip install mkdocs
```

## 5. Build the site

Ready to rock:

```sh
mkdocs build -f src/mkdocs.yml
```

Your shiny new localized sonic pi tutorial is now inside the `site` folder 😀.
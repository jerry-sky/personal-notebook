#!/bin/bash

pandoc "$1" \
    --mathjax='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' \
    --standalone \
    --from markdown+yaml_metadata_block \
    --to html \
    --template deployment/pandoc-template.html \
    --css '/deployment/style.css' \
    -H deployment/head.html

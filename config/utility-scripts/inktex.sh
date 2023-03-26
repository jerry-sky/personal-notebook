#!/bin/bash

# converts a SVG file to a format that is digestible by LaTeX
bn="$1"
bn="${bn%.*}"
inkscape -D -z --file="$bn.svg" --export-pdf="$bn.pdf" --export-latex

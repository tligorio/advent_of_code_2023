#!/bin/bash

case "$1" in
    "readme")
        python generate_readme.py && cp README.md /app/output/
        ;;
    "templates")
        python generate_file_templates.py
        ;;
    "scrape")
        python puzzle_scraper.py
        ;;
    *)
        echo "Usage: $0 {readme|templates|scrape}"
        exit 1
        ;;
esac 
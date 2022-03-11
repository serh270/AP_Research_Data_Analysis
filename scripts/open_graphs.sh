#!/bin/bash

echo "beginning tabulations"
python3.10 TAScalc.py
python3.10 graph_age.py
python3.10 graph_genre.py
python3.10 graph_genre_num.py
python3.10 graph_hrs_gaming.py

echo "tabulation complete. Opening graphs"
open graph_age.png
open graph_genre.png
open graph_genre_num.png
open graph_hrs_gaming.png

#!/bin/bash
fswatch -o ./blog | while read f; do
    python run_template.py
done
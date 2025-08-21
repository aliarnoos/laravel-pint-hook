#!/bin/bash
if [ ! -f "./vendor/bin/pint" ]; then
    echo "Laravel Pint not found. Run 'composer install' first."
    exit 1
fi

./vendor/bin/pint
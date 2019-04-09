#!/bin/bash

INPUTDIR="$1"
OUTPUTDIR="$2"

find "$INPUTDIR" -type f -name "*.tar.gz" -print0 | while IFS= read -r -d '' f
do

    mkdir -p "$OUTPUTDIR/tmp"
    pushd "$OUTPUTDIR/tmp"

    tar -zxvf "$f"

    find . -type f -name "*.mtx" -print0 | while IFS= read -r -d '' g
    do
        NAME="$(basename "$g")"

        gzip "$g"

        mv "$g.gz" "$OUTPUTDIR/$NAME.gz"
    done

    popd
    rm -rf "$OUTPUTDIR/tmp"

done
pandoc 01-amarel-setup.md \
    -o amarel-tutorial.pdf \
    --pdf-engine=xelatex \
    --lua-filter=pandoc-title.lua \
    --include-in-header=pandoc-header.tex \
    --toc \
    --toc-depth=2
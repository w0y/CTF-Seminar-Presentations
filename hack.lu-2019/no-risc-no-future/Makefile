SOURCES = $(wildcard *.md)
TARGETS = $(SOURCES:.md=.html)
DEP = $(wildcard *.sty *.jpg *.png) reveal.js

all: $(TARGETS)

%.html : %.md $(DEP)
	pandoc -s $< -t revealjs -o $@ -V revealjs-url=./reveal.js

reveal.js:
	git clone https://github.com/hakimel/reveal.js/

clean:
	@rm -rf $(TARGETS) reveal.js

# whether to use pdflatex (true) or latex (false)
PDF = true
# anything ending in .tex is a potential target
TARGETS = $(patsubst %.tex, %, $(wildcard *.tex) )
# which target to build by default
CURRTARGET = hw4template

ifeq ($(PDF), true) 
	EXTENSION = pdf
	LATEX = pdflatex
	VIEWER = evince
else 
	EXTENSION = dvi
	LATEX = latex
	VIEWER = xdvi
endif
BIBTEX= bibtex

OUTDIR = ./output
FLAGS = -file-line-error -interaction nonstopmode -output-directory=$(OUTDIR)
BIB_FLAGS = $(OUTDIR)/

# default target; build the document referenced by the CURRTARGET variable
default: $(CURRTARGET)

all: $(TARGETS)

# wildcard rule, so you can just do `make myfilename` without needing a
# special target for every file
%: %.tex | $(OUTDIR)
	$(LATEX) $(FLAGS) $@.tex; \
	$(BIBTEX) $(BIB_FLAGS)$@; \
	$(LATEX) $(FLAGS) $@.tex; \
	$(LATEX) $(FLAGS) $@.tex; 
# Note that we do latex, followed by bibtex, followed by latex two more times.
# The first call builds the document and figures out what references are needed,
# the call to bibtex builds the bibliography items,
# the next call to latex adds the bibliography to the document,
# and the final call fills in the correct references for your \cite{} commands


# convert to postscript 
ps:
ifeq ($(PDF), true)
	pdf2ps $(OUTDIR)/$(CURRTARGET).pdf $(OUTDIR)/$(CURRTARGET).ps 
else
	dvips -o $(OUTDIR)/$(CURRTARGET).ps $(OUTDIR)/$(CURRTARGET).dvi
endif

# convert to PDF
pdf:
ifeq ($(PDF), true)
	#nothing to do
else
	dvipdf $(OUTDIR)/$(CURRTARGET).dvi ; mv $(CURRTARGET).pdf $(OUTDIR) & 
endif

# make sure the output directory exists
$(OUTDIR):
	mkdir $(OUTDIR)

# display current target
view:
	$(VIEWER) $(OUTDIR)/$(CURRTARGET).$(EXTENSION) &

# clean up auxiliary output files
clean:
	@echo Cleaning auxiliary files...
	@for i in *.log *.blg *.dvi *.aux *.bbl *.out *~; \
		do rm -f $$i $(OUTDIR)/$$i; \
		done; \

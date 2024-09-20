# Makefile para compilar o documento LaTeX

# Nome do arquivo principal (sem a extensão .tex)
MAIN = resolution

# Comando para compilar o documento LaTeX
LATEX_COMPILER = pdflatex

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEX_COMPILER) $(MAIN).tex
	$(LATEX_COMPILER) $(MAIN).tex  # É necessário compilar duas vezes para atualizar referências

clean:
	rm -f $(MAIN).pdf $(MAIN).aux $(MAIN).log $(MAIN).out

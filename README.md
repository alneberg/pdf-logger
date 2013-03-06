pdf-logger
==========

Log your experiment scripts and result figures directly to a nicely formatted pdf.

Proposed Syntax
---------------
###Initalizing your logger

    pdf-logger init "Title of log file"


###New Section

    pdf-logger section "Section header"

###New Subsection

    pdf-logger subsection "Subsection header"

###Adding script to logger

    pdf-logger add my-script-file [HEADER] [CAPTION] --results my-result-files

The first file format to be supported for result files is png.

###View the log file

    pdf-logger view-log [TITLE]


Dependencies
------------
    LaTeX, python version 2.7, pdflatex
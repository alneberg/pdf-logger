import os

def init(args):
    log_dir = os.path.join(args.dir,'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_name = title_to_file_name(args.title)
    log_file_path = os.path.join(log_dir,log_file_name)
    log_file = open(log_file_path, 'w+')
    log_file.write(latex_template(args.title,args.author))
    log_file.close()

def title_to_file_name(title):
    return "_".join([string.lower() for \
                         string in title.split(" ")]) + "_log.tex"

def latex_template(title, author):
    return  r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}

\usepackage[fleqn]{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{listings}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage[font=small, margin=40]{caption}
\usepackage[left=1in,top=1in,right=1in,bottom=1in,nohead, vmargin=8em, hmargin=8em]{geometry}

\lstset{columns=fullflexible,basicstyle=\ttfamily}

\renewcommand{\P}[1]{\operatorname{P}\!\left( #1 \right)}
\newcommand{\Id}{\operatorname{Id}}
\renewcommand{\log}{\operatorname{log}}
\renewcommand{\exp}{\operatorname{exp}}

\begin{document}
\title{""" + title +r"}" + r"""
\author{""" + author +r"}" + """

\maketitle
\end {document}"""


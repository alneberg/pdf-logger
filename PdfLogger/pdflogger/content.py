def section(args):
    args.log_file.write(r"\section{0}{2}{1}".format("{","}",args.header))

def subsection(args):
    args.log_file.write(r"\subsection{0}{2}{1}".format("{","}",args.header))

def add_content(args):
    print args.script_file

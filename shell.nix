with import <nixpkgs> {};
mkShell {
  name = "actions-planning";
  buildInputs = [
    (python3.withPackages (ps: with ps; [
      ipython
      jupyter
      matplotlib
      networkx
      nltk
      numpy
      tabulate
    ]))
  ];
}


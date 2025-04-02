let pkgs = import <nixpkgs> { };
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (p: [
      p.pandas
      p.seaborn
      p.matplotlib
      p.geopandas
      p.shapely
      p.geodatasets
      p.plotly
      p.scikit-learn
    ]))
  ];
}

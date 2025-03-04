{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs.buildPackages; [
    python3
    python3Packages.pip
    python3Packages.pytest
    python3Packages.flask
    python3Packages.flask-cors
    nodejs
  ];
}


{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [
    paho-mqtt
    pytest
    requests
    cryptography
    sqlalchemy
    psycopg2
    python-dotenv
    pandas
    matplotlib
  ]);
in
pkgs.mkShell {
  buildInputs = [
    pythonEnv
    pkgs.git
    pkgs.openssl
    pkgs.postgresql
  ];

  shellHook = ''
    echo "🚀 IoT Simulator Dev Shell Ready"
    export PYTHONPATH=$PWD/src:$PYTHONPATH
  '';
}

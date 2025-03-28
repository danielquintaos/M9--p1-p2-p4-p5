{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = pkgs.python3.withPackages (ps: with ps; [
    paho-mqtt
    pytest
    python-dotenv
    sqlalchemy
    psycopg2
    requests
    cryptography
    pandas
  ]);
in
pkgs.mkShell {
  buildInputs = [
    pythonPackages
    pkgs.openssl
    pkgs.postgresql
    pkgs.git
  ];

  shellHook = ''
    echo "💡 IoT Simulator Dev Shell Ready"
    export PYTHONPATH=$PWD/src:$PYTHONPATH
  '';
}

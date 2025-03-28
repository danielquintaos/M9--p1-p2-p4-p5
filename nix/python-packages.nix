{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildEnv.override {
  extraLibs = with pkgs.python3Packages; [
    paho-mqtt
    pytest
    python-dotenv
    sqlalchemy
    psycopg2
    cryptography
    pandas
    requests
  ];
}

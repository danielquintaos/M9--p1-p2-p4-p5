{
  description = "IoT Simulator with MQTT, HiveMQ TLS, and Metabase Integration";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };

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

      in {
        devShells.default = pkgs.mkShell {
          name = "iot-simulator-env";
          buildInputs = [
            pythonEnv
            pkgs.git
            pkgs.openssl
            pkgs.postgresql
            pkgs.docker

          ];

          shellHook = ''
            echo "🚀 Welcome to the IoT Simulator Dev Shell"
            export PYTHONPATH=$PWD/src:$PYTHONPATH
          '';
        };
      });
}

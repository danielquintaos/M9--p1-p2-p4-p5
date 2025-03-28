{ pkgs, lib, config, ... }:

{
  services.postgresql = {
    enable = true;
    package = pkgs.postgresql_15;
    initialScript = pkgs.writeText "init.sql" ''
      CREATE USER iot_user WITH PASSWORD 'password';
      CREATE DATABASE iot_data OWNER iot_user;
    '';
    authentication = ''
      local   all             all                                     trust
      host    all             all             127.0.0.1/32            trust
      host    all             all             ::1/128                 trust
    '';
  };
}

{
  description = "cover-letter-llm";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells = {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              pkgs.python313
              pkgs.poetry
            ];

            shellHook = ''
              poetry env use "${pkgs.python313}/bin/python3"
              poetry install
              poetry run playwright install --with-deps chromium
            '';
          };
        };
      });
}

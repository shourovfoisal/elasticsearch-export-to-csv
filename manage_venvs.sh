#!/bin/bash

VENV_DIR="$HOME/venvs"
mkdir -p "$VENV_DIR"

list_venvs() {
  echo "Directory: $VENV_DIR"
  echo "-------- List ---------"
  ls -1 "$VENV_DIR"
}

create_venv() {
  if [ -z "$1" ]; then
    echo "VENV name is reqired"
    exit 1
  fi
  VENV_NAME=$1
  if [ -d "$VENV_DIR/$VENV_NAME" ]; then
    echo "$VENV_NAME already exists."
  else
    python3 -m venv "$VENV_DIR/$VENV_NAME"
    echo "$VENV_NAME created."
    list_venvs
  fi
}

delete_venv() {
  if [ -z "$1" ]; then
    echo "VENV name is required"
    exit 1
  fi
  VENV_NAME=$1
  if [ -d "$VENV_DIR/$VENV_NAME" ]; then
    rm -rf "$VENV_DIR/$VENV_NAME"
    echo "$VENV_NAME deleted"
    list_venvs
  else
    echo "$VENV_NAME does not exist."
  fi
}

case "$1" in
  create)
    create_venv "$2"
    ;;
  delete)
    delete_venv "$2"
    ;;
  list)
    list_venvs
    ;;
  *)
    echo "Example usage"
    echo "./manage_venvs.sh create <env-name>"
    echo "Or by using alias"
    echo "venvwizard create <env-name>"
    ;;
esac
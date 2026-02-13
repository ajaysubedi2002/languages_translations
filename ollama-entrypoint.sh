#!/bin/sh
set -e

ollama serve &

echo "Waiting for Ollama to be ready..."
# Wait until the CLI can talk to the server
until ollama list >/dev/null 2>&1; do
  sleep 1
done

echo "Ollama is ready."

# Pull models from env (skip if not set)
if [ -n "${Translate_model:-}" ]; then
  echo "Ensuring translate model exists: $Translate_model"
  ollama pull "$Translate_model" || echo "Failed to pull $Translate_model"
fi

echo "Done. Ollama running."
wait
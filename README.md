# API Key Vault

A local-first, single-page API Key Vault application.
Built with Vanilla HTML, CSS, and JS. 

## Features
- **Local First**: All keys are stored securely in your browser's `localStorage` via the Web Crypto API (`AES-GCM` + `PBKDF2`).
- **Auto-Import**: The bundled Python server automatically ingests local `.env` files securely into your vault upon unlocking.
- **AI Assistant**: Connects to a local Ollama instance (defaulting to `llama3`) running on `localhost:11434` for automatic key categorization and intelligent auditing.
- **Auto-Clearing Clipboard**: API keys copied to the clipboard are automatically erased after 30 seconds to prevent accidental pasting.
- **Beautiful UI**: Modern glassmorphism design with animated backgrounds and subtle micro-animations.

## Getting Started

1. Clone this repository.
2. Run the custom backend server to enable auto-import and static file hosting:
```bash
python3 server.py
```
3. Open your browser and navigate to `http://localhost:8000`.
4. Enter a Master Password to initialize your vault!

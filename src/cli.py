from __future__ import annotations

import sys
from collections.abc import Iterable

from dotenv import load_dotenv


def _normalize_content(content: object) -> str:
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str) and item:
                parts.append(item)
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text")
                if text:
                    parts.append(str(text))
        return "\n".join(parts).strip()

    return str(content)


def _extract_stream_text(content: object) -> str:
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str) and item:
                parts.append(item)
            elif isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text")
                if text:
                    parts.append(str(text))
        return "".join(parts)

    return ""


def _iter_stream_events(stream: Iterable[object]) -> tuple[str, list[dict[str, str]] | None]:
    assistant_parts: list[str] = []
    final_messages: list[dict[str, str]] | None = None
    started_output = False

    for event in stream:
        if not isinstance(event, tuple) or len(event) != 2:
            continue

        mode, payload = event
        if mode == "messages":
            if not isinstance(payload, tuple) or not payload:
                continue

            message_chunk = payload[0]
            text = _extract_stream_text(getattr(message_chunk, "content", ""))
            if text:
                if not started_output:
                    print("\rAgente: ", end="", flush=True)
                    started_output = True
                print(text, end="", flush=True)
                assistant_parts.append(text)

        elif mode == "values" and isinstance(payload, dict):
            raw_messages = payload.get("messages")
            if isinstance(raw_messages, list):
                final_messages = [
                    {
                        "role": message.type,
                        "content": _normalize_content(message.content),
                    }
                    for message in raw_messages
                    if hasattr(message, "type") and hasattr(message, "content")
                ]

    return "".join(assistant_parts).strip(), final_messages


def main() -> None:
    load_dotenv()
    try:
        from src.agente import hawk
    except ImportError as exc:
        print("Erro ao carregar o agente.")
        print(
            "Verifique se as dependencias foram instaladas com `pip install -r requirements.txt`."
        )
        print(f"Detalhe tecnico: {exc}")
        sys.exit(1)

    messages: list[dict[str, str]] = []

    print("Agente iniciado. Digite sua mensagem.")
    print("Use 'exit' ou 'quit' para encerrar.\n")

    while True:
        user_input = input("Você: ").strip()
        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Encerrando.")
            break

        messages.append({"role": "user", "content": user_input})
        try:
            print("Pensando...", end="", flush=True)
            assistant_text, final_messages = _iter_stream_events(
                hawk.stream({"messages": messages}, stream_mode=["messages", "values"])
            )
        except Exception as exc:
            print("Erro ao executar o agente.")
            print(
                "Confira se `GOOGLE_API_KEY` esta definida no arquivo `.env` e se o ambiente esta configurado."
            )
            print(f"Detalhe tecnico: {exc}\n")
            continue

        if not assistant_text:
            print("\rAgente: (sem resposta visivel)", end="")

        print("\n")
        if final_messages is not None:
            messages = final_messages


if __name__ == "__main__":
    main()

import re
from ollama import chat
from typing import Generator

SERVICE_COLORS = {
    "10": "#007bff",  # Blue
    "27": "#d39e00",  # Yellow/Brown
    "22": "#218838",  # Green
    "31": "#6f42c1",  # Purple
    "19": "#c82333",  # Red
    "7F": "#6c757d",  # Grey
}

def identify_service(frame: str) -> str:
    match = re.search(r"\b(10|27|22|31|19|7F)\b", frame, re.IGNORECASE)
    return match.group(1).upper() if match else "GEN"

def stream_can_trace(trace: str) -> Generator[str, None, None]:
    with open("prompt_template.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = template.replace("{$CAN_TRACE$}", trace.strip())

    response = chat(
        model="mistral:7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in response:
        if "content" in chunk["message"]:
            yield chunk["message"]["content"]

def parse_streamed_trace(trace: str) -> Generator[dict, None, None]:
    buffer = ""
    for token in stream_can_trace(trace):
        buffer += token
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            if not line.strip():
                continue
            service = identify_service(line)
            yield {
                "content": line.strip(),
                "color": SERVICE_COLORS.get(service, "#FFFFFF")  # Default black
            }

    if buffer.strip():
        service = identify_service(buffer)
        yield {
            "content": buffer.strip(),
            "color": SERVICE_COLORS.get(service, "#FFFFFF")
        }

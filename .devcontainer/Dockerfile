FROM python:3.12
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir uv \
    && useradd -m -u 1000 -s /bin/bash vscode
USER vscode
WORKDIR /workspaces
# Build stage: produce the wheel
FROM python:3.10.21-alpine3.24 AS builder

WORKDIR /build

COPY pyproject.toml ./
COPY src/ ./src/

RUN pip install --no-cache-dir build \
    && python -m build

# Runtime stage: expose only the dist directory
FROM scratch

COPY --from=builder /build/dist /dist

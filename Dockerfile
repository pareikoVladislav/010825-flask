FROM debian:12.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*


RUN useradd -ms /bin/bash appuser
WORKDIR /app
ENV EXAMPLE_LINC=https://example.com \
    TARGET=/data
COPY --chown=appuser:appuser datafetcher.sh .
RUN mkdir -p /data && \
    chown -R appuser:appuser /data && \
    chmod +x datafetcher.sh

VOLUME /data
USER appuser


ENTRYPOINT ["/app/datafetcher.sh"]
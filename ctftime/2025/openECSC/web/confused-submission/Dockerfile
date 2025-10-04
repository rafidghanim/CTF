FROM oven/bun:1

WORKDIR /app

COPY package.json bun.lock ./
RUN bun install

RUN bunx playwright install chromium
RUN bunx playwright install-deps

COPY . .

EXPOSE 3000

ENV FLAG=flagge{standard_docker_flagge}

CMD ["bun", "run", "src/index.ts"]

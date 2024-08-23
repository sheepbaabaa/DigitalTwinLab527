# 使用最新的官方 Node.js 镜像作为基础镜像，并命名为 `builder` 阶段
FROM node:18.18-slim AS builder

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的工作目录 `/app` 中
COPY . .

# 在容器中安装项目依赖
RUN npm install

# 在容器中构建项目
RUN npm run build

# 使用轻量级的官方 Nginx 镜像作为基础镜像
FROM nginx:alpine

# 时区
ENV TZ=Asia/Shanghai


# `builder` 阶段中复制构建好的文件到 Nginx 容器的网页根目录 `/usr/share/nginx/html`
COPY --from=builder /app/dist /etc/nginx/html

# 本地的 `nginx.conf` 文件复制到容器的 `/etc/nginx/conf.d/default.conf`
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

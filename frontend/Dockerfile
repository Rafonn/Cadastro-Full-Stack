# --- Estágio 1: Build ---
# Usa uma imagem do Node para construir a aplicação Angular
FROM node:20-alpine AS builder

WORKDIR /app

# Copia os arquivos de configuração de pacotes
COPY package.json package-lock.json ./

# Instala as dependências do Node
RUN npm install

# Copia o resto do código do frontend
COPY . .

# Executa o build de produção do Angular
RUN npm run build

# --- Estágio 2: Produção ---
# Usa uma imagem leve do Nginx para servir os arquivos
FROM nginx:1.25-alpine

# Remove a configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia a nossa configuração personalizada do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos construídos do estágio 'builder' para o diretório do Nginx
COPY --from=builder /app/dist/frontend/browser /usr/share/nginx/html

# Expõe a porta 80, que é a padrão do Nginx
EXPOSE 80
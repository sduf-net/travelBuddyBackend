FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl git
RUN curl -sfL https://direnv.net/install.sh | bash
RUN echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
# Optionally, ensure that .bashrc is sourced in non-interactive shells
RUN echo 'source ~/.bashrc' >> ~/.bash_profile

# Set working directory inside the container
WORKDIR /workspace

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

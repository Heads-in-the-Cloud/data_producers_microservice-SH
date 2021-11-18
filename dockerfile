FROM utopia_base

WORKDIR /app
COPY . /app

# RUN python app.py
# RUN flask db init
# RUN flask db migrate -m "Initial migration."
# RUN flask db upgrade
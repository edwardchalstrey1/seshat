FROM postgis/postgis
RUN echo "max_locks_per_transaction = 256" >> /var/lib/postgresql/data/postgresql.conf
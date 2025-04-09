-- PostgreSQL script de creation de la base de données


-- Créer la base de données
CREATE DATABASE blog;

-- Créer l'utilisateur avec un mot de passe sécurisé
CREATE USER blogadmin WITH ENCRYPTED PASSWORD '123456';

-- Configurer les paramètres de l'utilisateur
ALTER ROLE blogadmin SET client_encoding TO 'UTF8';
ALTER ROLE blogadmin SET default_transaction_isolation TO 'read committed';

-- Donner tous les privilèges sur la base de données
GRANT ALL PRIVILEGES ON DATABASE blog TO blogadmin;

-- Autoriser blogadmin à créer des bases de données si nécessaire
ALTER USER blogadmin CREATEDB;

-- Donner l'accès et les permissions de création sur le schéma public
GRANT USAGE, CREATE ON SCHEMA public TO blogadmin;
GRANT ALL ON SCHEMA public TO blogadmin;

-- Configurer les permissions par défaut pour les objets futurs
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO blogadmin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO blogadmin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO blogadmin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TYPES TO blogadmin;




-- Création de super user coté django
(.env) D:\Projet\website\src>python manage.py createsuperuser
Nom d’utilisateur (leave blank to use 'benjaminmupanzi'):
Adresse électronique: benjaminmupanzi@gmail.com
Password:123456
Password (again):123456
Ce mot de passe est trop court. Il doit contenir au minimum 8 caractères.
Ce mot de passe est trop courant.
Ce mot de passe est entièrement numérique.
Bypass password validation and create user anyway? [y/N]: Y
Superuser created successfully.

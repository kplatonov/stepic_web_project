# stepic_web_project

git clone https://github.com/kplatonov/stepic_web_project.git /home/box/web
bash /home/box/web/init.sh

for start nginx change path in ... etc/nginx.conf (sic! run under root => root home dir)

sudo gunicorn --pythonpath /home/box/web --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application  &
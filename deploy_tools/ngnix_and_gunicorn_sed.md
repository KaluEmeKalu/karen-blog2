# Ngnix

## Create our Nginx virtual host

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/karen-blog.100djangoapps.com/g" \
    | sudo tee /etc/nginx/sites-available/karen-blog.100djangoapps.com

## Activate File With symlink

sudo ln -s /etc/nginx/sites-available/karen-blog.100djangoapps.com \
    /etc/nginx/sites-enabled/karen-blog.100djangoapps.com

# Gunicorn

## Write Systemd Service

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/karen-blog.100djangoapps.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-karen-blog.100djangoapps.com.service

# Start Both Services

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-karen-blog.100djangoapps.com
sudo systemctl start gunicorn-karen-blog.100djangoapps.com

# Git Tag

git tag LIVE
export TAG=$(date +DEPLOYED-%F/%H%M)  # this generates a timestamp
echo $TAG # should show "DEPLOYED-" and then the timestamp
git tag $TAG
git push origin LIVE $TAG # pushes the tags up

# How to Deploy With Fab Command

fab deploy:host=kalu@superlists-staging.bigballerbook.com -u kalu
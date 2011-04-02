# post_update script for actions to be taken during a deploy

# generate the site
echo "building site..."
/var/lib/gems/1.8/bin/jekyll


# copy to web dir
echo "copying to /var/www/"
sudo cp -R _site/* /var/www/
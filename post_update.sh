# post_update script for actions to be taken during a deploy

# generate the site
/var/lib/gems/1.8/bin/jekyll
cp -R _site/* /var/www/
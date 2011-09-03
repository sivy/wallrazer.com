# post_update script for actions to be taken during a deploy

# generate the site
echo "building site..."
export PATH="$PATH:/var/lib/gems/1.8/bin/"
jekyll

cp -R $BUILD_DIR/* $DEST_DIR/
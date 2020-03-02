# install the standard version
cd ~/Downloads
npm install mermaid.cli

cp ~/notebooks/personal-notebook/config/mermaid/index.bundle.js ~/Downloads/node_modules/mermaid.cli/

sudo ln -s ~/Downloads/node_modules/.bin/mmdc /usr/bin/mermaid

echo "Done."

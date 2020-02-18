if [ -d ~/.config/nvim ] ; then
    cp ./nvim/init.vim ~/.config/nvim/
  else
    _print_error "No ~/.config/nvim directory"
  fi

printf " + copied NVim init file"

# TDD-neovim
neovim plugin which help me to build/run GTest.

add to plugin
-------------

```vimrc
function! DoRemote(arg)
  UpdateRemotePlugins
endfunction

Plug 'wow2006/TDD-neovim', { 'do': function('DoRemote') }
```


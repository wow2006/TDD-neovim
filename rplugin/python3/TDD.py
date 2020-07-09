import neovim


@neovim.plugin
class TDD():
    def __init__(self, vim):
        self.vim = vim
        self.vim.err_write("TDD")


# deoplete-emoji

`Deoplete-emoji` offers asynchronous completion of emoji codes. You can add emoji to your writing by typing `:EMOJICODE:`.
For a full list of available emoji and codes, see [emoji-cheat-sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/).

## Installation

To install `deoplete-emoji`, use your favorite [Neovim](https://neovim.io/) plugin manager.

#### Using [vim-plug](https://github.com/junegunn/vim-plug)

```vim
Plug 'Shougo/deoplete.nvim', {'do': ':UpdateRemotePlugins'}
Plug 'fszymanski/deoplete-emoji'
```

## Configuration

```vim
" Default: ['gitcommit', 'markdown']
call deoplete#custom#set('emoji', 'filetypes', ['markdown', 'rst'])
```

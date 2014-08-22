if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

let s:scriptdirpy = expand("<sfile>:h") . '/'
exec 'pyfile ' . s:scriptdirpy . 'misc.py'

function! s:FuncFormat()
  py func_format()
endfunc

command! FuncFormat :call s:FuncFormat()
nmap <F8> :FuncFormat<cr>

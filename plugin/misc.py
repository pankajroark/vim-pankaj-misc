import vim, re

# Returns a list of split params
def split_params(params_str):
  state = 0
  brackets = 0
  parts = []
  last_start = 0

  for i, c in enumerate(params_str):
    if state == 0:
      if c == ',':
        parts.append(params_str[last_start:i + 1])
        last_start = i + 1

      elif c == '[':
        brackets += 1
        state = 1

    elif state == 1: # square bracket
      if c == '[':
        brackets += 1
      elif c == ']':
        brackets -= 1
        if brackets == 0:
          state = 0
  parts.append(params_str[last_start:i + 1])
  return parts


  #return  params_str.split(',')


def func_format():
  line = vim.current.line
  pos = vim.current.window.cursor
  row = pos[0]
  col = pos[1]
  m = re.search('(.*)\((.*)\)(.*)', line)
  if m:
    prefix = m.group(1) + '(\n'
    leading_space = len(line) - len(line.lstrip())
    b = vim.current.buffer
    shift_width = b.options["shiftwidth"]
    params_leading_space = ' ' * (leading_space + shift_width)
    params =  split_params(m.group(2))
    stripped_params = [ p.strip() for p in params ]
    #mparams = [p + ',' for p in stripped_params[:-1]] + [stripped_params[-1]]
    shifted_params = [ params_leading_space + p for p in stripped_params ]
    suffix = (' '* leading_space) + ')' + m.group(3)
    b[row-1] = prefix
    b[row:row] = shifted_params + [ suffix ]




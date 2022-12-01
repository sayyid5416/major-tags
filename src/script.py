import os
from typing import Literal




def env(name:str, _def=''):
    return os.environ.get(name, _def)


def set_output(key:str, value:str):
    with open(env('GITHUB_OUTPUT'), 'a') as f:
        f.write(f'{key}={value}')


def set_annotation(
    message:str,
    title:str=None,
    _type:Literal['debug', 'notice', 'warning', 'error']='notice',
):
    title = f' title={title}' if title else ''
    print(f'::{_type}{title}::{message}')
    if _type == 'error':
        exit(1)




# Collect data
refName = env('GITHUB_REF_NAME')                                                    # [tag-version, branch-name, PR name, .....]
refType = env('GITHUB_REF_TYPE')                                                    # [tag, branch, PR, ....]


# Checks
errorTitle, errorMsg = '', ''
if refType != 'tag': 
    set_annotation(
        f'"{refType}" type is not supported. Run for tags only.',
        'Unsupported Type',
        'error'
    )


# Parsing
majorTag = refName.split('.', 1)[0]                                                 # Tag name like v1, v2 etc


# Set output
set_output('REF_NAME', refName)
set_output('MAJOR_VER', majorTag)

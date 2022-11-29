import os


def env(name:str):
    return os.environ.get(name, '')


# Collect data
refName = env('GITHUB_REF_NAME')                                                    # [tag-version, branch-name, PR name, .....]
refType = env('GITHUB_REF_TYPE')                                                    # [tag, branch, PR, ....]

# Checks
errorTitle, errorMsg = '', ''
if refType != 'tag': 
    errorTitle = 'Unsupported Type'
    errorMsg = f'\\"{refType}\\" type is not supported. Run for tags only.'

# Show error
if errorTitle: errorTitle = f' title={errorTitle}'
if errorMsg:
    os.system(f'echo "::error{errorTitle}::{errorMsg}"')
    exit(1)

# Parsing
majorTag = refName.split('.', 1)[0]                                                 # Tag name like v1, v2 etc

# Set output
os.system(f'echo "REF_NAME={refName}" >> $GITHUB_OUTPUT')
os.system(f'echo "MAJOR_VER={majorTag}" >> $GITHUB_OUTPUT')
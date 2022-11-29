# About
GitHub Action to add/update the major tags for any repository based on its minor tags
  - Like if you have a release/tag with tag `v2.3.5`
  - It could be accessed by major version tag `@v2`
  - All future releases/tags with `@2.*.*`  could be accessed by `@v2`
  - You can also access the specific releases/tags by full tag like `@v2.3.5`


<br>


# Example usage
```bash
name: Update Major Version

on:
  release:
    types:
      - released                        # When new version of your action is released
  workflow_dispatch:                    # To run manually on any tag

jobs:
  update-major-version:
    runs-on: ubuntu-latest
    steps:
      - name: Update major version
        uses: sayyid5416/major-tags@v1
```
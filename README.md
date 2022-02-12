# About

rendercad

computer-aided design for "infrastructure as code" files to be used on [Render](https://render.com).

**THIS IS EXPERIMENTAL SOFTWARE AND SHOULD NOT BE USED FOR CRITICAL INFRASTRUCTURE**

# Work to be done
- refactor to a more OOP design
  - each machine type has a:
    - type {'service', 'database', 'envvargroup'}
    - template_file
    - modifiable_fields
    - ???
- have user select services, then databases, then envVarGroups (implies being able to separate machines by type)
- have user be able to interactively supply non-default values

Proposed flow:
1. If a render.yaml exists, throw up a prompt to either exit or continue by overwriting existing file
2. Prompt user to select services to include
   1. for each selected service, present a sane default config and ask user if they'd like to modify it
   2. show user list of modifiable fields and allow them to select a field to modify
   3. repeat until user gives some kind of "done" input
3. Prompt user to select databases to include
   1. for each selected database, present a sane default config and ask user if they'd like to modify it
   2. show user list of modifiable fields and allow them to select a field to modify
   3. repeat until user gives some kind of "done" input 
4. Prompt user to select envVarGroups to include
   1. for each selected envVarGroup, present a sane default config and ask user if they'd like to modify it
   2. show user list of modifiable fields and allow them to select a field to modify
   3. repeat until user gives some kind of "done" input 

# Usage
```shell
git clone git@github.com:zachwick/rendercad
poetry install 
poetry run rendercad
```

Better usage docs forthcoming.

# Legal

Copyright 2022 zach wick <zach@zachwick.com>

Licensed under the GNU AGPLv3 or later
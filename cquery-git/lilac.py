#!/usr/bin/env python3
from lilaclib import *
import os

build_prefix = 'extra-x86_64'
makechrootpkg_args = ['-D', os.path.realpath('cquery')]

def pre_build():
    git_rm_files(['update-submodules.sh'])
    aur_pre_build(do_vcs_update=False)
    git_add_files('update-submodules.sh')
    run_cmd('sh update-submodules.sh cquery'.split(' '))

def post_build():
    aur_post_build()

if __name__ == '__main__':
  single_main(build_prefix)

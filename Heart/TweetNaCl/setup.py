# -*- coding: utf-8 -*-

"""
Build and install the TweetNaCl wrapper.
"""

from __future__ import print_function

import platform

from distutils.core import setup, Extension


libraries = []

if platform.system() == "Windows":
    libraries.append("advapi32")

nacl_module = Extension('_tweetnacl',
                        ["tweetnaclmodule.c", "tweetnacl.c", "randombytes.c"],
                        libraries=libraries,
                        extra_compile_args=["-O2",
                                            "-funroll-loops",
                                            "-fomit-frame-pointer"])

setup(name = 'tweetnaclCrypt',
       version = '0.1',
       author = "Brian Warner, Jan Mojžíš",
       description = """Python wrapper for TweetNaCl""",
       ext_modules = [nacl_module],
       packages = ["tweetnacl"],
       package_dir = {"tweetnacl": ""},
      )

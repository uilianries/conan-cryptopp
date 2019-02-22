#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    entry_script = "git clone https://github.com/uilianries/conan-cryptopp.git /home/conan/project && cd /home/conan/project && git checkout testing/5.6.5 && cd /home/conan"
    builder = ConanMultiPackager(username="uilianries", docker_entry_script=entry_script)
    builder.add_common_builds(pure_c=False)
    builder.run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    entry_script = "pwd; ls; ls /root/src/github.com/uilianries"
    builder = ConanMultiPackager(username="uilianries", docker_entry_script=entry_script)
    builder.add_common_builds(pure_c=False)
    builder.run()

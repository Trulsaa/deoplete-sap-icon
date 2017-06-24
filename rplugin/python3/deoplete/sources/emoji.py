# Copyright (c) 2017 Filip Szymański. All rights reserved.
# Use of this source code is governed by an MIT license that can be
# found in the LICENSE file.

import re

from .base import Base
from deoplete.util import load_external_module

load_external_module(__file__, 'sources/emoji')
from emoji_unicode import EMOJI_UNICODE


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.__pattern = re.compile(r':[^: \t]+')

        self.filetypes = ['gitcommit', 'markdown', 'text']
        self.mark = '[emoji]'
        self.matchers = ['matcher_length', 'matcher_full_fuzzy']
        self.name = 'emoji'

    def gather_candidates(self, context):
        return [
            {'word': name, 'kind': code_points} for name, code_points in EMOJI_UNICODE.items()
        ]

    def get_complete_position(self, context):
        match = self.__pattern.search(context['input'])
        if match:
            return match.start()

        return -1

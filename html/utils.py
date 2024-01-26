# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 16:21:07
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-14 16:21:23
def camel_to_kebab(camel_str):
    result = [camel_str[0].lower()]
    for char in camel_str[1:]:
        if char.isupper():
            result.extend(['-', char.lower()])
        else:
            result.append(char)
    return ''.join(result)
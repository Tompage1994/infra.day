from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
name: odd_elements
author: Tom Page
version_added: "0.0.1"
short_description: Only keep elements if they are in an odd index
description:
  - Only keep elements if they are in an odd index
options:
  _raw:
    description:
    - The input list which will be filtered
    type: list
    required: True
"""

EXAMPLES = r"""
- name: Parse Data
  ansible.builtin.set_fact:
    output: "{{ [0,1,2,3,4,5,6,7] |  odd_elements }}"  # returns [1,3,5,7]
"""

def _odd_elements(_raw):
    return _raw[1::2]

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'odd_elements': _odd_elements
        }

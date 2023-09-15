def encode(string):
    return [
        ord(char) - 96 for char in string
    ]

def decode(charnums):
    return ''.join([
        chr(charnum+96) for charnum in charnums
    ])


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'decode': decode,
            'encode': encode
        }

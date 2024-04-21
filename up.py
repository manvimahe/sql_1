byte_strings = [b'Select * from general_log', b"SET NAMES 'utf8mb4' COLLATE 'utf8mb4_general_ci'", b'SET NAMES utf8mb4', b'set autocommit=0', b'Select * from general_log', b"SET NAMES 'utf8mb4' COLLATE 'utf8mb4_general_ci'", b'SET NAMES utf8mb4', b'set autocommit=0']

# Decode byte strings into regular strings
strings = [bs.decode('utf-8') if isinstance(bs, bytes) else bs for bs in byte_strings]

# Print the decoded strings
for string in strings:
    print(string)
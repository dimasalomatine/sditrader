#!/usr/bin/python
import tradecoder

KEY='your-key-super-duper-secret-key-here-only-first-32-characters-are-used'
decrypted =  tradecoder.encrypt(KEY, 'Hello, world!')
print decrypted
print tradecoder.decrypt(KEY, decrypted)

KEY='y'
decrypted =  tradecoder.encrypt(KEY, 'Hello, world!')
print decrypted
print tradecoder.decrypt(KEY, decrypted)

KEY='yo'
decrypted =  tradecoder.encrypt(KEY, 'Hello, world!')
print decrypted
print tradecoder.decrypt(KEY, decrypted)

KEY='you'
decrypted =  tradecoder.encrypt(KEY, 'Hello, world!')
print decrypted
print tradecoder.decrypt(KEY, decrypted)

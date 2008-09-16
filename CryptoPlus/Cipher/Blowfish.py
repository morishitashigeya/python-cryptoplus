import blockcipher
import Crypto.Cipher.Blowfish

MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_OFB = 5
MODE_CTR = 6

def new(key,mode=blockcipher.MODE_ECB,IV=None,counter=None):
	return Blowfish(key,mode,IV,counter)

class Blowfish(blockcipher.BlockCipher):
	"""Blowfish using pycrypto for algo en pycryptoplus for ciphermode

	EXAMPLE:
	----------
	>>> import Blowfish
	>>> from binascii import hexlify, unhexlify
	>>> cipher = Blowfish.new(unhexlify('0131D9619DC1376E'))
	>>> hexlify( cipher.encrypt(unhexlify('5CD54CA83DEF57DA')) )
	'b1b8cc0b250f09a0'
	>>> hexlify( cipher.decrypt(unhexlify(_)) )
	'5cd54ca83def57da'

	CBC EXAMPLE:
	-----------------------------------------
	>>> from binascii import hexlify,unhexlify
	>>> import python_AES
	>>> key = unhexlify('0123456789ABCDEFF0E1D2C3B4A59687')
	>>> IV = unhexlify('FEDCBA9876543210')
	>>> plaintext = unhexlify('37363534333231204E6F77206973207468652074696D6520')
	>>> cipher = Blowfish.new(key,Blowfish.MODE_CBC,IV)
	>>> ciphertext = cipher.encrypt(plaintext)
	>>> hexlify(ciphertext).upper()
	'6B77B4D63006DEE605B156E27403979358DEB9E7154616D9'
	"""
	def __init__(self,key,mode,IV,counter):
		self.cipher = Crypto.Cipher.Blowfish.new(key)
		self.blocksize = Crypto.Cipher.Blowfish.block_size
		blockcipher.BlockCipher.__init__(self,key,mode,IV,counter)

def _test():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	_test()
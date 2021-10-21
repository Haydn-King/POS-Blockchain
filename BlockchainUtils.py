from Crypto.Hash import SHA256
import json
from builtins import staticmethod
import jsonpickle


class BlockchainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encode(objectToEncode):
        jsonpickle.encode(objectToEncode, unpicklable=True)

    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)

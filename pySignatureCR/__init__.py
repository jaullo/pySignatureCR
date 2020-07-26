from .xades_context import XAdESContext
from . import constants
from .policy import Policy, PolicyId
from . import template
from . import context_cr
from . import get_reversed_rdns_name
import xmlsig

# Version of the realpython-reader package
__version__ = "1.0.0"

def b64_print(s):
    return s
    
# Monkey patching xmlsig functions to remove unecesary tail and body newlines
xmlsig.signature_context.b64_print = b64_print
xmlsig.algorithms.rsa.b64_print = b64_print

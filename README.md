# pySignatureCR Python Electronic Invoice Signature

> Electronic invoice signature for Ministerio Hacienda

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger)   [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) 

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


---

## Example (Optional)

```python
// code away!

def sign_xml(cert, password, xml, policy_id='https://www.hacienda.go.cr/ATV/ComprobanteElectronico/docs/esquemas/'
             '2016/v4.2/ResolucionComprobantesElectronicosDGT-R-48-2016_4.2.pdf'):
    root = etree.fromstring(xml)
    signature = create_xades_epes_signature()

    policy = PolicyId2()
    policy.id = policy_id

    root.append(signature)
    ctx = XAdESContext2(policy)
    certificate = crypto.load_pkcs12(base64.b64decode(cert), password)
    ctx.load_pkcs12(certificate)
    ctx.sign(signature)

    return etree.tostring(root, encoding='UTF-8', method='xml', xml_declaration=True, with_tail=False)
```

---

## Installation

- Just install current version from github using pip3 python command

- Please note @1.0.0 that refers to the version you're installing. To install a different version just set the correct branch version and you're ready to go.

```python
pip3 install git+https://github.com/jaullo/pySignatureCR.git@1.0.0#egg=pysignaturecr
```

### Clone

- Clone this repo to your local machine using https://github.com/jaullo/pySignatureCR.git

### Setup

- After installation, just import required modules to your project

```python
from pySignatureCR.context_cr import XAdESContext2, PolicyId2, create_xades_epes_signature
from pySignatureCR.rdns_name import get_reversed_rdns_name
```

## Features
- Supports Electronic Invoice Signature
- Supports Electronic Ticket Signature
- Supports Electronic Credit Note Signature
- Supports Electronic Debit Note Signature
- Supports Electronic Exportation Invoice Signature
- Supports Electronic Buying Invoice Signature

## Usage (Optional)
## Documentation (Optional)

## Contributing

> There are many ways to help or contribute to this project, all of them are welcome.

### Three Ways

- **Option 1**
    - 🍴 Review the code, test it and open any Bug Report or new feature request

- **Option 2**

  - 🔃 Create a new pull request using <a href="hhttps://github.com/jaullo/pySignatureCR.git/compare/" target="_blank">`https://github.com/jaullo/pySignatureCR.git/compare/`</a>.

- **Option 3**

  - 👯 Clone this repo to your local machine using `https://github.com/jaullo/pySignatureCR.git`, review the code, extend it and send a PULL REQUEST

## Team

> Or Contributors/People

- This project has been developed by Jason Ulloa <jason.ulloa@techmicrocr.com> based on Etobella Python Signature and Ricardo Vong <rvong@indelsacr.com> code upgrades

- All credit to the original authors

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

---

## Support

Reach out to me at one of the following places!

- <jason.ulloa@techmicrocr.com>

---

## Donations (Optional)

- You could include a <a href="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" target="_blank">Gratipay</a> link as well.

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/fvcproductions/)


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="https://techmicrocr.com" target="_blank">TechMicro Inc. S.A.</a>.

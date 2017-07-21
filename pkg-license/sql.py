#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

db = MySQLdb.connect("localhost","root","","registry")
cursor = db.cursor()
cursor.execute("SELECT * FROM license WHERE COUNT > 50")
raw = cursor.fetchall()

licenseMap = {
    'Proprietary': 'Proprietary',

    'Public Domain': 'CC0',
    'CC0': 'CC0',
    'CC0-1.0': 'CC0',
    'CC-BY-NC-SA-4.0': 'CC BY-NC-SA 4.0',
    'CC-BY-SA-4.0': 'CC BY-SA-4.0',
    'CC-BY-4.0': 'CC BY-4.0',

    'Artistic-2.0': 'Artistic-2.0',

    'MPL': 'MPL-2.0',
    'MPL 2.0': 'MPL-2.0',
    'MPL-2.0': 'MPL-2.0',

    'unlicense': 'Unlicense',
    'Unlicense': 'Unlicense',
    'UNLICENSE': 'Unlicense',
    'UNLICENSED': 'Unlicense',

    'WTFPL': 'WTFPL',

    'x': 'MIT',
    'X': 'MIT',
    'X11': 'MIT',
    'MIT/X11': 'MIT',
    'mit': 'MIT',
    'pemrouz.mit-license.org': 'MIT',
    'MIT License': 'MIT',
    'MIT': 'MIT',

    'Zlib': 'Zlib',

    'VOL': 'Microsoft Volume Licensing',

    'GPL': 'GPL',
    'GNU': 'GPL',
    'GPL v2': 'GPLv2',
    'GPLv2': 'GPLv2',
    'GPL-2.0+': 'GPLv2.0+',
    'GPL-2.0': 'GPLv2',
    'GPLv3': 'GPLv3',
    'GPL3': 'GPLv3',
    'GPL-3.0+': 'GPLv3',
    'GPL v3': 'GPLv3',
    'GPL-3.0': 'GPLv3',

    'AGPL': 'AGPL',
    'AGPL-1.0': 'AGPLv1',
    'AGPLv3': 'AGPLv3',
    'AGPL-3.0': 'AGPLv3',

    'LGPL': 'LGPL',
    'LGPL-3.0': 'LGPLv3',
    'LGPLv3': 'LGPLv3',
    'LGPL-3.0+': 'LGPLv3',
    'LGPL-2.1': 'LGPLv2.1',

    'Apache 2.0': 'Apache-2.0',
    'Apache2': 'Apache-2.0',
    'Apache': 'Apache-2.0',
    'Apache 2': 'Apache-2.0',
    'Apache License 2.0': 'Apache-2.0',
    'Apache v2': 'Apache-2.0',
    'Apache 2.0 License': 'Apache-2.0',
    'Apache License, Version 2.0': 'Apache-2.0',
    'Apache-2': 'Apache-2.0',
    'Apache License v2.0': 'Apache-2.0',
    'Apache-2.0': 'Apache-2.0',

    'Beerware': 'Beerware',

    'EPL-1.0': 'EPL-1.0',

    'Fair': 'Fair',

    '(MIT OR Apache-2.0)': 'two licenses',


    'BSD': 'BSD',
    'BSD-2-Clause': 'BSD-2-Clause',
    'BSD-3-Clause': 'BSD-3-Clause',

    'ISC': 'ISC',

    'none': 'NONE',

    'SEE LICENSE IN LICENSE.md': 'outside',
    'SEE LICENSE IN LICENSE.txt': 'outside',
    'SEE LICENSE IN LICENSE': 'outside'
}

simplifyLicenseMap = {
    'outside': 'Other',
    'NONE': 'Other',
    'two licenses': 'Other',
    'Fair': 'Other',
    'EPL-1.0': 'Other',
    'Beerware': 'Other',
    'Microsoft Volume Licensing': 'Other',
    'Artistic-2.0': 'Other',
    'Zlib': 'Other',
    'Proprietary': 'Other',
    'Other': 'Other',
    'WTFPL': 'Other',
    'CC BY-4.0': 'Other',
    'CC BY-NC-SA 4.0': 'Other',
    'CC BY-SA-4.0': 'Other',
    'CC0': 'Other',
    'CC': 'Other',
    

    'AGPL': 'GPL',
    'AGPLv1': 'GPL',
    'AGPLv3': 'GPL',
    'GPL': 'GPL',
    'GPLv2': 'GPL',
    'GPLv2.0+': 'GPL',
    'GPLv3': 'GPL',
    'LGPL': 'GPL',
    'LGPLv2.1': 'GPL',
    'LGPLv3': 'GPL',

    'Apache-2.0': 'Apache-2.0',

    'BSD': 'BSD',
    'BSD-2-Clause': 'BSD',
    'BSD-3-Clause': 'BSD',

    'ISC': 'ISC',

    'MPL-2.0': 'Other',

    'Unlicense': 'Unlicense',

    'MIT': 'MIT'
}

result = {}
# for license, count, tags in raw:
#     mappedLicense = licenseMap[license.strip()]
#     cursor.execute("UPDATE license SET TAGS=('%s') WHERE LICENSE=('%s')" %(mappedLicense, license))
#     db.commit()
#     try:
#         result[mappedLicense] += count
#     except KeyError:
#         result[mappedLicense] = count

for license, count, tags in raw:
    mappedLicense = simplifyLicenseMap[tags]
    cursor.execute("UPDATE license SET TAGS=('%s') WHERE TAGS=('%s')" %(mappedLicense, tags))
    db.commit()
    try:
        result[mappedLicense] += count
    except KeyError:
        result[mappedLicense] = count

print result
print len(result)

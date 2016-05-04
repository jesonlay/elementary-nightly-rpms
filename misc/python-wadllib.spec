# Created by pyp2rpm-3.0.2
%global pypi_name wadllib

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        1%{?dist}
Summary:        Navigate HTTP resources using WADL files as guides

License:        LGPL v3
URL:            https://launchpad.net/wadllib
Source0:        https://pypi.python.org/packages/7e/94/9e5f9ad89001215f67619adc2ed3ac771dbbdb23bc7d91bf0bce4aff7bd6/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python2-lazr-uri

Requires:       python2-lazr-uri


%description
..
   Copyright (C) 2008-2013 Canonical Ltd.

   This file is part of wadllib.
wadllib is free software: you can redistribute it and/or modify it under
   the
terms of the GNU Lesser General Public License as published by the
   Free
Software Foundation, version 3 of the License.

   wadllib is distributed in
the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the
...

%package -n     python2-%{pypi_name}
Summary:        Navigate HTTP resources using WADL files as guides
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-setuptools
Requires:       python-lazr-uri
%description -n python2-%{pypi_name}
..
   Copyright (C) 2008-2013 Canonical Ltd.

   This file is part of wadllib.
wadllib is free software: you can redistribute it and/or modify it under
   the
terms of the GNU Lesser General Public License as published by the
   Free
Software Foundation, version 3 of the License.

   wadllib is distributed in
the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the
...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%check
%{__python2} setup.py test

%files -n python2-%{pypi_name} 
%doc README.txt src/wadllib/README.txt COPYING.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Initial package.

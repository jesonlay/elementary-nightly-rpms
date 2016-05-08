# Created by pyp2rpm-3.0.2
%global pypi_name lazr.restfulclient
%global prettyname lazr-restfulclient

Name:           python-lazr-restfulclient
Version:        0.13.4
Release:        2%{?dist}
Summary:        A self-contained, easily reusable library for parsing, manipulating,

License:        LGPL v3
URL:            https://launchpad.net/%{pypi_name}
Source0:        %{pypi_name}-0.13.4.tar.bz2
BuildArch:      noarch

BuildRequires:  python2-devel 

BuildRequires:  python-oauth
BuildRequires:  python-httplib2
BuildRequires:  python-setuptools
BuildRequires:  python2-wadllib


%description
..
    This file is part of %{pypi_name}.

    %{pypi_name} is free software: you can
redistribute it and/or modify it
    under the terms of the GNU Lesser General
Public License as published by
    the Free Software Foundation, version 3 of
the License.

    %{pypi_name} is distributed in the hope that it will be useful,
but
    WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY
 ...

%package -n     python2-%{prettyname}
Summary:        A self-contained, easily reusable library for parsing, manipulating,
%{?python_provide:%python_provide python2-%{prettyname}}
 
Requires:       python-setuptools
Requires:       python-oauth
Requires:       python-httplib2
Requires:       python-setuptools
Requires:       python2-wadllib

%description -n python2-%{prettyname}
..
    This file is part of %{pypi_name}.

    %{pypi_name} is free software: you can
redistribute it and/or modify it
    under the terms of the GNU Lesser General
Public License as published by
    the Free Software Foundation, version 3 of
the License.

    %{pypi_name} is distributed in the hope that it will be useful,
but
    WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY
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
# %{__python2} setup.py test

%files -n python2-%{prettyname} 
%doc README.txt src/lazr/restfulclient/README.txt COPYING.txt
# %{python2_sitelib}/%{pypi_name}_1.0.3_py2.7_nspkg.pth
%{python2_sitelib}/lazr
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.13.4-2
- Fix Requires.

* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Initial package.


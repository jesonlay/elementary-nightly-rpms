%global pip_name launchpadlib
%global debug_package %{nil}

Summary:        launchpad python client library
Name:           python-launchpadlib
Version:        1.10.3
Release:        1%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/launchpadlib

Source0:        https://launchpad.net/launchpadlib/trunk/1.10.3/+download/launchpadlib-1.10.3.tar.gz

BuildRequires:  python2-devel

BuildRequires:  python-httplib2
BuildRequires:  python-keyring
BuildRequires:  python-oauth
BuildRequires:  python2-lazr-restfulclient
BuildRequires:  python2-lazr-uri
BuildRequires:  python2-testresources
BuildRequires:  python2-wadllib

Requires:       python-httplib2
Requires:       python-keyring
Requires:       python-oauth
Requires:       python2-lazr-restfulclient
Requires:       python2-lazr-uri
Requires:       python2-testresources
Requires:       python2-wadllib


%description
Python client library for Launchpad's web service


%package -n python2-launchpadlib
Summary:    launchpad python client library
%description -n python2-launchpadlib
Python client library for Launchpad's web service


%prep
%setup -q -n %{pip_name}-%{version}


%build
%py2_build


%install
%py2_install


%clean
rm -rf %{buildroot}


%files

%files -n python2-launchpadlib
%{python2_sitelib}/%{pip_name}/
%{python2_sitelib}/%{pip_name}-%{version}-py2.7.egg-info/


%changelog
* Tue May 03 2016 Fabio Valentini <decathorpe@gmail.com> - 1.10.3-1
- Initial package.



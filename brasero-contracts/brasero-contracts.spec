%define rev 10
%define debug_package %{nil}

Summary: contractor: brasero contracts
Name: brasero-contracts
Version: 0.1~rev%{rev}
Release: 2%{?dist}
License: GPLv3
URL: http://launchpad.net/contractor

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

Requires: brasero
Requires: contractor


%description
contractor: brasero contracts


%prep
%autosetup


%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/contractor
install -m 0644 *.contract $RPM_BUILD_ROOT/%{_datadir}/contractor/


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files
%{_datadir}/contractor/*.contract


%changelog
* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev10-2
- Disable debug package for f23.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev10-1
- Initial package.




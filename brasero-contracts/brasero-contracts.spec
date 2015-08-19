%define rev 10

Summary: contractor: brasero contracts
Name: brasero-contracts
Version: 0.1~rev%{rev}
Release: 1%{?dist}
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
* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev10-1
- Initial package.




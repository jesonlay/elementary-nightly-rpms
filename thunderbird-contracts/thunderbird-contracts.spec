%define rev 17
%define debug_package %{nil}

Summary: contractor: thunderbird contracts
Name: thunderbird-contracts
Version: 0.1~rev%{rev}
Release: 2%{?dist}
License: GPLv3
URL: http://launchpad.net/contractor

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

Requires: thunderbird
Requires: contractor


%description
contractor: thunderbird contracts


%prep
%autosetup


%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/contractor

install -m 0755 thunderbird-attach $RPM_BUILD_ROOT/%{_bindir}/
install -m 0644 *.contract $RPM_BUILD_ROOT/%{_datadir}/contractor/


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files
%{_bindir}/thunderbird-attach
%{_datadir}/contractor/*.contract


%changelog
* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev17-2
- Update to remove debug package to make f23 happy.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev17-1
- Initial package.



